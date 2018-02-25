#-*#-*- coding:utf-8 -*-

from urllib2 import Request,urlopen,HTTPError,URLError,ProxyHandler,build_opener,install_opener
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np
import json
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# def set_params():
# 	global link_list,driver
# 	link_list = []
# 	headers_list = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
# {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}\
# ,{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
#     {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},\
#     {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 '},\
#     {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14 '},\
#     {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'}]
# 	dc_dic = dict(DesiredCapabilities.PHANTOMJS)
# 	dc_dic['phantomjs.page.settings.userAgent'] = headers_list[0]

def output(info_list):
	path = 'D:\my_documents\python\scrape\\find_job\\tianyancha\\info.csv'
	with open(path,'wb') as file:
		writer = csv.writer(file)
		for info in info_list:
			writer.writerow(info)

def scrape_city():
	global city_list
	city_list = []
	url = 'http://www.tianyancha.com/search?key=%E6%B0%94%E8%B1%A1&searchType=scope'
	# while len(city_list)==0:
	driver.get(url)
	# driver.implicitly_wait(8)
	time.sleep(3)
	soup = BeautifulSoup(driver.page_source, 'html')
	objs = soup.findAll('a', {'class': 'list c2 ng-binding'})
	objs += soup.findAll('a', {'class': 'list2 c2 ng-binding'})
	for obj in objs:
		if obj['href'][0]=='h':
			city_list.append(obj['href'].split('.')[0])
		else:
			pass
	return city_list

def scrape_links(city_list):
	info_list = []
	categories = ['base','id','estiblishTime','industry','legalPersonName','name','regCapital','regStatus','score']
	for city in city_list:
		# try:
		url = 'http://'+city+'.tianyancha.com/v2/search/%E6%B0%94%E8%B1%A1.json?&pn=1&base='+city+'&type=scope'
		sourcecode = requests.get(url).json()
		totalpage = sourcecode['totalPage']
		i = 1
		while i<=totalpage:
			url = 'http://'+city+'.tianyancha.com/v2/search/%E6%B0%94%E8%B1%A1.json?&pn='+str(i)+'&base='+city+'&type=scope'
			print url
			sourcecode = requests.get(url).json()
			json = sourcecode['data']
			for item in json:
				info = []
				for category in categories:
					info.append(item[category])#.encode('utf8'))
				info_list.append(info)
				print info
			print len(info_list)
			i+=1
			time.sleep(2)

	output(info_list)

def scrape_items():

	df = pd.read_csv('D:\my_documents\python\scrape\\find_job\\tianyancha\\pre.csv')
	columns = ['base','id','estiblishTime','industry','legalPersonName','name','regCapital','regStatus','score']
	df.columns = columns
	i = 0
	info_list = []
	for id in df['id']:
		i+=1
		# url = 'http://www.tianyancha.com/v2/company/'+str(id)+'.json'
		url = 'http://www.tianyancha.com/v2/company/17666219.json'
		print i,url
		categories = ['base', 'id', 'estiblishTime', 'industry', 'legalPersonName', 'name', 'regCapital', 'regStatus','score','businessScope','companyOrgType','regLocation','websiteList']
		sourcecode = requests.get(url).json()
		json = sourcecode['data']
		for item in json:
			info = []
			for category in categories:
				info.append(item[category])  # .encode('utf8'))
			info_list.append(info)
			print info

	output(info_list)

# set_params()
city_list = scrape_city()
scrape_links(city_list)
scrape_items()
#

#execfile('D:\my_documents\python\scrape\\find_job\meteorology\\meteorological_companies.py')



		# request = Request(url,headers=headers_list[random_num])
		# response = urlopen(request).read()
		# data = {'url':'/search?key=%E6%B0%94%E8%B1%A1','searchType':'scope'}
		# sourcecode = requests.post(url,data=data).json()
		# print 
		# obj  = driver.find_element_by_class_name('search_result_single search-2017 pb15 ng-scope')
		
		# driver.get('http://www.tianyancha.com/search/p'+str(i)+'?key=%E6%B0%94%E8%B1%A1&searchType=scope')
		# print soup
		# file = open('C:\Users\\think\Desktop\\meteo_comps.txt','wb')
		# file.write(soup)
		# soup = BeautifulSoup(response,'html')

