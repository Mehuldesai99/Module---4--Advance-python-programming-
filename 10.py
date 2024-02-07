#>>> 10.Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_path):
    word_frequency = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?()[]{}:;"\'').lower()
                    
                    if word:
                        word_frequency[word] = word_frequency.get(word, 0) + 1

        return word_frequency

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")

    frequency_dict = count_word_frequency(file_path)

    if frequency_dict:
        print("\nWord frequencies:")
        for word, count in frequency_dict.items():
            print(f"{word}: {count}")
