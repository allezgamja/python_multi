# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:14:00 2019

@author: student
"""
class GisaData:
    
    def __init__(self,s,e,k,eng,m,sci,h,t,mc,ac,lc):
        self.stdno = s
        self.email = e
        self.kor = k
        self.eng = eng
        self.math = m
        self.sci = sci
        self.hist = h
        self.tot = t
        self.mcode = mc
        self.acode = ac
        self.lcode = lc
        self.data1 = 0
        self.data3 = 0
        self.data4 = 0
        pass
    
    def calcu_q1(self):
        
        if self.lcode=="B":
            self.data1 = self.kor + self.eng
        pass
    
    def calcu_q2(self):
    
        pass
    
    def calcu_q3(self):    
        self.data2 = self.eng + self.math
        if self.data2 >=120:
            point = 2
            if self.mcode == "A":
                point = 5
            elif self.mcode == "B":
                point = 15
                pass
            self.data3= point + self.data2
            pass
        
        pass
    
    def calcu_q4(self):
        
        point = 15
        if self.lcode == "A" :
            point = 5
        elif self.lcode == "B":
            point = 10
            pass
        temp = self.kor + point
        if self.acode=="A" or self.acode == "B":
            if temp >= 50:
                self.data4 = 1         # data4 += 1 아님?
            pass
        pass
    
    def __str__(self):
        return "{} {} {:>3} {:>3} {:>3} {:>3} {} {} {}".format(self.stdno,self.tot,self.data1,self.data2,self.data3,self.data4,self.mcode,self.acode,self.lcode)
    pass
