"""Task 2: Palindrome Finder.

This script finds all the palindromes in a given text.
"""

text = """
Вчера Анна и Артем гуляли в парке. Анна заметила слово level на
старом плакате. Рядом кто-то написал radar, а чуть дальше было
нарисовано слово kayak. На скамейке сидел человек с книгой civic,
а возле фонтана дети мелом написали refer. Остальные слова в тексте
палиндромами не являются.
"""

split_text = text.split()

polyndromes = []

for word in split_text:
    word = word.strip("\n., ").lower()
    if word == word[::-1] and len(word) > 2:
        if word not in polyndromes:
            polyndromes.append(word)

print(polyndromes)
