import multiprocessing
import time


# Define a custom process class inheriting from multiprocessing.Process
class MyProcess(multiprocessing.Process):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        while self.count > 0:
            print(f"Counting down: {self.count}")
            self.count -= 1
            time.sleep(1)  # Sleep for 1 second to simulate some work


# Define a function to be run in a separate process
def do_something():
    print("Doing something in a separate process!")
    for i in range(5):
        print(f"Processing step {i + 1}")
        time.sleep(2)  # Simulate some work by sleeping for 2 seconds
    print("Finished separate process task")


if __name__ == '__main__':
    # Create two instances of MyProcess class with different countdown values
    p1 = MyProcess(10)  # Countdown from 10
    p2 = MyProcess(5)  # Countdown from 5

    # Start the custom process objects
    p1.start()
    p2.start()

    # Create a process for the separate function
    p3 = multiprocessing.Process(target=do_something)

    # Start the process for the function
    p3.start()

    # Wait for all processes to complete
    p1.join()
    p2.join()
    p3.join()

    print("All processes have completed.")