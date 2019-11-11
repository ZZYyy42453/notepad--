import re
#普通字符作为原子
string="yunfasdfasfdasdf"
pat="yun"
rst=re.search(pat,string)
print(rst)
#非打印字符
#\n换行符\t制表符
string1='''taobaodfhasdfas'''
pat="\n"
rst=re.search(pat,string1)
print(rst)
#通用字符作为源自
'''
\w   匹配任意一个字母数字下划线
\W    匹配任意非一个字母数字下划线
\d    十进制数
\D    非十进制数
\s    空白字符
\S    除空白字符
'''
string1='''taobaodfha   ewr4 564546512sdfas'''
pat="\w\d\s\d"
rst=re.search(pat,string1)
print(rst)

#原子表
string1='''taobaodfha   ewr4 564546512sdfas'''
pat="tao[^you]"#^为非的意思
rst=re.search(pat,string1)
print(rst)

#元字符
'''
. 除换行外的任意字符
^不再原子表时代表匹配初始位置
$结束位置
*0/1/多次
?0/1次
+1/多次
{n}恰好出现n次
{n,}至少n次
|模式选择符或
()模式单元,返回小括号内的内容
'''
string1="taobaodfha   ewr4 564546512sdfas"
pat="tao....."
pat="s*"
rst=re.search(pat,string1)
print(rst)
#模式修政符
'''
I 匹配是忽略大小写
M 多行匹配
L 本地化识别匹配
U unicode
S 让.匹配包括换行符
'''
string="Python"
pat="pyt"
rst=re.search(pat,string,re.I)
print(rst)


#贪婪模式和懒惰模式
string="Pythogny是zhanasg"
pat="p.*g"#贪婪模式
pat2="p.*?g"#懒惰模式
rst=re.search(pat,string,re.I)
rst2=re.search(pat2,string,re.I)
print(rst)
print(rst2)

#正则表达式函数
'''
match开头匹配
search
3全局匹配函数re.compile(正则表达式).findall(数据)
'''
string="Pythoganany是zanaanaanaanahaananasg"
pat="ana"
rst=re.compile(pat).findall(string)
print(rst)

#实例
#匹配网址
string="<a href='http://www.baidu.com'>百度首页</a>"
pat="[a-zA-Z]+://[^\s]*[.com|.cn]"
rst=re.compile(pat).findall(string)
print(rst)
#匹配电话号码
string="dsfadkfjhakjsdhfak081-18943003856sfdads"
pat="\d{3}-\d{11}"
rst=re.compile(pat).findall(string)
print(rst)
