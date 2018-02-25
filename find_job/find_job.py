#-*- coding:utf-8 -*-
# 异步爬虫 ，对于每一个分类建一个爬虫，对列表内的每一个分类，爬取分类下的所有link

import threading
import time
import Queue
from bs4 import BeautifulSoup
import requests
import csv
import re
import sys
from urllib2 import Request,urlopen,HTTPError,URLError,ProxyHandler,build_opener,install_opener

def set_params():
	global label_list,link_list,threadLock
	link_list = []
	threadLock = threading.Lock()
	# oriurl = 'http://gz.esf.leju.com/house/'
	label_list = ['/a1337/','/a1359/']

	#page_list = [i for i in xrange(1,page_num+1)]
	#Queue.Queue(maxsize=0)


class myThread(threading.Thread):
	def __init__(self,threadID,name,label):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.label = label
	def run(self):
		print "starting" + self.name
		threadLock.acquire()

		scrape_link(self.threadID,self.label)
		threadLock.release()


def scrape_link(ID,label):
	page_num = 10
	baseurl = 'http://gz.esf.leju.com/house/'
	while page_num>=0:
	
		page_link = baseurl+'/n'+str(page_num)+'-'+label
		request = Request(page_link)
		response = urlopen(request)
		soup = BeautifulSoup(response,'html.parser')
		print page_link,ID
        	obj = soup.findAll('h3',{'class':'house-title'})
        	for i in range(len(obj)):
            		link = obj[i].a['href']
            		link_list.append(link)  
        	print len(link_list)    
		#time.sleep(delay)
		page_num += -1

def test():
	count = 1
	for label in label_list:
		thread = myThread(count,'thread'+str(count),label)
		thread.start()
		count += 1

set_params()
test()

#execfile('D:\my_documents\python\scrape\\find_job\\find_job.py')
