class Data:
    def __init__(self):
        self.names = [["Mario", "1"], ["Luigi", "1"], ["Vito", "2"]]
        self.stories = ["Last square: {last}, current square: {current}, player: {player}"]

    def print_story(self, last, curr, pl, team):
        print(self.stories[0].format(last=last, current=curr, player=pl))
