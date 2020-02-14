# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:38:39 2019

@author: student
"""

class FourCal:
    def __init__(self,firstdata,seconddata):
        self.first = firstdata
        self.second = seconddata
        pass
        
    def setdata(self,f,s):
        self.first = f
        self.second = s
        pass
    
    def add(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second
    pass

class MoreFourCal(FourCal):
    
    def power(self):
        return self.first ** self.second
    
    def div(self):
        result = 0
        if self.second != 0:
            result = self.first / self.second
            pass
        return result
    
    pass



