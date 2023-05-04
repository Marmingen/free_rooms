###########################################################################
## @author M. Marminge
###########################################################################
## IMPORTS

import time
import requests
from bs4 import BeautifulSoup

###########################################################################
## ROOM CLASS

class Room():
    
    def __init__(self, name="Undefined Room", url=""):
        
        def __room_info():
            if len(self.name) < 6:
                self.house = int(self.name[0])
            else:
                self.house = 10
        
        self.name = name
        self.url = url
        self.house = -1
        self.booked_times = []
        self.free_times = []
        self.all_day = 0
        self.free_now = 0
        
        __room_info()
    
    ## magic methods ##
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    
    ## accessible methods ##
    
    def update_info(self):
        if self.url:
            self.page = requests.get(self.url)
            soup = BeautifulSoup(self.page.content, "html.parser")
            
            self.today = soup.find(class_="headline t dateIsToday")
            self.all_day = self.__occupied_times()
            self.__free_times()
            
        else:
            print("url is not set")

    ## secret methods ##
        
    def __occupied_times(self):
        """saves all occupied sessions in self.times"""
        
        # if self.today is None, then the room is free all day
        if not self.today:
            return 1
        else:
            # find the next <tr> (either a new day or a booked session)
            next_instance = self.today.parent.find_next("tr")
            
            # while the next <tr> exists and is not a new day
            while next_instance and not next_instance.find(class_="headline t"):
                occupied_time = next_instance.find(class_="time tt c-2").text
                self.booked_times.append(tuple(occupied_time.split(" - ")))
                
                # check next <tr>
                next_instance = next_instance.find_next("tr")
            return 0
        
    def __free_times(self):
        
        def __supertime(singletime):
            """converts to minutes"""
            return int(singletime[:2])*60+int(singletime[3:])
            
        def __inverse_supertime(supertime):
            """converts to string of hours and minutes
            output format: "HH:MM" """
            hours = supertime//60
            return f"{hours:02}:{supertime-hours*60:02}"
        
        def __get_time_difference(check_time, booking):
            """time2 = ("HH:MM", "HH:MM")
            returns None if check_time is within or after the booked time
            otherwise returns ("HH:MM", "HH:MM") of free time"""
            
            # checks if check_time is within the booked time
            if __supertime(check_time) >= __supertime(booking[0]) and __supertime(check_time) < __supertime(booking[1]):
                return None
            # checks if check_time is after the booked time
            if __supertime(check_time) >= __supertime(booking[1]):
                return None
            
            return (check_time, booking[0])
            
        # now is GMT+2
        now = time.strftime("%H:%M",time.gmtime(time.time()+2*60**2))
        
        check_time = now
        
        for i in range(len(self.booked_times)):

            # discards 15min free times
            if check_time[:3] + "15" == self.booked_times[i][0]:
                check_time = self.booked_times[i][1]
                continue
            
            free_timeslot = __get_time_difference(check_time, self.booked_times[i])
            
            if free_timeslot:
                self.free_times.append(free_timeslot)
            if check_time == now:
                self.free_now = 1
            
            # checks the next time
            check_time = self.booked_times[i][1]
        
        # appends the last booked time to the days end
        self.free_times.append((check_time,"00:00"))
            
###########################################################################
## MAIN

def main():
    URL = "https://cloud.timeedit.net/uu/web/schema/ri1X50gQ7560YfQQ96Z6578Y0Zy5007591Y62Q060.html"
    
    URL2 = "https://cloud.timeedit.net/uu/web/schema/ri1X50g77560Y7QQ5YZ8258Y0Zy500Q691460Q060f.html"
    
    ROOM = Room()

    ROOM.set_url("4001", URL2)
    
    ROOM.update_info()
    
    print(ROOM.free_times)
    
    print(time.strftime("%Y-%m-%d",time.localtime()))
    
if __name__ == "__main__":
    main()