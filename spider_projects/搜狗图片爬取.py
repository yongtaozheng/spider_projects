# -*- coding：utf-8 -*-import requests
import time
import json
import os
import socket
import requests
from bs4 import BeautifulSoup
import re
# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(8)
 
def sougou_pic_url(num, keyword):
    pic_url= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    for i in range((num // 48) + 1):
        url = 'https://pic.sogou.com/pics?query=' + keyword + '&mode=1&start={}&reqType=ajax&reqFrom=result&tn=0'.format(i * 47)
        imgs = requests.get(url)
        jd = json.loads(imgs.text)
        jd = jd['items']
        for j in jd:
            pic_url.append(j['pic_url'])
 
    #print(len(pic_url))
    return pic_url
 
def down_img(num, keyword):
    pic_url  = sougou_pic_url(num, keyword)
 
    if os.path.exists('D:/p_images/'+keyword):
        pass
    else:
        os.makedirs('D:/p_images/'+keyword)
 
    path = 'D:/p_images/'
    for index,i in enumerate(pic_url):
        try:
            filename = path + keyword + '/' + str(index) + '.jpg'
            print(filename)
            with open(filename, 'wb+') as f:
                f.write(requests.get(i).content)
            if(index >= (num-1)):
                break
        except:
            continue
if __name__ == '__main__':
    while 1:
        print("1.搜索图片")
        print("2.退出程序")
        print("提示：图片默认存储路径为 D:/p_images/")
        choose = int(input("请选择："))
        if(choose == 1):
            keyword = input('请输入图片关键词：')
            num = int(input('请输入爬取图片数目：'))
            down_img(num, keyword)
        elif(choose == 2):
            break
        else:
            print("输入有误，请重新输入！")
