import urllib2
import bs4
import telepot

#api_key = "2e2075150a9adcc2"


class Color:
    BOLD = '\033[1m'
    END = '\033[0m'

message = "null"

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
    def get_book_of_the_day(self, url):
        https = "https:"
        packtpub = "https://www.packtpub.com"
        html = self.get_html(url)
        #parsejar
        soup = bs4.BeautifulSoup(html, "lxml")
        title_html = soup.find("div","dotd-title")
        title = title_html.text
        title = self.transform_string(title)

        image_container = soup.find("div", "dotd-main-book-image float-left")
        summary_link_html = image_container.find("a")
        summary_link = summary_link_html["href"]

        image_link_html = image_container.find("img")
        image_link = https + image_link_html['src']

        book_info_soup = self.get_html(packtpub + summary_link)
        book_info_html = bs4.BeautifulSoup(book_info_soup, "lxml")

        book_resume_html = book_info_html.find("div", "book-top-block-info-one-liner")
        book_resume = self.transform_string(book_resume_html.text)

        book_description_html = book_info_html.find("div", "book-info-bottom-indetail-text")
        book_description = self.transform_string(book_description_html.text)

        return title, image_link, book_resume, book_description
        #print title
        #temp_high_n  = temp_high.find("normal")
        #temp_high_n_c  = temp_high_n.find("c").text
        #print temp_high_n_c


    def get_html(self, url):

        #url = "http://api.wunderground.com/api/"
        #url += self.api_key + "/" + apicall
        #url += "/q/CA/" + city + ".xml"

        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    def transform_string(self, title):
        return title.strip()

def handler(msg):
    chat_id = msg['chat']['id']
    chat_message = msg['text']

    #main_keyboard = [['Option #1', 'Option #2'], ['Option #3', 'Option #4']]
    #sub_keyboard = [['Sub option #1_1', 'Sub option #1_2'], ['Sub option #1_3', 'Sub option #1_4'],['Back to Main menu']]


    if chat_message == "/description":
        bot.sendMessage(chat_id, message)

    # if chat_message=='/start':
    #     bot.sendMessage(chat_id, 'Main options', reply_markup={'keyboard': main_keyboard})
    # elif chat_message in [j for i in main_keyboard for j in i]:
    #     # an option from Main keyboard is chosen:
    #
    #     # Ex: Option #1 > You selected Option #1
    #     bot.sendMessage(chat_id, 'Main selected: %s' %chat_message)
    #
    #     if chat_message == 'Option #1':
    #         sub_buttons = {'keyboard': sub_keyboard}
    #         bot.sendMessage(chat_id, 'Sub options', reply_markup=sub_buttons)
    #
    # elif chat_message in [j for i in sub_keyboard for j in i]:
    #     # an option from Sub keyboard is chosen:
    #     if chat_message == 'Sub option #1_1':
    #         bot.sendMessage(chat_id, 'Sub selected %s' %chat_message)
    #     if chat_message == 'Back to Main menu':
    #         bot.sendMessage(chat_id, 'Main options', reply_markup={'keyboard': main_keyboard})
    #
    # else:
    #     bot.sendMessage(chat_id, 'Invalid Message. please select an option from keyboard')



if __name__=="__main__":

    url = "https://www.packtpub.com/packt/offers/free-learning"
    image = "//dz13w8afd47il.cloudfront.net/sites/default/files/imagecache/dotd_main_image/3804OS_4958_Bayesian Analysis with Python.png"
    client = BookClient()
    color = Color()
    book_title, image_link, book_resume, book_description = client.get_book_of_the_day(url)
    message = book_description
    bot = telepot.Bot('468797274:AAEZZcDGCiDXk6jJAV84PLOMc1_RSXzd2IY')
    bot.sendMessage(469707767, '*'+ book_title + '* \n' + book_resume, parse_mode='Markdown')
    bot.sendPhoto(469707767, image_link)
    bot.message_loop(handler, run_forever=True)

    #bot.sendMessage(469707767, book_title + book_resume + book_description)
    #bot.sendPhoto(469707767, image_link)


    #response = bot.getUpdates()
    #print response
    #print bot.getMe()
    #bot.sendMessage(469707767, book_title)
    #img_src="https://www.packtpub.com/sites/default/files/9781786463128.png"
    #bot.sendPhoto(469707767, image_link)
