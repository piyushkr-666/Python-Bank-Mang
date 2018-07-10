import pickle
import os


class Account:
    AcNo=0
    def __init__(self,Name):
        Account.AcNo=Account.AcNo+1
        self.AccountNumber=Account.AcNo
        self.AccountHolderName=Name
        self.AmountAvail=0.0
    def __str__(self):
        return '{:<20}\t{:<30}\t{:>10}'.format(self.AccountNumber,self.AccountHolderName,self.AmountAvail)
    


file=open('MaxAccount.bin','rb')
try:
    while True:
        obj=pickle.load(file)
        Account.AcNo=int(obj)
except EOFError:
    pass
file.close()
      
while True:
    choice=input('Do you want to continue Y/N: ')
    if choice.upper()=='N':
        break
    elif choice.upper()=='Y':
        password=input("Enter Password: ")
        if password=='12345':
            print('*'*30+'\n'*2+'Welcome'.center(30,' ')+'\n'+'To'.center(30,' ')+'\n'+'Piyush\'s Bank Management'.center(30,' ')+'\n'*3+'*'*30)
            while True:
                print('What You Want To Do:')
                print('1. Open new account'+'\n'+'2. Deposit'+'\n'+'3. Withdrawal'+'\n'+'4. Show Balance'+'\n'+'5. Show All'+'\n'+'6. Modify Account'+'\n'+'7. Close Account'+'\n'+'8. Exit')
                action=input("Enter serial no of action you want to perform: ")

                
                if action=='1':
                    file=open('BankMang Detail.bin','ab')
                    name=input("Enter name of account holder: ")
                    account=Account(name+' '*(30-len(name)))                                              #1 open new account
                    pickle.dump(account,file)
                    file.close()
                    file=open('MaxAccount.bin','rb+')
                    try:
                        while True:
                            t=pickle.load(file)
                            t=str(Account.AcNo)
                            file.seek(0)
                            pickle.dump(t,file)
                    except EOFError:
                        pass
                    file.close()


                    
                elif action=='2':
                    if not os.path.isfile('BankMang Detail.bin'):
                        print('No account available to show')
                    else:
                        found='N'
                        file=open('BankMang Detail.bin','rb+')
                        accNo=int(input("Enter Account Number: "))
                        try:
                            while True:
                                pos=file.tell()
                                t=pickle.load(file)                                                                          #2 deposit
                                if t.AccountNumber==accNo:
                                    found=='Y'
                                    avail=t.AmountAvail
                                    amount=float(input('Enter amount to deposit: '))
                                    t.AmountAvail=avail+amount
                                    file.seek(pos)
                                    pickle.dump(t,file)
                                    print(amount,'Sucessfully deposited to account',accNo)
                                    break
                        except EOFError:
                            pass
                        if found=='N':
                            print('SORRY! Account not available')
                        file.close()


                        
                    
                elif action=='3':
                    if not os.path.isfile('BankMang Detail.bin'):
                        print('No account available to withdraw')
                    else:
                        found='N'
                        file=open('BankMang Detail.bin','rb+')
                        accNo=int(input("Enter Account Number: "))
                        try:
                            while True:
                                pos=file.tell()
                                t=pickle.load(file)
                                if t.AccountNumber==accNo:
                                    found='Y'
                                    amount=float(input('Enter amount to Withdraw: '))                                           #3 withdraw
                                    if amount>t.AmountAvail:
                                        print('Amount Not Available')
                                        break
                                    else:
                                        avail=t.AmountAvail
                                        t.AmountAvail=avail-amount
                                        file.seek(pos)
                                        pickle.dump(t,file)
                                        print(amount,'Sucessfully Withdrawed from Account',accNo)
                                        break
                        except EOFError:
                            pass
                        if found=='N':
                            print("SORRY! Account not available")
                        file.close()






                        
                elif action=='4':
                    if not os.path.isfile('BankMang Detail.bin'):
                        print('No account available')
                    else:
                        found='N'
                        file=open('BankMang Detail.bin','rb')
                        accNo=int(input("Enter account number: "))  
                        try:
                            while True:                                                                                             #4 show bal
                                t=pickle.load(file)
                                if t.AccountNumber==accNo:
                                    found='Y'
                                    print('Available amount in account',accNo ,'is',t.AmountAvail)
                                    break
                                
                        except EOFError:
                            pass
                        if found=='N':
                            print('SORRY! Account not available')
                        file.close()
                                
                                
                            
                elif action=='5':
                    if not os.path.isfile('BankMang Detail.bin'):
                        print('No account available to show')
                    else:
                        file=open('BankMang Detail.bin','rb')
                        try:
                            while True:
                                t=pickle.load(file)                                                                              #5 show all accounts
                                print(t)
                        except EOFError:
                            pass
                        file.close()



                    
                elif action=='6':
                    if not os.path.isfile('BankMang Detail.bin'):
                        print('No account available to show')
                    else:
                        found='N'
                        file=open('BankMang Detail.bin','rb+')
                        accNo=int(input("Enter Account Number: "))
                        try:
                            while True:
                                pos=file.tell()
                                t=pickle.load(file)                                                                           #6 modify account detail
                                if t.AccountNumber==accNo:
                                    found='Y'
                                    name=input("Enter new name of account holder: ")
                                    t.AccountHolderName=name+' '*(30-len(name))
                                    file.seek(pos)
                                    pickle.dump(t,file)
                                    print('Sucessfully updated!')
                                    break
                        except EOFError:
                            pass
                        if found=='N':
                            print('SORRY! Account not available')
                        file.close()

                                    
                    



                    
                elif action=='7':
                    if not os.path.isfile('BankMang Detail.bin'):
                        print('No account available to show')
                    else:
                        found='N'
                        file=open('BankMang Detail.bin','rb')
                        file1=open('BankMangDEl.bin','ab')
                        accNo=int(input("Enter account number to remove: "))                                                      #7 Close Account
                        try:
                            while True:
                                t=pickle.load(file)
                                if t.AccountNumber==accNo:
                                    found='Y'
                                    print('Account',accNo,'successfully removed')
                                    
                                else:
                                    pickle.dump(t,file1)

                        except EOFError:
                            pass
                        file.close()
                        file1.close()
                        os.remove('BankMang Detail.bin')
                        os.rename('BankMangDEl.bin','BankMang Detail.bin')
                        if found=='N':
                            print('Account not available')
                
                        
                        
                        
                
                    
                elif action=='8':
                    break
                else:
                    print('Please! Enter available serial no')
            
        else:
            print("Incorrect Password")
            continue
    else:
        print("Enter Y Or N")
print('ThankYou! Have A Nice Day')

        
        
            
        


        
        
    
