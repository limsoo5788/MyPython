'''

# n개 배열에서 m개 만큼 숫자를 뽑고,
# focus X 가 존재하고, X가 target을 향해 좌, 우중 최적의 경로로 진행하도록

Size, Num = input().split()
Size = int(Size)
TargetList = [int(x) for x in input().split()]
QList = list(range(1, int(Size)+1))
Focus = 0
total = 0
Move = 0

print(QList, TargetList)

# QList = list(range(1, int(Size)+1))
# print(QList)

# 20칸의 큐라면 나 기준 -19칸, +19칸
# 방법 1
# 좌, 우 어디로 가야할지 알려주는 매서드
# 해당 방향으로 갔을때 몇칸 이동하는지 알려주는 매서드
# 칸수 종합하는 매서드+해당 위치 값 0 으로 변경하는 메인

# 방법 2
# 그냥 왼쪽 오른쪽 하나씩 이동해서 원하는 값 나올때까지 비교하는 방법

def HowManyMove(Size, QList, TargetNum, Focus):
    print("HowManyMove 시작!")
    Move = 0
    ToRight     = Focus
    ToLeft      = Focus

    while(QList[Focus] == 0):
        Focus = Focus +1
        
    if(QList[Focus]==TargetNum):
        return Move, Focus

    while (Move < Size):
        Move = Move +1
        ToRight     = ToRight +1
        ToLeft      = ToLeft -1

        if(ToRight >= Size):
            ToRight = 0
        if(ToLeft < 0) :
            ToLeft = Size-1

        print(Move, "회차", ToRight, ToLeft)
        while(QList[ToRight] == 0):
            print("ToRight 루프 진입", ToRight)
            ToRight = ToRight +1
            if(ToRight >= Size):
                ToRight = 0
        while(QList[ToLeft] == 0):
            print("ToLeft 루프 진입", ToLeft)
            ToLeft = ToLeft -1
            if(ToLeft < 0) :
                ToLeft = Size-1
        
        if(QList[ToRight] == TargetNum):
            Focus = ToRight
            break
        elif(QList[ToLeft] == TargetNum):
            Focus = ToLeft
            break;

    return Move, Focus


for TargetNum in TargetList:
    print("I Want : ", TargetNum)
    Move, Focus = HowManyMove(Size, QList, TargetNum, Focus)
    print("움직인 횟 수 : ", Move)
    total = total + Move

    QList[Focus] = 0
    print(QList)

print("총 이동", total)


# 좌, 우로 한칸씩 이동
# list 값이 0 이면 한칸 더 이동
# 이동할 떄 마다 over 여부 검사



#================================================

# 길이가 N인 정수 배열 A와 B
# 함수 S를 정의하자.



# 방법 1
# def Treasure(iSize, arA, arB):
#     for i in range(len(arA)):
#         iSmall = 999
#         iIdx = 0
#         for iNum in arB:
#             if(iSmall > iNum):
#                 iSamll = iNum
#         #가장 작은값이 어디 들었는지 찾기
#         print("arB: ", arB)
#         iIdx = arB.index(iSmall)
#         print("iIdx: ", iIdx)
#         arA[iIdx] = arC[i]

iSize = int(input())
arA = list(map(int, input().split()))
arB = list(map(int, input().split()))
S = 0

# 방법 2
# def Treasure(iSize, arA, arB):
#     arCopyB = arB[:]
#     arCopyB.sort()
#     arCopyA = arA[:]
#     arCopyA.sort(reverse=True)
#     for i in range(len(arA)):
#         iIdx = 0
#         # iIdx = arB.index(int(min(arB)))
#         iIdx = arB.index(arCopyB[i])
#         arA[iIdx] = arCopyA[i]
#     return arA

# 방법 3
# 즉 정렬 하지 않고 배열에서 작은 수를 차례대로 뽑아내는 방법?
def Treasure(iSize, arA, arB):
    arCopyA = arA[:]
    arCopyA.sort()
    for iNum in arCopyA:
        

if(len(arA) == iSize
    and len(arA) == iSize):
    arA = Treasure(iSize, arA, arB)
    for i in range(iSize):
        S += arA[i] * arB[i]
else:
    print("크기 불일치")

# print(iSize, arA, arB, "S = ", S)
print(arA)
print(S)

'''

# 2개의 수식 3개의 수 즉 5자리를 읽고
# 2*3-2
# 앞 수식이 플, 마, 곱, 나 일때 뒤에 수식이 플 마 곱 나 라면 
# 괄호를 n개 썻을떄도 연산해야할듯

# 플-플, 플-마, 
# 최대값이 나오게 하려면 곱은 최대한 크게
# 플러스 크게
# 마이너스 작게
# 나누기 최소로

# 음수 곱하기는 1순위
# 곱하기 앞뒤 숫자는 큰 양수여아한다
# 나누기 앞에값은 묶는다

# 곱, 플 뒤는 클수록 좋고
# 마, 나 뒤는 작을수록 좋다
# 묶기용 배열 만들고, 각자 우선순위 나열

# 곱-나-플-마 순의 수선순위를 넣고
# 3번 인덱스를 괄호하면 1, 5번은 괄호 불가
# 곱곱 노 4*4*4
# 곱나 ? 4*4/4 (뒷 값을 낮출 수 있다면) 
# 곱플 예 4*4+4
# 곱마 노 4*4-4

# 나곱 노 4/4*4 
# 나나 예 4/4/4
# 나플 노 4/4+4
# 나마 예 4/4-4

# 플곱 노 4+4*4 
# 플나 예 4+4/4
# 플플 노 4+4+4
# 플마 노 4+4-4

# 마곱 예 4-4*4
# 마나 예 4-4/4
# 마플 노 4-4+4
# 마마 노 4-4-4

# 곱플, 나나, 나마, 플나, 마곱, 마나
# 5자리씩 비교
# 어느 인덱스 수식을 묶었는지 저장하는 list 필요


# if(iSize != len(aList)):
#     print("달라")
# else:
#     print(aBracket)
#     for x in range(3, iSize, 2):
#         if not aBracket:
#             print("test")
#         else:
#             for BracketIdx in aBracket:
#                 if(x != BracketIdx-2
#                     and x != BracketIdx
#                     and x != BracketIdx+2):
#                     print(x, "이게되나?")

# 이 인덱스가 괄호에 적당한 인덱스인지 확인해서 true, false 내려 줘야할듯?
# 차라리 짝지어서 순위뽑고 우선순위 높은걸로 괄호치는게..?

iSize = int(input())
aList = input()
#aBracket = list()
aNumber = aList[0::2]
aMath = aList[1::2]
dic = [['*', '+'], ['/', '/'], ['/', '-'], ['+', '/'], ['-', '/'], ['-', '-']]


# aMath 를 순서대로 묶어서 우선순위 list에 넣기
aBracket = [0 for asdf in range(len(aMath))]
print(aMath)
for x in range(1, len(aMath)):
    #x는 연산 인덱스(맨 앞 연산자는 제외)
    zSerch = [aMath[x-1], aMath[x]]
    print("zSerch = ", zSerch)
    for y in range(len(dic)):
        #y는 우선순위(1~6순위)
        print("y = ", y)
        if(zSerch == dic[y]):
            #우선순위 list에 넣어주기
            aBracket[x] = y+1
            break
    print("우선순위 : ", aBracket)



# 1. 괄호를 우선 계산한다.
# 2. 좌에서 우로 계산한다.