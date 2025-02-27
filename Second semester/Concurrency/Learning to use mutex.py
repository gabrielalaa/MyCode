# simulates concurrent bank account transactions

# (5) multiple threads will attempt to withdraw and deposit money into a shared bank account
# each thread should make multiple deposit and withdrawal transactions

# ensure that the account balance remains consistent
import threading
lock = threading.Lock()

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        # Acquire the lock before modifying the balance
        lock.acquire()
        try:
            self.balance += amount
            print(f"Deposited {amount}, New Balance: {self.balance}")
        finally:
            # Release the lock after modification
            lock.release()

    def withdraw(self, amount):
        # Acquire the lock before modifying the balance
        lock.acquire()
        try:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, New Balance: {self.balance}")
            else:
                print(f"Failed to withdraw {amount}, Insufficient Balance: {self.balance}")
        finally:
            # Release the lock after modification
            lock.release()

    def get_balance(self):
        # Acquire the lock before accessing the balance
        lock.acquire()
        try:
            return self.balance
        finally:
            # Release the lock after accessing the balance
            lock.release()

# Create a shared BankAccount instance
account = BankAccount(100)

# Function to simulate transactions
def simulate_transactions():
    for _ in range(5):
        account.deposit(200)
        account.withdraw(250)

# Example of usage
threads = []
for t in range(5):
    thread = threading.Thread(target=simulate_transactions)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print final balance
print(f"Final Balance: {account.get_balance()}")
