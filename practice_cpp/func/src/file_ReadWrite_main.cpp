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

    //文件打开方式选项：
    //　ios::in　　　　= 0x01,　//供读，文件不存在则创建(ifstream默认的打开方式)
    //　ios::out　　　 = 0x02,　//供写，文件不存在则创建，若文件已存在则清空原内容(ofstream默认的打开方式)
    //　ios::ate　　　 = 0x04,　//文件打开时，指针在文件最后。可改变指针的位置，常和in、out联合使用
    //　ios::app　　　 = 0x08,　//供写，文件不存在则创建，若文件已存在则在原文件内容后写入新的内容，指针位置总在最后
    //　ios::trunc　　 = 0x10,　//在读写前先将文件长度截断为0（默认）
    //　ios::nocreate　= 0x20,　//文件不存在时产生错误，常和in或app联合使用
    //　ios::noreplace = 0x40,　//文件存在时产生错误，常和out联合使用
    //　ios::binary　　= 0x80　 //二进制格式文件

    if (!f) {
        cout << "打开文件出错" << endl;
        return;
    }

    //如果知道数据格式，可以直接用>>读入
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
    const char* file_name = "../data/file_ReadWrite_data.txt"; // file path
    char abs_path_buff[PATH_MAX];
    //realpath函数返回: null表示获取失败; 否则返回指向abs_path_buff的指针
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

    fstream f;
    f.open("../data/output.txt",ios::out);
    char trim_character = ' ';
    f << 0.2 << trim_character << 132 << trim_character << "string";
    f.close();
    return 0;
}