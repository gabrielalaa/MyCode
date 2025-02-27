import threading
counter = 0

def increment_counter():
    global counter
    for x in range(111):
        counter += 1

# Create and start the threads
threads = []

for x in range(10):
    thread = threading.Thread(target=increment_counter)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Counter value: {counter}")