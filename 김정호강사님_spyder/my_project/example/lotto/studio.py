# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:30:39 2019

@author: student
"""
import random as rnd
class LottoBall:
    def __init__(self,n):
        self.number = n
        pass
    
    def __str__(self):
        return str(self.number) 
    pass

class LottoMachine:
    
    def set_balls(self,balls):
        self.balls = balls
        pass
    
    def start_selection(self):
        select_numbers = []
        for i in range(6):
            ball = self.select_ball()
            select_numbers.append(ball)
            pass
        return select_numbers
    
    
    def select_ball(self):
        index = rnd.randrange(len(self.balls))
        ball = self.balls.pop(index)
        return ball
    
    pass