#!/usr/bin/env python
# -*- coding: utf-8 -*-# vim: set fileencoding=utf8 :
# vim: set fileencoding=utf8 :

import urllib2
import bs4
import sys

https = "https:"

class BookClient(object):


    """
    @param url: url where is going to extract the information.
    @return: Returns the title, oneline information of the book, description and the url of the book image.
    """
    def get_book_of_the_day(self, url):


        html = self.get_html(url)
        soup = bs4.BeautifulSoup(html, "lxml")
        title = self.get_title(soup)
        image_link = self. get_image_link(soup)
        summary_link = self.get_summary_link(soup)
        book_resume, book_description = self.get_summary(summary_link)
        return title, image_link, book_resume, book_description


    """
    @param url: url where is going to extract the information.
    @return: Returns the HTML of the URL.
    """
    def get_html(self, url):

        try:
            f = urllib2.urlopen(url)
        except ValueError:
            print("Can't acced to URL.")
            sys.exit(0)
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    """
    @param summary_link: part of the url where is located the summary information.
    @return: Returns book resume in one line and the book description as strings.
    """
    def get_summary(self, summary_link):

        packtpub = "https://www.packtpub.com"
        book_info_soup = self.get_html(packtpub + summary_link)
        if book_info_soup == None: return None
        book_info_html = bs4.BeautifulSoup(book_info_soup, "lxml")
        if book_info_html == None: return None

        book_resume_html = book_info_html.find("div", "book-top-block-info-one-liner")
        if book_resume_html == None: return None
        book_resume = self.transform_string(book_resume_html.text)

        book_description_html = book_info_html.find("div", "book-info-bottom-indetail-text")
        if book_description_html == None: return None
        book_description = self.transform_string(book_description_html.text)
        return book_resume, book_description


    """
    @param soup: HTML parsed to LXML.
    @return: Returns the book title as string.
    """
    def get_title(self, soup):

        title_html = soup.find("div","dotd-title")
        if title_html == None: return None
        title = title_html.text
        if title == None: return None
        return self.transform_string(title)


    """
    @param soup: HTML parsed to LXML.
    @return: Returns the url where is located the book copert image.
    """
    def get_image_link(self, soup):

        image_container = soup.find("div", "dotd-main-book-image float-left")
        if image_container == None: return None
        image_link_html = image_container.find("img")
        if image_link_html == None: return None
        return  https + image_link_html['src']


    """
    @param soup: HTML parsed to LXML.
    @return: Returns a part of the url whre is located the book summary.
    """
    def get_summary_link(self, soup):

        image_container = soup.find("div", "dotd-main-book-image float-left")
        if image_container == None: return None
        summary_link_html = image_container.find("a")
        if summary_link_html == None: return None
        return summary_link_html["href"]


    def transform_string(self, title):
        return title.strip()



if __name__=="__main__":

    url = "https://www.packtpub.com/packt/offers/free-learning"
    client = BookClient()
    book_title, image_link, book_resume, book_description = client.get_book_of_the_day(url)

    print "******",book_title,"******"
    print book_resume, "\n"
    print "Description:"
    print book_description, "\n"
    #The reason of the image_link is his usage in a telepot project. 
