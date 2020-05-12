import urllib.request
from html.parser import HTMLParser
import os

class NewParser(HTMLParser):
    a = 0
    def get_ext(self,link):
        l = link.split(".")
        return l[-1]
    def handle_starttag(self, tag,attrs):
        if tag == 'img':
            for attr,value in attrs:
                if attr == 'src':
                    image_url = str(self.a) + "." + self.get_ext(value)
                    url = 'image/' + image_url
                    try:
                        urllib.request.urlretrieve(value,url)
                    except:
                        print(str(self.a)+ " : " + "File not found!!")
                    self.a += 1


#parse = NewParser()
if not os.path.isdir('image'):
    os.mkdir('image')

print("Enter Path of the folder : ")
directory = input()
data = os.listdir(directory)

parse = NewParser()
for i in data:
    url = directory + "/" + i
    file = open(url,'r')
    html = file.read()
    parse.feed(html)