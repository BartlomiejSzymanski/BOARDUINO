class Data:
    def __init__(self):
        self.names = ["Mario", "Luigi", "Vito"]
        self.stories = ["Last square: {last}, current square: {current}, player: {player}"]

    def print_story(self, last, curr, pl):
        print(self.stories[0].format(last=last, current=curr, player=pl))
