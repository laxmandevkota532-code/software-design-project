
# Movie related function
# List movies
# Select movie
# simple movie booking script
# movies: id, title, time, price
films = [
    {"id": 1, "name": "Avengers", "time": "1:00 PM", "price": 10},
    {"id": 2, "name": "Bahubhali", "time": "4:00 PM", "price": 8},
    {"id": 3, "name": "RRR", "time": "7:00 PM", "price": 12},
    {"id": 4, "name": "KGF", "time": "9:30 PM", "price": 9}
]

def show_list():
    print("\n--- WHAT'S PLAYING ---")
    for f in films:
        # id | name | time | cost
        print(f"[{f['id']}] {f['name']} @ {f['time']} (${f['price']})")

def book_ticket():
    show_list()
    
    # get user choice
    uid = input("\nEnter Movie ID: ")
    
    if not uid.isdigit():
        print("Error: Input a number.")
        return
    
    uid = int(uid)
    pick = None
    
    # find the movie in the list
    for f in films:
        if f['id'] == uid:
            pick = f
            break
            
    if not pick:
        print("Movie not found.")
        return

    #  NEW FEATURE: Seat Booking
    num = input(f"How many tickets for {pick['name']}? ")
    
    if not num.isdigit() or int(num) <= 0:
        print("Invalid ticket count.")
        return
    
    count = int(num)
    total = count * pick['price']
    
    print("-" * 20)
    print(f"CONFIRMED: {count}x {pick['name']}")
    print(f"TOTAL COST: ${total}")
    print("Enjoy the show!")

book_ticket()

