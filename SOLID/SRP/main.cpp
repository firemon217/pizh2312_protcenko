#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstdint>
#include <filesystem>
#include <unordered_map>

using namespace std;

struct Params {
    uint16_t h = 0;
    uint16_t w = 0;
    string in_file;
    string out_folder;
    uint64_t max_steps = 0;
    uint64_t save_freq = 0;

    static Params parse(int argc, char* argv[]) {
        unordered_map<string, string> args_map;
        for (int i = 1; i + 1 < argc; i += 2) {
            args_map[argv[i]] = argv[i + 1];
        }

        Params p;
        if (args_map.count("-l")) p.h = stoi(args_map["-l"]);
        if (args_map.count("--length")) p.h = stoi(args_map["--length"]);
        if (args_map.count("-w")) p.w = stoi(args_map["-w"]);
        if (args_map.count("--width")) p.w = stoi(args_map["--width"]);
        if (args_map.count("-i")) p.in_file = args_map["-i"];
        if (args_map.count("--input")) p.in_file = args_map["--input"];
        if (args_map.count("-o")) p.out_folder = args_map["-o"];
        if (args_map.count("--output")) p.out_folder = args_map["--output"];
        if (args_map.count("-m")) p.max_steps = stoull(args_map["-m"]);
        if (args_map.count("--max-iter")) p.max_steps = stoull(args_map["--max-iter"]);
        if (args_map.count("-f")) p.save_freq = stoull(args_map["-f"]);
        if (args_map.count("--freq")) p.save_freq = stoull(args_map["--freq"]);

        return p;
    }
};

class Sandpile {
private:
    vector<vector<uint64_t>> grid;

public:
    Sandpile(uint16_t height, uint16_t width)
        : grid(height, vector<uint64_t>(width, 0)) {
    }

    void load_from_file(const string& path) {
        ifstream in(path);
        string line;
        while (getline(in, line)) {
            istringstream ss(line);
            int x, y;
            uint64_t c;
            ss >> x;
            ss.ignore();
            ss >> y;
            ss.ignore();
            ss >> c;
            if (y >= 0 && y < (int)grid.size() && x >= 0 && x < (int)grid[0].size()) {
                grid[y][x] += c;
            }
        }
    }

    bool update() {
        int h = grid.size();
        int w = grid[0].size();
        vector<vector<uint64_t>> tmp = grid;
        bool active = false;

        for (int y = 0; y < h; ++y) {
            for (int x = 0; x < w; ++x) {
                if (grid[y][x] >= 4) {
                    uint64_t drop = grid[y][x] / 4;
                    tmp[y][x] -= drop * 4;
                    if (y > 0) tmp[y - 1][x] += drop;
                    if (y + 1 < h) tmp[y + 1][x] += drop;
                    if (x > 0) tmp[y][x - 1] += drop;
                    if (x + 1 < w) tmp[y][x + 1] += drop;
                    active = true;
                }
            }
        }

        grid = std::move(tmp);
        return active;
    }

    const vector<vector<uint64_t>>& data() const {
        return grid;
    }
};

class BMPWriter {
private:
#pragma pack(push, 1)
    struct BMPHeader {
        uint16_t type = 0x4D42;
        uint32_t size;
        uint32_t reserved = 0;
        uint32_t offset = 54;
        uint32_t header_size = 40;
        int32_t width;
        int32_t height;
        uint16_t planes = 1;
        uint16_t bpp = 24;
        uint32_t compression = 0;
        uint32_t img_size;
        int32_t x_res = 1000;
        int32_t y_res = 1000;
        uint32_t used = 0;
        uint32_t important = 0;
    };
#pragma pack(pop)

    static constexpr uint8_t palette[5][3] = {
        {255, 255, 255},
        {0, 255, 0},    
        {128, 0, 128},  
        {255, 255, 0},  
        {0, 0, 0}       
    };

public:
    static void write(const string& filename, const vector<vector<uint64_t>>& data) {
        int h = data.size();
        int w = data[0].size();
        int row_bytes = (w * 3 + 3) & ~3;
        int total_size = 54 + row_bytes * h;

        BMPHeader header;
        header.size = total_size;
        header.width = w;
        header.height = h;
        header.img_size = row_bytes * h;

        ofstream out(filename, ios::binary);
        if (!out) {
            cerr << "Failed to open output file: " << filename << endl;
            return;
        }

        out.write(reinterpret_cast<char*>(&header), sizeof(header));

        vector<uint8_t> row(row_bytes);

        for (int y = h - 1; y >= 0; --y) {
            fill(row.begin(), row.end(), 0);
            for (int x = 0; x < w; ++x) {
                int v = data[y][x] > 3 ? 4 : static_cast<int>(data[y][x]);
                row[x * 3 + 0] = palette[v][2]; 
                row[x * 3 + 1] = palette[v][1]; 
                row[x * 3 + 2] = palette[v][0]; 
            }
            out.write(reinterpret_cast<char*>(row.data()), row_bytes);
        }
    }
};

int main(int argc, char* argv[]) {
    if (argc < 9) {
        cout << "Usage: ./sandpiles -l <height> -w <width> -i <input.tsv> -o <output_dir> -m <max_iter> -f <freq>\n";
        return 1;
    }

    Params params = Params::parse(argc, argv);

    filesystem::create_directories(params.out_folder);

    Sandpile sandpile(params.h, params.w);
    sandpile.load_from_file(params.in_file);

    for (uint64_t i = 0; i <= params.max_steps; ++i) {
        if (params.save_freq && i % params.save_freq == 0) {
            string filename = params.out_folder + "/state_" + to_string(i) + ".bmp";
            BMPWriter::write(filename, sandpile.data());
        }

        if (!sandpile.update()) {
            cout << "Stable at iteration: " << i << endl;
            break;
        }
    }

    if (params.save_freq == 0) {
        string filename = params.out_folder + "/final.bmp";
        BMPWriter::write(filename, sandpile.data());
    }

    return 0;
}
