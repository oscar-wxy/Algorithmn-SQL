/*
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

Easy to trap:

when x < 0, n = -2^31, 
(1/x)^(-n) => (1/x)^(2^31), stackover flow, so we need a long
**/

class Solution {
    private double fastPow(double x, long n) {
        if (n == 0) {
            return 1.0;
        }
        double half = fastPow(x, n / 2);
        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        return fastPow(x, N);
    }
};