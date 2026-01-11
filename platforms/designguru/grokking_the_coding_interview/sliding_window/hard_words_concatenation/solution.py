from collections import defaultdict


class Solution:
    def findWordConcatenation(self, str1: str, words: list[str]):
        result_indices = []
        words_count, word_length = len(words), len(words[0])
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1

        for i in range(len(str1) - (word_length * words_count) + 1):
            words_seen = defaultdict(int)
            for j in range(0, words_count):
                seeing_word_first_index = i + (word_length * j)
                seeing_word = str1[seeing_word_first_index : seeing_word_first_index + word_length]

                if seeing_word not in word_freq:
                    break

                # Add the word to the map on the `i` iteration
                words_seen[seeing_word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[seeing_word] > word_freq[seeing_word]:
                    break
                
                # If you can end the iteration without break, the window starting from `i` is success
                if j + 1 == words_count:
                    result_indices.append(i)

        return result_indices
