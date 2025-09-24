def palindrome_words(text):
    for word in text.split():
        cleaned_word = word.lower()
        if cleaned_word == cleaned_word[::-1]:
            yield word 


matn = "Anna va Otto uyga ketdi, level esa bordi"

for p in palindrome_words(matn):
    print(p)
