import urllib2
import bs4

api_key = "2e2075150a9adcc2"


class WeatherClient(object):

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def almanac(self, city):
        #obtenir xml
        xml = self.get_xml("almanac", city)
        print xml
        #parsejar
        soup = bs4.BeautifulSoup(xml, "lxml")
        temp_high  = soup.find("temp_high")
        temp_high_n  = temp_high.find("normal")
        temp_high_n_c  = temp_high_n.find("c").text
        print temp_high_n_c

        dades = {}
        dades["max"] = {}
        dades["max"]["normal"] = temp_high_n_c
        print dades["max"]["normal"]
        #retornar dades

    def get_xml(self, apicall, city):
        url = "http://api.wunderground.com/api/"
        url += self.api_key + "/" + apicall
        url += "/q/CA/" + city + ".xml"

        f = urllib2.urlopen(url)
        xml = f.read()
        f.close()
        return xml

if __name__=="__main__":
    client = WeatherClient(api_key)
    client.almanac("Lleida")
