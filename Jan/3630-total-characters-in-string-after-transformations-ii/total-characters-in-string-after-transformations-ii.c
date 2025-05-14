#define MOD 1000000007
#define L 26

typedef struct {
    int a[L][L];
} Mat;

/* identity matrix */
Mat I() {
    Mat m;
    memset(&m, 0, sizeof(m));
    for (int i = 0; i < L; i++) {
        m.a[i][i] = 1;
    }
    return m;
}

Mat mul(Mat x, Mat y) {
    Mat res;
    memset(&res, 0, sizeof(res));
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < L; j++) {
            for (int k = 0; k < L; k++) {
                res.a[i][j] =
                    (res.a[i][j] + (long long)x.a[i][k] * y.a[k][j]) % MOD;
            }
        }
    }
    return res;
}

/* matrix exponentiation by squaring */
Mat quickmul(Mat x, int y) {
    Mat ans = I();
    Mat cur = x;
    while (y > 0) {
        if (y & 1) {
            ans = mul(ans, cur);
        }
        cur = mul(cur, cur);
        y >>= 1;
    }
    return ans;
}

int lengthAfterTransformations(char* s, int t, int* nums, int numsSize) {
    Mat T;
    memset(&T, 0, sizeof(T));
    for (int i = 0; i < L; i++) {
        for (int j = 1; j <= nums[i]; j++) {
            T.a[(i + j) % L][i] = 1;
        }
    }

    Mat res = quickmul(T, t);

    int f[L] = {0};
    for (char* p = s; *p; p++) {
        f[*p - 'a']++;
    }

    int ans = 0;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < L; j++) {
            ans = (ans + (long long)res.a[i][j] * f[j]) % MOD;
        }
    }
    return ans;
}