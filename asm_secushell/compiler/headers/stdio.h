#define NULL ((void*)0)
typedef struct _IO_FILE FILE;
extern FILE* stdin;
extern FILE* stdout;
extern FILE* stderr;
int printf(const char* format, ...);
