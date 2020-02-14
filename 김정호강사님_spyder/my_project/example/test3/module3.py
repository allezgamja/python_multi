# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:01:09 2019

@author: student
"""
import random as rnd
class WordsGame:
    
    def __init__(self):
        self.words = "internationalization"
        self.hidden_size = int(len(self.words)*0.3)
        self.hidden_index = self.make_index()
        pass
    
    
    def make_index(self):
        hidden_index = []
        while True:
            temp = rnd.randrange(len(self.words))
            if temp not in hidden_index:
                hidden_index.append(temp)
            
            if len(hidden_index)==self.hidden_size:
                break
            pass
        return hidden_index
    
    
    def display_word(self):
        for idx in range(len(self.words)):
            if idx not in self.hidden_index:
                print(self.words[idx],end=' ')
            else :
                print("_",end=' ')
                pass
            pass
        print()      
        pass
    
    def start_game(self):
        # while True:
        for i in range(6):    
            try_letter = input('please input letter >>> ')
            # 로직처리
            temp_number = []
            for idx,letter in enumerate(self.words):
                if try_letter == letter:
                    temp_number.append(idx)
                    pass
                pass
            
            if not temp_number:
                print('incorrect : {}'.format(try_letter))
                
            #print('temp_number',temp_number)   
            for num in temp_number:
                if num in self.hidden_index:
                    print('correct : {}'.format(try_letter))
                    self.hidden_index.remove(num)
                
                # 처리결과
            #print('hidden_index',self.hidden_index)
            self.display_word()
            # 출력함수 적용
            if len(self.hidden_index)==0:
                break
                pass
            pass
    
            