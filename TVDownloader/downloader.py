#UTF-8

from bs4 import BeautifulSoup
import requests
from  urllib.error import HTTPError
from urllib.request import urlopen
import re


class Downloader(object):

    def __init__(self):

        self.url = ''
        self.ed2kLinks = []
        self.magnet = []
        self.movieTitle = ''
        self.bsObj = {}

    def get_bsObj(self,url = None):
        '''
        Open the url and create the beautiful soup object
        '''
        if url:
            self.url = url
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            print(e)
            return
        if html is None:
            print("URL is not found")
            return
        else:
            self.bsObj = BeautifulSoup(html.read(), 'lxml')


    def get_ed2k(self):
        '''
        get all the ed2k type link from the a tag in the whole page
        '''
        self.get_bsObj()
        
        if self.bsObj:

            links = self.bsObj.find_all('a', {"href" : re.compile("^ed2k://")})
            for link in links:
                self.ed2kLinks.append({"Title" : link.get_text(), "Link" : link['href']})
    
    def get_magnet(self):
        '''
        get all the magnet link from the a tag in the whole page
        '''
        self.get_bsObj()

        if self.bsObj:

            links = self.bsObj.find_all('a', {"href" : re.compile(r"^magnet:\?xt=urn:")})
            for link in links:
                self.magnet.append({"Title" : link.get_text(), "Link" : link['href']})

    def print_link(self, type = None ):

        '''
        There are two type, one type is 'ed2k', the second type is 'magnet'.
        '''
        if type == 'ed2k':
            self.get_ed2k()
            for link in self.ed2kLinks:
                print(link)
        elif type == 'magnet':
            self.get_magnet()
            for link in self.magnet:
                print(link)

    def get_movie_title(self):
        '''
        '''
        self.get_bsObj()

        if self.bsObj:
            self.movieTitle = self.bsObj.find('h1', {'itemprop' : 'name'}).get_text()
            if self.movieTitle:
                print(self.movieTitle)
            else:
                print(r'Don\'t have the title' )




downloader = Downloader()

downloader.url = 'http://www.msj1.com/archives/5013.html'

downloader.get_movie_title()

    








