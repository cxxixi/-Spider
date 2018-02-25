#coding:utf-8

import json
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen,Request
from urllib import urlencode
import numpy as np
import re
import time
from proxy import IPspider,Checkout_ip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {'Cookie':'user_trace_token=20170210122001-3088c971-ef48-11e6-a0ea-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
#LGUID=20170210122001-3088cbef-ef48-11e6-a0ea-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=F932455493647CA3A3BF36D28CD0F565; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3Fpx%3Dnewcity%3D%25E4%25B8%258A%25E6%25B5%25B7; SEARCH_ID=8f44145d13d04519b8a840da477b1d9c; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491005685,1491014652,1491057153,1491091722; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491097763; _ga=GA1.2.1798339582.1486700394; LGSID=20170402094127-7cf7b7f2-1745-11e7-b790-525400f775ce; LGRID=20170402094925-99c64af5-1746-11e7-9696-5254005c3644
# def output():

def scrape_city():
    city_url = 'https://www.lagou.com/jobs/allCity.html?keyword=Java&px=default&city=%E5%85%A8%E5%9B%BD&positionNum=500+&companyNum=0&isCompanySelected=false&labelWords='
    city_list = []
    request = Request(city_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'})
    response = urlopen(request)
    soup = BeautifulSoup(response,'html')
    objs = soup.findAll('ul',{'class':'city_list'})
    for obj in objs:
        items = obj.findAll('li')
        for item in items:
            city_list.append(item.a.text)

    return city_list

def set_proxy():
    tag = False
    while not tag:
        random_num = np.random.randint(1,1000)
        tag,ip = IPspider(random_num)
        if tag:
            try:
                proxy_handler = ProxyHandler({'http': proxy})
                opener = build_opener(proxy_handler)
                install_opener(opener)
                scrape_district()
            except:
                tag = False

def scrape_district(city_list):
    district_dic = {}
    # city_list = [city_list[1]]
    i = 0
    while i<=len(city_list):


        # # try:
        # city_url = 'https://www.lagou.com/jobs/list_?px=new'
        # params = {'city':city_list[i].encode('utf8')}
        # print city_list[i]
        # city_url += urlencode(params)
        # city_url += '#filterBox'
        # print city_url
        # district_list = []
        # session = requests.session()
        # values = urlencode({'px': 'new', 'city':'广州','needAddtionalResult':'false'})
        # response = session.post(city_url, data=values, headers=headers)
        # soup = BeautifulSoup(response.text,'html')
        # objs = soup.find('li', {'class': 'detail-district-area'}).findAll('a')
        # for obj in objs:
        #     district_list.append(obj.text)
        # print district_list
        # print len(district_list)
        # time.sleep(5)
        # i+=1
        # print 'ok'
        #     # return none
        # # except AttributeError as e:
        # #     print 'resetting a new proxy'
        # #     set_proxy()


city_list = scrape_city()
scrape_district(city_list)




