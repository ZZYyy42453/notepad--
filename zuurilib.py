#urlretrieve(网址,本地文件地址) 直接下载网页到本地
#urllib.request.urlretrieve("http://www.baidu.com","C:\\Users\\zy\\Desktop\\baidu.html")
#urllib.request.urlcleanup()
#查看简介信息info()
#file=urllib.request.urlopen("http://www.baidu.com")
#print(file)
#getcode()200为正常状态码
#print(file.getcode())
#获取当前访问网页的url,geturl()
#print(file.geturl())
'''
import urllib.request
def test_one():
       #超时设置
    for i in range(0,100):
        file=urllib.request.urlopen("http://www.baidu.com",timeout=1)
        try:
            print(len(file.read().decode("utf-8")))
        except Exception as er:
            print("出现异常")
'''
'''
#get请求实例
#浏览器伪装
import urllib.request,re
keywd="张雨"
keywd=urllib.request.quote(keywd)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
base_url="https://www.baidu.com/s?wd="+keywd+"&pn="
def test_one():
    for i in range(0,10):
        resquest = urllib.request.Request(url=base_url+str(i*10), headers=headers)
        data=urllib.request.urlopen(resquest).read().decode('utf-8')
        pat='"title":"(.*?)"'
        rst=re.compile(pat).findall(data)
        print(rst)
'''
'''
import urllib.request,re
keywd="张雨"
keywd=urllib.request.quote(keywd)
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
def test_one():
    for i in range(0,10):
        url="https://www.baidu.com/s?wd="+keywd+"&pn="+str(i*10)
        data=opener.open(url).read().decode('utf-8')
        pat='"title":"(.*?)"'
        rst=re.compile(pat).findall(data)
        print(rst)
'''
'''
#post请求实战
import urllib.request,urllib.parse
def test_one():
    posturl="https://www.iqianyue.com/mypost/"
    postdata=urllib.parse.urlencode({
        "name":"张雨",
        "pass":"zhangyu"
    }).encode("utf-8")
    #进行post,需要使用urllib.request下的Request(真实post地址,post数据)
    req=urllib.request.Request(posturl,postdata)
    data=urllib.request.urlopen(req).read().decode('utf-8')
    print(data)

#异常处理
'''
'''
URLError:包括HTTPError
1)连不上服务器
2)远程url不存在
3)无网络
4)触发hTTPerror
'''
'''
import urllib.request
import urllib.error
def test_one():
    try:
        urllib.request.urlopen("http://www.baidu.com")
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
'''
'''
#爬取腾讯新闻实战
import urllib.request,re
url="http://news.baidu.com/tech"
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
#resquest = urllib.request.Request(url=url, headers=headers)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat='<li><a.*?href="(.*?)".*?mon="'
rst=re.compile(pat).findall(data)

def test_one():
    for i in range(0,100):
        url=rst[i]
        data1 = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        pat1='class="bjh-p">(.*?)</span>'
        pat2='<title>(.*?)</title>'
        rst1=re.compile(pat1).findall(data1)
        rst2=re.compile(pat2).findall(data1)
        print(rst2)
        print(rst1)
'''
#爬去csdn博客文章
'''
import urllib.request,re
url = "https://blog.csdn.net"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
resquest = urllib.request.Request(url=url, headers=headers)
def test_one():

    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='<a.*?href="(.*?)" target="_blank"'
    rst1=re.compile(pat).findall(data)

    #for i in range(0,len(rst1)):
    url1 = rst1[0]
    resquest = urllib.request.Request(url=url1, headers=headers)
    data2 = urllib.request.urlopen(url1).read().decode("utf-8", "ignore")
    pat = '<title>(.*?)</title>'
    rst2 = re.compile(pat).findall(data2)
    print(data2)
'''
'''
import urllib.request,re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
base_url = "http://www.budejie.com/"
for i in range(1,6):
    url=base_url + str(i)
    resquest = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(url).read().decode("UTF-8")
    #print(data)
    pat ='<a href="/detail-\d{8}.html">(.*?)</a>'
    rst=re.compile(pat).findall(data)
    print(rst)
'''
'''
#用户代理池构建
import urllib.request,re,random
uapools=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/68.0']

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
ua(uapools)
'''


'''
#ip代理构建
import urllib.request
ip="0.0.0.0:6000"
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
urllib.request.install_opener(opener)
url="http://www.baidu.com"
data=urllib.request.urlopen(url).read()
print(len(data))
'''
'''
#淘宝爬虫
import requests,re
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'}
kwd="arduino"
base_url="https://s.taobao.com/search?q="
url="https://s.taobao.com/search?q=arduino&s=44"
data=requests.get(url,headers=headers).text
pat="ST NUCLEO-F446RE STM32F446RET6 Cortex-M4开发板 兼容"
rst=re.compile(pat).findall(data)
print(data)
'''
def main():
    test_one()
    print("run well")

if __name__ == '__main__':
    main()