def init_database(): 
    names = ["Edon", "James", "Joseph", "Turk", "Levi"]
    ranks = ["Captain", "Commander", "Lieutenant", "Ensign", "Lt. Commander"]
    divs = ["Command", "Operations", "Security", "Operations", "Command"]
    ids = ["6701", "6702", "6703", "6704", "6705"] ## Sorry about 67 !!!
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
    new_name = input("Full name : ")
    new_rank = input("Rank : ")
    new_div  = input("Division : ")
    new_id   = input("Unique ID : ")
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("New member added!")

def remove_member(names, ranks, divs, ids):
    rem_id = input("Enter ID of member to remove: ")
    if rem_id in ids:
        idx = ids.index(rem_id)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Removed crew member with ID:", rem_id)
    else:
        print("ERROR: ID not found.")

def update_rank(names, ranks, ids):
    id_rank = input("Enter ID of person whos rank you want to change: ")
    if id_rank not in ids:
        print("ID NOT FOUND!")
        return
    idx = ids.index(id_rank)
    print("Name : ", names[idx], "  Current Rank : ", ranks[idx])

    new_rank = input("Enter new rank : ")
    ranks[idx] = new_rank
    print("Rank Updated.")

def display_roster(names, ranks, divs, ids):
    if len(names) == 0:
        print("No crew in database.")
        return
    else:
        print("Roster List:")
        for i in range(len(names)): 
            print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + ids[i] ) 

def search_crew(names, ranks, divs, ids):
    search = input("Enter name of person you want to search for: ")
    found = False
    for i in range(len(names)):
        if search in names[i]:
            print(ids[i], "-", names[i], "-", ranks[i], "-", divs[i])
            found = True
    if not found:
        print("No matches found.")

def filter_by_division(names, divs):
    print("Placeholder")

def calculate_payroll(ranks):
    total = 0
    for rank in ranks:
        if rank == "Captain":
            total += 6700
        elif rank == "Commander":
            total += 4670 
        elif rank == "Lt. Commander":
            total += 3670
        elif rank == "Lieutenant":
            total += 2670
        elif rank == "Ensign":
            total += 670
        else:
            total += 0
    return total 

def count_officers(ranks):
    Count = 0 
    for rank in ranks: 
        if rank == "Captain" or rank == "Commander":
            Count += 1
    return Count 

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