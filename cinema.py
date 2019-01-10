print('\t WELCOME TO CINEWORLD \t')
print('NOW SHOWING ')
print("SIMMBA \t ZERO \t AQUAMAN \t 3BAHADUR")
def platinum(movie_name):
    if movie_name=="all":
        print("\t Platinum cinema")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("ZERO \t |12:30 pm \t |2:30 \t |900RS")
        print("____________________________________________________________")
        print("Aquaman \t|3:00pm \t |5:30 \t |850RS")
        print("____________________________________________________________")
        print("Aquaman \t|9:30pm \t |12:00 \t |850RS")
        print("____________________________________________________________")
        print("Simmba \t |7:00pm \t |9:00 \t |900RS")
        print('===========================================================')
    elif movie_name=="zero":
        print('===========================================================')
        print("\t Platinum cinema ")
        print('===========================================================')
        print("Movie name | ZERO ")
        print("____________________________________________________________")
        print("Start time |12:30 pm \nEnd time |2:30 \nTicket price |900RS")
        print('===========================================================')
    elif movie_name=="aquaman":
        print('===========================================================')
        print("\t Platinum cinema \t")
        print('===========================================================')
        print("Movie name |Aquaman  ")
        print("____________________________________________________________")
        print("start time|3:00pm \nEnd time  |5:30 \nTicket price |850RS")
        print("____________________________________________________________")
        print("Movie name |Aquaman \nStart time|9:30pm \nEnd time |12:00 \n Ticket price|850RS")
        print('===========================================================')
    elif movie_name=="simmba":
        print('===========================================================')
        print("\t Platinum cinema \t")
        print('===========================================================')
        print("Movie name |Simmba  ")
        print("____________________________________________________________")
        print("start time |7:00pm \n|End time  |9:00 \n Ticket price|900RS")
def gold(movie_name):
    if movie_name=="all":
        print('===========================================================')
        print("\t GOLD cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("ZERO \t |1:30 pm \t |3:30pm \t |700RS")
        print("____________________________________________________________")
        print("Aquaman \t|6:00pm \t |8:30pm \t |650RS")
        print("____________________________________________________________")
        print("Simmba \t|10:30pm \t |01:00am \t |700RS")
        print("____________________________________________________________")
        print("Simmba \t |4:00pm \t |6:00pm \t |700RS")
        print('===========================================================')
    elif movie_name=='zero':
        print('===========================================================')
        print("\t GOLD cinema \t")
        print('===========================================================')
        print("Movie name |ZERO   ")
        print("start time |1:30 pm \nEnd time  |3:30pm \nTicket price |700RS")
        print("____________________________________________________________")
    elif movie_name=="aquaman":
        print('===========================================================')
        print("\t GOLD cinema \t")
        print('===========================================================')
        print("Movie name |Aquaman   ")
        print("Start time|6:00pm \nEnd time|8:30pm \nTicket price  |650RS")
        print("____________________________________________________________")
    elif movie_name=="simmba":
        print('===========================================================')
        print("\t GOLD cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("Simmba \n|10:30pm \n |01:00am \n |700RS")
        print("____________________________________________________________")
        print("Simmba \n |4:00pm \n |6:00pm \n |700RS")
        print('===========================================================')
def silver(movie_name):
    if movie_name=="all":
        print('===========================================================')
        print("\t SILVER cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("ZERO \t |4:30 pm \t |6:30pm \t |600RS")
        print("____________________________________________________________")
        print("ZERO \t|1:00pm \t |3:00pm \t |600RS")
        print("____________________________________________________________")
        print("Aquaman \t|10:30pm \t |01:00am \t |550RS")
        print("____________________________________________________________")
        print("Simmba \t |4:00pm \t |6:00pm \t |600RS")
        print('===========================================================')
    elif movie_name=="zero":
        print('===========================================================')
        print("\t SILVER cinema \t")
        print('===========================================================')
        print("____________________________________________________________")
        print("ZERO \t |4:30 pm \t |6:30pm \t |600RS")
        print("____________________________________________________________")
        print("ZERO \t|1:00pm \t |3:00pm \t |600RS")
        print("____________________________________________________________")
        print("Movie name |start time |End time |Ticket price ")
    elif movie_name=="aquaman":
        print('===========================================================')
        print("\t SILVER cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("Aquaman \n|10:30pm \n |01:00am \n |550RS")
        print("____________________________________________________________")
    elif movie_name=="simmba":
        print('===========================================================')
        print("\t SILVER cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("Simmba \n |4:00pm \n |6:00pm \n |600RS")
        print('===========================================================')
def cinema_3d(movie_name):
    if movie_name=="all":
        print('===========================================================')
        print("\t 3D cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("3 Bahadur \t |1:30 pm \t |3:30pm \t |1000RS")
        print("____________________________________________________________")
        print("Aquaman \t|6:00pm \t |8:30pm \t |1000RS")
        print("____________________________________________________________")
        print("Aquaman \t|10:30pm \t |01:00am \t |1000RS")
        print("____________________________________________________________")
        print("3 Bahadur \t |4:00pm \t |6:00pm \t |1000RS")
    elif movie_name=="3bahadur":
        print('===========================================================')
        print("\t 3D cinema \t")
        print('===========================================================')
        print("Movie name |start time |End time |Ticket price ")
        print("____________________________________________________________")
        print("3 Bahadur \t |1:30 pm \t |3:30pm \t |1000RS")
        print("____________________________________________________________")
        print("3 Bahadur \t |4:00pm \t |6:00pm \t |1000RS")
        movie_time=input("Which of the above timings would you like?(ans in a or b) ")
        if movie_time=="a":
            print("____________________________________________________________")
            print("3 Bahadur \n |1:30 pm \n |3:30pm \n |1000RS")
        elif movie_time=="b":
            print("____________________________________________________________")
            print("3 Bahadur \n |4:00pm \n |6:00pm \n |1000RS")
    elif movie_name=="aquaman":
        print("____________________________________________________________")
        print("Aquaman \t|6:00pm \t |8:30pm \t |1000RS")
        print("____________________________________________________________")
        print("Aquaman \t|10:30pm \t01:00am \t |1000RS")
        print("____________________________________________________________")
        movie_time = input("Which of the above timings would you like?(ans in a or b) ")
        if movie_time == "a":
            print("____________________________________________________________")
            print("Aquaman \n|6:00pm \n |8:30pm \n |1000RS")
            print("____________________________________________________________")
        elif movie_time=="b":
            print("____________________________________________________________")
            print("Aquaman \n|10:30pm \n |01:00am \n |1000RS")
            print("____________________________________________________________")
platinum("all")
gold("all")
silver("all")
cinema_3d("all")
proceed=input("Do you want to continue? ").lower()
pt_number=1
g_number=1
s_number=1
d_number=1
while proceed != "no":
    if proceed=="yes":
        cinema_type=input("Which cinema/screening would you like to choose? ").lower()
        if cinema_type=="platinum":
            platinum("all")
            if pt_number <= 50:
                movie_type=input("Which of the above mentioned movies would you like to watch? ").lower()
                print("\t \t \t ticket no",pt_number)
                pt_number=pt_number+1
                platinum(movie_type)
                proceed="no"
            else:
                print("Sorry! Cinema is full. Please select any other cinema.")
        elif cinema_type=="gold":
            gold("all")
            if g_number <=50:
                movie_type=input("Which of the above mentioned movies would you like to watch? ").lower()
                print("\t \t \t ticket no", g_number)
                gold(movie_type)
                proceed=='no'
            else:
                print("Sorry! Cinema is full. Please select any other cinema.")
        elif cinema_type=="silver":
            silver("all")
            if s_number <=50:
                print("\t \t \t ticket no", s_number)
                movie_type=input("Which of the above mentioned movies would you like to watch? ").lower()
                silver(movie_type)
            else:
                print("Sorry! Cinema is full. Please select any other cinema.")
        elif cinema_type=="3d cinema":
            cinema_3d("all")
            if d_number <= 50:
                print("\t \t \t ticket no", d_number)
                movie_type=input("Which of the above mentioned movies would you like to watch? ").lower()
                cinema_3d(movie_type)
                proceed="no"
            else:
                print("Sorry! Cinema is full. Please select any other cinema.")
        else:
            print("Please select one of the above mentioned cinema type.")
print('COME BACK SOON')
print("")