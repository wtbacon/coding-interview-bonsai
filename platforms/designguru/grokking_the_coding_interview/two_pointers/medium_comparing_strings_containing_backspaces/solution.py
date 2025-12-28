class Solution:
    def compare(self, str1, str2):
        i1, i2 = len(str1) - 1, len(str2) - 1
        while i1 >= 0 and i2 >= 0:
            compared_idx1, compared_idx2 = (
                self._next_valid_char_idx(str1, i1),
                self._next_valid_char_idx(str2, i2),
            )

            if compared_idx1 < 0 and compared_idx2 < 0:
                return True
            if compared_idx1 < 0 or compared_idx2 < 0:
                return False
            if str1[compared_idx1] != str2[compared_idx2]:
                return False
            i1, i2 = compared_idx1 - 1, compared_idx2 - 1

        return True

    def _next_valid_char_idx(self, str, idx):
        backspace_counter = 0

        while idx >= 0:
            if str[idx] == "#":
                backspace_counter += 1
            elif str[idx] != "#" and backspace_counter > 0:
                backspace_counter -= 1
            elif str[idx] != "#" and backspace_counter == 0:
                break
            idx -= 1

        return idx
