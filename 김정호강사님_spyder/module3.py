# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:01:09 2019

@author: student
"""
import random as rnd
class WordsGame:
    
    def __init__(self):
        self.words = "welcome"#"internationalization"
        self.hidden_size = int(len(self.words)*0.3)
        pass
    
    
    def make_index():
        hidden_index = []
        while True:
            temp = rnd.randrange(len(words))
            if temp not in hidden_index:
                hidden_index.append(temp)
            
            if len(hidden_index)==hidden_size:
                break
            pass
        return hidden_index
    
    hidden_index = make_index()
    print(hidden_index)
    hidden_letter = [words[i] for i in hidden_index]
    
    def display_word():
        for idx in range(len(words)):
            if idx not in hidden_index:
                print(words[idx],end=' ')
            else :
                print("_",end=' ')
                pass
            pass
        print()
        
        
        pass
    
    # while True:
    for i in range(6):    
        try_letter = input('please input letter >>> ')
        # 로직처리
        temp_number = []
        for idx,letter in enumerate(words):
            if try_letter == letter:
                temp_number.append(idx)
                pass
            pass
        
        if not temp_number:
            print('incorrect : {}'.format(try_letter))
            
        print('temp_number',temp_number)   
        for num in temp_number:
            if num in hidden_index:
                print('correct : {}'.format(try_letter))
                hidden_index.remove(num)
            
            # 처리결과
        print('hidden_index',hidden_index)
        display_word()
        # 출력함수 적용
        if len(hidden_index)==0:
            break
            pass
        pass
    
            