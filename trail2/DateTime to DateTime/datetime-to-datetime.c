#include <stdio.h>

int main() {
    // Please write your code here.
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int now = 11 + 11 * 60 + 11 * 24 * 60;
    int end = c + b * 60 + a * 24 * 60;

    if (end < now){
        printf("-1");
    }
    else {
        printf("%d", end - now);
    }

    return 0;
}