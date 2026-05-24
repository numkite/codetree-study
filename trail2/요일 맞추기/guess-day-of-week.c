#include <stdio.h>

int main() {
    // Please write your code here.
    int m1, d1, m2, d2;
    int now = 0;
    int end = 0;

    scanf("%d %d %d %d", &m1, &d1, &m2, &d2);
    const char* week[7] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
    int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    for (int i = 1; i <= m1; i++){
        if (i == m1){
            now += d1;
            break;
        }
        now += month[i];
    }
    for (int i = 1; i <= m2; i++){
        if (i == m2){
            end += d2;
            break;
        }
        end += month[i];
    }

    int days = end - now;
    int idx = (1 + days) % 7;
    if (idx < 0) idx += 7;

    printf("%s", week[idx]);

    return 0;
}