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


'''
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
def Treasure(iSize, arA, arB):
    arCopyB = arB[:]
    arCopyB.sort()
    arCopyA = arA[:]
    arCopyA.sort(reverse=True)
    for i in range(len(arA)):
        iIdx = 0
        # iIdx = arB.index(int(min(arB)))
        iIdx = arB.index(arCopyB[i])
        arA[iIdx] = arCopyA[i]
    return arA

if(len(arA) == iSize
    and len(arA) == iSize):
    arA = Treasure(iSize, arA, arB)
    for i in range(iSize):
        S += arA[i] * arB[i]
else:
    print("크기 불일치")

# print(iSize, arA, arB, "S = ", S)
print(S)