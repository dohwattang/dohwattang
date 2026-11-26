num1 = int(input("몇단을 입력할까요?>"))
num2 = int(input("몇번까지 출력할까요?>"))

print("[{0}단]".format(num1))
print("="*10)
for i in range(1, num2+1):
    print("{0} x {1} = {2}".format(num1, i, num1*i))