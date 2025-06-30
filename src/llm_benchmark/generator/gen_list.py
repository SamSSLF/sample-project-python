from random import randint
from typing import List
import numpy as np


class GenList:
    @staticmethod
    def random_list(n: int, m: int) -> List[int]:
        """Generate a list of random integers

        Args:
            n (int): Number of integers to generate
            m (int): Maximum value of integers (exclusive)

        Returns:
            List[int]: List of random integers
        """
        return [randint(0, m) for _ in range(n)]

    @staticmethod
    def random_matrix(rows: int, cols: int) -> List[List[int]]:
        """Generate a matrix of random integers

        Args:
            rows (int): Number of rows
            cols (int): Number of columns

        Returns:
            List[List[int]]: Matrix of random integers
        """
        return np.random.randint(0, cols, size=(rows, cols)).tolist()