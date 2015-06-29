class BankAccount:

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.total_fee = 0
    
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance = self.balance - amount 
        if self.balance < 0:
            self.balance = self.balance - 5
            self.total_fee = self.total_fee + 5
        
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return(self.balance)
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return(self.total_fee)
    
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()