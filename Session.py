
from globals import *

class Session():
    
    def __init__(self, room_list):
        
        self.room_list = room_list
        self.updated = 0
        self.updated_rooms = []
        
    def start(self):
        self.__main_menu()
        
    def __main_menu(self):
        
        def __free_rooms():
            clear()
            if not self.updated:
                print("no rooms have been updated")
            else:
                for room in self.room_list:
                    if room.free_now:
                        print(room.name)
        
        def __exit(room_list):
            pass
        
        choices = {"free": __free_rooms, "update": self.update_menu, "exit": __exit}
    
        while True:
            clear()
            
            print("Select Action")
            print(bar)
            print(f"{'show all currently free updated rooms: ':{'.'}<30}{' free':{'.'}>23}")
            print(f"{'select rooms to update: ':{'.'}<30}{' update':{'.'}>23}")
            print(f"{'exit the program: ':{'.'}<31}{' exit':{'.'}>23}")
            print(bar)
            
            choice = input("input: ").strip().lower()
            clear()
            
            if choice in choices.keys():
                choices[choice]()
            else:
                print("incorrect input")
            clear()
    
    def update_menu(self):
        
        def __parser(input, commands):
            """parser for the command input string, description in README file"""    
            for command in input:
                
                try:
                    digit_index = [index for (index, cmd) in enumerate(command) if cmd.isdigit()][0]
                    parsed_command = command[:digit_index]
                    suffix = command[digit_index:]
                except:
                    parsed_command = command
                    suffix = -1
                
                if parsed_command in commands.keys():
                    commands[command](suffix)
            
        def __add_house(suffix):
            for room in self.room_list:
                if room.house == suffix:
                    update_list.add(room)
                    
        def __update_all(suffix):
            pass
        
        update_list = set()
        
        commands = {"house": __add_house, "h": __add_house, "all":__update_all}
        
        while True:
            clear()
            
            print("Select rooms to update")
            print(bar)
            # print(f"{'show all currently free updated rooms: ':{'.'}<30}{' free':{'.'}>23}")
            # print(f"{'select rooms to update: ':{'.'}<30}{' update':{'.'}>23}")
            # print(f"{'exit the program: ':{'.'}<31}{' exit':{'.'}>23}")
            print(bar)
            
            choice = input("input: ").strip().lower().split()
            clear()
            
            
            
            __parser(choice, commands)
            
            input()
            
            
            # if choice in choices.keys():
            #     choices[choice]()
            # else:
            #     print("incorrect input")
            # clear()
        