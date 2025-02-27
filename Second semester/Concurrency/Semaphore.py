import threading
import requests

# Create a semaphore that allows only 2 threads to run concurrently
s = threading.Semaphore(2)


# Function to fetch a page, using the semaphore for thread control
def fetch_page(url):
    s.acquire()  # Acquiring the semaphore (blocking if there are already 2 threads running)
    print(f"Acquired semaphore for {url}")

    try:
        response = requests.get(url)  # Fetch the page
        print(f"Fetched {url}: {len(response.text)} characters")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    finally:
        s.release()  # Releasing the semaphore so another thread can run
        print(f"Released semaphore for {url}")


# List of URLs to fetch
urls = [
    "http://google.com",
    "http://www.ort.at",
    "http://derstandard.at",
    "http://example.com"
]

# Creating and starting threads for each URL
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_page, args=(url,))
    threads.append(thread)
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

print("All pages fetched.")