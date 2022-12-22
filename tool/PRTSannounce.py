import requests
from bs4 import BeautifulSoup
import regex as re
from lxml import etreeclass 
class announce():
    def __init__(self,act_name,link):
        self.act_namr = act_name
        self.text = requests.get(link)
        self.text = self.deal_txt()[0]
        self.pic = pic
        self.image_dict = {}
    def deal_txt(self):
        self.text = re.subf("<p>(.*?)</p>","{1}",self.text)
        self.text = self.text.replace("<strong>", "'''")
        self.text = self.text.replace("</strong>", "'''")
        self.text = re.subf("""<div class="content">(.*?)</div>""","{1}",self.text)
        p = 1
        pic_dict = {}
        for i in list(re.findall("""<div class="media-wrap image-wrap"><img src=".*?"\/>""",self.text)):
            a = re.search("""<div class="media-wrap image-wrap"><img src="(.*?)"\/>""",i).group()[1]
            pic_name =f"test{str(p)}"
            pic_dict[pic_name] = a
            p += 1
        print(pic_dict)
        return self.text
    def return_pic_dict(self):
        ...



a = announce("风雪过境2022","https://ak.hycdn.cn/announce/Android/announcement/1077_1669881967.html")
print(a.deal_txt())