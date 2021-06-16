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
                mafiozów z Wołominu. Ponosicie duże straty i zarządzacie odwrót."""
            ]
            ,
            'B': ["""'Nawet idiota, który ma sprawną tylko jedną półkulę, domyśliłby się, że muszą w tym maczać palce jakieś służby.' – to zdanie wypowiedział
                doradca Klepaka, wysyłając Cię na przeszpiegi nadzwyczajnego spotkania, jak się okazało, skorumpowanych urzędników i pruszkowskich tuz 
                w podstarzałej kamienicy, o których dowiedział się wasz szpicel. Uciekając ze zlotu przez [{pole}] upuszczasz walizkę z pieniędzmi i zbyt późno 
                orientujesz się, że ją zgubiłeś.""",
                """'Ale jeśli życie czegoś mnie nauczyło to tego, że wyborów należy dokonywać samodzielnie, a nie spełniać oczekiwania innych'. 
                Po tych słowach Klepak skinieniem głowy rozkazuje Ci zlikwidować Andrzeja Leniarta, zastępcę szefa Komisji Bezpieczeństwa Narodowego, podczas
                "rozmowy" w biurze obsadzonym przez pruszkowskich gangsterów. Musisz zapłacić ogromne odszkodowanie, aby zatuszować sprawę.""",
                """'Jeśli robisz coś złego, zrób to stanowczo, a wyjdziesz na prowadzenie.'  Klepak zleca Ci zabójstwo prawnika, który od wielu lat ściga
                wołomińskie interesy. Uważaj na jego obstawę."""
            ],
            'C': ["""Prawnik ze swoją teczką może nakraść więcej niż stu ludzi z rewolwerami.
                Przejmujesz [{pole}] po przekręcie finansowym dokonanym przez waszego 
                księgowego, który przekupił pracownika Urzędu Skarbowego, aby ten przymknął oko 
                na wasze poczynania. Uważaj na rozwścieczonych bandytów Wołominu, czyhających w okolicznych dzielnicach.""",
                """Poszukując Anastazji, Pershing wysyła Cię na zwiady w okolice stadionu, w okolicy którego po raz ostatni
                wychwycono sygnał z jej komórki. Po córce szefa ani śladu, za to znaleźliście skład kontrabandy ukryty w piwnicy
                opustoszałego bundyku nieopdal stadionu. Postanawiacie przejąć nieruchomość, opłacając skarbówkę.""",
                """Inwestycje rządzą światem. Przekazujecie kilkadziesiąt tysięcy gotówki na rozkręcenie lombardu nieopodal {pole}.
                Pomaga Ci w tym zadaniu "Masa" – jeden z najbardziej zaufanych współpracowników Pershinga."""

            ],
            'D': ["""{pole} jest dość smakowitym kąskiem, na który od kilku miesięcy czaił się zarówno wasz gang, jak i wrogowie z Pruszkowa. Sytuacja przybiera
                dość ciekawy obrót, gdy zyskujecie potężną kartę przetargową w postaci dowodów defraudacji pieniężnej przez biznesmena, kierującego wiekszością 
                okolicznych mini-przedsiębiorstw. Od tej pory ściągacie z nich haracz.""",
                """{pole} jest idealnym miejscem pod wybudowanie nowej restauracji "Srogi Okoń", w podziemiach której razem z zaufanym doradcą podatkowym Miry
                uruchamiacie kasyno. Klepak zjawaia się tam razem z zarządem. Świetnie się bawicie.""",
                """Po ciężkim dniu w pracy razem ze swoimi przyjaciółmi przesiadujecie w barze, gdzie barman sprzedaje wam cynk o nielegalnej
                licytacji budynku na {pole} lansowanej przez skorumpowanych służbistów Urzędu Ochrony Państwa. Nie możesz przepuścić tej okazji. 
                Dzwonisz do Klepaka, który daje Ci aprobatę na przejęcie licytacji ze specjalnie przydzielonym zespołem interwencyjnym."""
            ],
            'E': ["""'Baranina' pozyskuje dla Ciebie przepustkę z więzienia w razie, gdyby złapano Cię w akcji, do której jesteś
                przygotowywany. Nie zdradza jednak szczegółów i każe Ci czekać na odpowiedni moment (wykorzystaj dobrze tę wiadomość).""",
                """Zostajesz wrobiony w kradzież biżuterii niskiego sortu. Trafiasz do aresztu na kilka miesięcy.""",
                """Idź na Dworzec Zachodni. Będą tam na Ciebie czekać konsultanci podatkowi przyjaźni Pershingowi, z którymi
                być może dobijesz targu.""",
                """Idź na Aleje Ujazdowskie. Szef oczekuje, że będziesz w pełni gotowści na zaplanowaną obławę policyjną.""",
                """'Jeśli robisz coś złego, zrób to stanowczo, a wyjdziesz na prowadzenie.' Tym zdaniem Klepak rozkazuje Ci 
                zlikwidować Mirosława "Maliznę" Danielaka, członka zarządu gangu pruszkowskiego, który akurat dzisiaj 
                wychodzi na warunkowym zwolnieniu z więzienia. Musisz zapłacić strażnikowi przy bramie, by usunął się z miejsca akcji na czas,
                jak mu to ująłeś, 'akcji dywersyjnej'. """,
                """Przejdź na start. Zacznij knowania ze świeżym umysłem.""",
                """Centralne Biuro Antykorupcyjne w porozumieniu z CBŚ organizuje szeroko zakrojony najazd na wasze placówki, m.in. Zakłady Naprawcze Taboru Kolejowego,
                gdzie znajdują w skrytkach kilka ton narkotyków i kontrabandy. Trafiasz do więzienia, a każdy z graczy musi zapłacić M150 (włącznie z Tobą), 
                aby zapobiec kolejnym akcjom i uciszyć niewygodnych urzędników.""",
                """Udajesz się na Ulicę Świetokrzyską, gdzie pod Gmachem Ministerstwa Finansów odbywa się rozmowa między Pershingiem, a zastępcą wiceministra
                Finansów w ważkich sprawach. Stanowisz jego ochronę.""",
                """Przesiadując spokojnie w swoim domu z rodziną przy niedzielnym obiedzie, nagle słyszysz strzały. Szkło rozlewa się lawiną na podłogę salonu, a 
                w ogrodzie słyszysz odgłosy napastników. Jako że codziennie towarzyszy Ci stres związany z pracą z gangiem, jesteś na to przygotowany.
                Postanawiasz natychmiast ewakuować się z domu do najbliższego rewiru pruszkowskiego – do browarni Zbigniewa
                'Carringtona' Mikołajewskiego. Cudem uchodzicie z życiem. Cofnij się o trzy pola.""",
                """Pershing wysyła Cię na specjalną misję do Płocka. Masz odebrać aktywa finansowe ważnej firmy. Nie powiedział Ci jakiej. Nie kwestionujesz
                jego decyzji. Bierzesz najszybszy pociąg z rana, jaki tylko możesz. Idź na najbliższy Dworzec Kolejowy.""",
                """Ku Twojemu zaskoczeniu Mira Orłow, była żona Pershinga, odwiedza Cię, gdy idziesz do kiosku kupić najnowszą gazetę. Proponuje Ci przejście na
                jej stronę, wygarniając, jak możesz współpracować "z takim potworem, jakim jest Andrzej Kolikowski". Odmawiasz jej, przez co 
                zza rogu zaczynają gonić Cię jej obstawa. Cofasz się o pięć pól.""",
                """Nadszedł dzień Twoich urodzin. Mimo ciężkiej natury pracy, której się podejmujesz, Pershing postanawia wynagrodzić Cię za lojalność. Koledzy
                z Pruszkowa wyprawiają Ci huczne przyjęcie urodzinowe na jachcie na Wiśle. Otrzymujesz pokaźne podarki. Pobierz M250.""",
                """Podczas wymiany zakładników w Ożarowie Mazowieckim nieopodal willi Pershinga dochodzi do strzelaniny, w wyniku której zostajesz postrzelony
                w nogę. Trafiasz do szpitala. Aby uniknąć alarmowania policji o zajściu, płacisz dodatkowo lekarzowi M150.""",
                """Jeremiasz "Baranina" Barański prosi Cię o przysługę. Dziwisz się, gdyż jest ekspertem od załatwiania wszelkich spraw. Niemniej jednak
                Centrum Bankowo-Finansowego, aby dostarczyć dokumenty, o co prosił cię "Baranina". Idź na Aleje Jerozolimskie. Jeżeli przejdziesz przez START,
                pobierz M250.""",
                """Pershing na zgromadzeniu zarządu postanawia odrestaurować część posiadanych nieruchomości. Każdy z was płaci M25 do wspólnego majątku 
                rewaloryzacyjnego.""",
                """Dzisiaj są imieniny drugiej córki szefa. Pershing każe Ci pójść z nią do kina "Wisła". Idź na plac Wilsona. Płacisz M5.""",
                """W niewyjaśnionych okolicznych ginie Twój bezdzietny wuj, emerytowany członek mafii wołomińskiej, który jednak postanowił Tobie, najstarszemu
                bratankowi przekazać w spadku swój majątek. Pobierz M400.""",
                """Będąc w wirze nieustannych walk między najpotężniejszymi gangami w Warszawie, zaskakuje Cię wieść o niespłaconych rachunkach za prąd i wodę.
                Odłożenie rachunków sprawia, że musisz dopłacić dodatkowe M45.""",
                """W warszawskiej restauracji 'Gamma' dochodzi do masakry, w której ginie czterech pruszkowskich gangsterów z rąk zamaskowanych napastników.
                O mało nie giniesz w trakcie. Tracisz jedno z pól i M25.""",
                """W kasynie Miry Orłow wraz z jednym z współpracowników pod przykrywką obcokrajowców oszukujecie podczas gry w jednorękiego bandytę. Zyskujesz M50."""

            ],
            'F': ["""Obrabowałeś bank na przedmieściach. Zyskujesz dla swojego gangu M200.""",
                """Jeden z sędziów przychylny do tej pory Mirze Orłow odwrócił się do was plecami. Na szczęście posiadał dowody
                tylko na nieliczne przestępstwa, więc niewielka grzywna zdała egzamin. Płacisz M150.""",
                """Założone przez Ciebie konto w szwajcarskim banku okazało się być strzałem w dziesiątkę. Doszło do awarii systemów
                płatniczych, dzięki którym zyskujesz M200.""",
                """Doszło do wybuchu w willi byłego emerytowanego szefa waszego gangu "Dziada". Jako że Klepak silnie przywiązany jest 
                do tradycji mafijnych waszego ugrupowania, musisz zapłacić 115M jako zapomogę dla dawnego szefa.""",
                """Mira, jako miłośniczka odradzającej się zachodniej kultury, organizuje przepastny 
                wybieg mody w warszawskim "Domu Towarowym Braci Jabłkowskich". Kierownik centrum handlowego zatrudnia Cię jako bramkarza
                na wydarzeniu. Zyskujesz 40M. """,
                """Przejdź na start. Wspieraj gang na co raz to nowsze sposoby.""",
                """Klepak w porozumieniu z Mirą organizują zlot kilku mniejszych ugrupowań mafijnych z okolic Warszawy, aby dokonać ewentualnej fuzji. Wydarzenie
                jest huczne, poprzedzone balem, kolacją i występem kilku raperów. Udajesz się na Ulicę Marszałkowską.""",
                """Zaufany kontakt Mariana Klepackiego Andrzej ps. 'Kikir', z którym wcześniej Wołomin dokonywał wielu utargów, ma zamiar przylecieć samolotem 
                z Gdańska do Warszawy z gotówką i kilkoma gangsterami, co ma pomóc w zaognionej walce z Pruszkowem. Idź na najbliższe lotnisko. Zapłać M10.""",
                """Niespodziewanie dochodzi do ataku gangsterów z ugrupowania ząbkowsko-praskiego, który to mały odłam mafii warszawskiej wykorzystuje zaistniałą
                sytuację. Tracisz jedno pole.""",
                """Marian Klepak organizuje imprezę w podwarszawskim klubie "Acapulco". Jest to jedna z większych imprez tuż po upadku komunistycznego rządu. 
                Alkohol leje się strumieniami, podobnie jak pieniądze. Każdy gracz zyskuje M150.""",
                """Mira Orłow, kontynuując swoją osobistą wendetę (której genezą z nikim nie chce się podzielić) na byłym mężu Andrzeju 'Pershingu' Kolikowskim, 
                organizuje najazd na Państwowe Zakłady Tele- i Radiotechniczne, w którym uczestniczysz. Wie, że dokładnie tam jej były mąż ukrył pokaźne ilości gotówki
                jeszcze z czasów sprzed upadku komunizmu. Doskonale orientuje się w sytuacji, że urząd ten jest ściśle chroniony przez oddział policyjny, 
                który nie przepuści nikogo z gangu pruszkowskiego przez próg, za to ją, mającą silne wpływy w Sądzie Najwyższym, owszem. Udaj się na ulicę Grochowską.""",
                """Andrzej 'Kikir' przesyła pozdrowienia Klepakowi wraz z solidnymi porcjami kontrabandy i gotówki w zaplombownych skrzynkach. Zyskujesz M50
                jako premię za dobre sprawowanie. """,
                """Szpicel Miry Orłow z Agencji Bezpieczeństwa Wewnętrznego dowiaduje się, że dojdzie do próby zlikwidowania "Baniaka" – wielokrotnie utrudniającego śledztwa
                przeciwko Wołominowi sekretarza Centralnego Biura Śledczego, kuzyna Miry. Rozkazuje Ci i kilku gangsterom sprawować nad nim ścisłą ochronę w najbliższych
                dniach. Udajesz się na Nowy Świat.""",
                """W ramach zakrojonej na wielką skalę akcji Krajowej Administracji Skarbowej, mającej na celu wychwycenie aktów korupcji i defraudacji, Klepak rozkazuje
                Ci pomóc w usuwaniu wszelkich śladów niedogodności finansowych w jednej z siedzib gangu. Cofasz się o cztery pola.""",
                """Na granicy ulicy Ząbkowskiej i Kalinowskije zauważasz, że śledzi Cię od dłuższego czasu tajemniczy czarny pojazd z zadymionymi szybami. Nadrabiasz
                więc drogi jadąc do willi Klepaka. Cofnij się o trzy pola.""",
                """Na spotkaniu zarządu w hotelu jednego z kuzynów Klepaka okazuje się, że kuzyn ten jest podwójnym agentem. CBA wkracza do akcji, aresztując razem z policją
                wielu gangsterów wołomińskich i przechwycając gotówkę z nielegalnego obrotu. Tracisz M50.""",
                """Anastazja Kolikowska, córka Pershinga, ucieka z niewoli po otrzymaniu pomocy ze strony jednego z gangsterów, któy jak się okazało, był podwójnym agentem. 
                Mira rokazuje Ci znaleźć Anastazję za wszelką cenę i podpowiada, gdzie mogła uciec. Udaj się na Elektrownię. Jeśli przechodzisz przez START, nie pobieraj
                dodatkowych pieniędzy""",
                """Bez uzgodnienia z zarządem wołomińskim gangster Jeremiasz ps. "Tyburek" Tyburski atakuje i zabija policjanta, który aresztował jego brata. Wszyscy płacicie
                M25 do wspólnego majątku gangu, żeby zamieść sprawę pod dywan.""",
                """Ginie syn Mariana Klepaka w starciu z policją w jednym z podwarszawskich klubów. Jedziesz na jego pogrzeb. Udaj się na Aleje Ujazdowskie. """,
                """Do Twojego domu wita człowiek podający się za agenta nieruchomości. Nie spodziewałeś\aś się nikogo takiego, więc po krótkiej rozmowie okazuje się, że było
                to zwykłe nieporozumienie. 2 godziny po jego wyjściu orientujesz się, że z Twojej szuflady giną oszczędności. Tracisz M50."""

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
                    print(None)
                else:
                    print(choice(self.stories['A'].format(pole=self.fields[curr])))
            else:
                if (buy == "buy"):
                    print(choice(self.stories['D'].format(pole=self.fields[curr])))
                elif (buy == "not"):
                    print(None)
                elif (buy == "owning"):
                    print(None)
                else:
                    print(choice(self.stories['B'].format(pole=self.fields[curr])))
