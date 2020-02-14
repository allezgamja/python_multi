# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:27:04 2019

@author: student
"""
import random as rnd
class DigitalBaseBall:
    
    def __init__(self):
        self.hidden_number = self.make_number()
        
        pass
    
    def make_number(self):    
        temp_number = None
        while True:
            temp_number = str(rnd.randrange(1000,10000))
            flag = self.is_same_number(list(temp_number))
            if not flag:
                break
        return list(temp_number)
    
    
    def is_same_number(self,num_list):
        flag = False
        while num_list:
            temp = num_list.pop()
            if temp in num_list:
                flag = True
                break
        return flag
    
    def game_start(self):
        
        for i in range(10):
           try_number = input("please number input >>> ") 
           (strike,ball) = self.judge(list(try_number))
           print(" {} strike(s), {} ball(s)".format(strike,ball))
           if strike==4:
               print('good job')
               break
           pass
        pass
    
    def judge(self,try_list):
        temp = None
        strike = 0
        ball = 0
        for i in range(4):
            for j in range(4):
                if self.hidden_number[i]==try_list[j]:
                    if i==j:
                        strike += 1
                    else:
                        ball += 1
                        pass
                    pass
                pass
            pass
        temp = (strike,ball)
        return temp
    
    pass