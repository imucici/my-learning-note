class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.lower() == word:
            return True
        elif word.capitalize() == word :
            return True
        else:
            return False
