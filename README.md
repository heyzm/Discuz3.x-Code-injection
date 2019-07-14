### Discuz ML! V3.X存在代码注入漏洞，攻击者通过精心构建的请求报文可以直接执行恶意的PHP代码，进一步可获取整个网站的服务器权限。
#### 漏洞影响版本：

- Discuz!ML v.3.4
- Discuz!ML v.3.2 
- Discuz!ML v.3.3

Usage: ``python poc.py <url> <php function>``
```
python discuz3.x_poc.py url system(id)
```

### Author: heyzm
