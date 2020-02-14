# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:36:24 2019

@author: student
"""
from example.gisa import gisa_data
class GisaTest:
    
    def __init__(self,lines):     # lines를 어디서 가져오는 것?
        self.students = self.make_student(lines)  # 순서 널뛰기 상관 x?
        pass
    
    def make_student(self,lines):
        data = []
        for line in lines:
            std_no = line[0:6]
            email = line[6:10]
            kor = int(line[10:13])
            eng = int(line[13:16])
            math = int(line[16:19])
            sci = int(line[19:22])
            hist = int(line[22:25])
            tot = int(line[25:28])
            mcode = line[28:29]
            acode = line[29:30]
            lcode = line[30:31]     # 왜 gisa_data와 gisa_test 분리?
            temp = gisa_data.GisaData(std_no,email,kor,eng,math,sci,hist,tot,mcode,acode,lcode)
            temp.calcu_q1()
            temp.calcu_q3()
            temp.calcu_q4()
            data.append(temp)
        return 
     
    def solve_1(self):   # 답은 어떻게 봄?  
        result = 0
        temp = sorted(self.students,key=lambda x: (-x.data1,x.stdno))
        result = temp[4].stdno
        return result
    
    def solve_2(self):
        result = 0
        temp = sorted(self.students,key=lambda x: -x.data1)
        #print(temp[0])
        result = temp[0].data1
        return result
    
    def solve_3(self):
        result = 0
        for stu in self.students:
            result += stu.data3
        return result
    
    def solve_4(self):
        result = 0
        for stu in self.students:
            result += stu.data4
        return result
    pass
