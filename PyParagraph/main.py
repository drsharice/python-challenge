#!/usr/bin/python

import re

with open('Resources/text.txt') as infile:
    data = infile.read()

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in data:
    line = line.strip("\n")
    words = line.split()
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(data)

sentence_pat = re.compile(r"""
    \b                # sentences will start with a word boundary
    ([^.!?]+[.!?]+)   # continue with one or more non-sentence-ending
                      #    characters, followed by one or more sentence-
                      #    ending characters.""", re.X)

word_pat = re.compile(r"""
    (\S+)             # Words are just groups of non-whitespace together
    """, re.X)
character_pat =re.compile(r"""
    (\S+)            
    """, re.X) 

sentences = sentence_pat.findall(data)
words = word_pat.findall(data)
characters = character_pat.findall(data)

average_sentence_length = sum([len(sentence) for sentence in sentences])/len(sentences)
average_word_length = sum([len(word) for word in words])/len(words)
average_character_length = sum([len(character) for character in characters])/len(characters)
str_word = str(number_of_words)
str_sentence = str(number_of_lines)
str_average_character_length = str(average_character_length)
str_average_sentence_length = str(average_sentence_length)

print("Paragraph Analysis")
print("------------------")
print("Approximate Word Count: " +str_word)
print("Approximate Sentence Count: " +str_sentence)
print("Average Letter Count: " +str_average_character_length)
print("Average Sentence Length: " +str_average_sentence_length)

