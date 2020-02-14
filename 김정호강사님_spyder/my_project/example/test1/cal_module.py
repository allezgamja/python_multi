# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:41:52 2019

@author: student
"""
import calendar as cal
class MyCalendar:
    
    def view_month(self,year,month):
        self.year = year
        self.month = month
        self.data = cal.monthrange(year,month)
        print(self.data)
        self.space = (self.data[0] + 1) % 7
        self.last_day = self.data[1]
        print('\t\t\t{}년 {}월\n'.format(self.year,self.month))
        print('일\t월\t화\t수\t목\t금\t토')
        print('\t'*self.space,end='')
        
        for i in range(1,self.last_day+1):
            print('{}\t'.format(i),end='')
            if (i+self.space) % 7 == 0:
                print()
                pass
            pass
        pass
    
    pass