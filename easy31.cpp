#include <stdio.h>

int main() {
    int n; 
    scanf("%d", &n);
    for (int i = 0; i<n; i++) {
        for (int j = n-i-1; j<n; j++) {
            printf("*");
        }
        printf("\n");
    }

    for (int i = 0; i<2*n; i++) printf("-");
    printf("\n");

    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            if (i+j+1 < n) printf(" ");
            else printf("*");
        }
        printf("\n");
    }

    for (int i = 0; i<2*n; i++) printf("-");
    printf("\n");

    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            if (i+j == n-1) printf("*") ;
            else printf(" ");
        }
        for (int j = n-2; j>=0; j--) {
            if (i+j == n-1) printf("*") ;
            else printf(" ");
        }
        printf("\n");
    }

    for (int i = 0; i<2*n; i++) printf("-");
    printf("\n");

    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            if (i+j == n-1) printf("*") ;
            else if (i == j) printf("*");
            else printf(" ");
        }
        printf("\n");
    }

    for (int i = 0; i<2*n; i++) printf("-");
    printf("\n");

    for (int i = 0; i<n; i++) {
        for (int j = (n+1)%2; j<n; j++) {
            if (i+j < n/2) printf(" ");
            else if (j-i > n/2) printf(" ");
            else if (i-j > (n-1)/2) printf(" ");
            else if (i+j > n+(n/2)-1) printf(" ");
            else printf("*");
        }
        printf("\n");
    }

    for (int i = 0; i<2*n; i++) printf("-");
    printf("\n");


    n = n*2-1;
    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            if (i+j < n/2) printf("A");
            else if (j-i > n/2) printf("B");
            else if (i-j > n/2) printf("C");
            else if (i+j > n-1+(n/2)) printf("D");
            else if (i+j == n/2) printf("*");
            else if (j-i == n/2) printf("*");
            else if (i-j == n/2) printf("*");
            else if (i+j == n-1+(n/2)) printf("*");
            else printf("E");
        }
        printf("\n");
    }

}