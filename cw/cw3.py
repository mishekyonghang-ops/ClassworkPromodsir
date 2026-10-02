consumed=int(input("enter theelectricity units consumed :"))
if consumed <= 20:
    total_bill=consumed*5
elif consumed<=50:
    total_bill=(consumed*5)+(consumed-20)*7
elif consumed<=100:
    total_bill=(consumed*5)+(consumed*7)+(consumed-50)*10
else:
    total_bill=(consumed*5)+(consumed*7)+(consumed*10)+(consumed-100)*12
print(f"total bill={total_bill}")