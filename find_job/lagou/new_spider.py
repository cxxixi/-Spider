import requests
from urllib2 import Request,urlopen
from urllib import urlencode
from bs4 import BeautifulSoup
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Cookie": "user_trace_token=20170210122001-3088c971-ef48-11e6-a0ea-525400f775ce; LGUID=20170210122001-3088cbef-ef48-11e6-a0ea-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=BD586850FBEEAF377B7DD662EC284BF5; TG-TRACK-CODE=search_code; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491352225,1491370892,1491387113,1491435847; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491447976; _ga=GA1.2.1798339582.1486700394; LGRID=20170406110619-01dabde2-1a76-11e7-9fb1-525400f775ce; SEARCH_ID=2dd5fb112f9a461d80d5be94cf4546e5"
}

session = requests.session()


url2 = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&district=%E6%9C%9D%E9%98%B3%E5%8C%BA&bizArea=%E6%9C%9B%E4%BA%AC&needAddtionalResult=false'
values = urlencode({'px':'new','city':'北京','district':'朝阳区','bizArea':'望京'})
data={"first":"false","pn":1,"kd":"数据分析师"}

response=session.post(url2,data=values,headers=headers)
max_num = len(json.loads(response.text)["content"]["positionResult"]["result"])
print max_num
