
N= int(input())
F= int(input())

num1 = N // 100
num2 = num1 * 100
while num2% F != 0:
    num2 +=1
            




num2 = num2 % 100
if num2 < 10:
    print(f"0{num2}")
else: 
    print(num2)