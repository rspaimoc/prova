import urllib2
import bs4

#api_key = "2e2075150a9adcc2"


class BookClient(object):

    #def __init__(self, api_key):
    #    super(WeatherClient, self).__init__()
    #    self.api_key = api_key

    # def almanac(self, city):
    #     #obtenir xml
    #     xml = self.get_xml("almanac", city)
    #     print xml
    #     #parsejar
    #     soup = bs4.BeautifulSoup(xml, "lxml")
    #     temp_high  = soup.find("temp_high")
    #     temp_high_n  = temp_high.find("normal")
    #     temp_high_n_c  = temp_high_n.find("c").text
    #     print temp_high_n_c
    #
    #     dades = {}
    #     dades["max"] = {}
    #     dades["max"]["normal"] = temp_high_n_c
    #     print dades["max"]["normal"]
        #retornar dades
    def get_book_of_the_day(self):
        html = self.get_html()
        #parsejar
        soup = bs4.BeautifulSoup(html, "lxml")
        title_html = soup.find("div","dotd-title")
        title = title_html.text
        title = self.transform_string(title)

        #print title
        #temp_high_n  = temp_high.find("normal")
        #temp_high_n_c  = temp_high_n.find("c").text
        #print temp_high_n_c


    def get_html(self):
        url = "https://www.packtpub.com/packt/offers/free-learning"
        #url = "http://api.wunderground.com/api/"
        #url += self.api_key + "/" + apicall
        #url += "/q/CA/" + city + ".xml"

        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    def transform_string(self, title):
        print title.strip()

if __name__=="__main__":
    client = BookClient()
    client.get_book_of_the_day()
    #client.almanac("Lleida")
