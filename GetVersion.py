#coding=utf-8

import requests
from lxml import etree

def get_version():
    html = requests.get("https://www.pgyer.com/xxxx")
    etree_html = etree.HTML(html.text)
    content_1 = etree_html.xpath('/html/body/div[3]/div[5]/div/div[1]/div/p/span/text()')
    content_2 = etree_html.xpath('/html/body/div[3]/div[5]/div/div[2]/div/p/span/text()')
    for ios_verison,andriod_version in zip(content_1,content_2):
        return ios_verison,andriod_version
