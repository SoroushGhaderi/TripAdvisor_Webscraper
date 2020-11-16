import requests
import json
from bs4 import BeautifulSoup
import time

def save_object( file_name  , saved_object , writing_method):
    saved_object = json.dumps(saved_object, indent=3 , ensure_ascii= False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object)

def hotel_link_scrapper():

    counter = 1
    temp = 30
    full_links = []
    base_url = "https://www.tripadvisor.com"
    base_url_hotels = 'https://www.tripadvisor.com/Hotels-g187849-Milan_Lombardy-Hotels.html'
    while counter <= 46:
        if counter == 1:
            response = requests.get (base_url_hotels)
            soup = BeautifulSoup ( response.text , 'html.parser' )
            name_of_hotel_with_link = soup.find_all('a' , attrs={'class':'property_title prominent'})
            link_of_hotels = [hotel["href"] for hotel in name_of_hotel_with_link]
            for link in link_of_hotels:
                full_links.append(base_url + link)

            save_object("milan_hotels.json", full_links, "w")

            counter += 1
        else:
            response = requests.get ('https://www.tripadvisor.com/Hotels-g187849-oa{}-Milan_Lombardy-Hotels.html'.format(temp) )
            soup = BeautifulSoup ( response.text , 'html.parser' )
            name_of_hotel_with_link = soup.find_all('a' , attrs={'class':'property_title prominent'})
            link_of_hotels = [hotel["href"] for hotel in name_of_hotel_with_link]
            for link in link_of_hotels:
                full_links.append(base_url + link)
            
            save_object("milan_hotels.json", full_links, "w")

            counter += 1
            temp = temp + 30
    
    time.sleep(1)


if __name__ == "__main__":
    hotel_link_scrapper()