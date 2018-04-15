// InfosecLab1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <string.h>  
#include <openssl/sha.h>  
using namespace std;
static const char hex_chars[] = "0123456789abcdef";  
   
void convert_hex(unsigned char *md, unsigned char *mdstr)  
{  
    int i;  
    int j = 0;  
    unsigned int c;  
   
    for (i = 0; i < 20; i++) {  
        c = (md[i] >> 4) & 0x0f;  
        mdstr[j++] = hex_chars[c];  
        mdstr[j++] = hex_chars[md[i] & 0x0f];  
    }  
    mdstr[40] = '\0';  
}  
   
int main(int argc, char **argv)  
{  
	while(true)
	{
		SHA_CTX shactx;  
		char data[] = "1515300022";
		static int x=1;
		char cx[1024];
		memset(cx,0,1024);
		itoa(x,cx,10);
		strcat(data,cx);

		unsigned char md[SHA_DIGEST_LENGTH];  
		unsigned char mdstr[40];  
  
		SHA1_Init(&shactx);  
		SHA1_Update(&shactx, data, 6);  
		SHA1_Update(&shactx, data+6, 9);  
		SHA1_Final(md, &shactx);  
		convert_hex(md, mdstr);  

		char shr[]="ffffffffffffffffffffffffffffffffffffffff";
		cout << "input the value of 'd' : ";
		cin >> d;
		int d;
		for(int j=0;j<d;j++)
		{
			shr[j]='0';
		}

		int i=(strcmp(shr,(const char*)mdstr));

		if(i>0)
		{
			cout<<"d = "<<d<<endl;
			printf ("SHA1 : %s\n", mdstr);
			printf ("Shr :    %s\n", shr);  
			cout<<"x = "<<x<<endl;
			return 0;
		}
		++x;
	}
    return 0;  
}  