#-*#-*- coding:utf-8 -*-

from urllib2 import Request,urlopen,HTTPError,URLError,ProxyHandler,build_opener,install_opener
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np
from selenium import webdriver
# import os.system as sys
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def set_params():
	global link_list,driver
	link_list = []
	headers_list = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}\
,{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 '},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14 '},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'}]
	dc_dic = dict(DesiredCapabilities.PHANTOMJS)
	dc_dic['phantomjs.page.settings.userAgent'] = headers_list[0]
   	driver = webdriver.PhantomJS(executable_path='E:\phantomjs-2.1.1-windows\\bin\phantomjs')


def output(link_list):
	path = 'D:\my_documents\python\scrape\\find_job\\tianyancha\\meteorology_links.txt'
	with open(path,'wb') as file:
		for link in link_list:
			file.write(link+'\n')

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
			obj = obj['href'].split('.')[0].split('/')[-1]
			city_list.append(obj)
		else:
			pass
	return city_list

def scrape_links(city_list):

	city_list = ['bj']
	categories = ['base','id','estiblishTime','industry','legalPersonName','name','regCapital','regStatus','score']
	for city in city_list:
		# try:
		info_list = []
		i = 1
		url = 'http://'+city+'.tianyancha.com/v2/search/%E6%B0%94%E8%B1%A1.json?&pn='+str(i)+'&base='+city+'&type=scope'
		#url = city.encode('utf8')+'.tianyancha.com/search/p'+str(i)+'?key=%E6%B0%94%E8%B1%A1&searchType=scope'
		print url
		#values ={'user':'Smith','passwd':'123456}
		# request = Request(url)
		# response = urlopen(request)
		sourcecode = requests.get(url).json()
		# json =  response.read()
		json = sourcecode['data']
		for item in json:
			info = []
			for category in categories:
				info.append(item[category])
			#,'id','estiblishTime','industry','legalPersonName'])
			info_list.append(info)
			print info
			print len(info_list)
		# sys("pause")
		time.sleep(10)
		# driver.get(url)
		# driver.implicitly_wait(8)
		# soup = BeautifulSoup(driver.page_source, 'html')
		# soup = BeautifulSoup(response, 'html')
		# page_num = soup.findAll('div', {'class': 'total ng - binding'})
		# print page_num
		# print len(page_num)
		# while i<=page_num:
        #
		# 	url = city.encode('utf8') + '.tianyancha.com/search/p' + str(i) + '?key=气象&searchType=scope'
		# 	print city+':'+'now retriving data from page'+str(i)
		# 	driver.get(url)
		# 	time.sleep(10)
		# 	soup = BeautifulSoup(driver.page_source,'html')
		# 	objs = soup.findAll('a',{'class':'query_name search-new-color'})
		# 	print len(objs)
		# 	if i!=page_num:
		# 		if len(objs)>0:
		# 			for obj in objs:
		# 				link_list.append(obj['href'])
		# 				i+=1
		# 		else:
		# 			pass
		# 	else:
		# 		if len(objs)>0:
		# 			i+=1
		# 	print len(link_list)
		# # except:
		# # 	break
	output(link_list)

def scrape_items():
	
	for obj in objs:
		url = obj['href']
		driver.get(url)
		driver.implicitly_wait(8)
		soup = BeautifulSoup(driver.page_source,'html')
		title = soup.find('div',{'class':'in-block ml10 f18 mb5 ng-binding'}).get_text()
		founded_time = soup.find('div',{'class':'baseinfo-module-content-value ng-binding'})[2].get_text()
		fund = soup.find('div',{'class':'baseinfo-module-content-value ng-binding'})[1].get_text()
		tr = soup.find('div',{'class':'row b-c-white company-content base2017'}).findAll('tr')
		location = tr[4].get_text()
		service = tr[5].get_text()

		print title,founded_time,fund,location,service

set_params()
city_list = scrape_city()
scrape_links(city_list)
#

#execfile('D:\my_documents\python\scrape\\find_job\meteorology\\meteorological_companies.py')



		# request = Request(url,headers=headers_list[random_num])
		# response = urlopen(request).read()
		# data = {'url':'/search?key=%E6%B0%94%E8%B1%A1','searchType':'scope'}
		#
		# print 
		# obj  = driver.find_element_by_class_name('search_result_single search-2017 pb15 ng-scope')
		
		# driver.get('http://www.tianyancha.com/search/p'+str(i)+'?key=%E6%B0%94%E8%B1%A1&searchType=scope')
		# print soup
		# file = open('C:\Users\\think\Desktop\\meteo_comps.txt','wb')
		# file.write(soup)
		# soup = BeautifulSoup(response,'html')

