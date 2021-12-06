import requests
from bs4 import BeautifulSoup
from datetime import datetime
from wiki import search
import random 
from markdown import markdown



query = "thai" #input("Search: ")
limit =  50 #int(input("No. of videos you want: "))
trending_videos = "https://spankbang.com/trending_videos/"
#new_videos = "https://spankbang.com/new_videos/"
#r = requests.get(f"https://spankbang.com/s/{query}").text
r = requests.get(f"{trending_videos}").text
#r = requests.get(f"{new_videos}").text

soup = BeautifulSoup(r, 'lxml')


KEYWORD = ['แทงบอล ไม่อั้น','เว็บ พนัน ฟุตบอล','แทงบอล เว็บพนันบอล เว็บตรง','แทงบอล ufapro888 ดียังไง','เว็บแทงบอล แนะนํา','พนัน ฟุตบอล ออนไลน์ ufapro888','สมัครแทงบอล',
    'แทงบอล กับเว็บหลัก','แทงบอล กับเว็บหลัก','แทงบอล รวยจริง','แทงบอล รายวัน','แทงบอลตามเซียน','เว็บพนันที่ดี','แทงบอลไม่อั้น','พนันบอลสด','เว็บบอลอันดับ1','วิธีเอาชนะ พนันบอล',
    'เว็บสถิติบอล', 'ผลบอลอัตราต่อรอง', 'ผลบอลต่อรอง', 'ผลบอลราคาต่อรองวันนี้', 'ผลบอลพร้อมราคาต่อรอง', 'ผลบอลต่อ', 'ผลบอลสดนาทีต่อนาที', 
    'เว็บพนันบอล', 'เว็บ แทงบอล', 'เว็บ แทงบอลออนไลน์', 'ทางเข้าแทงบอล ', 'เว็บพนันบอล ออนไลน์', 'แทงบอล คาสิโน 888', 'หาเว็บแทงบอล ', 'แทงบอล ออนไลน์ 888', 'พนันบอล 888', 
    'แทงบอล 888', 'แทงบอลออนไลน์', 'พนันบอลออนไลน์ ', 'เว็บ พนัน บอล', 'เว็บพนันบอล คาสิโนบาคาร่า', 'สมัครแทงบอล', 'พนัน บอล ออนไลน์', 'สมัครแทง บอลออนไลน์', ' รับแทงบอลออนไลน์', 
    'เว็บไซต์ แทงบอล ออนไลน์', 'แทง บอล กับ ','เว็บ พนันแทงบอล', 'เว็บ แทง บอล', 'เว็บแทงบอล', ' เว็บแทงบอลออนไลน์', 'เว็บ 888 พนัน บอล ออนไลน์', 'เว็บ ฟุตบอล ออนไลน์',
    'พนัน ฟุตบอล ออนไลน์','สมัคร แทง บอล', 'แทงบอล 888', 'แทงบอล ผ่านเว็บ ', 'แทงบอล888', ' แทงบอล ไม่อั้น', ' คืนยอดเสียทุกเดือน', 'เว็บไซต์ พนัน บอล', ' แทงบอล ให้เครดิต',
    'แทงบอล สด ', 'เว็บ 888', 'เว็บแทง บอล ','เดิมพัน บอล ออนไลน์', 'เว็ปแทงบอล ', 'เล่น พนัน บอล ออนไลน์', 'เว็บ แทงบอลออนไลน์', 'เว็บ พนัน ฟุตบอล', 'แทงบอล ให้คุ้มค่า',
    'แทงบอล ฝากถอนไว', ' สมัครแทงบอลออนไลน์', ' เว็บพนันบอล สมัคร แทงบอลออนไลน์', 'แทงบอล ', ' สมัคร แทงบอลออนไลน์', 'แทงบอล ufapro เว็บพนันบอล เว็บตรง',
    'ufapro สมัครเว็บบอลออนไลน์', 'แทงบอล กับเว็บหลัก', 'เว็บแทง บอล888', 'เว็บ พนัน 888','เว็บพนันบอล 888', 'แทงบอลผ่านเว็บ', 'เว็บไซต์ แทงบอลออนไลน์', 'เว็บไซต์ แทงบอลออนไลน์',
    'สมัครเว็บแท่งบอล ', 'เว็บ เล่นบอล', 'แทงบอล สมัครวันนี้ฟรีเครดิต', 'สมัคร แทง บอล ออนไลน์', 'ufabet บาคาร่า ', 'เว็บ แทงบอลยูโร', 'เว็บ บอล888', 'แทงบอล รูปแบบใหม่', 
    'พนันบอล ออนไลน์', 'เว็บแทงบอล แนะนํา', 'แทงบอล ดียังไง']


for item in soup.find_all('div', class_='video-item')[0:limit]:

    try:
        full_video = item.find("a", class_='thumb')['href']
    except:
        print(f'No videos found for: {query}')

    # sometimes /category/ shows up
    # which isn't a video link.
    if "/category/" in full_video:
        continue

    # cba to find the proper title from html
    # note that this may not always give proper title
    Xtitle = full_video.split('/')[3].replace('+', ' ')
    tag = full_video.split('/')[3].replace('+', '","')
    vid_id = full_video.split('/')[1]

    prev = item.picture.img
    keyk = random.choice(KEYWORD)
    ttext = search(keyk)
    sstext = ttext.split('ค้นหาใน:(หลัก)')[1]
    #ssstext = sstext.split('เหตุผลอื่นซึ่งทำให้ข้อความนี้แสดง')[0]
    #print()

    # sometimes preview image or preview video
    # won't load for whatever reason.
    try:
        prev_vid = prev['data-preview']
        image = prev['data-src']
    except:
        prev_vid = "Not Found"
        image = "Not Found"

    mdFile = (f"""---
author: "I-LIKE ADMIN"
title: {Xtitle}
date: {datetime.today().strftime('%Y-%m-%d')}
description: {Xtitle} {datetime.today().strftime('%Y-%m-%d')} {prev_vid}
tags: ["{tag[0]}","{keyk}"]
keywords: ["{tag}"]
thumbnail: {image}
PreviewVideo: {prev_vid}
---
{datetime.today().strftime('%Y-%m-%d')}{Xtitle}{prev_vid}
<!--more-->

<iframe width="100%" height="315" src="https://spankbang.com/{vid_id}/embed/"></iframe>

# {Xtitle}

{Xtitle}[{keyk}](https://ufapro888s.info/){sstext}

""")
    print(mdFile)
    with open('./exampleSite/content/warehouse/'+Xtitle.replace(' ','-')+".md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(mdFile)
 #https://spankbang.com/watch{full_video}

