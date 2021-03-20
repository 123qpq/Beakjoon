#include <stdio.h>

int main() {
    int T;
    int dp[41][2] = {{1, 0}, {0, 1}};
    for (int i = 2; i <= 40; i++) {
        dp[i][0] = dp[i-1][0] + dp[i-2][0];
        dp[i][1] = dp[i-1][1] + dp[i-2][1];
    }
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);
        printf("%d %d\n", dp[N][0], dp[N][1]);
    }
    return 0;
}