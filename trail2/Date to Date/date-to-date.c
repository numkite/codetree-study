#include <stdio.h>

int main() {
    // Please write your code here.
    int m1, m2, d1, d2;
    scanf("%d %d %d %d", &m1, &d1, &m2, &d2);

    int num_of_days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int now = 0;
    int end = 0;

    for (int i = 1; i <= m1; i++){
        if (i == m1){
            now += d1;
            break;
        }
        now += num_of_days[i];
    }

    for (int i = 1; i <= m2; i++){
        if (i == m2){
            end += d2;
            break;
        }
        end += num_of_days[i];
    }

    printf("%d", end - now + 1);

    return 0;
}