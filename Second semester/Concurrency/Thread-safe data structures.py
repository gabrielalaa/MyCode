import threading
import time
from queue import Queue

# Create a FIFO queue (maxsize 5 to demonstrate its use)
q = Queue(maxsize=5)

# Producer function
def producer():
    for i in range(10):
        item = f"Item {i}"
        q.put(item)  # Put an item into the queue (blocks if queue is full)
        print(f"Producer put: {item}")
        time.sleep(0.5)  # Simulating production time

# Consumer function
def consumer():
    while True:
        item = q.get()  # Get an item from the queue (blocks if queue is empty)
        print(f"Consumer got: {item}")
        q.task_done()  # Mark the item as processed
        time.sleep(1)  # Simulating processing time

# Creating producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)  # Daemon so it exits when the program ends

# Starting the threads
producer_thread.start()
consumer_thread.start()

# Wait for the producer thread to finish
producer_thread.join()

# Wait for all items in the queue to be processed
q.join()

print("All items have been produced and consumed.")