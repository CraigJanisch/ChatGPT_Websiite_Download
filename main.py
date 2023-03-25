import os
import requests
from bs4 import BeautifulSoup

url = "https://www.craigjanisch.com"
response = requests.get(url)

if response.status_code == 200:
	soup = BeautifulSoup(response.content, 'html.parser')
	media_urls = []
	for img in soup.find_all('img'):
		media_urls.append(img.get('src'))
	for source in soup.find_all('source'):
		media_urls.append(source.get('src'))
	for url in media_urls:
		response = requests.get(url)
		if response.status_code == 200:
			filename = os.path.join("downloads", os.path.basename(url))
			with open(filename, "wb") as file:
				file.write(response.content)
			print(f"Downloaded {filename} successfully!")
		else:
			print(f"Failed to download {url}. Status code: {response.status_code}")
else:
	print(f"Failed to download website. Status code: {response.status_code}")
