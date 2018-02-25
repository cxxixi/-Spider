#-*- coding: UTF-8 -*-
#Compatible With: Python2.7
#Author : cxxixi
#Last modified: 2017/4/6

## scrape the proxies from xiciproxy and check the whether the ips is robust and available.

from urllib2 import Request,urlopen,ProxyHandler,build_opener,install_opener
from bs4 import BeautifulSoup
import csv
import socket

def IPspider(random_num):

	headers_list = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}\
,{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]
    
	file = open('PUT YOUR PATH HERE','wb')

	url = 'http://www.xicidaili.com/nn/'
	for num in xrange(1,max_num+1):
		ipurl = url+str(num)
		print 'now scraping data from PAGE'+str(num)
		print ipurl
		request = Request(ipurl,headers = headers_list[num%5])
		response = urlopen(request,timeout=10)
		html = response.read()
		soup = BeautifulSoup(html,'html.parser')
		obj = soup.findAll('tr')
		for item in obj:
			try:
				info = item.findAll('td')
				ip = info[1].get_text()+':'+info[2].get_text()
				print ip
				file.write(ip+'\n')
			except IndexError:
				pass

def Checkout_ip():
	socket.setdefaulttimeout(1)
	ip_pool = []
	file = open('PUT YOUR PATH HERE')
	#reader = csv.reader(file)
	for row in file:
		proxy = row
		proxy_handler = ProxyHandler({'http':proxy})
		opener = build_opener(proxy_handler)
		install_opener(opener)
		try:
			html = urlopen('http://baidu.com')
			ip_pool.append(row)
			print row
		except Exception:
			continue
	print len(ip_pool)

	file1 = open('PUT YOUR PATH HERE','wb')
	for ip in ip_pool:
		file1.write(ip)


IPspider(10)
Checkout_ip()

#execfile('D:\my_documents\python\scrape\IPsPool\\IPspider.py')