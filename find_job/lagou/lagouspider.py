#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

def main():

	driver = webdriver.PhantomJS(executable_path='E:\phantomjs-2.1.1-windows\\bin\phantomjs')

	driver.get('https://www.lagou.com/jobs/list_?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=')
	soup = BeautifulSoup(driver.page_source,'xml')
	print soup
	count = 0
	while True:
		print count
		count += 1
		source = soup.find('ul',{'class':'item_con_list'})

		source = source.findAll('li')#,{'class':'con_list_item first_row default_list'})
		print len(source)
		for item in source:
			try:
				title = item.find('h2').get_text().strip()
				# name = item.find('span',{'class':'dy-name ellipsis fl'}).get_text()
				# audience = item.find('span',{'class':'dy-num fr'}).get_text()
				print title#,name,audience
			except:
				print 'error'
				continue
		element = driver.find_element_by_class_name('next_disabled next')
		if element:
			element.click()
			soup = BeautifulSoup(driver.page_source, 'xml')
		if driver.find_element_by_class_name('next_disabled next ban'):
			break

if __name__=='__main__':
	main()

#execfile('D:\my_documents\python\\scrape\\find_job\lagou\\lagouspider.py')