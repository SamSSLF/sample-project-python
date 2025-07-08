# comment test lorem ipsum dolor sit amet

from typing import List


class Fibonacci:
    @staticmethod
    def nth_fibonacci(n: int) -> int:
        """Calculate the nth number in the Fibonacci sequence

        Args:
            n (int): The position in the Fibonacci sequence (0-based)

        Returns:
            int: The nth Fibonacci number

        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Position must be non-negative")
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def fibonacci_sequence(n: int) -> List[int]:
        """Generate Fibonacci sequence up to n (inclusive)

        Args:
            n (int): Upper limit for the sequence

        Returns:
            List[int]: List of Fibonacci numbers up to n

        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Limit must be non-negative")
        
        sequence = [0]
        if n < 1:
            return sequence
        
        sequence.append(1)
        while sequence[-1] + sequence[-2] <= n:
            sequence.append(sequence[-1] + sequence[-2])
        
        return sequence
