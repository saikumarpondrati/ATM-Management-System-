# ATM MINI

username="pondrati"
password=1433
user=input("enter the name:")
pass_word=int(input("enter the password:"))
if user==username and pass_word==password:
    print=('''
            1.credit
            2.debit
            3.mini statement
            4.exit''')
    amount=100000   
    option=int(input("select your option:"))
    if option==1:
        crt=int(input("enter the amoumt:"))
        amount+=crt
        print("Totalamount:",amount)
    # elif option==2:
    #     deb=int(input("enter the amount:"))
    #     amount-=deb
    #     print("Total amount:",amount)
    # elif option==3:
    #     print("===========ATM========")
    #     print("username:",username)
    #     print("Total amount:",amount)
    #     print("$$$$$$ THANK YOU $$$$$")
    # elif option==4:
    #         exit()
    else:
        print("Retry")