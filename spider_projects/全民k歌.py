import requests
from bs4 import BeautifulSoup
import re

#默认存储位置
root = "D://p_music//"
while(1):
    print("默认下载位置为D://p_music//，可以先自行创建")
    print("1.下载歌曲")
    print("2.退出程序")
    choose = input("请选择：")
    if choose == '1':
        #歌曲名字
        name = input("请输入歌曲名字：")
        #歌曲链接
        mainPage =input("请将歌曲分享的链接粘贴到这里：")
        #f'https://kg.qq.com/node/play?s=pkoD3KpUbu6T6pss&shareuid=6b9f9d852c28358e3c&topsource=a0_pn201001003_z11_u920095258_l1_t1589955099__&g_f=' #主网页
        r = requests.get(mainPage)
        src = r.text
        pattern = re.compile(r'\"playurl\":\"http:\/\/.+\.m4a')
        url = pattern.findall(src)
        lists = url[0].split("\"")
        print("歌曲链接："+lists[-1])
        r1 = requests.get(lists[-1])
        music = r1.content
        with open(root+name+".mp4",'wb') as f:
            f.write(music)
            print("下载完成")
            print("——————————————————————————")
    elif choose == '2':
        print("已退出程序")
        print("——————————————————————————")

        break
    else :
        print("请输入正确指令")
        print("——————————————————————————")

