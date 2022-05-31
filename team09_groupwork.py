import pandas as pd
import numpy as np

a=int(input())
data=np.random.randint(1,11,size=(a,a))
df = pd.DataFrame(data)

print(df)

def f(a):                                #주어진 리스트의 모든 순열을 구하는 함수
    length=len(a)
    if length==1:                        # 리스트에 원소가 1개 밖에 없다면 인수로는 받았던 리스트를 반환
        return [a]
    else:
        result=[]
        for i in a:
            b=a.copy()                   # b에 인수로 받은 리스트를 복사
            b.remove(i)                  # 맨 앞자리에 i가 오는 경우 일단 b에서 i를 제거
            b.sort()                     # i가 제거된 b를 오름차순으로 정렬
            for j in f(b):               # b에 속한 원소들을 나열하는 순열의 모든 경우를 리스트로
                j.insert(0, i)           # 다시 맨 앞자리에 i를 추가
                if j not in result:      # result에 j 가 존재하지 않는다면 result에 j를 추가
                    result.append(j)
    return result

b=[i for i in range(a)]
print(f(b))

def g(x):             #작업 처리에 필요한 비용을 구하는 함수
    re=0                #할당 전 비용 0
    c=f(b)[x]           #x번째 순열
    for i in range(a):
        re+=df[i][c[i]]   #df의 i행 c[i]열 값의 총합(순열이므로 i != j이면 c[i] != c[j])
    return re           #비용 총합 반환

s=[]

for i in range(len(f(b))):
    s.append(g(i))           #모든 경우의 총 비용 s에 추가

s.sort()                   #s 크기 순 정렬
sol=[]
for i in range(len(f(b))):
    if s[0]==g(i):           #비용의 최솟값이 나오는 순열의 순서
        sol+=f(b)[i]           #위에서 찾은 순서의 순열 = sol




