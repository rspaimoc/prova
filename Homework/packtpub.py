import urllib2
import bs4
import telepot


message = "null"

class BookClient(object):

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


    def get_html(self, url):



        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    def transform_string(self, title):
        return title.strip()



if __name__=="__main__":

    url = "https://www.packtpub.com/packt/offers/free-learning"
    image = "//dz13w8afd47il.cloudfront.net/sites/default/files/imagecache/dotd_main_image/3804OS_4958_Bayesian Analysis with Python.png"
    client = BookClient()
    color = Color()
    book_title, image_link, book_resume, book_description = client.get_book_of_the_day(url)
    message = book_description
    print "verga"
