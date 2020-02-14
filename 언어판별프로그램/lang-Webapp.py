#!/usr/bin/env python3
import cgi, os.path
from sklearn.externals import joblib
# 학습 데이터 읽어 들이기*******
pklfile = os.path.dirname(__file__) + "/freq.pkl"  # __file__: .pkl까지가 경로. dirname= directory name (/freq.pkl) 나랑 같은 경로에 있는 pkl파일 
clf = joblib.load(pklfile)
# 텍스트 입력 양식 출력하기
def show_form(text, msg=""):     # html 만드는 코드
    print("Content-Type: text/html; charset=euc-kr")
    print("")
    print("""
        <html><body><form>
        <textarea name="text" rows="8" cols="40">{0}</textarea>
        <p><input type="submit" value="판정"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(cgi.escape(text), msg))
# 판정하기
def detect_lang(text):
    # 알파벳 출현 빈도 구하기
    text = text.lower() 
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)]
    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n < 26: cnt[n] += 1
    total = sum(cnt)
    if total == 0: return "입력이 없습니다"
    freq = list(map(lambda n: n/total, cnt))
    # 언어 예측하기
    res = clf.predict([freq])
    # 언어 코드를 한국어로 변환하기
    lang_dic = {"en":"영어","fr":"프랑스어",
        "id":"인도네시아어", "tl":"타갈로그어"}
    return lang_dic[res[0]]
# 입력 양식의 값 읽어 들이기
form = cgi.FieldStorage()   #입력상자 - 상호작용. 이때까지는 출력결과 없는 상태라 form이 null값
text = form.getvalue("text", default="")   # 이때도 값이 없다. null
msg = ""
if text != "":    # text가 null이 아니라면 판정...판졍결과_lang
    lang = detect_lang(text)
    msg = "판정 결과:" + lang
# 입력 양식 출력
show_form(text, msg)   # show_form 함수로 뛴다.