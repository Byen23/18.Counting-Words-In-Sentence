# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17,2019

File: Countingwords.py
@author: Byen23
"""

# This will be my 18th program to be uploaed on Github.

sentence = input("Enter a sentence: ")
listofwords = sentence.split()
print("There are", len(listofwords), "words.")
sum = 0
for word in listofwords:
	sum += len(word)
print("The average word length is", sum / len(listofwords))

