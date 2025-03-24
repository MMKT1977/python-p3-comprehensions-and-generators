#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [n for n in num_list if n % 2==0]
    return even_nums
return_evens(num_list=(1,7,9,6,13,11))

def make_exclamation(sentence_list):
    return [new_sentence + "!" for new_sentence in sentence_list]
make_exclamation(sentence_list=("Who are you","Why are you here","Tell me"))