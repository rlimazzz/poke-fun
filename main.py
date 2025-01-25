import pandas as pd

df = pd.read_csv('pokemon.csv')

class Program:
    def __init__(self):
        print("Welcome to pokeFun!!!");
        self.team = []

        while True:
            self.menu()

    #the main menu where the user can choose to search for a pokemon or form a team 
    def menu(self):
        print("Do you want to (S)earch for a Pokemon or do you want to form a (T)eam? S or T")
        option = input("Enter your option: ")

        while option != 'S' and option != 'T':
            print("Invalid option")
            option = input("Enter your option: ")

        if option == 'S':
            while True:
                answer = input("Enter the name of the Pokemon: Q for quit");
                
                if self.search(answer) == True:
                    print(df.loc[df['Name'] == answer])

                elif answer == 'Q':
                    break

        if option == 'T':
            self.teamMenu()


    #the team menu where the user can add pokemons to and see their theam
    def teamMenu(self):
        while True:
            answerTeam = input("Do you want to (A)dd a Pokemon to your team or (S)ee your team? A or S or (Q for quit)|")

            if answerTeam == 'A':
                while True:
                    print("Type the name of the Pokemon you want to add to your team:")
                    pokemon = input("Enter the name of the Pokemon: (Q for Quit)")
                    
                    if self.search(pokemon) == True and len(self.team) < 6:
                        self.team.append(pokemon)
                        print("Pokemon added to your team!")
                    elif pokemon == 'Q':
                        break
                    elif len(team) == 6:
                        print("You have reached the maximum number of pokemons in your team")
                        print("Do you wanna exclude a pokemon from your team? Y or N")
                        answer = input("Enter your option: ")

                        if answer == 'Y':
                            print("Type the name of the Pokemon you want to exclude from your team:")
                            pokemonExcluded = input("Enter the name of the Pokemon: (Q for Quit)")

                            if pokemonExcluded in self.team:
                                self.team.remove(pokemonExcluded)
                                print("Pokemon excluded from your team!")
                            else:
                                print("Pokemon not in your team")

                        elif answer == 'N':
                            break

            elif answerTeam == 'S':
                print("Your team: ")
                print(self.team)

            elif answerTeam == 'Q':
                break

    #searching if pokemon is in the CSV file or not
    def search(self, answer):
        result = df.loc[df['Name'] == answer]

        if result.empty:
            return False
        else:
            return True

Program()