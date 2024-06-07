from datetime import date

class Hotel:

    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'stand': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110], 'modern': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210], 'delux': [301, 302, 303, 304, 305, 306, 307, 308, 309, 310], 'president': [401, 402, 403]}#dictionary of hotel rooms
        self.roomprice={1:100,2:200,3:400,4:800}#price per night

    def check_in(self, firstname, lastname, phone):
        roomtype=int(input('Room types: \n1.Standard \n2.Modernized\n3.Delux\n4.Presidental\nSelect a room type (1-4): '))
        if roomtype==1:
            if self.available_rooms['stand']:
                room_number=self.available_rooms['stand'].pop (0)
            else:
                print('Sorry, no standard room available')
                return
        elif roomtype==2:
            if self.available_rooms ['modern']:
                room_number=self.available_rooms['modern'].pop(0)
            else:
                print('Sorry, no modernized room available')
                return
        elif roomtype==3:
            if self.available_rooms ['delux']:
                room_number=self.available_rooms['delux'].pop (0)
            else:
                print('Sorry, no delux room available')
                return
        elif roomtype==4:
            if self.available_rooms ['president']:
                room_number=self.available_rooms['president'].pop(0)
            else:
                print('Sorry, no Presidental room available')
                return
        else:
            print('Invalid room type')
        d,m,y=map(int,input('Enter check-in-date in this kind of format:\n day, month, year: ').split())
        check_in=date(y,m,d)
        self.rooms [room_number] = {
                'firstname': firstname,
                'lastname': lastname,
                'phone': phone,
                'check_in_date': check_in,
                'room_type': roomtype,
        }
        print (f"Checked in {firstname} {lastname} to room: {room_number} on {check_in}")

    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at the moment.")
        else:
            print("Occupied Rooms: ")
            print("------------------------------")
            print('Room type/number, Last name, Phone')
            for room_number, details in self.rooms.items():
                print(details['room_type'],'\t',room_number, '\t',details['lastname'],  '\t',details['phone'])
            print("------------------------------")
    
    def check_out(self, room_number):
        if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms [room_number] ['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype=self.rooms [room_number] ['room_type']
            if roomtype==1:
                self.available_rooms['stand'].append(room_number)
            elif roomtype==2:
                self.available_rooms['modern'].append(room_number)
            elif roomtype==3:
                self.available_rooms['delux'].append(room_number)
            elif roomtype==4:
                self.available_rooms['president'].append(room_number)
            print("------------------------------")
            print('Hotel Bill')
            print (f"Lastname: {self.rooms [room_number] ['lastname']}\nPhone number: {self.rooms [room_number] ['phone']} ")
            print (f'Room Number: {room_number}')
            print (f'Check in date: { check_in_date.strftime(" %d %b ") } ' )
            print (f'Check out date: {check_out_date.strftime(" %d %b ")}')
            print (f'Price per night: Euro. {self.roomprice [roomtype]}')
            roombill=self.roomprice [roomtype] *duration
            print('Totall bill: Euro.',roombill)
            print("------------------------------")
            del self.rooms [room_number]
        else:
            print (f"Room {room_number} is not occupied.")

    def program_start(self):

        while True:
            print('Welcome to the "Hotel California"')
            print("1. Check-in")
            print("2. Display Occupied Rooms")
            print("3. Check-out")
            print("4. Exit")
            option = input("Choose an option (1-4): ")
            if option == '1':
                firstname = input("Enter client's Firstname: ")
                lastname = input("Enter client's Lastname: ")
                phone = input("Enter client's contact number: ")
                self.check_in(firstname, lastname, phone)
            elif option == '2':
                self.display_occupied()
            elif option == '3':
                room_number = int(input("Enter room number: "))
                self.check_out(room_number)
            elif option == '4':
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    h=Hotel()
    h.program_start()
    
if __name__ == "__main__":
    main()