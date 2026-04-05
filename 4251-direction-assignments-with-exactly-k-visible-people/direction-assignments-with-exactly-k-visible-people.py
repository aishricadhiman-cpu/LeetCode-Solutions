class Solution(object):
    def countVisiblePeople(self, n, pos, k):
        """
        :type n: int
        :type pos: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # factorial
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD

        # inverse factorial
        inv = [1] * (n + 1)
        inv[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n-1, -1, -1):
            inv[i] = inv[i+1] * (i+1) % MOD

        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv[r] % MOD * inv[n-r] % MOD

        return nCr(n-1, k) * 2 % MOD
        