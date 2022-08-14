import constants, copy, random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

experienced = []
inexperienced = []

panthers = []
bandits = []
warriors = []

updated_teams = [panthers, bandits, warriors]


def clean_data():
    for player in players:
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'].lower() == 'yes':
            player['experience'] = True
            experienced.append(player)
        else:
            player['experience'] = False
            inexperienced.append(player)
        player['height'] = int(player['height'][:2])
    return players


def balance_teams(team):
    while len(experienced) != 0 and len(team) < 3:
        team.append(experienced.pop(random.randrange(len(experienced))))
        
    while len(inexperienced) != 0 and len(team) < 6:
        team.append(inexperienced.pop(random.randrange(len(inexperienced))))
        
        
def extract_names(team):
    player_names = []
    for player in team:
        player_names.append(player['name'])
    return (', ').join(player_names)


def avg_height(team):
    player_height = []
    for player in team:
        player_height.append(player['height'])
    player_height.sort()
    return round(sum(player_height) / len(player_height), 2)


def guardians(team):
    player_guardians = []
    for player in team:
        player_guardians.append((', ').join(player['guardians']))
    return (', ').join(player_guardians)


def main_function():
    clean_data()
    balance_teams(panthers)
    balance_teams(bandits)
    balance_teams(warriors)
    
    
if __name__ == "__main__":
    main_function()
    app_running = True

while app_running:
    print("\n**** MENU ****\n\nPlease choose from the following:\n1) Display Team Stats\n2) Quit\n\n")
    option = input("Please choose an option: ")
    if option == "1":
        print("\nPick from the following teams:\n--------------------\n\n1) Panthers\n2) Bandits\n3) Warriors\n\n")
        team_number = input("Please choose an option (1, 2 or 3): ")
        try:

            def doc_string():
                return (f"""
            
Team {teams[int(team_number) - 1]} Stats
--------------------

Total Players: {len(panthers)}
Experienced Players: {3}
Inexperienced Players: {3}
Player Names: {extract_names(updated_teams[int(team_number) - 1])}
Average Player Height: {avg_height(updated_teams[int(team_number) - 1])} inches
Player Guardians: {guardians(updated_teams[int(team_number) - 1])}
                
                """)
            
            print(doc_string())
            input("Press Enter to continue...")
        except (ValueError, IndexError) as err:
            print(f"{err}. Please choose again.")
            input("Press Enter to continue... ")
    elif option == "2":
        app_running = False
    else:
        print(f"\"{option}\" is not a valid entry, please choose an available option. ")
        input("Press Enter to continue... ")