//
// Created by wangwei on 18-8-22.
//

//#include <cstdlib>
#include <iostream> // use std::cout
#include <fstream>
#include <vector>
#include <limits.h> // use PATH_MAX

using namespace std;

typedef double data_type;

void textReadAll(string& file, size_t col_num, std::vector<std::vector<data_type>>& data) {
    fstream f;
    cout << "start read file: " << file << endl;

    f.open(file, ios::in);

    // open_mode is a integer-type number, here is a list:

    // ios::in　　　　= 0x01,　// read, create new file if not exist (ifstream default mode).
    // ios::out　　　 = 0x02,　// write (overwrite when file exist), create new file if not exist (ofstream default mode).
    // ios::ate　　　 = 0x04,　// put the pointer at the end of the file when opened. The pointer can be changed, usually used along with ios::in and ios::out.
    // ios::app　　　 = 0x08,　//write (append), create new file if not exist, the pointer is always at the end of the opened file.
    // ios::trunc　　 = 0x10,　// any current content is discarded, assuming a length of zero on opening.
    // ios::nocreate　= 0x20,　// return error when file doesn't exist, usually used along with ios::in and ios::app.
    // ios::noreplace = 0x40,　// return error when file exist, usually used along with ios::out.
    // ios::binary　　= 0x80　 // open file in binary format.

    if (!f) {
        cout << "failed to open file!" << endl;
        return;
    }

    data.clear();

    double tmp[col_num];
    while (!f.eof()) {
        for (size_t i = 0; i < col_num; ++i) {
            f >> tmp[i];
        }
        std::vector<data_type> row_data(tmp, tmp + col_num);
        data.push_back(row_data);
    }
    data.pop_back(); // the last row is read twice, remove one record.
    f.close();
}

int main(){
    // read from file
    const char* file_name = "../data/file_ReadWrite/file_ReadWrite_data.txt"; // file path
    char abs_path_buff[PATH_MAX];
    //realpath returns the absolute path; null - failed, otherwise return ptr of abs_path_buff.
    if(realpath(file_name, abs_path_buff)){
        printf("%s\n", abs_path_buff);
    }
    else{
        printf("the file '%s' is not exist\n", file_name);
    }

    string data_path(abs_path_buff);

    typedef double data_type;
    size_t col_num = 3;
    vector<vector<data_type>> data;
    textReadAll(data_path, col_num, data);
    for (auto &iter : data) {
        for (int j = 0; j < col_num; ++j) {
            printf("%.8f ", iter[j]);
        }
        cout << "\n";
    }

    // write to file
    fstream f;
    f.open("../data/file_ReadWrite/output.txt",ios::out);
    char trim_character = ' ';
    f << 0.2 << trim_character << 132 << trim_character << "string";
    f.close();
    return 0;
}