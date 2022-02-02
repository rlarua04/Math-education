import random


def radiusVector():
    while True:
        detailkategorie = int(input("세부 카테고리의 번호를 입력해주세요. (동경의 일반각 : 1, 제N사분면 : 2) : "))
        
        if detailkategorie == 1:
            while True:
                randomNum = random.randrange(-110, 111) * 10
                result = randomNum % 360  
                print(f"{randomNum}의 일반각을 구하시오.")
                if int(input("(360 * n + a) a에 들어갈 값을 입력해주세요. : ")) == result:
                    print("정답")
                else:
                    print("오답")
                    
                if int(input("{0:-^50}".format('계속하기 : 1, 뒤로가기 : 2'))) == 2:
                    break
        elif detailkategorie == 2:
            while True:
                randomNum = random.randrange(-110, 111) * 10
                result = randomNum % 360 
                if 0 < result and result < 90:
                    quadrant = 1
                elif 90 < result and result < 180:
                    quadrant = 2
                elif 180 < result and result < 270:
                    quadrant = 3
                elif 270 < result and result < 360:
                    quadrant = 4
                else:
                    quadrant = 5 # 예외처리
                    
                print(f"{randomNum}의 동경이 위치하는 사분면을 입력해주세요. *어느 사분면에도 속하지 않으면 5를 입력")
                if int(input("제n사분면의 n을 입력해주세요. : ")) == quadrant: # 1,2,3,4 사분면 구분하기
                    print("정답")
                else:
                    print("오답")
                    
                if int(input("{0:-^50}".format('계속하기 : 1, 뒤로가기 : 2'))) == 2:
                    break
                    
        if int(input("{0:-^50}".format('다른 세부 카테고리 선택 : 1, 뒤로가기 : 2'))) == 2:
            break

def sector():
    while True:
        detailkategorie = int(input("세부 카테고리의 번호를 입력해주세요. (호의 길이와 넓이 : 1, 중심각의 크기와 반지름의 길이 : 2) : "))
        if detailkategorie == 1:
            while True:
                radius = random.randrange(1,13) #반지름
                centralAngle = [random.randrange(1, 9), random.randrange(1, 9)] #중심각
                resultArc = reduceFraction(centralAngle[0] * radius, centralAngle[1]) #호의 길이
                resultArea = reduceFraction(radius, 2) #넓이 계산중
                resultArea[0] *= resultArc[0] #넓이 계산중 
                resultArea[1] *= resultArc[1] #넓이 계산중
                resultArea = reduceFraction(resultArea[0], resultArea[1]) #넓이
                
                print(f"반지름 : {radius}")
                print(f"중심각 : {centralAngle[0]}/{centralAngle[1]}파이")
                
                if input("호의 길이를 입력해주세요. (입력 예시 : 2/3파이) : ") == str(resultArc[0]) + "/" + str(resultArc[1]) + "파이":
                    print("정답")
                else:
                    print("오답")
                    
                if input("넓이를 입력해주세요. (입력 예시 : 2/3파이) : ") == str(resultArea[0]) + "/" + str(resultArea[1]) + "파이":
                    print("정답")
                else:
                    print("오답")
                    
                if int(input("{0:-^50}".format('계속하기 : 1, 뒤로가기 : 2'))) == 2:
                    break
        elif detailkategorie == 2:
            while True:
                arc = random.randrange(1,9)
                area = random.randrange(4, 50)
                resultRadius = reduceFraction(area * 2, arc)
                resultcentralAngle = reduceFraction(arc * resultRadius[1], resultRadius[0])
                
                print(f"호의 길이 : {arc}")
                print(f"넓이 : {resultRadius[0]}파이")
                
                if input("반지름을 입력해주세요. (입력 예시 : 2/3파이) : ") == str(resultRadius[0]) + "/" + str(resultRadius[1]) + "파이":
                    print("정답")
                else:
                    print("오답")
                    
                if input("중심각의 크기를 입력해주세요. (입력 예시 : 2/3파이) : ") == str(resultcentralAngle[0]) + "/" + str(resultcentralAngle[1]) + "파이":
                    print("정답")
                else:
                    print("오답")
                
                if int(input("{0:-^50}".format('계속하기 : 1, 뒤로가기 : 2'))) == 2:
                    break
            
        if int(input("{0:-^50}".format('다른 세부 카테고리 선택 : 1, 뒤로가기 : 2'))) == 2:
            break             
                

def T_Function():
    while True:
        detailkategorie = int(input("세부 카테고리의 번호를 입력해주세요. (조건을 보고 삼각함수 값 : 1, 삼각함수의 성질을 이용한 값 : 2) : "))
        
        if detailkategorie == 1:
            while True:
                coordinates = [random.randrange(-10, 10), random.randrange(-10,10)]
                print(f"원점 O와 점 P({coordinates[0]},{coordinates[1]})을 지나는 동경 OP가 나타내는 각의 크기를 θ라고 할때 sinθ, cosθ, tanθ의 값을 구하세요.")
                r = sqrtf(coordinates[0]**2 + coordinates[1]**2)
                sin = reduceFraction(coordinates[1] * r[0], r[0] ** 2 * r[1])
                cos = reduceFraction(coordinates[0] * r[0], r[0] ** 2 * r[1])
                tan = reduceFraction(coordinates[1] * r[0], coordinates[0])
                sin = minus(sin[0], sin[1])
                cos = minus(cos[0], cos[1])
                tan = minus(tan[0], tan[1])
                
                if input("sinθ의 값을 입력해주세요. (입력 예시 : 3루트2/5 : ") == str(sin[0]) + "루트" + str(r[1]) + "/" + str(sin[1]):
                    print("정답")
                else:
                    print("오답")
                    
                if input("cosθ의 값을 입력해주세요. (입력 예시 : 3루트2/5 : ") == str(cos[0]) + "루트" + str(r[1]) + "/" + str(cos[1]):
                    print("정답")
                else:
                    print("오답")
                    
                if input("tanθ의 값을 입력해주세요. (입력 예시 : 2/5 : ") == str(tan[0]) + "/" + str(tan[1]):
                    print("정답")
                else:
                    print("오답")
                if int(input("{0:-^50}".format('계속하기 : 1, 뒤로가기 : 2'))) == 2:
                    break
                    
        elif detailkategorie == 2:
            while True:
                print("삼각함수의 성질은 준비중입니다.")
                if int(input("{0:-^50}".format('계속하기 : 1, 뒤로가기 : 2'))) == 2:
                    break
                
        if int(input("{0:-^50}".format('다른 세부 카테고리 선택 : 1, 뒤로가기 : 2'))) == 2:
            break   
                
def sqrtf(num):
    firstNum = num
    numList = [0,0,0,0,0]
    while True:
        if num % 2 == 0:
            num = num // 2
            numList[0] += 1
        elif num % 3 == 0:
            num = num // 3
            numList[1] += 1
        elif num % 5 == 0:
            num = num // 5
            numList[2] += 1
        elif num % 7 == 0:
            num = num // 7
            numList[3] += 1
        elif num % 11 == 0:
            num = num // 11
            numList[4] += 1
        else:
            break
            
    goBack = True
    for i in range(5):
        if numList[i] >= 2:
            goBack = False
    if goBack:
        return [1, firstNum]
    result = [1,1]
    for i in range(5):
        if numList[i] % 2 == 1:
            if i == 0:
                numList[i] -= numList[i] % 2
                result[1] *= 2
            elif i == 1:
                numList[i] -= numList[i] % 2
                result[1] *= 3
            elif i == 2:
                numList[i] -= numList[i] % 2
                result[1] *= 5
            elif i == 3:
                numList[i] -= numList[i] % 2
                result[1] *= 7
            elif i == 4:
                numList[i] -= numList[i] % 2
                result[1] *= 11
            
        if (numList[i] != 0):
            if i == 0:
                result[0] *= 2 ** (numList[i] // 2)
            elif i == 1:
                result[0] *= 3 ** (numList[i] // 2)
            elif i == 2:
                result[0] *= 5 ** (numList[i] // 2)
            elif i == 3:
                result[0] *= 7 ** (numList[i] // 2)
            elif i == 4:
                result[0] *= 11 ** (numList[i] // 2)  
    return result;
            
        

def reduceFraction(bunja, bunmo): # 약분
    frac = [ bunja, bunmo ]

    if (frac[1] == 0): # 분모가 0일 경우에 에러 반환
        frac[0] = 0
        frac[1] = 0
        return frac

    gcd_result = gcd(frac[0], frac[1])

    frac[0] = int(frac[0] / gcd_result)
    frac[1] = int(frac[1] / gcd_result)

    return frac

def gcd(a, b): # 최대 공약수 계산
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

def minus(a,b):
    if a < 0 and b < 0:
        return [abs(a) , abs(b)]
    else:
    	return [a,b]
    	
print("본 프로그램은 수학1 삼각함수 교육용 프로그램입니다.")
print("동경의 일반각, 부채꼴의 호의 길이와 넓이, 삼각함수를 배울 수 있습니다.")
while True:
    kategorie = int(input("학습할 카테고리의 번호를 입력해주세요. (동경 : 1, 부채꼴 : 2, 삼각함수 : 3) : "))
    if kategorie == 1:
        radiusVector()
    elif kategorie == 2:
        sector()
    elif kategorie == 3:
        T_Function()
    if int(input("{0:-^50}".format('다른 카테고리 선택 : 1, 뒤로가기 : 2'))) == 2:
        break