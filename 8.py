# >>> 8.Write a python program to find the longest words. 

def find_longest_words(words_list):
    max_length = max(len(word) for word in words_list)
    longest_words = [word for word in words_list if len(word) == max_length]
    return longest_words

word_list = ["apple", "banana", "orange", "strawberry", "kiwi", "pineapple"]

longest_words = find_longest_words(word_list)
print("Longest word(s):", longest_words)