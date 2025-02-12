# Task 4: Unique Word Counter 

sentence = input("Etner the sentence: ")

words = sentence.split()
unique_words = set(words)

print(len(unique_words))