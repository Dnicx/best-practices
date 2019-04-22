#include <stdio.h>

int main() {
    int n;
    int plist[10000] = { };
    plist[0] = 2;
    int ct = 1;
    scanf("%d", &n);
    if (n < 2) printf("none");
    bool p = true;
    for (int i = 2; i<=n; i++) {
        p = true;
        int temp = 0;
        // printf("temp = %d", temp);
        while (temp < ct && plist[temp] <= i/2) {
            if (i%plist[temp] == 0 ){
                p = false;
                break;
            }
            temp++;
        }
        if (p) {
            if (i > plist[ct])
            plist[ct++] = i;
            printf("%d ", i);
        }
    }
}