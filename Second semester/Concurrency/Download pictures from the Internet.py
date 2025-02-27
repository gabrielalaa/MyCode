import requests
import threading

def download_file(url):
    response = requests.get(url)
    filename = url.split("/")[-1] # Extract the filename from the URL
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

urls = ["https://assets.orf.at/mims/2024/22/49/crops/w=640,h=256,q=70,r=2/2220963_opener_842949_suedafrika_wahl_pv_im.jpg",
		"https://assets.orf.at/mims/2024/22/29/crops/w=640,h=256,q=70,r=2/2222512_opener_843529_us_wahl_trump_prozess_schlussplaedoyers_miab_ap.jpg"]

for url in urls:
    t1 = threading.Thread(target=download_file, args=(url,))
    t1.start()