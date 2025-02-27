import threading
counter = 0

# Mutex Lock (threading.Lock())
# Use case: Ensure that only one thread accesses a shared resource at a time.
lock = threading.Lock()
with lock:
    counter += 1  # Critical section

###

# Semaphore (threading.Semaphore(value))
# Use case: Limit the number of threads accessing a resource.
semaphore = threading.Semaphore(3)
with semaphore:
    access_database()  # Only 3 threads can run this at a time

###

# BoundedSemaphore (threading.BoundedSemaphore(value))
# Use case: Similar to Semaphore, but raises an error if released too many times
bounded_semaphore = threading.BoundedSemaphore(2)
with bounded_semaphore:
    process_request()  # Ensures max limit of resource release

###

# Event (threading.Event())
# Use case: One thread signals others to proceed.
event = threading.Event()
event.set()  # Signal other threads

###

# Condition (threading.Condition([lock]))
# Use case: More advanced signaling between threads, typically with locks.
condition = threading.Condition()
with condition:
    while not item_available:
        condition.wait()  # Wait until notified
    consume_item()

###

# Reentrant Lock (threading.RLock())
# Use case: Allow a thread to acquire the lock multiple times without deadlocking itself
rlock = threading.RLock()
with rlock:
    recursive_function()  # Can acquire the lock multiple times