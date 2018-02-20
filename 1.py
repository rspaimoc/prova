import urllib2
import bs4

#***
#Client web simmple
#@author: rs6
#2e2075150a9adcc2
#***

class Client(object):
    def run(self):
        # get web
        html = readHtml("http://www.eps.udl.cat")
        # parse
        soup = bs4.BeautifulSoup(html, "lxml")
        activitats = soup.find_all("div", "featured-links-item")
        print activitats
        for activitat in activitats:
            title_html = activitat.find("span", "flink-title")
            title  = title_html.text
            link_html = activitat.find("a")
            link = link_html["href"]
            print title,"------", link
        # exec
        pass

def readHtml(url):
    f = urllib2.urlopen("http://www.eps.udl.cat")
    html = f.read()
    f.close()
    return html

if __name__=="__main__":
    client = Client()
    client.run()
