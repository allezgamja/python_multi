# 희소행렬(Sparse Matrix)

희소행렬이란 행렬 안의 많은 항들이 0으로 되어있는 행렬. 예를 들어 txt1에는 '이상해씨'라는 단어가 10000번 나왔는데 txt2~txt100에는 한 번도 안 나온다면, 모든 문서에 나오는 단어들을 하나의 행렬로 만들 때, 지나치게 많은 항들이 0이 되어 메모리 낭비가 심해진다. 따라서 아래와 같이 행렬 내의 0이 아닌 값들을 추려 그 정보만 저장한다.

![sparse1](https://user-images.githubusercontent.com/51535130/73839862-49c31680-485a-11ea-9aad-1ed37e0c2fcf.png)

![sparse2](https://user-images.githubusercontent.com/51535130/73839873-4d569d80-485a-11ea-9f98-ed48dd66c0e6.png)



### 방법

1) COO(Coordinate Format): (행, 열, 값)의 튜플로 저장

2) CSR(Compressed Sparse Row Format): 가로 순서대로 재정렬. 행에 관여하여 정리압축

![sparse3](https://user-images.githubusercontent.com/51535130/73840182-f1d8df80-485a-11ea-9fa3-42f4c3a47549.png)



참고자료: https://m.blog.naver.com/PostView.nhn?blogId=demonic3540&logNo=221247954709&proxyReferer=https%3A%2F%2Fwww.google.com%2F

http://scipy-lectures.org/advanced/scipy_sparse/index.html

[https://ko.wikipedia.org/wiki/%ED%9D%AC%EC%86%8C%ED%96%89%EB%A0%AC#Coordinate_list_(COO)](https://ko.wikipedia.org/wiki/희소행렬#Coordinate_list_(COO))