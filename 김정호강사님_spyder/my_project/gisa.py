# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:42:16 2019

@author: student
"""

from example.gisa import gisa_test
file = open('./data/Abc1115.txt')
lines = file.readlines()
file.close()
#print(lines[0:5])
test = gisa_test.GisaTest(lines)

r1 = test.solve_1()
print(r1)
r2 = test.solve_2()
print(r2)    
r3 = test.solve_3()
print(r3)
r4 = test.solve_4()
print(r4)

output = open('./data/answers.txt','w')
output.write("{}\n".format(r1))
output.write("{}\n".format(r2))
output.write("{}\n".format(r3))
output.write("{}\n".format(r4))
output.close()


'''
sample = test.students[0:10]
for s in sample:
    #print(s)
    pass

count = 0
tot = 0
for stu in test.students:
    if stu.data3 > 0:
        count += 1
        tot += stu.data3
        print(stu)
        pass
    pass

print(count,tot)
'''