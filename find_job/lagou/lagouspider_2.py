#coding:utf-8

import json
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen,Request
import threading
import numpy as np
import re
# class mThread(threading.Thread):
# 	def __init__(self,threadID,name):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 	def run(self):
# 		print 



# def get_json(url,data):

# 	sourcecode = requests.post(url,data).json()
# 	result = sourcecode['content']['positionResult']['result']
# 	print len(result)

def set_params():

	city_list = ['广州']
	district_list = ['天河区','海珠区','越秀区','番禺区','白云区',萝岗区 荔湾区 黄埔区 花都区 南沙区 增城市 增城区 增城 从化 从化市 从化区]
	source_url = []
	headers_list = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}\
,{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 '},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14 '},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'}]

	for city in city_list:
		city_url = 'https://www.lagou.com/jobs/list_?px=default&city='+city
		print city_url
		random_num = np.random.randint(0,9)
		request = Request('https://www.lagou.com/jobs/list_?px=default&city=%E5%B9%BF%E5%B7%9E',headers = headers_list[random_num])
		response = urlopen(request)
		print response.read()

		soup = str(BeautifulSoup(response,'lxml'))
		file = open('C:\Users\\think\Desktop\\html.txt','wb')
		file.write(soup)

		districts = re.findall('^(<a)',soup)#,{'class':'detail-district-area'})#.findAll('a')[1:]

		
		print districts
		for district in districts:
			print district.get_text()



	while count<=30:
		for city in city_list:

			url = baseurl+city 
			# if count ==1：
			data = {'pn':str(count)}#'first'='true' }
			print count
			get_json(url,data)

		count+=1

set_params()
##

# 建线程
#execfile('D:\my_documents\python\scrape\\find_job\lagou\lagouspider_2.py')

