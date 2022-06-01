import pandas as pd
import numpy as np
import logging

logger=logging.getLogger("main")        # logger 설정
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)          # 모든 로그를 남김

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

def g(x):             #작업 처리에 필요한 비용을 구하는 함수
    re=0                #할당 전 비용 0
    c=f(b)[x]           #x번째 순열
    for i in range(a):
        re+=df[i][c[i]]   #df의 i행 c[i]열 값의 총합(순열이므로 i != j이면 c[i] != c[j])
    return re           #비용 총합 반환

logger.info("프로그램 시작")                  # 예외처리

try:
    a=input()
    if a not in ['1','2','3','4','5','6']:  # 입력값이 1~6 사이의 integer 형식이 아닐 경우 에러 발생
        raise Exception()
except Exception as e:
    logger.error("부적절한 입력값입니다.")        # 에러메세지
else: 
    a=int(a)
    data=np.random.randint(1,11,size=(a,a))
    logger.debug("dataframe 생성")
    df = pd.DataFrame(data)
    logger.debug(df)
    b=[i for i in range(a)]
    s=[]

    for i in range(len(f(b))):
        s.append(g(i))           #모든 경우의 총 비용 s에 추가
    logger.debug("비용의 모든 경우의 수")
    logger.debug(s)
    s.sort()                   #s 크기 순 정렬
    sol=[]
    for i in range(len(f(b))):
        if s[0]==g(i):           #비용의 최솟값이 나오는 순열의 순서
            sol+=f(b)[i]           #위에서 찾은 순서의 순열 = sol
            
    if len(sol)>a               # 동일한 최솟값이 2개 이상이 경우
        logger.warning("최솟값이 나오는 경우가 2개 이상입니다.")
    sol=sol[0:a]
    logger.debug("최솟값을 가지는 경우")
    logger.debug(sol)
    machine=['m_'+str(i) for i in range(a)]
    work=['w_'+str(i) for i in range(a)]
    logger.debug("기계의 종류")
    logger.debug(machine)
    logger.debug("작업의 종류")
    logger.debug(work)
    c=[machine[i]+' : '+work[sol[i]] for i in range(a)]   
    logger.debug("최적화되 기계와 작업의 매핑")
    logger.debug(c)
      
