class BalanceException(Exception):
    pass


class BankAccount:
     def __init__(self,initialAmount, accName):
         self.balance = initialAmount
         self.name = accName
         print(f"\nAccount '{self.name}' created.\nBalance = R{self.balance:.2f}")
         
     def getBalance(self):
          print(f"\nAccount '{self.name}'  balance = R{self.balance:.2f}")
          
     def deposit(self, amount):
         self.balance = self.balance + amount
         print("\nDeposit complete")
         self.getBalance()
         
     def viableTransaction(self, amount):
         if self.balance >= amount:
             return
         else:
             raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of R{self.balance:.2f}") 
     def withdraw(self, amount):
        try:
             self.viableTransaction(amount)
             self.balance = self.balance - amount
             print("\nWithdraw complete")
             self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted:{error}')
      
     def transfer(self, amount, account):
          try:
              print('\n**********\n\nBeggining Transfer..🚀')
              self.viableTransaction(amount)
              self.withdraw(amount)
              account.deposit(amount)
              print('\nTransfer completed!✅\n\n***********')       
          except BalanceException as error:
              print('f\nTransfer interrupted.❌{error}')
              
class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance =self.balance + (amount * 1.05)
        print("\nDeposit complete")
        self.getBalance()
        
class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)  
        self.fee = 5     
        
    def  