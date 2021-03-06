# -*- coding:utf-8 -*-
'''
Created on 2019/09/04
@author: damxin
@group :
@contact: nfx080523@hotmail.com
'''

# 市场类型字段
DICTCONS_MARKETTYPE = {1: "沪市A股",
                       2: "深市A股",
                       3: "中小板",
                       4: "创业板",
                       5: "新三板",
                       6: "科创板"}
# 产品代码与市场类型
DICTCONS_CODETOMARKETTYPE = {"000": 2,  "001": 2,  "002": 3,  "003": 2,
                             "100": 97, "110": 98, "120": 98, "129": 97,
                             "200": 83, "201": 96,
                             "300": 4 , "310": 95,
                             "500": 94, "550": 93,
                             "600": 1,  "601": 1,  "603": 1,  "688": 6,
                             "700": 92, "710": 91, "701": 90, "711": 89, "720": 88, "730": 87, "735": 86, "737": 85,
                             "900": 84}

# 公司年资产负债表
#http: // quotes.money
#.163.com / service / zcfzb_600675.html?type = year
