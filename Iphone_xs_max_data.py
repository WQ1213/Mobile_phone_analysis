import requests
import re
import json
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count


class get_Iphone_xs_max_alldatas(object):

    def __init__(self):
        self.taobao_urls_list = [
            'https://rate.tmall.com/list_detail_rate.htm?itemId=577383278492&sellerId=2616970884&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=578309370213&sellerId=2616970884&currentPage=',
            'https://rate.tmall.com/list_detail_rate.htm?itemId=577502983385&sellerId=713805254&currentPage=',
            ]
        self.jingdong_urls_list = [
            'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv37&productId=100000287117&score=0&sortType=5&page=',
            'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv37&productId=100000469412&score=0&sortType=5&page=1',
            'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv37&productId=32942468231&score=0&sortType=5&page=',
            'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv37&productId=32901296096&score=0&sortType=5&page=',
            ]
        self.cpu_count = cpu_count()

    def get_HtmlText(self,url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.content.decode('utf-8')
        except:
            return ''

    def get_jingdongHtmlText(self,url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ''

    def taobao_urlsdata_save(self,html, datalist):
        try:
            datas=re.findall(r'rateContent":"(.*?)"', html)
            data = []
            if datas not in datalist:
                for i in datas:
                    data.append(i)
                    data.append("\n")
            datalist.append(datas)
            if data:
                f=open("Iphone_xs_max.txt", 'a+', encoding="utf-8")
                f.writelines(data)
                f.write('\n')
                return 'continue'
            else:
                return 'end'

        except:
            return 'end'

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
                f=open('Iphone_xs_max.txt', 'a+', encoding="utf-8")
                f.writelines(data)
                f.write('\n')
                return 'continue'
            else:
                return 'end'
        except:
            return 'end'

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

def dealwith_Iphone_xs_max_alldatas():
    file1 = open('Iphone_xs_max.txt', 'r', encoding='utf-8')
    file2 = open('Iphone_xs_max_clean.txt', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if  line == '\n' or line == '此用户没有填写评论!\n' or line == '此用户未填写评价内容\n':
                line = line.replace('此用户没有填写评论!\n','').replace('此用户未填写评价内容\n','')
                line = line.strip('\n')
            file2.write(line)
    finally:
        file1.close()
        file2.close()

def Iphone_xs_max_data_main():
    getalldatas = get_Iphone_xs_max_alldatas()
    getalldatas.taobao_out_urls()
    getalldatas.jingdong_out_urls()
    dealwith_Iphone_xs_max_alldatas()
