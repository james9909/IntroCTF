#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char *flag = "not_rigged";

void election_results(int length, char *flag_to_give, char *result) {
    int votes = rand() % 100;
    printf("Here are the results:\n");
    printf("You got %d votes!\n", votes);
    if (votes > 500) {
        printf("You win!");
    } else {
        printf(result);
    }
}

int main() {
    srand(time(NULL));
    setbuf(stdout, NULL);
    char result[96] = "You lose!";
    char name[64];
    bzero(name, 64);

    printf("Hello, candidate. What is your name?\n");
    fgets(name, sizeof(name) + sizeof(result), stdin);

    printf("Welcome to elections, %s", name);
    election_results(strlen(flag), flag, result);

    fflush(stdout);
    return 0;
}
