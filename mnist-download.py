import urllib.request as req 
import gzip, os, os.path
savepath = "./mnist"
baseurl = "http://yann.lecun.com/exdb/mnist"   # 이 경로로 mnist data 요청
files = [
    "train-images-idx3-ubyte.gz",   # 이 파일을 baseurl뒤에 붙이기
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"]
# 다운로드
if not os.path.exists(savepath): os.mkdir(savepath) # savepath가 존재하면(mnist가있냐) true-> mkdir해달라, 존재하지않으면 false 
# http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz 이주소를 미리 알아내는 것
    for f in files:
    url = baseurl + "/" + f     #전체경로 하나 나왔다
    loc = savepath + "/" + f   # savepath는 파일명에 따라서 폴더를 따로 만든다.
    print("download:", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)  # 폴더가 있으면 이미 다운로드된적있다고 생각, 없으면 urlretrieve(url만 넘겨주면  http요청을 보내고 loc위치에 자동으로 다운로드)
# GZip 압축 해제
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, "rb") as fp:   # 해당경로에서 파일을 읽어들여서 그대로 내보낸다(압축풀기)
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("ok")