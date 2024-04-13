#include <stdio.h>
#include <stdlib.h>
#include <openssl/evp.h>

void compute_md5(const char *filename) {  // Renommée de main à compute_md5
    unsigned char c[EVP_MAX_MD_SIZE];
    unsigned int md_len;
    FILE *inFile = fopen(filename, "rb");
    EVP_MD_CTX *mdContext;
    int bytes;
    unsigned char data[1024];

    if (inFile == NULL) {
        printf("Cannot open file: %s\n", filename);
        return;
    }

    mdContext = EVP_MD_CTX_new();
    if (!mdContext) {
        printf("Failed to create MD context\n");
        fclose(inFile);
        return;
    }

    if (EVP_DigestInit_ex(mdContext, EVP_md5(), NULL) != 1) {
        printf("Failed to initialize digest\n");
        fclose(inFile);
        EVP_MD_CTX_free(mdContext);
        return;
    }

    while ((bytes = fread(data, 1, 1024, inFile)) != 0) {
        if (EVP_DigestUpdate(mdContext, data, bytes) != 1) {
            printf("Failed to update digest\n");
            fclose(inFile);
            EVP_MD_CTX_free(mdContext);
            return;
        }
    }

    if (EVP_DigestFinal_ex(mdContext, c, &md_len) != 1) {
        printf("Failed to finalize digest\n");
        fclose(inFile);
        EVP_MD_CTX_free(mdContext);
        return;
    }

    fclose(inFile);
    EVP_MD_CTX_free(mdContext);

    printf("MD5 hash of \"%s\": ", filename);
    for (int i = 0; i < md_len; i++) printf("%02x", c[i]);
    printf("\n");
}