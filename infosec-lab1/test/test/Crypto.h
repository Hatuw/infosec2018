


void SHA1_buffer(unsigned char * string, unsigned int len, unsigned char *outputBuffer);

void SHA1_file(char * string, unsigned char *outputBuffer);

void AES_CBC128_encrypt_buffer (unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *iv);

void AES_CBC128_decrypt_buffer (unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *iv);

void AES_CTR128_encrypt_buffer (unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *counter);
    
void AES_CTR128_decrypt_buffer (unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *counter);

void AES_ECB128_encrypt_buffer(unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key);

void AES_ECB128_decrypt_buffer(unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key);

void AES_CFB128_encrypt_buffer (const unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *iv);

void AES_CFB128_decrypt_buffer (const unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *iv);

void AES_OFB128_encrypt_buffer (const unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *iv);

void AES_OFB128_decrypt_buffer (const unsigned char *in, unsigned char *out, unsigned int length, unsigned char *key, unsigned char *ivec);


void RSA_init_keypair (int bits, RSA ** publickey, RSA ** privatekey);

void RSA_free_keypair (RSA * publickey, RSA * privatekey);


void RSA_public_encrypt_buffer (unsigned char *in, int insize, unsigned char *out, int *outsize, RSA *key);

void RSA_private_decrypt_buffer (unsigned char *in, int insize, unsigned char *out, int *outsize, RSA *key);

void RSA_private_encrypt_buffer (unsigned char *in, int insize, unsigned char *out, int *outsize, RSA *key);

void RSA_public_decrypt_buffer (unsigned char *in, int insize, unsigned char *out, int *outsize, RSA *key);


 int RSA_sign_buffer(unsigned char *m, unsigned int m_len, unsigned char *sigret, unsigned int *siglen, RSA *rsa);

int RSA_verify_buffer(unsigned char *m, unsigned int m_len, unsigned char *sigbuf, unsigned int siglen, RSA *rsa);

void DSA_init_keypair (int bits, DSA **pdsa, DSA **sdsa);

void DSA_free_keypair (DSA *pdsa, DSA *sdsa);

int DSA_sign_buffer (const unsigned char *dgst, int len, unsigned char *sigret, unsigned int *siglen, DSA *dsa);

int DSA_verify_buffer (const unsigned char *dgst, int len, unsigned char *sigbuf, int siglen, DSA *dsa);