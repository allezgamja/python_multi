# botengine.py는 파일을 실제로 실행하는 기능
# 응답을 내보낼 때 주어진 정보를 토대로 하여 자동으로 만든다.

import codecs
from bs4 import BeautifulSoup
import urllib.request
from konlpy.tag import Twitter
import os, re, json, random
dict_file = "chatbot-data.json"
dic = {}
twitter = Twitter()
# 딕셔너리에 단어 등록하기 --- (※1)
def register_dic(words):
    global dic
    if len(words) == 0: return
    tmp = ["@"]          # 단어세트의 첫 시작을 @로 알린다.
    for i in words:
        word = i[0]
        if word == "" or word == "\n" or word == "\n": continue  # 단어의 첫글자가 공백 혹은 엔터면 continue
        tmp.append(word)       # 공백 혹은 엔터가 아니라면 tmp 리스트에 추가
        if len(tmp) < 3: continue  # tmp에 담긴 단어가 3개 미만이면 continue
        if len(tmp) > 3: tmp = tmp[1:]  # 3개 이상이면 제일 처음의 단어 빼고 다시 시작 ---> 결국 단어가 세 개씩 리스트에 돌아가면서 저장됨
        set_word3(dic, tmp)
        if word == "." or word == "?": # 단어의 첫 글자가 .이나 ?이면 다시 문장이 시작한다고 보고 tmp=["@"]
            tmp = ["@"]
            continue
    # 딕셔너리가 변경될 때마다 저장하기
    json.dump(dic, open(dict_file,"w", encoding="utf-8"))
# 딕셔너리에 글 등록하기
def set_word3(dic, s3):   # 딕셔너리 구조화해서 보여주도록 하는 함수
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1
# 문장 만들기 --- (※2)
def make_sentence(head):
    if not head in dic: return ""
    ret = []
    if head != "@": ret.append(head)        
    top = dic[head]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        if w1 in dic and w2 in dic[w1]:
            w3 = word_choice(dic[w1][w2])
        else:
            w3 = ""
        ret.append(w3)
        if w3 == "." or w3 == "？ " or w3 == "": break
        w1, w2 = w2, w3
    ret = "".join(ret)
    # 띄어쓰기
    params = urllib.parse.urlencode({
        "_callback": "",
        "q": ret
    })
    # 네이버 맞춤법 검사기를 사용합니다.
    #data = urllib.request.urlopen("https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn?" + params)
    #data = data.read().decode("utf-8")[1:-2]
    #data = json.loads(data)
    #data = data["message"]["result"]["html"]
    #data = soup = BeautifulSoup(data, "html.parser").getText()
    # 리턴
    return ret

def word_choice(sel):    # 랜덤으로 다음 단어 고르는 함수
    keys = sel.keys()
    return random.choice(list(keys))

def spell(s):
    import requests
    data={}
    data["sentence"]=s.encode("utf-8")
    r = requests.post("https://alldic.daum.net/grammar_checker.do", data=data)
    soup = BeautifulSoup(r.text,'html.parser')
    result=[]
    for text in soup.find_all('a'):
        if not text.get('data-error-output') == None:
            a=text.get('data-error-output')
            result.append(a)
    return(result)

# 챗봇 응답 만들기 --- (※3)
def make_reply(text):
    # 단어 학습시키기 ---> 사용자가 입력하는 단어 학습시키기
    if not text[-1] in [".", "?"]: text += "."
    words = twitter.pos(text)   # .pos: 형태소분석해서 품사 태그해주는 역할
    register_dic(words)
    # 사전에 단어가 있다면 그것을 기반으로 문장 만들기
    for word in words:
        face = word[0]
        if face in dic: return make_sentence(face)
    return make_sentence("@")
# 딕셔너리가 있다면 읽어 들이기
if os.path.exists(dict_file):
    dic = json.load(open(dict_file,"r"))