#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <locale>
#include <set>
#include <codecvt>
#include <memory>

using namespace std;

struct IFileAnalyzer {
    virtual ~IFileAnalyzer() = default;
    virtual int getLines() const = 0;
    virtual int getWords() const = 0;
    virtual int getBytes() const = 0;
    virtual int getChars() const = 0;
    virtual void analyze(const string& filename) = 0;
};

class FileAnalyzer : public IFileAnalyzer {
    int lines = 0;
    int words = 0;
    int bytes = 0;
    int chars = 0;

public:
    void analyze(const string& filename) override {
        lines = words = bytes = chars = 0;

        ifstream byteFile(filename, ios::binary);
        if (!byteFile.is_open()) {
            wcerr << L"Ошибка: не удалось открыть файл '" << filename.c_str() << L"'" << endl;
            return;
        }
        byteFile.seekg(0, ios::end);
        bytes = byteFile.tellg();
        byteFile.close();

        wifstream file(filename);
        file.imbue(locale(locale(), new codecvt_utf8<wchar_t>));
        if (!file.is_open()) {
            wcerr << L"Ошибка: не удалось открыть файл '" << filename.c_str() << L"'" << endl;
            return;
        }

        wstring line;
        while (getline(file, line)) {
            lines++;
            wistringstream wiss(line);
            wstring word;
            while (wiss >> word) {
                words++;
            }
            chars += line.length();
        }
        file.close();
    }

    int getLines() const override { return lines; }
    int getWords() const override { return words; }
    int getBytes() const override { return bytes; }
    int getChars() const override { return chars; }
};

void parseOptions(const vector<string>& args, set<string>& options, vector<string>& filenames) {
    for (const string& arg : args) {
        if (!arg.empty() && arg[0] == '-') {
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

class StatsPrinter {
public:
    void print(const IFileAnalyzer& analyzer, const set<string>& options, const string& filename, bool showFilename = true) {
        if (options.empty() || options.count("lines"))
            wcout << L"Lines: " << analyzer.getLines() << L" -- ";
        if (options.empty() || options.count("words"))
            wcout << L"Words: " << analyzer.getWords() << L" -- ";
        if (options.empty() || options.count("bytes"))
            wcout << L"Bytes: " << analyzer.getBytes() << L" -- ";
        if (options.empty() || options.count("chars"))
            wcout << L"Chars: " << analyzer.getChars() << L" -- ";
        if (showFilename)
            wcout << filename.c_str();
        wcout << endl;
    }
};

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

    unique_ptr<IFileAnalyzer> analyzer = make_unique<FileAnalyzer>();
    StatsPrinter printer;

    for (const string& filename : filenames) {
        analyzer->analyze(filename);
        printer.print(*analyzer, options, filename, filenames.size() > 1);
    }

    return 0;
}
