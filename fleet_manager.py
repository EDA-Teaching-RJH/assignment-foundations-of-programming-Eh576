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