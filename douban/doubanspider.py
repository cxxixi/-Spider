##-*- coding:utf-8 -*-
#Compatible With: Python2.7
#Author : cxxixi
#Last modified: 2017/2/25

##scrape bookname and info from douban,a book sharing and recommendation website according to specific key words.

from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError,URLError,Request
import urllib
import sys
import numpy as np
import time
import re
import csv

#py2.7 has kind of problems with encoding when it comes to Chinese
#Just ignore it if you're using python3 
reload(sys)
sys.setdefaultencoding('gb18030')

headers_list = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}\
,{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
#}
 
 
def crawl_book(book_tag):
	book_num = 0
	missed_url = []
	
##check whether the tag exists##
	try:
		url = 'http://book.douban.com/tag/'+book_tag
		req = Request(url,headers=headers_list[0])
	except HTTPError as e:
		print 'oops! HTTPError'
		return None
	html = urlopen(req)
	bsobj = BeautifulSoup(html,'html')
	if bsobj == None:
		print('No such tag exists.')	
	else: 
		print('start to collect data!')
		page_num = bsobj.findAll('a',{'href':re.compile('^(/tag).*(type=T)$')})[-2].get_text()
		page_num = int(page_num)
		while(page_num >=1):
			seed=np.random.rand()
			time.sleep(seed*5)
			url = 'http://book.douban.com/tag/'+book_tag+"?start="+str(book_num)+'&type=T'
			try:
				print time.time()
				req = Request(url,headers=headers_list[(book_num/20)%3])
				resp = urlopen(req,timeout=15)
				print time.time()
				print 'successfully move to next page'
			except (Exception,HTTPError,URLError),e:
				print e,'oops'
				resp = None
				missed_url.append(url)
				continue
			try:
				bsobj = BeautifulSoup(resp,'html')
			 	obj_list = bsobj.findAll('li',{'class':'subject-item'})
			 	for obj in obj_list:
		 			book_title = obj.h2.a['title'].strip()
		 			book_link = obj.h2.a['href']
		 			pub_info = obj.find('div',{'class':'pub'}).get_text().strip()
		 			try:
		 				rating_nums = obj.find('span',{'class':'rating_nums'}).get_text().strip()
		 			except AttributeError:
		 				rating_nums = None
		 			try:
		 				comment_num = obj.find('span',{'class':'pl'}).get_text().strip()
		 			except:
		 				comment_num = None
		 			try:
		 				description = obj.p.get_text().strip()
		 			except AttributeError:
		 				description = None
			except AttributeError as e:
				print e#

			page_num += -1
			book_num+=20
			info = [book_title,book_link,pub_info,rating_nums,comment_num,description]

			csv_writer.writerow(info)
			
		
def crawl_prep(book_tag_list):
	for tag in book_tag_list:
		book_list = crawl_book(tag)


def print_book_list(book_tag_list,book_list):

	path = 'PUT YOUR PATH HERE'
	for i in range(len(book_tag_list)):
		path += book_list[i]+'_'	
	csv_file = open(path,'w')
	for item in range(len(book_list)):
		csv_file = csv.writer(book_list[item])


if __name__=="__main__":

	book_tag_list = [PUT THE KEY WORD(S) HERE]
	path = 'PUT YOUR PATH HERE'
	global csv_writer
	csv_file = open(path,'w')
	csv_writer = csv.writer(csv_file)
	crawl_prep(book_tag_list)
	#print_book_list(book_tag_list,book_list)
