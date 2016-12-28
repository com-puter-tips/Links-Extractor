#!/usr/bin/python

__author__ = "Devharsh Trivedi"
__copyright__ = "Copyright 2016, Devharsh Trivedi"
__license__ = "GPL"
__version__ = "1.3"
__maintainer__ = "Devharsh Trivedi"
__email__ = "devharsh@live.in"
__status__ = "Production"

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

try:

	for link in sys.argv[1:]:
		page = requests.get(link)
		soup = BeautifulSoup(page.text, "lxml")
		extlist = list()
		intlist = list()
		
		for a in soup.findAll("a", attrs={"href":True}):
			if len(a['href'].strip()) > 1 and a['href'][0] != '#' and 'javascript:' not in a['href'].strip() and 'mailto:' not in a['href'].strip() and 'tel:' not in a['href'].strip():
				if 'http' in a['href'].strip() or 'https' in a['href'].strip():
					if urlparse(link).netloc.lower() in urlparse(a['href'].strip()).netloc.lower():
						intlist.append(a['href'])
					else:
						extlist.append(a['href'])
				else:
					intlist.append(a['href'])
		
		print('\n')
		print(link)
		print('---------------------')
		print('\n')
		print(str(len(intlist)) + ' internal links found:')
		print('\n')
		for il in intlist:
			print(il)
		print('\n')
		print(str(len(extlist)) + ' external links found:')
		print('\n')
		for el in extlist:
			print(el)
		print('\n')
		
except Exception as e:
	print(e)