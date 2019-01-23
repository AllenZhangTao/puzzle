#coding:utf-8
import os
import requests
import json
import urllib

def getBilibiliImag():

    path = os.path.abspath('.')+"\\downloadpic\\"

    print(path)
    imgs = requests.get('https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=illustration&type=hot&page_num=0&page_size=20')
    jd = json.loads(imgs.text)
    
    jd = jd['data']['items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['item']['pictures'][0]['img_src'])
    m = 0

    print(imgs_url)
    for img_url in imgs_url:
            print('***** '+str(m)+'.jpg *****'+'   Downloading...')
            urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            m = m + 1
    print('Download complete!')

getBilibiliImag()
 