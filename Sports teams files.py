import os
team_file = open("teams.txt", "r+")
empty = False
def main():
    global empty

    name = input("Please enter your name: ")
    team1 = input("Please enter name of your favorite football team: ")
    team2 = input("Please enter name of your second favorite football team: ")
    team3 = input("Please enter name of your third favorite football team: ")
    team4 = input("Please enter name of your fourth favorite football team: ")
    team5 = input("Please enter name of your fifth favorite football team: ")
    
    if team1 == "Sunderland" or team2 == "Sunderland" or team3 == "Sunderland" or team4 == "Sunderland" or team5 == "Sunderland":
        print("Your tastes are trash")
        team_file.close()
        exit()
    if team1 == "sunderland" or team2 == "sunderland" or team3 == "sunderland" or team4 == "sunderland" or team5 == "sunderland":
        print("Your tastes are trash")
        team_file.close()
        exit()
    
    if os.stat("teams.txt").st_size != 0:
        team_file.truncate(0)

    write(name, team1, team2, team3, team4, team5)

    read()

    use_again()
    
def write(name, team1, team2, team3, team4, team5):
    
    team_file.seek(0)
    
    newline = name + "'s favorite team is" + team1 + "\n"
    team_file.write(newline)
    
    newline = name + "'s second favorite team is" + team2 + "\n"
    team_file.write(newline)
    
    newline = name + "'s third favorite team is" + team3 + "\n"
    team_file.write(newline)
    
    newline = name + "'s fourth favorite team is" + team4 + "\n"
    team_file.write(newline)
    
    newline = name + "'s fifth favorite team is" + team5 + "\n"
    team_file.write(newline)

def read():
    team_file.seek(0)
    print(team_file.readline())
    print(team_file.readline())
    
def use_again():
    while True:
        again = input("Do you want to enter another? (Y/N) : ").lower()
        if again == "y":
            main()
            break
        elif again == "n":
            print ("Bye!")
            team_file.close()
            exit()
        else:
            print("Invalid Input")
            continue

if __name__ == "__main__":
    main()
