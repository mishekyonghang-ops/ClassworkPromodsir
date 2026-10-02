name=str(input("Enter students name:"))
M1=int(input("Enter marks of first subject:"))
M2=int(input("Enter marks of second subject:"))
M3=int(input("Enter marks of third subject:"))
print(f"Total marks is:{M1+M2+M3}")
avg=(M1+M2+M3)/3
print(f"Average marks is:{avg}")

if M1>M2>M3:
    print(f"highest={M1}")
elif M2>M3>M1:
    print(f"Highest={M2}")
else:
    print(f"highest={M3}")

if avg>=90:
    print("Grade=A+")
elif avg>=80:
    print("Grade=A")
elif avg>=70:
    print("Grade=B")
elif avg>=40:
    print("Grade=C")
else:
    print("Grade=F")



