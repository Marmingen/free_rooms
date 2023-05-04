###########################################################################

###########################################################################
## IMPORTS

import os
import time
import csv
from Room import Room
from Session import Session

from globals import *

###########################################################################
## CLASSES

###########################################################################
## FUNCTIONS

def load_urls():
    
    room_list = []
    loaded_rooms = 0
    
    print(f"loaded rooms: {loaded_rooms}", end="\r")
    
    with open("urls") as urls:
        reader = csv.reader(urls)
        
        for row in reader:
            room_list.append(Room(row[0], row[1]))
        
            loaded_rooms += 1
        
            print(f"loaded rooms: {loaded_rooms}", end="\r")
        
    print(f"loaded rooms: {loaded_rooms}", end="\n")
        
    return room_list


###########################################################################
## MAIN

def main():
    
    room_list = load_urls()
    
    current_session = Session(room_list)
    
    current_session.update_menu()
    
if __name__ == "__main__":
    main()

# time.strftime("%Y-%m-%d",time.gmtime())