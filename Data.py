from random import choice


class Data:
    def __init__(self):
        self.names = {[
            "Andrzej", "Leszek", "Anita", "Iwona", "Aniela", "Bogusław", "Jarosław", "Janusz", "Kinga",
            "Eugeniusz", "Weronika", "Jeremiasz", "Ignacy", "Horacy", "Ewa", "Ilona", "Adrianna", "Sasza",
            "Misza", "Zofia", "Maryla", "Dorota", "Tomasz", "Jerzy"
        ]
        }
        self.fields = {
            1: "START", 2: "Ulica Konopacka", 3: "Kasa Społeczna", 4: "Ulica Stalowa",
            5: "Podatek Dochodowy", 6: "Dworzec Zachodni ", 7: "Ulica Radzymińska", 8: "Szansa",
            9: "Ulica Jagiellońska", 10: "Ulica Targowa", 11: "Więzienie", 12: "Ulica Płowiecka",
            13: "Elektrownia", 14: "Ulica Marsa", 15: "Ulica Grochowska", 16: "Dworzec Gdański",
            17: "Ulica Obozowa", 18: "Kasa Społeczna", 19: "Ulica Górczewska", 20: "Ulica Wolska",
            21: "Bezpłatny parking", 22: "Ulica Mickiewicza", 23: "Szansa", 24: "Ulica Słowackiego",
            25: "Plac Wilsona", 26: "Dworzec Wschodni", 27: "Ulica Świętokrzyska", 28: "Krakowskie Przedmieście",
            29: "Wodociągi", 30: "Nowy Świat", 31: "Idź do więzienia", 32: "Plac Trzech Krzyży",
            33: "Ulica Marszałkowska", 34: "Kasa Społeczna", 35: "Aleje Jerozolimskie", 36: "Dworzec Centralny",
            37: "Szansa", 38: "Ulica Belwederska", 39: "Domiar Podatkowy", 40: "Aleje Ujazdowskie"
        }
        self.synopsis = """Polska, Warszawa, lata 90. Trwa spór między dwoma grupami przestępczymi:
        pruszkowską i wołomińską. Obie przodują w przemycie spirytusu i papierosów,
        napadami na TIR-y, wymuszaniu haraczy, obrotem narkotykami i zabójstwami na zlecenie.
        Głowa mafii pruszkowskiej – Andrzej Kolikowski ps. “Pershing” – został zmuszony do
        podjęcia radykalnych działań po udanym zamachu na jego syna – Janusza P. i uprowadzeniu
        jego córki Anastazji przez wrogów z Wołominu pod przewodnictwego Mariana „Klepaka” Klepackiego
        i byłej żony Kolikowskiego – Miry Orłow (wpływowej bizneswoman, siostry sędziego Sądu Najwyższego),
        którzy to przez ostatnie miesiące ukrywali się, by uderzyć ze zdwojoną siłą.
        Pershing rozpoczął masową rekrutację w szeregi mafii wielu nowych popleczników (w tym graczy),
        aby zapewnić ochronę swoim własnościom oraz w celu poszerzania wpływów w całej Warszawie i
        okolicach w obliczu nagłego natarcia. Jednak jego głównym motywem jest osobista wendetta po
        zabójstwie syna. Gracze są znajomymi drugiego syna Pershinga – Jeremiasza Barańskiego
        – z czasów strajków studenckich z 1968, jak również przeciwnego gang. W trakcie ponownego
        zaognienia się konfliktu między dwoma największymi organizacjami przestępczymi nad Wisłą
        okazuje się, że urzędnicy i państwo niekoniecznie pragną zakończenia konfliktu,
        pospolity obywatel, mówiący „dzień dobry” na klatce schodowej nie jest wcale taki niewinny,
        na jakiego by się wydawał, a za całym konfliktem kryją się rodzinne tragedie i dawne zażyłości…

        Jako nowym członkom graczom zależy na udowadnianiu swoich umiejętności przedsiębiorczych i
        lojalności do “rodziny”. Zdobywanie nowych ulic, inwestowanie, przynoszenie zysków
        doceniane są przez ich szefa, który finansuje ich działania i oferuje ochronę.
        """

        # A: Pruszków wchodzi na -> Wołomin
        # B: Wołomin wchodzi na-> Pruszków
        # C: Pruszków kupuje
        # D: Wołomin kupuje
        # E: Szansa/Kasa Społeczna Pruszków 
        # F: Szansa/Kasa Społeczna Wołomin

        self.stories = {
            'A': ["""W kościele protestanckim przy [{pole}] trwa uroczyste wesele siostry Mariana Klepaka, szefa Wołominu. Zakradacie się tam
                pod przykrywką kelnerów i uprowadzacie wpływowego przedsiębiorcę obecnego na przyjęciu, gdy ten wychodzi zapalić na zewnątrz. 
                Zorganizowanie tego precedensu kosztowało niemałe grosze.""",
                """Grupa skorumpowanych funkcjonariuszy policji postanowiła zagarnąć [{pole}] należące jeszcze do niedawna przez
                gangsterów z Wołominu. Wasz księgowy, a zarazem syn Pershinga – Jeremiasz Barański, korzystając z wyświadczonej 
                przysługi wobec oficera CBŚ, przejmuje dla was lokalne nieruchomości na półlegalnie. Pershing przerabia uzyskane
                budowle w bar, pralnię i klub disco, gdzie możecie rekrutować kolejnych wykidajłów.""",
                """Starasz się razem z ekipą z [{pole}] przepędzić wrogich bandytów ze spornego terytorium. Nie udaje się to wam.
                Z kawiarni, której właścicielką jest Mira Orłow, była małżonka Pershinga, wyskakuje zastęp uzbrojonych po zęby
                mafiozów z Wołominu. Ponosicie duże straty i zarządzacie odwrót.""",
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """
            ]
            ,
            'B': ["""'Nawet idiota, który ma sprawną tylko jedną półkulę, domyśliłby się, że muszą w tym maczać palce jakieś służby.' – to zdanie wypowiedział
                doradca Klepaka, wysyłając Cię na przeszpiegi nadzwyczajnego spotkania, jak się okazało, skorumpowanych urzędników i pruszkowskich tuz 
                w podstarzałej kamienicy, o których dowiedział się wasz szpicel. Uciekając ze zlotu przez [{pole}] upuszczasz walizkę z pieniędzmi i zbyt późno 
                orientujesz się, że ją zgubiłeś.""",
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """

            ],
            'C': ["""Prawnik ze swoją teczką może nakraść więcej niż stu ludzi z rewolwerami.
                Przejmujesz [{pole}] po przekręcie finansowym dokonanym przez waszego 
                księgowego, który przekupił pracownika Urzędu Skarbowego, aby ten przymknął oko 
                na wasze poczynania. Uważaj na rozwścieczonych bandytów Wołominu, czyhających w okolicznych dzielnicach.""",
                """Poszukując Anastazji, Pershing wysyła Cię na zwiady w okolice stadionu, w okolicy kótrego po raz ostatni
                wychwycono sygnał z jej komórki. Po córce szefa ani śladu, za to znaleźliście skład kontrabandy ukryty w piwnicy
                opustoszałego bundyku nieopdal stadionu. Postanawiacie przejąć nieruchomość, opłacając skarbówkę.""",
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """

            ],
            'D': [""" """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """
            ],
            'E': ["""'Baranina' uzyskuje dla Ciebie przepustkę z więizienia w razie, gdyby złapano się w akcji, do której Cię
                przygotowuje. Nie zdradza jednak szczegółów i każe Ci czekać na odpowiedni moment.""",
                """Zostajesz wrobiony w kradzież biżuterii niskiego sortu. Trafiasz do aresztu na kilka miesięcy.""",
                """Idź na Dworzec Zachodni. """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """

            ],
            'F': [""" """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """,
                """ """

            ]
        }

    def print_story(self, last, curr, pl, team, buy):
        if (curr = "Szansa" or "Kasa Społeczna"):
            if (team = "P"):
                print(choice(self.stories['E'].format(pole=self.fields[curr])))
            else:
                print(choice(self.stories['F'].format(pole=self.fields[curr])))
        elif: (curr = "Domiar Podatkowy" or "Podatek Dochodowy"):
            if (team = "P"):
            else:    
        elif: (curr = "Bezpłatny parking"):
            if (team = "P"):
                print("Czekasz na nowe zlecenia od Pershinga.")
            else:    
                print("Czekasz na nowe zlecenia od Klepaka.")
        elif: (curr = "Więzienie"):
            print("Przejeżdżasz obok więzienia. Postaraj się nie złapać.")
        elif: (curr = "Idź do więzienia"):
            print("Zostałeś aresztowany.")
        elif: (curr = "Start"):
            if (team = "P"):
                print("Kolejny miesiąc w szeregach Pruszkowa")
            else:        
                print("Kolejny miesiąc w szeregach Wołominu")
        else:
            if (team == "P"):
                if (buy == "buy"):
                    print(choice(self.stories['C'].format(pole=self.fields[curr])))
                elif (buy == "not"):
                    print(None)
                elif (buy == "owning"):
                    print(choice(self.stories['A'].format(pole=self.fields[curr])))
                else:
                    print("Wkroczyłeś na terytorium zajęte przez wroga")
            else:
                if (buy == "buy"):
                    print(choice(self.stories['D'].format(pole=self.fields[curr])))
                elif (buy == "not"):
                    print(None)
                elif (buy == "owning"):
                    print(choice(self.stories['B'].format(pole=self.fields[curr])))
                else:
                    print("Wkroczyłeś na terytorium zajęte przez wroga")
