#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [n for n in num_list if n % 2==0]
    return even_num



input = [0,1,3,5,7,8,9]
print(return_evens(input))
    
    

def make_exclamation(sentence_list):
    new_exclamated_sentence =  [(sentence+'!') for sentence in sentence_list]
    return new_exclamated_sentence


input_sentences = ["Hello, how are you", "Have a nice day", "Python is awesome"]
print(make_exclamation(input_sentences))