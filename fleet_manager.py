def init_database(): 
    names = ["Edon", "James", "Joseph", "Turk", "Levi"]
    ranks = ["Captain", "Commander", "Lieutenant", "Captain", "Lt. Commander"]
    divs = ["Command", "Operations", "Security", "Operations", "Command"]
    ids = ["6701, 6702, 6703, 6704, 6705"] ## Sorry about 67 !!!
    return names, ranks, divs, ids

def display_menu(user):
    print("Users Full Name : ", user)
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit") 
    return input("Select option: ") 


def add_member(names, ranks, divs, ids):
    print("Placeholder")

def remove_member(names, ranks, divs, ids):
    print("Placeholder")
    
def update_rank(names, ranks, ids):
    print("Placeholder")

def display_roster(names, ranks, divs, ids):
    print("Placeholder")

def search_crew(names, ranks, divs, ids):
    print("Placeholder")

def filter_by_division(names, divs):
    print("Placeholder")

def calculate_payroll(ranks):
    print("Placeholder")

def count_officers(ranks):
    print("Placeholder")



def main():
    names, ranks, divs, ids = init_database() 

    user = input("Enter your full name: ")
    if user == "":
        user = "Not Known" 

    while True:
        option = display_menu(user) 

        if option == "1":
            add_member(names, ranks, divs, ids)
        elif option == "2":
            remove_member(names, ranks, divs, ids)
        elif option == "3":
            update_rank(names, ranks, ids)
        elif option == "4":
            display_roster(names, ranks, divs, ids)
        elif option == "5":
            search_crew(names, ranks, divs, ids)
        elif option == "6":
            filter_by_division(names, divs)
        elif option == "7":
            print("Total payroll cost:", calculate_payroll(ranks))
        elif option == "8":
            print("High ranking officers:", count_officers(ranks))
        elif option == "9":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()