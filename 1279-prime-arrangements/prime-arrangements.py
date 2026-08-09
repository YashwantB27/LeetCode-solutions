class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Count primes from 1 to n
        prime_count = 0

        for i in range(2, n + 1):
            is_prime = True

            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_count += 1

        non_prime_count = n - prime_count

        # Prime numbers can be arranged among prime indices
        # Non-prime numbers can be arranged among non-prime indices
        return (math.factorial(prime_count) *
                math.factorial(non_prime_count)) % MOD