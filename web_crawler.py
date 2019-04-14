import requests
from bs4 import BeautifulSoup

import re

index = 0

result = []

while (index <= 60):
	url = 'https://www.com.tw/star/checktestareaid_81_103' + str(index+139) + '_108.html'
	resp = requests.get(url)
	if resp.status_code == 404:
		continue
	soup = BeautifulSoup(resp.text, 'html.parser')

	tmp_result = soup.find_all("a", href = re.compile("check"))
	
	for i in tmp_result:
		result.append(i.text.strip())
	index = index + 1

url = 'https://www.com.tw/star/checktestareaid_81_103295_108.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

tmp_result = soup.find_all("a", href = re.compile("check"))

for i in tmp_result:
	result.append(i.text.strip())
		
result.sort()
		
for i in result:
	print (i)