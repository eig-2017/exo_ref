import string
import requests
import time
from requests_futures.sessions import FuturesSession
from bs4 import BeautifulSoup as bs
from pymongo import Client
session = FuturesSession()

conn = Client()
db =
def build_datastore_SIL():
    urls = [("http://www-01.sil.org/iso639-3/codes.asp?order=639_2&letter=%s"%n) for n in string.ascii_lowercase]

    def store_results(future):
        response = future.result()

        data = bs(response.text, "lxml").find("table", {"class":"stripeMe"})
        letter_ref = "\n".join(["\t".join([n.text for n in  n.findAll("td")
                                    if n.text != ""])
                                    for n in data.findAll("tr") if n.text != ""])
        # print(response.url, len(letter_ref))
        print(letter_ref)

    for url in urls:

        future = session.get(url)
        future.add_done_callback(store_results)

def build_datastore_ILOC():
    '''bloqué par le proxy et LOC: remote adress IP'''
    urls = ["http://id.loc.gov/search/?q=cs:http://id.loc.gov/vocabulary/iso639-2&start=%i"%i for i in range(1, 521, 20)]
    #/vocabulary/iso639-2/mun

    def store_results(future):
        response = future.result()

        data = bs(response.text, "lxml").find("tbody")
        #print(data)
        for n in data.findAll("tr"):
            print("\t".join(cell.text.strip() for cell in n.findAll("td")))

        # letter_ref = "\n".join(["\t".join([n.text for n in  n.findAll("td")
        #                             if n.text != ""])
        #                             for n in data.findAll("tr") if n.text != ""])
        # print(response.url, len(letter_ref))
        #print(repr(letter_ref))

    for url in urls:

        future = session.get(url)
        future.add_done_callback(store_results)

if __name__ =="__main__":

    build_datastore_ILOC()
