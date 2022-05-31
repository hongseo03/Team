
def main():
    while True:
        print("숫자를 뽑을 차레입니다. 4자리 숫자를 입력해주세요")
        goal=int(input("정답 숫자를 입력해주세요: "))
        if len(str(goal))!=4:
            print("4자리 숫자가 아닙니다. 다시 입력하세요")
        else:
            break
            
    print()
    
    tries=1
    while True:
        print("숫자를 맞출 차례입니다. 숫자를 한 개씩 입력해주세요")
        target=[]
        
        while len(target)<4:
            num=int(input("{}번째 숫자를 입력하세요: ".format(len(target)+1)))
            
            if num<0 or num>9:
                print("법위를 벗어나느 숫자입니다. 다시 입력하세요.")
            elif num in target:
                print("중복되는 숫자입니다. 다시 입력하세요")
            else:
                target.append(num)

    def score(goal, target):
        strike = 0
        ball = 0
        for i in range(3):
            if target[i] == goal[i]:
                strike += 1

        for i in range(3):
            if target[i] in answer and goal[i] != targer[i]:
                ball += 1
        if strike == 0 and ball == 0:
         result = out
        else:
         result = strike, ball

         return result

main()
a=score(goal, target)
print(a)
        
if a=='4S0B':
    print("축하합니다! 정답을 {}번의 시도만에 맞추셨습니다".format(tries))
     break
else:
    tries+=1
    print()

