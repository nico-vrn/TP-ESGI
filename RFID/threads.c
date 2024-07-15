#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

// Fonction pour simuler l'utilisation de CPU à 100%
void *cpu_max_usage(void *arg) {
    while (1) {
    }
    return NULL;
}

// Fonction pour simuler l'utilisation de CPU à 50%
void *cpu_half_usage(void *arg) {
    while (1) {
        for (int i = 0; i < 500000; i++); 
        usleep(500);                      
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <binary_message>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int num_threads = sysconf(_SC_NPROCESSORS_ONLN);
    pthread_t threads[num_threads];
    int is_max = argv[1][0] == '0';

    for (int i = 0; i < num_threads; i++) {
        if (is_max) {
            pthread_create(&threads[i], NULL, cpu_max_usage, NULL);
        } else {
            pthread_create(&threads[i], NULL, cpu_half_usage, NULL);
        }
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
