import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        translator = str.maketrans('', '', string.punctuation + 'n')

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.translate(translator)
                        words += line.lower().strip().split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        results = {}
        for file_name, words in all_words.items():
            word_lower = word.lower()
            if word_lower in words:
                first_position = words.index(word_lower) + 1
                results[file_name] = first_position
        return results

    def count(self, word):
        all_words = self.get_all_words()
        results = {}
        for file_name, words in all_words.items():
            word_lower = word.lower()
            count = words.count(word_lower)
            if count > 0:
                results[file_name] = count
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))