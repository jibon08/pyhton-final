class user:
    all_account=[]
    def __init__(self,name,email,address,account_type,account_number) -> None:
        
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_number=account_number
        print("\n created account \n")

        self.balance=0
        user.all_account.append(self)

        self.history_all_work=[]

        self.trac=False

        self.loan_on_off=False

        # self.history_deposit=[]
        # self.history_trancefer=[]

        self.limit=0

        self.loan_balance_of=0

    def money_withdraw(self,money):
        if self.trac==False:
            if money>=0 and money<self.balance:
                self.balance-=money
                t=f"money withdraw : {money}"
                self.history_all_work.append(t)
                print(f"\n money withdraw {money} current balance :{self.balance}")
            else:
                print("\nWithdrawal amount exceeded\n")
        else:
            print("\n -- bank account bankrupt\n---")

    def money_deposit(self,money):
        if self.trac==False:

            if money>=0:
                self.balance+=money
                p=f"money deposit :{money}"
                print(f"\n money deposit{money}in current balance :{self.balance}")
                self.history_all_work.append(p)

            else:
                print("\nWithdrawal amount exceeded\n")
        else:
            print("\n --bank account bankrupt\n---")


    def avilable_balance(self):
        print(f"\navilable_balance {self.balance}\n")
    

    def bank_loan(self,money):
        
        if self.loan_on_off==False:
            if(self.limit<2):
                self.balance+=money
                self.loan_balance_of+=money
                self.limit+=1
                print(f"\n bank loan{money}and main balance {self.balance}")
            else:
                print("\n-already take two loan-\n")
        else:
            print("\ndonot take loan beacause loan switch off\n")


    def transfer(self,money,address):
        if self.trac==False:

            self.t=True
            if len(self.all_account)>=2:
                for add in self.all_account:
                    if add.account_number==address:
                        self.t=False
                        if money<=self.balance:
                            add.balance+=money
                            print(f"\n transper balance{add.balance}\n")
                            self.balance-=money
                        else:
                            print("nAccount does not exist and account money low \n")
            else:
                print("nAccount does not exist\n")

            if self.t==True:
                print("\nAccount does not exist\n")
        else:
            print("\n --bank account bankrupt\n---")
 
       
    def history(self):
        for acc in self.history_all_work:
            print(acc)

    def delete_any(self,id):

        su=True
        for acc in user.all_account:
            t2=acc.account_number
            if t2==id:
                su=False
                self.all_account.remove(acc)
                print("\n remove success fully of value \n")
        if su==True:
            print("\n NOT FOUND \n")


    def show_all_user(self):
        for show in user.all_account:
            print(f" name-{show.name} email-:{show.email} address- :{show.address} account_type-:{show.account_type} account number-:{show.account_number}")
            
    def loan_2(self):
        print(f"\n total  {self.loan_balance_of} loan balance  \n")

        
class saving(user):
    def __init__(self, name, email, address, account_type,account_number) -> None:
        super().__init__(name, email, address, account_type,account_number)
        

class current(user):
    def __init__(self, name, email, address, account_type,account_number) -> None:
        super().__init__(name, email, address, account_type,account_number)

class admin:
    def __init__(self, user_name,password) -> None:
        self.user_name=user_name
        self.password=password
        print("\n---admin  login success---\n")

class user_login:
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
        print("\n -----user login  sucessful---\n ")
        

        
current_user=None 

while (True):
    if current_user==None:

        print("\n --- account no logged--- ")

        na=input("enter the name:")
        ema=input("enter the email:")
        add=input("enter the address:")
        acc_type=input("account type (saving or current):")
        acc_num=int(input("account number:"))
        print()
        if acc_type=="saving":
            t=saving(na,ema,add,acc_type,acc_num)
            current_user=t
            print()
        else:
            t5=current(na,ema,add,acc_type,acc_num)
            current_user=t5
            print() 
    else:
        print("----WELCOME------")

        f=input("select the work ( have or exit )")

        if f=="have":
    
            ac=input("which do you  give access (user or admin)")

            if ac=="user":
                print("-- for login user id than fulfil  bleow requarments--\n")
                nam=input("user name:")
                id=input("user id:")
                we=user_login(nam,id)

                while(True):
                    # print("1:create account--")
                    print("2:money withdraw--")
                    print("3:money deposit--")
                    print("4: money transfer--")
                    print("5:bank loan--")
                    print("6:history withdraw and deposit--")
                    print("7:avilable balance--")
                    print("8:exit--")
                    print()
            
                    ch=int(input("\nenter the option :"))

                    if ch==2:
                        mon=int(input("enter the money:"))
                        current_user.money_withdraw(mon)
                        print()

                    elif ch==3:
                        mon1=int(input("enter the money:"))
                        current_user.money_deposit(mon1)
                        print()

                    elif(ch==4):
                        mo=int(input("enter the money:"))
                        id=int(input("enter the id number:"))
                        current_user.transfer(mo,id)
                        print()

                    elif ch==5:
                        m=int(input("enter the money need you:"))
                        current_user.bank_loan(m)
                        print() 

                    elif ch==6:
                        current_user.history()
                        print()
    
                    elif ch==7:
                        current_user.avilable_balance()
                        print()

                    elif ch==8:
                        break
                    else:
                        print("\nselect  option wrong\n")

            elif ac=="admin":
                print("\n-- for login admin please fulfil the rquarments--\n ")
                user_name=input("admin_name:")
                password=input("password:")
                t=admin(user_name,password)

                while(True):
                   
            
                    print("1:create account--")
                    print("2:delete any account--")
                    print("3:show all uer_account--")
                    print("4:cheeck total avaible balance of bank--")
                    print("5:total loan balance--")
                    print("6:on/ off loan feture of bank--")
                    print("7:bankrupt")
                    print("8:exit")

                    tr=int(input("select the option:"))
                    if tr==1:
                        na=input("enter the name:")
                        ema=input("enter the email:")
                        add=input("enter the address:")
                        acc_type=input("account type (saving or current ):")
                        acc_num=int(input("account number:"))
                        print()
                        if acc_type=="saving":

                            t=saving(na,ema,add,acc_type,acc_num)
                            current_user=t
                            print()
                        else:
                            t5=current(na,ema,add,acc_type,acc_num)
                            current_user=t5
                            print()
                    elif tr==2:
                        id1=int(input("enter the id:"))
                        current_user.delete_any(id1)    
                        print()

                    elif tr==3:
                        current_user.show_all_user()
                        print()

                    elif tr==4:
                        current_user.avilable_balance()
                        print()

                    elif tr==5:
                        current_user.loan_2()
                        print()

                    elif tr==6:
                        current_user.loan_on_off=True
                        print()
                    elif tr==7:
                        current_user.trac=True
                        print()
                    elif tr==8:
                        break
                    else:
                        print("\n select  option wrong\n")
        else:
            break


        

            
        










       
   
        