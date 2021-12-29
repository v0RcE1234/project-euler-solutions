
import csv

l = list(csv.reader(open('C:\\Users\\Rohan\\Downloads\\p042_words.txt')))
words = l[0]

# generate first 20 triangular numbers
triangleNumbers = [1]
for i in range(2, 20):
    triangleNumbers.append(triangleNumbers[-1]+i)

def char_positon(letter):
    return ord(letter.lower()) - 96

def get_word_value(word):
    out = 0
    for char in word:
        out += char_positon(char)
    return out

totalTriangleWords = 0
for word in words:
    if get_word_value(word) in triangleNumbers:
        totalTriangleWords += 1
        
print(totalTriangleWords)