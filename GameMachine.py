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
        self.fields = {
            1: ["START", ""], 2: ["Ulica Konopacka", ""], 3: ["Kasa Społeczna", ""], 4: ["Ulica Stalowa", ""],
            5: ["Podatek Dochodowy", ""], 6: ["Dworzec Zachodni ", ""], 7: ["Ulica Radzymińska", ""], 8: ["Szansa", ""],
            9: ["Ulica Jagiellońska", ""], 10: ["Ulica Targowa", ""], 11: ["Więzienie", ""], 12: ["Ulica Płowiecka", ""],
            13: ["Elektrownia", ""], 14: ["Ulica Marsa", ""], 15: ["Ulica Grochowska", ""], 16: ["Dworzec Gdański", ""],
            17: ["Ulica Obozowa", ""], 18: ["Kasa Społeczna", ""], 19: ["Ulica Górczewska", ""], 20: ["Ulica Wolska", ""],
            21: ["Bezpłatny parking", ""], 22: ["Ulica Mickiewicza", ""], 23: ["Szansa", ""], 24: ["Ulica Słowackiego", ""],
            25: ["Plac Wilsona", ""], 26: ["Dworzec Wschodni", ""], 27: ["Ulica Świętokrzyska", ""], 28: ["Krakowskie Przedmieście", ""],
            29: ["Wodociągi", ""], 30: ["Nowy Świat", ""], 31: ["Idź do więzienia", ""], 32: ["Plac Trzech Krzyży", ""],
            33: ["Ulica Marszałkowska", ""], 34: ["Kasa Społeczna", ""], 35: ["Aleje Jerozolimskie", ""], 36: ["Dworzec Centralny", ""],
            37: ["Szansa", ""], 38: ["Ulica Belwederska", ""], 39: ["Domiar Podatkowy", ""], 40: ["Aleje Ujazdowskie", ""]
        }

    # ------ game setup section - adding, deleting and editing players at the beginning of game ------

    def setup_game(self):
        """Called at the beginning of game.
        Sets up players and allows for editing players"""

        while True:
            self.output.print_screen(f"Pick name for player {self.get_player_num() + 1}: 1 - Mario, 2 - Luigi, 3 - Vito; # to stop")
            key = self.input.get_numpad()
            # self.output.print_screen(key)
            if key == "#":
                if self.get_player_num() > 6:
                    self.delete_players()
                if self.get_player_num() > 1:
                    break
                else:
                    self.output.print_screen("Add more players")
            elif key.isdigit() and int(key) in range(1, len(self.data.names) + 1):
                self.add_player(self.data.names[int(key) - 1][0], self.data.names[int(key) - 1][1])
                self.output.print_screen(f"Added {self.data.names[int(key) - 1]}")
            else:
                self.output.print_screen("wrong input - try again")
        while True:
            gm.show_players("Players")
            if self.get_player_num() < 3:
                self.output.print_screen("Do you want to (1) edit player's name, (#) proceed to game?")
            else:
                self.output.print_screen("Do you want to (1) edit player's name, (2) delete player, (#) proceed to game?")
            key = self.input.get_numpad()
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
            ind = self.input.get_numpad()
            if ind.isdigit() and int(ind) in range(1, self.get_player_num() + 1):
                self.output.print_screen("choose new player name")
                self.output.print_screen(self.data.names)
                key = self.input.get_numpad()
                if key.isdigit():
                    self.update_player(int(ind) - 1, self.data.names[int(key) - 1][0], self.data.names[int(key) - 1][1])
            elif ind == '#':
                break

    def delete_players(self):
        while True:
            self.show_players("Choose player to delete (# to stop)")
            key = self.input.get_numpad()
            if key.isdigit() and int(key) in range(1, self.get_player_num() + 1):
                self.__players.pop(int(key) - 1)
                if self.get_player_num() < 3:
                    break
            elif key == '#' and self.get_player_num() > 6:
                self.output.print_screen("To many players. You have to delete more.")
            elif key == '#':
                break
            else:
                self.output.print_screen("wrong input - try again")

    def show_players(self, title):
        """Displays list of players with given title"""

        i = 1
        self.output.print_screen(f"--- {title} ---")
        for pl in self.__players:
            self.output.print_screen(f'{i}: {pl}')
            i += 1

    def add_player(self, name, team):
        self.__players.append(Player(name, team))

    def update_player(self, index, name, team):
        self.__players[index].name = name
        self.__players[index].team = team

    def get_player_num(self):
        return len(self.__players)

    # ------ gameplay sections - turn, move ------

    def start_game(self):
        self.__current_player = self.__players[self.__current_player_index]
        self.turn()

    def turn(self):
        while True:
            self.output.print_screen(f'{self.__current_player} your turn')
            self.output.print_screen(f'1 - move. 2 - bankrupt, 3 - undo move, # - end turn')
            key = self.input.get_numpad()
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
                self.output.print_screen("invalid input - try again")

    def move(self):
        while True:
            self.output.print_screen("Waiting for field")
            field = self.input.get_field()
            if field in range(1, 41):
                self.__current_player.add_turn(int(field))
                if self.fields[int(field)][1] == "":
                    while True:
                        self.output.print_screen("Buying? (1 - y, 2 - n)")
                        dec = self.input.get_numpad()
                        if dec == "1":
                            self.fields[int(field)][1] = self.__current_player.team
                            occupied = "buy"
                            break
                        elif dec == "2":
                            occupied = "not"
                            break
                        else:
                            self.output.print_screen("wrong input. try again")
                elif self.fields[int(field)][1] == self.__current_player.team:
                    occupied = "owning"
                else:
                    occupied = "enemy"
                self.show_message(occupied)
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

    def show_message(self, buy):
        self.data.print_story(self.__current_player.last_field(),
                              self.__current_player.current_field(),
                              self.__current_player.name,
                              self.__current_player.team,
                              buy)

    def get_player_info(self):
        return (self.__current_player.last_field(),
                self.__current_player.current_field(),
                self.__current_player.name,
                self.__current_player.team)


gm = GameMachine()
# gm.add_player("Mario")
# gm.add_player("Luigi")
# gm.add_player("Vito")
gm.setup_game()
# gm.start_game()
