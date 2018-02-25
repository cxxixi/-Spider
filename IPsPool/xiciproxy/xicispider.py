#-*- coding: UTF-8 -*-
#Compatible With: Python2.7
#Author : cxxixi
#Last modified: 2017/4/1

##PURPOSE########
#scrape ip from xiciproxy and store them in MqSQL database


import requests
import re
import pymysql
from pymysql import cursors


#insert instruction for an established database Proxy_info
insert_sql = '''INSERT INTO proxy_info(`ip`,`port`,`live`,`time`) VALUES(%s,%s,%s,%s)'''

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'www.xicidaili.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

#connect to the database
def connectdb():
	global cursor,conn
	config = {'host':'YOUR HOST','port':YOUR PORT,'user':'root','password':'YOUR PASSWORD','charset':'utf8'}
	try:
		conn = pymysql.connect(**config)
		cursor = conn.cursor()
		print 'successfully connect to the server'
	except:
		print 'ERROR: cannot connect to the server'
		return

	sql = 'USE proxy'
	#execute the sql
	cursor.execute(sql)

#insert data
def insert_data(proxy_list):

	for item in proxy_list:
		print item
		cursor.execute(insert_sql,item)
	conn.commit()


def get_request(url,headers):
	html = requests.get(url,headers=headers).text
	if html:
		print 'OK'
		# print html
	return html

#scrape the proxies from the website.
def get_proxy(html_code,proxy_list):

	proxy_list = []
	proxy_ip_list = re.findall(r'<td>\d+.\d+.\d+.\d+</td>',html_code)
	proxy_port_list = re.findall(r'<td>\d+</td>',html_code)
	proxy_time_list = re.findall(r'<td>\d+-\d+-\d+ \d+:\d+</td>',html_code)
	proxy_live_list = re.findall(u'<td>\d+[分钟小时天]+</td>',html_code)
	print len(proxy_live_list)
	for i in range(len(proxy_ip_list)):
		proxy_ip = proxy_ip_list[i].replace('<td>','').replace('</td>','').encode('utf8')
		proxy_port = proxy_port_list[i].replace('<td>','').replace('</td>','').encode('utf8')
		proxy_live = proxy_live_list[i].replace('<td>','').replace('</td>','').encode('utf8')
		proxy_time = proxy_time_list[i].replace('<td>','').replace('</td>','').encode('utf8')
		info = [proxy_ip,proxy_port,proxy_live,proxy_time]
		proxy_list.append(info)
	return proxy_list


if __name__=='__main__':

	num_page = 2
	connectdb()
	for i in xrange(1,num_page):
		url = 'http://www.xicidaili.com/nn/'+str(i)
		print 'now retrieving data from page',i
		html_code = get_request(url,headers)
		proxy_list = []
		proxy_list = get_proxy(html_code,proxy_list)
		insert_data(proxy_list)
	conn.close()

