balance=int(input("Enter your acc balance:"))
withdraw=int(input("Enter the amount to withdraw:"))
pin=int(input("Enter your PIN:"))
correct_pin=112233
if pin==correct_pin and withdraw>0 and withdraw <= balance:
    remaining_balance=balance-withdraw
    print("Withdrawal successful!")
    print(f"The remaining balance is:{remaining_balance}")
elif pin!=correct_pin:
    print("invalid pin")
elif withdraw<= 0:
    print("Invalid withdrawal amount!")
else:
    print("Insufficient balance!") 

    