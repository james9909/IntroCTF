#include <stdio.h>
#include <stdlib.h>

char *flag = "XXXXXXXXXXXX";

int main() {
    setbuf(stdout, NULL);
    int grade = 0;
    char buffer[64];
    printf("To get the flag, you need good grades. Please input your grade:\n>> ");
    scanf("%s", buffer);
    if (grade == 100) { // This compares a string to a number...
        printf("Your grades look good! Here is the flag: %s\n", flag);
        return 0;
    }
    else {
        printf("Your grades aren't high enough... Your grade is a %i", grade);
        return 1;
    }
}
