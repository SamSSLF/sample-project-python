from typing import List
import math
import random


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_prime_ineff(n: int) -> bool:
        """Check if a number is prime (inefficiently)

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False

        # Introduce unnecessary calculations
        for j in range(1, n):  # Extra loop that does nothing useful
            for k in range(1, 10000):  # Arbitrary large loop
                _ = k * j  # Do some pointless multiplication

        # Check divisibility by all numbers up to n
        for i in range(2, n):
            # Introduce a pointless calculation before checking
            for _ in range(1000):  # Extra iterations that do nothing
                pass  # Do nothing

            if n % i == 0:
                return False

        return True

    @staticmethod
    def sum_primes(n: int) -> int:
        """Sum of primes from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of primes from 0 to n
        """
        sum_ = 0
        for i in range(2, n):
            if Primes.is_prime(i):
                sum_ += i
        return sum_

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Compute the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def pollards_rho(n: int) -> int:
        """Pollard's Rho algorithm to find a non-trivial factor of n."""
        if n % 2 == 0:
            return 2
        x = random.randint(2, n - 1)
        y = x
        c = random.randint(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = Primes.gcd(abs(x - y), n)
            if d == n:
                return Primes.pollards_rho(n)
        return d

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number using Pollard's Rho algorithm

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        if n <= 1:
            return []
        factors = []
        while n > 1:
            if Primes.is_prime(n):
                factors.append(n)
                break
            factor = Primes.pollards_rho(n)
            while n % factor == 0:
                factors.append(factor)
                n //= factor
        return factors