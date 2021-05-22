from Player import Player
from GameInput import GameInput
from GameOutput import GameOutput
from Data import Data


class GameMachine:
    def __init__(self):
        self.__players = []
        self.__current_player_index = 0
        self.__current_player = None
        self.__bankrupts = []
        self.input = GameInput()
        self.output = GameOutput()
        self.data = Data()

    # ------ game setup section - adding, deleting and editing players at the beginning of game ------

    def setup_game(self):
        """Called at the beginning of game.
        Sets up players and allows for editing players"""

        while True:
            print(f"Pick name for player {self.get_player_num() + 1}: 1 - Mario, 2 - Luigi, 3 - Vito; # to stop")
            key = self.input.numpad()
            # print(key)
            if key == "#":
                if self.get_player_num() > 6:
                    self.delete_players()
                if self.get_player_num() > 1:
                    break
                else:
                    print("Add more players")
            elif key.isdigit() and int(key) in range(1, len(self.data.names) + 1):
                self.add_player(self.data.names[int(key) - 1])
                print(f"Added {self.data.names[int(key) - 1]}")
            else:
                print("wrong input - try again")
        while True:
            gm.show_players("Players")
            if self.get_player_num() < 3:
                print("Do you want to (1) edit player's name, (#) proceed to game?")
            else:
                print("Do you want to (1) edit player's name, (2) delete player, (#) proceed to game?")
            key = self.input.numpad()
            if key.isdigit() and int(key) == 1:
                self.edit_players()
            elif key.isdigit() and int(key) == 2 and self.get_player_num() > 2:
                self.delete_players()
            elif key == '#':
                break
        self.start_game()

    def edit_players(self):
        """Method responsible for editing players name.

        Allows user to choose player and his name until
        user types #"""

        while True:
            self.show_players("Choose player to edit (# to stop)")
            ind = self.input.numpad()
            if ind.isdigit() and int(ind) in range(1, self.get_player_num() + 1):
                print("choose new player name")
                print(self.data.names)
                key = self.input.numpad()
                if key.isdigit():
                    self.update_player(int(ind) - 1, self.data.names[int(key) - 1])
            elif ind == '#':
                break

    def delete_players(self):
        while True:
            self.show_players("Choose player to delete (# to stop)")
            key = self.input.numpad()
            if key.isdigit() and int(key) in range(1, self.get_player_num() + 1):
                self.__players.pop(int(key) - 1)
                if self.get_player_num() < 3:
                    break
            elif key == '#' and self.get_player_num() > 6:
                print("To many players. You have to delete more.")
            elif key == '#':
                break
            else:
                print("wrong input - try again")

    def show_players(self, title):
        """Displays list of players with given title"""

        i = 1
        print(f"--- {title} ---")
        for pl in self.__players:
            print(f'{i}: {pl}')
            i += 1

    def add_player(self, name):
        self.__players.append(Player(name))

    def update_player(self, index, name):
        self.__players[index].set_name(name)

    def get_player_num(self):
        return len(self.__players)

    # ------ gameplay sections - turn, move ------

    def start_game(self):
        self.__current_player = self.__players[self.__current_player_index]
        self.turn()

    def turn(self):
        while True:
            print(f'{self.__current_player} your turn')
            print(f'1 - move. 2 - bankrupt, 3 - undo move, # - end turn')
            key = self.input.numpad()
            if key == '#':
                self.end_turn()
            elif key.isdigit() and key == "1":
                self.move()
            elif key.isdigit() and key == "2":
                self.bankrupt()
                self.end_turn()
            elif key.isdigit() and key == "3":
                self.undo()
            else:
                print("invalid input - try again")

    def move(self):
        while True:
            print("Waiting for field")
            field = self.input.field()
            if field in range(1, 41):
                self.__current_player.add_turn(int(field))
                self.show_message()
                break

    def end_turn(self):
        self.__current_player_index += 1
        self.__current_player_index = self.__current_player_index % self.get_player_num()
        self.__current_player = self.__players[self.__current_player_index]
        self.turn()

    def bankrupt(self):
        pass

    def undo(self):
        pass

    def show_message(self):
        self.data.print_story(self.__current_player.last_field(),
                              self.__current_player.current_field(),
                              self.__current_player.get_name())


gm = GameMachine()
gm.add_player("Mario")
gm.add_player("Luigi")
gm.add_player("Vito")
# gm.setup_game()
gm.start_game()
