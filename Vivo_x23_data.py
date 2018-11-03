import requests
import re
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
import json

class get_Vivo_x23_alldatas(object):
    #淘宝七家店铺和京东两家还有vivo官网商城的json评论网址
    def __init__(self):
        self.taobao_urls_list = [
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575602013665&sellerId=883737303&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575446668300&sellerId=2616970884&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575743333423&sellerId=1999920158&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575579308869&sellerId=1637289231&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575580236569&sellerId=1687434761&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575749197781&sellerId=707928640&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=575982975316&sellerId=1864868535&currentPage=',
            ]
        self.jingdong_urls_list = [
            'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv37&productId=31461047265&score=0&sortType=5&page=',
            'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv37&productId=100000469124&score=0&sortType=5&page=',
        ]
        self.vivo_official_urls_list = [
            'http://shop.vivo.com.cn/product/remark?prodId=10486&onlyHasPicture=false&fullpaySkuIdSet=5424%2C5425&pageNum=',
            ]

        self.cpu_count = cpu_count()
    #淘宝，vivo官网商城网页源码解析
    def get_HtmlText(self,url):
        try:
            r = requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.content.decode('utf-8')
        except:
            return ''
    #京东源码解析
    def get_jingdongHtmlText(self,url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ''

    #淘宝评论提取和保存
    def taobao_urlsdata_save(self, html, datalist):
        try:
            datas=re.findall(r'rateContent":"(.*?)"', html)
            data = []
            if datas not in datalist:
                for i in datas:
                    data.append(i)
                    data.extend("\n")
            datalist.append(datas)
            if data:
                f=open("Vivo_x23.txt", 'a+', encoding="utf-8")
                f.writelines(data)
                f.write('\n')
                return 'continue'
            else:
                return 'end'

        except:
            return 'end'


    #淘宝七家店铺网址循环采集
    def taobao_out_urls(self):
        for u in self.taobao_urls_list:
            urls = []
            datalist = []
            for num in range(1, 1000):
                url = u + str(num)
                urls.append(url)
            for html in ThreadPoolExecutor(self.cpu_count).map(self.get_HtmlText, urls):
                data = self.taobao_urlsdata_save(html, datalist)
                if data != 'continue':
                    break

    #京东评论提取和采集
    def jingdong_urlsdata_save(self,html):
        try:
            js_data = html.replace('fetchJSON_comment98vv37(', '').strip(');')
            comment = json.loads(js_data)
            comment = comment['comments']
            data = []
            for i in comment:
                content = i['content']
                data.append(content)
                data.append("\n")
            if data:
                f=open('Vivo_x23.txt', 'a+', encoding="utf-8")
                f.writelines(data)
                f.write('\n')
                return 'continue'
            else:
                return  'end'
        except:
            return 'end'
    #京东两家店铺网址循环
    def jingdong_out_urls(self):
        for u in self.jingdong_urls_list:
            urls=[]
            for num in range(1, 1000):
                url = u + str(num) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
                urls.append(url)

            for html in ThreadPoolExecutor(self.cpu_count).map(self.get_jingdongHtmlText, urls):
                data = self.jingdong_urlsdata_save(html)
                if data != 'continue':
                    break
    #vivo官网商城评论提取和保存
    def vivo_official_urldatas_save(self, html):
        try:
            html = etree.HTML(html)
            data = html.xpath('//li[@class="evaluate"]/p/text()')
            datas = []
            for i in list(data):
                datas.append(i)
                datas.append('\n')
            if data:
                f=open('Vivo_x23.txt', 'a+', encoding='utf-8')
                f.writelines(datas)
                f.write('\n')
                return 'continue'
        except:
            return 'end'
    #vivo官网商城网址循环
    def vivo_official_out_urls(self):

        for u in self.vivo_official_urls_list:
            urls = []
            for num in range(1, 1000):
                url = u + str(num)
                urls.append(url)
            for html in ThreadPoolExecutor(self.cpu_count).map(self.get_HtmlText, urls):
                data = self.vivo_official_urldatas_save(html)
                if data != 'continue':
                    break

#评论清洗
def dealwith_Vivo_x23_alldatas():
    file1 = open('Vivo_x23.txt', 'r', encoding='utf-8')
    file2 = open('Vivo_x23_clean.txt', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if  line == '\n' or line == '此用户没有填写评论!\n' or line == '此用户未填写评价内容\n':
                line = line.replace('此用户没有填写评论!\n','').replace('此用户未填写评价内容\n','')
                line = line.strip('\n')
            file2.write(line)
    finally:
        file1.close()
        file2.close()

def Vivo_x23_data_main():
    getalldatas = get_Vivo_x23_alldatas()
    getalldatas.taobao_out_urls()
    getalldatas.jingdong_out_urls()
    getalldatas.vivo_official_out_urls()
    dealwith_Vivo_x23_alldatas()