class Solution:
    def checkIfPangram(self, sentence):
        unique_letters = set()
        for char in sentence:
            char_code = ord(char)
            if char_code in range(65, 91) or char_code in range(97, 123):
                unique_letters.add(char.lower())

        if len(unique_letters) == 26:
            return True
        return False
