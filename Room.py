###########################################################################
## 
###########################################################################
## IMPORTS

import time
import requests
from bs4 import BeautifulSoup

###########################################################################
## ROOM CLASS

class Room():
    def __init__(self, url=""):
        self.url = url
    
    def update_info(self):
        if self.url:
            self.page = requests.get(self.url)
            soup = BeautifulSoup(self.page.content, "html.parser")
            
            times = soup.find(class_="headline t dateIsToday")
            times = times.find_next(class_="time tt c-2")
            print(times)
            
            self.__update_day_list(soup)
            
        else:
            print("url is not set")
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    
    def __update_day_list(self, soup):
        self.today = soup.find(class_="headline t dateIsToday")
        self.days = [day.text[4:15].strip() for day in soup.find_all(class_="headline t")]
        
    def set_url(self, name, in_url):
        self.name = name
        self.url = in_url
        self.page = requests.get(self.url)
    
    def is_free(self):
        if not self.today:
            return "is free all day"
        else:
            pass


def main():
    URL = "https://cloud.timeedit.net/uu/web/schema/ri1X50gQ7560YfQQ96Z6578Y0Zy5007591Y62Q060.html"
    
    ROOM = Room()

    ROOM.set_url("4001", URL)
    
    ROOM.update_info()

    print(ROOM.is_free())
    
    print(time.strftime("%Y-%m-%d",time.gmtime()))
    
if __name__ == "__main__":
    main()