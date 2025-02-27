import threading

# Lock to protect shared resources
lock = threading.Lock()

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        with lock:
            self.balance += amount
            print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        with lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, New Balance: {self.balance}")
            else:
                print(f"Failed to withdraw {amount}, Insufficient Balance: {self.balance}")

    def get_balance(self):
        with lock:
            return self.balance

# Example of usage
if __name__ == "__main__":
    account = BankAccount(100)  # Shared BankAccount instance

    threads = []

    for _ in range(5):
        # Deposit threads
        thread_deposit = threading.Thread(target=account.deposit, args=(200,))
        threads.append(thread_deposit)

        # Withdraw threads
        thread_withdraw = threading.Thread(target=account.withdraw, args=(250,))
        threads.append(thread_withdraw)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Check final balance
    print(f"Final Balance: {account.get_balance()}")