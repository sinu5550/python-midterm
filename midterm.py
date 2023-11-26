class Star_Cinema:
    __hall_list=[]
    def entry_hall(self,hall):
        Star_Cinema.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no): 
        self._seats = {}
        self._show_list=[]
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        self.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        self._show_list.append((id,movie_name,time))
        self._seats[id] =[[0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0]
                         ]
    def book_seats(self,id, book_seat):
        if id not in self._seats:
               print("\nShow ID not Valid !")        
        try:
            flag = 0
            matrix= self._seats[id]
            for seat in book_seat:
                row,col = seat

                if matrix[row][col] == 1:
                     print(f'\nSeat {seat} is already booked.')
                     flag = 0
                elif (row >= self._rows) or (col >= self._cols) or (row < 0) or (col < 0):
                     print(f'\nSeat {seat} is not valid.')
                     flag = 0
                else:
                     matrix[row][col]=1
                     flag=1
        
            self._seats[id] = matrix
            if flag==1:    
                print(f'\nSeats {book_seat} booked fow show {id}')
        except:
            print("\nSeat is Not Valid !")

    def view_show_list(self):
         for show in self._show_list:
              print(f'Movie Name: {show[1]}({show[0]}) ID: {show[0]} Time: {show[2]}')

    def view_available_seats(self,id):         
        try:
         matrix = self._seats[id]
         print(f'Updated seat matrix for hall {self._hall_no}: ')
         for seat in matrix:
              print(seat)
        except:
         print("Show ID not Valid !\n")


hall1 = Hall(7, 7, 1)
hall1.entry_show("111", "Jibon Majhi", "26/11/23 11:00 AM")
hall1.entry_show("222", "Nouka Pakhi", "26/11/23 02:00 PM")

op = None

while op != 4:
     print("\n----------------------")
     print("1. VIEW ALL SHOW TODAY")
     print("2. VIEW ALL AVAILABLE SEATS")
     print("3. BOOK TICKETS")
     print("4. EXIT\n")
     op = input("Enter Option: ")
     print("----------------------\n")

     if op == "1":
        hall1.view_show_list()
     elif op == "2":
        id = input("Show ID: ")
        hall1.view_available_seats(id)
     elif op == "3":
        id = input("Show ID: ")
        
        if id not in hall1._seats:
            print("Show ID not Valid !\n")         
        else:
            num_of_tickets = int(input("Number of Tickets: "))
            if num_of_tickets <= 0 :
                print("Option is not Valid. Please choose again.")
            seat_book=[]
            for i in range(num_of_tickets):
                row = int(input("Enter seat row: "))
                col = int(input("Enter seat column: "))
                seat_book.append((row,col))
            hall1.book_seats(id,seat_book)
              
          
              
          
     elif op == "4":
          break
     
     else:
          print("Option is not Valid. Please choose again.")
        


              



        


