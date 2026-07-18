user_info={"ATM PIN":"0000","Name":"Rakesh","Balance":50000,"Transaction History":[]}
print("Please Insert ATM card")
remaining_attempts=3
while remaining_attempts>0:
    pin=input("Enter 4 digit ATM pin: ")
    if len(pin)==4:
        if pin in user_info['ATM PIN']:
            print("Select")
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Balance enquiry")
            serv=int(input())
            if serv==1:
                withdraw_amount=int(input("Enter withdraw amount:"))
                if (withdraw_amount<=user_info['Balance']) and (withdraw_amount>=500) and  (withdraw_amount%100==0) :
                    user_info['Balance']-=withdraw_amount
                    print("Amount withdraw successfully")
                    print("Balance amount after withdraw:",user_info['Balance'])
                else:
                    print("Enter valid amount")
            elif serv==2:
                deposit_amount=int(input("Enter Deposit amount:"))
                user_info['Balance']+=deposit_amount
                print("Balance amount: after deposit",user_info['Balance'])
            elif serv==3:
                print("Balance:",user_info['Balance'])
        else:
            print("Invalid PIN")
            remaining_attempts-=1
            if remaining_attempts>0:
                print(f"remaining attempts are{remaining_attempts}")
            else:
                print("Your ATM card is blocked")
    else:
        print("Please enter 4 digit pin")       
