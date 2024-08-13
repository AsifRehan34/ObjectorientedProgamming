# create a class named player
class Player:
# create constructor
    def __init__(self,name,score):
        self.name=name
        self.score=score
        self.team=None
    def show_stats(self):
        print(self.name)
        print(self.score)
        print(self.team)
    def select_team(self):
        team=input("Enter a team name: ")
        self.team=team
player1=Player("asif","30")
player1.show_stats()
player1.select_team()
player1.show_stats()