from bank_accounts import *

Keo = BankAccount(2000, "Keo")
Pelo = BankAccount(2500, "Pelo")

Keo.getBalance()
Pelo.getBalance()

Pelo.deposit(500)

Keo.withdraw(2500)

Pelo.transfer(3000, Keo)

Pelo.getBalance()
Pelo.deposit(5000)

Olga = InterestRewardsAcc(1000, "Olga")

Olga.getBalance()

Olga.deposit(100)

Olga.transfer(100, Keo)