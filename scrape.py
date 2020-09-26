#!usr/bin/python

code = ['KDFW'] 
#,'KTEB','KPHL','KCGS']
import csv

import urllib.request

for x in code:
	address = 'http://wxweb.meteostar.com/sample/sample.shtml?text=' + x
	content = urllib.request.urlopen(address)

	read_content = content.read()

	from bs4 import BeautifulSoup

	soup=BeautifulSoup(read_content,'html.parser')

	tables = soup.find_all('table')

	table_body = tables[1].find_all('td')
	for td in table_body:
			fn = (x + '.csv')
			w = csv.writer(open(fn,'a'), dialect='excel')
			w.writerows(td.text)
			
#			print (td.text)

#pAll = soup.find_all('td')
#par0 = pAll[0].text

#par1 = pAll[1].text

#par2 = pAll[2].text
#print(par0)
#print(par1)
#print(par2)


