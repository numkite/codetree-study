#include <stdio.h>

int A, B, C, D;

int main() {
    scanf("%d %d %d %d", &A, &B, &C, &D);
    
    // Please write your code here.
    int now = 0;
    int end = 0;
    now = A * 60 + B;
    end = C * 60 + D;

    printf("%d", end - now);
    
    return 0;
}