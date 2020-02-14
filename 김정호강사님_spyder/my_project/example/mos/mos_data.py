# -*- coding: utf-8 -*-

class Mos:
    def __init__(self):
        self.l1 = ['A', 'B', 'C']
        self.l2 = ['.-', '-...', '-.-.']
        
        pass
    
    def eng_to_mos(self, x):     # 알파벳 -> 모스부호
        self.x = list(x)
        for eng in self.x:
            for i,s in enumerate(self.l1):
                if s == eng:
                    print(self.l2[i], end = ' ')
        print()
        pass
    
    def mos_to_eng(self, x):       # 모스부호 -> 알파벳
        self.x = list(x)
        for mos in self.x:
            for i, s in enumerate(self.l2):
                if s == mos:
                    print(self.l1[i])


mos1 = Mos()
mos1.eng_to_mos('ABC')
mos1.mos_to_eng('-.-.','.-')