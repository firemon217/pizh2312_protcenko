#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <locale>
#include <set>
#include <codecvt>

using namespace std;

struct FileStats {
    int lines = 0;
    int words = 0;
    int bytes = 0;
    int chars = 0;
};

FileStats analyzeFile(const string& filename) {
    FileStats stats;

    ifstream byteFile(filename, ios::binary);
    if (!byteFile.is_open()) {
        wcerr << L"Ошибка: не удалось открыть файл '" << filename.c_str() << L"'" << endl;
        return stats;
    }
    byteFile.seekg(0, ios::end);
    stats.bytes = byteFile.tellg();
    byteFile.close();

    wifstream file(filename);
    file.imbue(locale(locale(), new codecvt_utf8<wchar_t>));

    if (!file.is_open()) {
        wcerr << L"Ошибка: не удалось открыть файл '" << filename.c_str() << L"'" << endl;
        return stats;
    }

    wstring line;
    while (getline(file, line)) {
        stats.lines++;
        wistringstream wiss(line);
        wstring word;
        while (wiss >> word) {
            stats.words++;
        }
        stats.chars += line.length();
    }

    file.close();
    return stats;
}

void parseOptions(const vector<string>& args,
    set<string>& options,
    vector<string>& filenames) {
    for (const string& arg : args) {
        if (arg.size() > 0 && arg[0] == '-') {
            if (arg.substr(0, 2) == "--") {
                options.insert(arg.substr(2));
            }
            else {
                for (size_t i = 1; i < arg.size(); ++i) {
                    switch (arg[i]) {
                    case 'l': options.insert("lines"); break;
                    case 'w': options.insert("words"); break;
                    case 'c': options.insert("bytes"); break;
                    case 'm': options.insert("chars"); break;
                    default:
                        wcerr << L"Неизвестная опция: -" << arg[i] << endl;
                    }
                }
            }
        }
        else {
            filenames.push_back(arg);
        }
    }
}

void printStats(const FileStats& stats, const set<string>& options, const string& filename, bool showFilename = true) {
    if (options.empty() || options.count("lines"))
        wcout << L"Lines: " << stats.lines << L" -- ";
    if (options.empty() || options.count("words"))
        wcout << L"Words: " << stats.words << L" -- ";
    if (options.empty() || options.count("bytes"))
        wcout << L"Bytes: " << stats.bytes << L" -- ";
    if (options.empty() || options.count("chars"))
        wcout << L"Chars: " << stats.chars << L" -- ";
    if (showFilename)
        wcout << filename.c_str();
    wcout << endl;
}

int wmain(int argc, wchar_t* argv[]) {
    locale::global(locale(""));

    if (argc < 2) {
        wcerr << L"Использование: WordCount [опции] файл1 [файл2 ...]" << endl;
        return 1;
    }

    vector<string> args;
    for (int i = 1; i < argc; ++i) {
        wstring ws(argv[i]);
        string s(ws.begin(), ws.end());
        args.push_back(s);
    }

    set<string> options;
    vector<string> filenames;

    parseOptions(args, options, filenames);

    if (filenames.empty()) {
        wcerr << L"Ошибка: не указаны файлы для обработки." << endl;
        return 1;
    }

    for (const string& filename : filenames) {
        FileStats stats = analyzeFile(filename);
        printStats(stats, options, filename, filenames.size() > 1);
    }

    return 0;
}
