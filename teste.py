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
            answer = input("Enter the name of the Pokemon: ");
            print(answer)

        if option == 'T':
            self.teamMenu()


    #the team menu where the user can add pokemons to and see their theam
    def teamMenu(self):
        answerTeam = input("Do you want to (A)dd a Pokemon to your team or (S)ee your team? A or S")

        if answerTeam == 'A':
            print("Type the name of the Pokemon you want to add to your team: ")
            pokemon = input("Enter the name of the Pokemon: ")
            
            if self.search(pokemon) == True:
                self.team.append(pokemon)
                print("Pokemon added to your team!")

        elif answerTeam == 'S':
            print("Your team: ")
            print(self.team)

    #searching if pokemon is in the CSV file or not
    def search(self, answer):
        result = df.loc[df['Name'] == answer]

        if result.empty:
            return False
        else:
            return True

Program()