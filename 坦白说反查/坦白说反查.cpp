// 坦白说反查.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;

int main()
{
	string db[3][10] = { { "oe","oK","ow","oi","7e","7K","7w","7i","Ne","NK" },
						 { "n","6","-","o","v","4","C","S","c","E" },
						 { "z","5","A","i","P","k","s","l","F","q" } };
	int num[3] = { 2,1,1 };
	bool flag = 1;
	string find;
	while (flag) {
		cout << "Input what you want to find" << endl;
		cin >> find;
		cout << "QQnum is :";
		unsigned int count = 0;
		for (int i = 0; count < find.length(); i++) {
			string temp = find.substr(count, num[i % 3]);
			for (int k = 0; k < 10; k++) {
				if (db[i % 3][k] == temp) {
					cout << k;
					break;
				}
			}
			count += num[i % 3];
		}
		cout << endl;
		flag = 0;
		cout << "again?" << endl;
		getchar();
		if (getchar() == 'y') {
			flag = 1;
		}
	}
	return 0;
}

