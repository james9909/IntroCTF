#include <stdio.h>
#include <stdlib.h>

char *flag = "that_wasnt_between_1_and_100";

int main() {
    int input = 0;
    printf("Give me a number from 1 to 100: ");
    scanf("%d", &input);
    if (input == 13333337) {
        printf("Good job, now here is the flag: %s\n", flag);
        return 0;
    }
    else {
        printf("WRONG! NO FLAG FOR YOU!!!! \n");
        return 1;
    }
}
