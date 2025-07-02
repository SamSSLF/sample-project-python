class StrOps:
    @staticmethod
    def str_reverse(s: str) -> str:
        return s[::-1]

    @staticmethod
    def palindrome(s: str) -> bool:
        return s == s[::-1]