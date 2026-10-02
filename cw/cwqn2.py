num=int(input("Enter an integer:"))
if num>=0:
    print(f"num is +ve")
elif num<=0:
    print("num is -ve")
else:
    print("num is zero")

if num %2==0:
    print(f"The number is even")
else:
    print(f"The number is odd")

if num%3==0:
    print(f"The number is divisible by 3")
else:
    print(f"The num is not divisible by 3")

if num%5==0:
    print(f"The number is divisible by 5")
else:
    print(f"The num is not divisible by 5")

if num%3==0 and num%5==0:
    print(f"The number is divisible by both 3 and 5")
else:
    print(f"The num is not divisible by both  3 and 5")