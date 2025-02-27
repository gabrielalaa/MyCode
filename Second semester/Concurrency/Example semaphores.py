import threading
import time

# Semaphore to synchronize consumer and producer
signal = threading.Semaphore(0)

# Shared resource
item = None

# Consumer function
def consumer():
    global item
    print("Consumer is waiting.")
    signal.acquire()  # Wait for the producer to produce the item
    print("Consumer got:", item)

# Producer function
def producer():
    global item
    for i in range(5):  # Producing 5 items
        time.sleep(1)  # Simulating time to produce
        item = f"Item {i}"
        print("Producer produced:", item)
        signal.release()  # Signal to the consumer that the item is ready

# Creating the threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting the threads
consumer_thread.start()
producer_thread.start()

# Waiting for both threads to complete
producer_thread.join()
consumer_thread.join()

print("Processing complete.")