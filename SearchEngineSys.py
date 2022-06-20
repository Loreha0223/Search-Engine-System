import pandas as pd # 데이터프레임 사용
from math import log # IDF 계산
from konlpy.tag import Kkma, Komoran, Okt # 형태소 분석
import itertools #중복 단어 계산
from numpy import dot 
from numpy.linalg import norm

### read txt file
f = open("full_corpus.txt", "r")
docs = f.read().split("<title>")
docs = [i.strip() for i in docs]
docs.pop(0)
f.close()

### declare function
N = len(docs)        # 총 문서의 수

def tf(t, d):
  return d.count(t)

def idf(t):
  df = 0
  for doc in docs:
    df += t in doc
  return log(N/(df+1))

def tfidf(t, d):
  return tf(t,d)* idf(t)

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

################# Indexing Time ###################
### 형태소 분류기 호출
komoran = Komoran()
okt = Okt()
apb=[] # 단어 저장(중복x)

### 추출된 단어 리스트에 다 때려박기
for i in docs:
    doc_i = komoran.nouns(i)
    apb.append(doc_i)
    doc_i = okt.nouns(i)
    apb.append(doc_i)
apb = list(set(itertools.chain(*apb))) # 중복단어 제거

### docs에 있는 단어 전부 tf-idf 계산
result=[]
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(apb)):
        t = apb[j]
        result[-1].append(tfidf(t,d))
result.append([]) # query를 docs처럼 취급
#df = pd.DataFrame(result, columns = apb)

################ Query Time ##################
result[N]=[0]*len(apb) # 검색시 항상 query 초기화
query = []
q = input("검색창 > ")
q_d = komoran.nouns(q)
query.append(q_d)
q_d = okt.nouns(q)
query.append(q_d)
query = list(set(itertools.chain(*query)))
#print(query)

### query에 있는 단어
for d in query:
    if d not in apb:
        continue
    result[N][apb.index(d)] = tfidf(d,d)
#print(result[N])


answer = []
### 어느 doc과 유사한지 계산
for i in range(len(docs)):
    cos = cos_sim(result[i], result[N])
    if cos!=0:
        answer.append([i+1, cos])
        #print("doc",i+1,":", cos)
answer.sort(key=lambda x:-x[1])

#print(answer)

print("검색결과는 >> doc ", end='')
cnt = 0
for i in range(len(answer)):
    if cnt==5: break
    print(answer[i][0], end=",")
    cnt+=1
print('\b')