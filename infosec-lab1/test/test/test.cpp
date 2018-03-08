// test.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "string.h"

#include <openssl\rsa.h>
#include <openssl\dsa.h>

#include "Crypto.h"

int _tmain(int argc, _TCHAR* argv[])
{

		unsigned char buffer[160];
		unsigned char sig[]={"abc"};

SHA1_buffer(sig, 3, buffer);


for (int i = 0; i < 20; i++)
	printf ("%02x,",buffer[i]);
printf ("\n");



    DSA * dsa, *pdsa;
    unsigned char input_string[]="1234";
    unsigned char sign_string[2048];
    unsigned int sig_len;
    unsigned int i;
 
    // check usage
 //   if (argc != 2) {
 //       fprintf(stderr, "%s <plain text>\n", argv[0]);
 //       exit(-1);
 //   }
 
    // set the input string
  //  input_string = (unsigned char*)calloc(strlen(argv[1]) + 1,
 //           sizeof(unsigned char));
 //   strncpy((char*)input_string, argv[1], strlen(argv[1]));
 
    // Generate random DSA parameters with 1024 bits 
    //dsa = DSA_generate_parameters(1024, NULL, 0, NULL, NULL, NULL, NULL);
 
    // Generate DSA keys
   // DSA_generate_key(dsa);
 
	//memcpy (&publicdsa, dsa, sizeof(publicdsa));

	//publicdsa.priv_key = NULL;
    DSA_init_keypair (1024, &pdsa, &dsa);

    // sign input_string
    if (DSA_sign_buffer(input_string, strlen((char*)input_string),
                sign_string, &sig_len, dsa) == 0) {
        fprintf(stderr, "Sign Error.\n");
        exit(-1);
    }
 
    // verify signature and input_string
    int is_valid_signature = DSA_verify_buffer(input_string, strlen((char*)input_string), 
            sign_string, sig_len, pdsa);
 
    // print
    DSAparams_print_fp(stdout, dsa);
    printf("input_string = %s\n", input_string);
    printf("signed string = ");
    for (i=0; i<sig_len; ++i) {
        printf("%x%x", (sign_string[i] >> 4) & 0xf, 
                sign_string[i] & 0xf);    
    }
    printf("\n");
    printf("is_valid_signature? = %d\n", is_valid_signature);
 
    return 0;

}

