#include <stdio.h>

int main() {
    int n;
    while (true) {
        scanf("%d", &n);
        if (n%400 == 0) printf("true");
        else if (n%100 != 0 && n%4 == 0) printf("true");
        else printf("false");
    }
}