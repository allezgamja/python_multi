# 프로그램이 시작되면 중복되지 않은 숫자 4개가 생성된다
# 사용자가 생성된 숫자를 힌트에 따라 모두 맞추는 게임
# 힌트
 # 사용자가 4자리 숫자를 한번에 입력하면 시스템은 생성한 숫자와 비교하여 결과 알려준다.
 # 숫자 자리와 숫자가 모두 같으면 스트라이크, 숫자 자리는 틀리고 같은 숫자가 있으면 볼로 판정하여 알려준다.
 # e.g. 생성숫자 5421 입력숫자 1458 -> 결과: 1스트라이크 1볼

class Baseball:
    def __init__(self):
        

import random
list = [0,1,2,3,4,5,6,7,8,9]
list
answer = random.sample(list, 4)

count = 0
count2 = 0
for num in range():
    for i, s in enumerate(list):
        if s == num & num[i] == answer[i]:
            count = count + 1
            pass
        if s == num & num[i] != answer[i]:
            count2 = count2 + 1
    if count == 4:
        print ('정답입니다')
    else:
        print(count, '스트라이크', count2, '볼')


# sample
        
from example.game import baseball

ball = baseball.DigitalBaseBall()
print(ball.hidden_number)
ball.game_start()