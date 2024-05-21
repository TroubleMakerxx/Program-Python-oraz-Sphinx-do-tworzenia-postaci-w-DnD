import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton
from durable.lang import *

class CharacterCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.rule_set_created = False
        
        self.race_descriptions = self.load_descriptions('race_descriptions.txt')
        self.class_descriptions = self.load_descriptions('class_descriptions.txt')
        
        self.race_combo.currentIndexChanged.connect(self.update_race_description)
        self.class_combo.currentIndexChanged.connect(self.update_class_description)
        

    def load_descriptions(self, file_path):
        descriptions = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read().split('\n\n')
                for section in data:
                    section_parts = section.split(':', 1)
                    if len(section_parts) == 2:
                        descriptions[section_parts[0].strip()] = section_parts[1].strip()
            return descriptions
        except FileNotFoundError:
            return {}

    def update_race_description(self):
        selected_race = self.race_combo.currentText()
        race_description = self.race_descriptions.get(selected_race, "Description not found for this race.")
        self.race_description_label.setText(race_description)
        self.race_description_label.show()

    def update_class_description(self):
        selected_class = self.class_combo.currentText()
        class_description = self.class_descriptions.get(selected_class, "Description not found for this class.")
        self.class_description_label.setText(class_description)
        self.class_description_label.show()

    def init_ui(self):
        layout = QVBoxLayout()

        self.race_label = QLabel("Choose Race:")
        self.race_combo = QComboBox()
        self.race_combo.addItem("Select Race")
        self.race_combo.addItems(["Dragonborn", "Dwarf", "Elf", "Human", "Tiefling"])

        self.class_label = QLabel("Choose Class:")
        self.class_combo = QComboBox()
        self.class_combo.addItem("Select Class")
        self.class_combo.addItems([
            "Furia_i_Wscieklosc", "Mistrz_Miecza", "Sztuki_walki_i_duchowa_energia",
            "Straznik_Swiatla", "Infiltracja_i_Obrazenia_krytyczne", "Wsparcie_i_Leczenie",
            "Inzynieria_magiczna", "Wiedza_i_Arkana_Magi", "Narodzony_z_Magia",
            "Muzyka_i_Magia", "Zrecznosc_i_Bron_dystansowa", "Magia_paktow_i_Cienie",
            "Przywiazanie_do_natury"
        ])

        
        self.race_combo.setCurrentText("Select Race")
        self.class_combo.setCurrentText("Select Class")
        
        self.display_button = QPushButton("Create Character")
        self.display_button.clicked.connect(self.show_character)

        self.character_info_label = QLabel("Character Information:")
        self.character_info = QLabel("")
        self.race_description_label = QLabel("")
        self.class_description_label = QLabel("")
        
        self.reload_button = QPushButton("Zakończ")
        self.reload_button.clicked.connect(self.restart)
        self.reload_button.hide()
        self.character_info_label.hide()
        self.race_description_label.hide()
        self.class_description_label.hide()

        layout.addWidget(self.race_label)
        layout.addWidget(self.race_combo)
        layout.addWidget(self.race_description_label)
        layout.addWidget(self.class_label)
        layout.addWidget(self.class_combo)
        layout.addWidget(self.class_description_label)
        layout.addWidget(self.display_button)
        layout.addWidget(self.character_info_label)
        layout.addWidget(self.character_info)
        layout.addWidget(self.reload_button)

        self.setLayout(layout)
        self.setWindowTitle("Character Creator")
    
        
    def show_character(self):
        race = self.race_combo.currentText()
        char_class = self.class_combo.currentText()
        
        if race == "Select Race" and char_class == "Select Class":
            self.character_info.setText("Please select a race and class.")
            self.character_info_label.show()
        elif race == "Select Race":
            self.character_info.setText("Please select a race.")
            self.character_info_label.show()
        elif char_class == "Select Class":
            self.character_info.setText("Please select a class.")
            self.character_info_label.show()
        else:
            characters = {}
            
            if self.rule_set_created:
                delete_ruleset('tworzenie_postaci')

            with ruleset('tworzenie_postaci'):
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Furia_i_Wscieklosc'))
                def Dragonborn_Barbarian(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Barbarian',
                        'opis': '''Stworzona Postać! 
                                  Imie: Roland Barns
                                  Rasa: Dragonborn
                                  Klasa: Barbarian
                                  Historia: Smoczy wojownik który opuścił swoje rodzinne miasto Nemfis w poszukiwaniu przygód.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                            
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Mistrz_Miecza'))
                def Dragonborn_Fighter(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Fighter',
                        'opis': '''Stworzona Postać!
                                  Imię: Dragan Żelazna Dłoń
                                  Rasa: Dragonborn
                                  Klasa: Fighter
                                  Historia: Wytrawny wojownik, opuścił swoją rodzinę i ojczyznę, by zdobyć sławę i szacunek w brutalnym świecie walki.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Sztuki_walki_i_duchowa_energia'))
                def Dragonborn_Monk(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Monk',
                        'opis': '''Stworzona Postać!
                                    Imię: Lirael Miedziany Pazur
                                    Rasa: Dragonborn
                                    Klasa: Monk
                                    Historia: Mnich-szermierz, który opuścił zakon, aby doskonalić umiejętności walki i ducha.
                                '''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Straznik_Swiatla'))
                def Dragonborn_Paladin(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Paladin',
                        'opis': '''Stworzona Postać!
                                Imię: Zephyr Błękitnouchy
                                Rasa: Dragonborn
                                Klasa: Paladin
                                Historia: Zwiastun sprawiedliwości i ochrony, opuścił rodzinne miasto, aby bronić słabszych i zwalczać zło.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Infiltracja_i_Obrazenia_krytyczne'))
                def Dragonborn_Rouge(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Cleric',
                        'opis': '''Stworzona Postać!
                                Imię: Tordek Kamienne Serce
                                Rasa: Dwarf
                                Klasa: Rogue
                                Historia: Tordek jest zręcznym złodziejem i przemytnikiem, który opuścił góry, aby prowadzić życie w podziemnym świecie intryg i skradania.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Wsparcie_i_Leczenie'))
                def Dragonborn_Cleric(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Cleric',
                        'opis': '''Stworzona Postać! 
                                  Imie: Elara Stormwing
                                  Rasa: Dragonborn
                                  Klasa: Cleric
                                  Historia: Kapłanka oddana służbie swojego bóstwa, gotowa do leczenia i wsparcia sojuszników.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Inzynieria_magiczna'))
                def Dragonborn_Artificer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Artificer',
                        'opis': '''Stworzona Postać! 
                                  Imie: Vendra Scaleforge
                                  Rasa: Dragonborn
                                  Klasa: Artificer
                                  Historia: Inżynier magiczny, mistrz tworzenia magicznych przedmiotów i urządzeń.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Wiedza_i_Arkana_Magi'))
                def Dragonborn_Wizard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Sorcerer',
                        'opis': '''Stworzona Postać!
                                Imię: Ignar Cieniodyszny
                                Rasa: Dragonborn
                                Klasa: Wizard
                                Historia: Uczeń magii, opuścił spokojne smocze miasto, aby zgłębiać tajniki zaklęć i starożytnych artefaktów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Narodzony_z_Magia'))
                def Dragonborn_Sorcerer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Sorcerer',
                        'opis': '''Stworzona Postać! 
                                  Imie: Xander Flamebreath
                                  Rasa: Dragonborn
                                  Klasa: Sorcerer
                                  Historia: Posiadający wrodzoną moc magiczną, kontroluje i manipuluje magią w najmroczniejszych zakamarkach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Muzyka_i_Magia'))
                def Dragonborn_Bard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Bard',
                        'opis': '''Stworzona Postać! 
                                  Imie: Lyra Flameheart
                                  Rasa: Dragonborn
                                  Klasa: Bard
                                  Historia: Muzyk i opowieścista, używa magii w swojej sztuce, oczarowuje publiczność i wrogów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Zrecznosc_i_Bron_dystansowa'))
                def Dragonborn_Ranger(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Bard',
                        'opis': '''Stworzona Postać!
                                Imię: Draegon Steal
                                Rasa: Dragonborn
                                Klasa: Ranger
                                Historia: Zdobywca, który odszedł z górskiej enklawy, aby stać się mistrzem w strzelaniu z łuku i łączeniu się z przyrodą.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Magia_paktow_i_Cienie'))
                def Dragonborn_Warlock(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Bard',
                        'opis': '''Stworzona Postać!
                                Imię: Xalith Warn
                                Rasa: Dragonborn
                                Klasa: Warlock
                                Historia: Podpisał tajemniczą umowę z potężnym smoczym patronem, uzyskując moc nieznaną w rodzinnej wiosce aby móc wyruszyć w przygodę.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Przywiazanie_do_natury'))
                def Dragonborn_Druid(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dragonborn Bard',
                        'opis': '''Stworzona Postać!
                                Imię: Draga Drewniane Serce
                                Rasa: Dragonborn
                                Klasa: Druid
                                Historia: Z wyboru natury, opuściła góry, aby odkryć tajemnice przyrody i poznać tajemnicze siły lasów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Furia_i_Wscieklosc'))
                def Dwarf_Barbarian(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Barbarian',
                        'opis': '''Stworzona Postać!
                                      Imię: Thronir Kamienny Ostróg
                                      Rasa: Dwarf
                                      Klasa: Barbarian
                                      Historia: Krasnoludzki wojownik, który opuścił swe góry w poszukiwaniu wielkich wyzwań i bitew.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Mistrz_Miecza'))
                def Dwarf_Fighter(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Fighter',
                        'opis': '''Stworzona Postać!
                                  Imię: Dolgrin Żelazna Pięść
                                  Rasa: Dwarf
                                  Klasa: Fighter
                                  Historia: Wytrawny krasnoludzki wojownik, porzucił swój klan, by zyskać sławę i szacunek w krwawym świecie walk.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Sztuki_walki_i_duchowa_energia'))
                def Dwarf_Monk(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Monk',
                        'opis': '''Stworzona Postać!
                                  Imię: Keldar Brązowy Brat
                                  Rasa: Dwarf
                                  Klasa: Monk
                                  Historia: Mnich z krasnoludzkiego klasztoru, który opuścił zakon, by doskonalić umiejętności walki i ducha.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                
                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Straznik_Swiatla'))
                def Dwarf_Paladin(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Paladin',
                        'opis': '''Stworzona Postać!
                                  Imię: Thelga Błyszczący Tarcza
                                  Rasa: Dwarf
                                  Klasa: Paladin
                                  Historia: Zwiastun sprawiedliwości i ochrony, opuścił rodzinne krasnoludzkie kopalnie, aby bronić słabszych i zwalczać zło.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Infiltracja_i_Obrazenia_krytyczne'))
                def Dwarf_Rogue(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Rogue',
                        'opis': '''Stworzona Postać!
                                  Imię: Horgar Skradający się Cień
                                  Rasa: Dwarf
                                  Klasa: Rogue
                                  Historia: Krasnoludzki zręczny złodziej i przemytnik, opuścił góry, by prowadzić życie w podziemnym świecie intryg i skradania.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Wsparcie_i_Leczenie'))
                def Dwarf_Cleric(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Cleric',
                        'opis': '''Stworzona Postać!
                                  Imię: Bardin Kamienne Serce
                                  Rasa: Dwarf
                                  Klasa: Cleric
                                  Historia: Kapłan oddany służbie swej wiary, gotowy do leczenia i wsparcia sojuszników.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Inzynieria_magiczna'))
                def Dwarf_Artificer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Artificer',
                        'opis': '''Stworzona Postać!
                                  Imię: Oskar Kamienne Ręce
                                  Rasa: Dwarf
                                  Klasa: Artificer
                                  Historia: Inżynier magiczny, mistrz tworzenia magicznych przedmiotów i urządzeń.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Wiedza_i_Arkana_Magi'))
                def Dwarf_Wizard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Wizard',
                        'opis': '''Stworzona Postać!
                                  Imię: Thordin Głębokie Zaklęcie
                                  Rasa: Dwarf
                                  Klasa: Wizard
                                  Historia: Uczeń magii, opuścił swe krasnoludzkie kopalnie, aby zgłębiać tajemnice zaklęć i starożytnych artefaktów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Narodzony_z_Magia'))
                def Dwarf_Sorcerer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Sorcerer',
                        'opis': '''Stworzona Postać!
                                  Imię: Durgan Magiczna Skała
                                  Rasa: Dwarf
                                  Klasa: Sorcerer
                                  Historia: Posiadający wrodzoną moc magiczną, kontroluje i manipuluje magią w górskich otchłaniach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Muzyka_i_Magia'))
                def Dwarf_Bard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Bard',
                        'opis': '''Stworzona Postać!
                                  Imię: Glimmer Opowieściopiękny
                                  Rasa: Dwarf
                                  Klasa: Bard
                                  Historia: Muzyk i opowieścista, używa magii w swojej sztuce, oczarowuje publiczność i wrogów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Zrecznosc_i_Bron_dystansowa'))
                def Dwarf_Ranger(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Ranger',
                        'opis': '''Stworzona Postać!
                                  Imię: Korgan Cieniostąp
                                  Rasa: Dwarf
                                  Klasa: Ranger
                                  Historia: Łowca, który opuścił krasnoludzką enklawę, aby stać się mistrzem w strzelaniu z łuku i łączeniu się z przyrodą.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Magia_paktow_i_Cienie'))
                def Dwarf_Warlock(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Warlock',
                        'opis': '''Stworzona Postać!
                                  Imię: Morgar Ukryty Pakt
                                  Rasa: Dwarf
                                  Klasa: Warlock
                                  Historia: Podpisał tajemniczą umowę z mrocznym patronem, uzyskując moc nieznaną w swym krasnoludzkim świecie.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Dwarf') & (m.klasa == 'Przywiazanie_do_natury'))
                def Dwarf_Druid(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Dwarf Druid',
                        'opis': '''Stworzona Postać!
                                  Imię: Thalir Kamienne Żniwo
                                  Rasa: Dwarf
                                  Klasa: Druid
                                  Historia: Oddana naturze, opuściła krasnoludzkie kopalnie, by odkryć tajemnice przyrody i poznać jej moc.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Furia_i_Wscieklosc'))
                def Elf_Barbarian(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Barbarian',
                        'opis': '''Stworzona Postać!
                                  Imię: Elara Szumiący Liść
                                  Rasa: Elf
                                  Klasa: Barbarian
                                  Historia: Elfyjska wojowniczka, poszukująca wyzwań i starć, opuściła leśne ostępy, aby zdobyć sławę w bitwach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Mistrz_Miecza'))
                def Elf_Fighter(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Fighter',
                        'opis': '''Stworzona Postać!
                                  Imię: Aelar Szybki Strzał
                                  Rasa: Elf
                                  Klasa: Fighter
                                  Historia: Zwinny elfi wojownik, wyruszył poza leśne granice, by stać się mistrzem walki i odnaleźć swoją drogę.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Elf') & (m.klasa == 'Sztuki_walki_i_duchowa_energia'))
                def Elf_Monk(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Monk',
                        'opis': '''Stworzona Postać!
                                  Imię: Liara Cicha Strzała
                                  Rasa: Elf
                                  Klasa: Monk
                                  Historia: Elfi mnich, dążący do doskonałości w walce i duchowości, opuściła swoją wspólnotę, by rozwijać umiejętności.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                
                @when_all((m.rasa == 'Elf') & (m.klasa == 'Straznik_Swiatla'))
                def Elf_Paladin(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Paladin',
                        'opis': '''Stworzona Postać!
                                  Imię: Thalor Świetlisty Duch
                                  Rasa: Elf
                                  Klasa: Paladin
                                  Historia: Elfi obrońca, opuścił swoje rodzinne lasy, by walczyć o sprawiedliwość i światło w ciemnościach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Infiltracja_i_Obrazenia_krytyczne'))
                def Elf_Rogue(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Rogue',
                        'opis': '''Stworzona Postać!
                                  Imię: Elenion Cienista Noc
                                  Rasa: Elf
                                  Klasa: Rogue
                                  Historia: Elfi mistrz kradzieży i subtelności, opuścił lasy, by żyć w cieniu i odnosić zwycięstwa w milczeniu.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Wsparcie_i_Leczenie'))
                def Elf_Cleric(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Cleric',
                        'opis': '''Stworzona Postać!
                                  Imię: Auriel Śpiewający Gaj
                                  Rasa: Elf
                                  Klasa: Cleric
                                  Historia: Elfi kapłan oddany leczeniu i wsparciu, opuścił lasy, by niesć pomoc i nadzieję w świecie.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Inzynieria_magiczna'))
                def Elf_Artificer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Artificer',
                        'opis': '''Stworzona Postać!
                                  Imię: Galadriel Mistrzyni Artefaktów
                                  Rasa: Elf
                                  Klasa: Artificer
                                  Historia: Elfi inżynier magiczny, poszukujący wiedzy i tworzący magiczne przedmioty.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Elf') & (m.klasa == 'Wiedza_i_Arkana_Magi'))
                def Elf_Wizard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Wizard',
                        'opis': '''Stworzona Postać!
                                  Imię: Lorien Zaklęta Księga
                                  Rasa: Elf
                                  Klasa: Wizard
                                  Historia: Elfi uczony, odkrywający tajemnice magii i studiujący starożytne artefakty.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Narodzony_z_Magia'))
                def Elf_Sorcerer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Sorcerer',
                        'opis': '''Stworzona Postać!
                                  Imię: Elwin Upiór Mgły
                                  Rasa: Elf
                                  Klasa: Sorcerer
                                  Historia: Elfi czarodziej z wrodzoną mocą, manipulujący mgłą i naturą.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Elf') & (m.klasa == 'Muzyka_i_Magia'))
                def Elf_Bard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Bard',
                        'opis': '''Stworzona Postać!
                                  Imię: Melian Pieśniarka Leśnych Opowieści
                                  Rasa: Elf
                                  Klasa: Bard
                                  Historia: Elfi artystka, łącząca magię z muzyką, opowiadająca historie i radosne ballady.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Zrecznosc_i_Bron_dystansowa'))
                def Elf_Ranger(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Ranger',
                        'opis': '''Stworzona Postać!
                                  Imię: Faelyn Łowczyni Cieni
                                  Rasa: Elf
                                  Klasa: Ranger
                                  Historia: Elfi łowczyni, mistrzyni łuku, żyjąca w harmonii z naturą.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Elf') & (m.klasa == 'Magia_paktow_i_Cienie'))
                def Elf_Warlock(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Warlock',
                        'opis': '''Stworzona Postać!
                                  Imię: Erevan Nawiązujący Pakt
                                  Rasa: Elf
                                  Klasa: Warlock
                                  Historia: Elfi uzyskujący moc poprzez tajemniczy pakt z cieniem.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Elf') & (m.klasa == 'Przywiazanie_do_natury'))
                def Elf_Druid(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Elf Druid',
                        'opis': '''Stworzona Postać!
                                  Imię: Thalara Strażniczka Leśnej Równowagi
                                  Rasa: Elf
                                  Klasa: Druid
                                  Historia: Elfi strażniczka natury, oddana ochronie i harmonii lasu.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Human') & (m.klasa == 'Furia_i_Wscieklosc'))
                def Human_Barbarian(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Barbarian',
                        'opis': '''Stworzona Postać!
                                  Imię: John Smith
                                  Rasa: Human
                                  Klasa: Barbarian
                                  Historia: Odważny wojownik, poszukujący przygód i walki, opuścił swoją osadę, by zdobyć sławę w bitwach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Mistrz_Miecza'))
                def Human_Fighter(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Fighter',
                        'opis': '''Stworzona Postać!
                                  Imię: Emily Johnson
                                  Rasa: Human
                                  Klasa: Fighter
                                  Historia: Wytrawna wojowniczka, pragnąca doskonałości w walce, opuściła swoją rodzinę, by być mistrzem miecza.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})


                @when_all((m.rasa == 'Human') & (m.klasa == 'Sztuki_walki_i_duchowa_energia'))
                def Human_Monk(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Monk',
                        'opis': '''Stworzona Postać!
                                  Imię: William Turner
                                  Rasa: Human
                                  Klasa: Monk
                                  Historia: Mnich praktykujący sztuki walki i duchowość, opuścił swoją osadę, by doskonalić umiejętności.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Straznik_Swiatla'))
                def Human_Paladin(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Paladin',
                        'opis': '''Stworzona Postać!
                                  Imię: Sarah Davis
                                  Rasa: Human
                                  Klasa: Paladin
                                  Historia: Bojowniczka o sprawiedliwość i ochronę słabszych, opuściła swoją społeczność, by bronić innych.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})
                    
                @when_all((m.rasa == 'Human') & (m.klasa == 'Infiltracja_i_Obrazenia_krytyczne'))
                def Human_Rogue(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Rogue',
                        'opis': '''Stworzona Postać!
                                  Imię: Rebecca Brown
                                  Rasa: Human
                                  Klasa: Rogue
                                  Historia: Zręczny i sprytny złodziej, wykorzystujący umiejętności intrygi, opuścił swoje rodzinne miasto.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Wsparcie_i_Leczenie'))
                def Human_Cleric(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Cleric',
                        'opis': '''Stworzona Postać!
                                  Imię: Michael White
                                  Rasa: Human
                                  Klasa: Cleric
                                  Historia: Oddany kapłan, gotowy do leczenia i wspierania sojuszników, opuścił swoją wspólnotę w imię wiary.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Inzynieria_magiczna'))
                def Human_Artificer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Artificer',
                        'opis': '''Stworzona Postać!
                                  Imię: Olivia Green
                                  Rasa: Human
                                  Klasa: Artificer
                                  Historia: Inżynier magiczny, tworzący przedmioty i urządzenia, opuścił swoje miejsce urodzenia w poszukiwaniu wiedzy.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Wiedza_i_Arkana_Magi'))
                def Human_Wizard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Wizard',
                        'opis': '''Stworzona Postać!
                                  Imię: Daniel Clark
                                  Rasa: Human
                                  Klasa: Wizard
                                  Historia: Uczeń magii, pragnący zgłębić tajemnice zaklęć i artefaktów, opuścił swoje rodzinne miasto.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Narodzony_z_Magia'))
                def Human_Sorcerer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Sorcerer',
                        'opis': '''Stworzona Postać!
                                  Imię: Sophia Taylor
                                  Rasa: Human
                                  Klasa: Sorcerer
                                  Historia: Posiadająca wrodzoną moc magii, kontrolująca i manipulująca energią, opuściła swoje rodzinne ziemie.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Narodzony_z_Magia'))
                def Human_Sorcerer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Sorcerer',
                        'opis': '''Stworzona Postać!
                                  Imię: Sophia Miller
                                  Rasa: Human
                                  Klasa: Sorcerer
                                  Historia: Posiadająca wrodzoną moc magiczną, kontrolująca i manipulująca magią.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Muzyka_i_Magia'))
                def Human_Bard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Bard',
                        'opis': '''Stworzona Postać!
                                  Imię: David Wilson
                                  Rasa: Human
                                  Klasa: Bard
                                  Historia: Muzyk i opowieścista, używający magii w swojej sztuce, oczarowujący publiczność i wrogów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Zrecznosc_i_Bron_dystansowa'))
                def Human_Ranger(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Ranger',
                        'opis': '''Stworzona Postać!
                                  Imię: Emma Thompson
                                  Rasa: Human
                                  Klasa: Ranger
                                  Historia: Łowczyni, mistrzyni broni dystansowej, zdolna łączyć się z przyrodą.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Magia_paktow_i_Cienie'))
                def Human_Warlock(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Warlock',
                        'opis': '''Stworzona Postać!
                                  Imię: Samuel Clark
                                  Rasa: Human
                                  Klasa: Warlock
                                  Historia: Posiada tajemniczy pakt, pozyskujący niezwykłą moc w świecie magii.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Human') & (m.klasa == 'Przywiazanie_do_natury'))
                def Human_Druid(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Human Druid',
                        'opis': '''Stworzona Postać!
                                  Imię: Grace Anderson
                                  Rasa: Human
                                  Klasa: Druid
                                  Historia: Oddana naturze, odkrywająca jej tajemnice i siłę.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Furia_i_Wscieklosc'))
                def Tiefling_Barbarian(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Barbarian',
                        'opis': '''Stworzona Postać!
                                  Imię: Azazel Krew i Ogień
                                  Rasa: Tiefling
                                  Klasa: Barbarian
                                  Historia: Potężny wojownik, wykorzystujący swoje demonicznego pochodzenia w walce.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Mistrz_Miecza'))
                def Tiefling_Fighter(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Fighter',
                        'opis': '''Stworzona Postać!
                                  Imię: Lilith Cienista Ostra
                                  Rasa: Tiefling
                                  Klasa: Fighter
                                  Historia: Sztandarowa wojowniczka, wykorzystująca swoją demoniczność, by zdobyć sławę.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Sztuki_walki_i_duchowa_energia'))
                def Tiefling_Monk(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Monk',
                        'opis': '''Stworzona Postać!
                                  Imię: Mephistopheles Duchowy Walkir
                                  Rasa: Tiefling
                                  Klasa: Monk
                                  Historia: Mnich o demonicznych korzeniach, pragnący osiągnięcia wewnętrznej równowagi.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Straznik_Swiatla'))
                def Tiefling_Paladin(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Paladin',
                        'opis': '''Stworzona Postać!
                                  Imię: Belial Płomień Sprawiedliwości
                                  Rasa: Tiefling
                                  Klasa: Paladin
                                  Historia: Odpowiedzialny paladyn, wykorzystujący swoje demonicznego pochodzenia, by walczyć ze złem.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Infiltracja_i_Obrazenia_krytyczne'))
                def Tiefling_Rogue(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Rogue',
                        'opis': '''Stworzona Postać!
                                  Imię: Asmodeus Skryty Cień
                                  Rasa: Tiefling
                                  Klasa: Rogue
                                  Historia: Sprytny i przebiegły złodziej, wykorzystujący swoje demoniczne cechy w podziemnym świecie.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Wsparcie_i_Leczenie'))
                def Tiefling_Cleric(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Cleric',
                        'opis': '''Stworzona Postać!
                                  Imię: Lucifer Święty Wybawca
                                  Rasa: Tiefling
                                  Klasa: Cleric
                                  Historia: Kapłan oddany swej demonicznej naturze, gotowy do leczenia i wsparcia sojuszników.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Inzynieria_magiczna'))
                def Tiefling_Artificer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Artificer',
                        'opis': '''Stworzona Postać!
                                  Imię: Baphomet Mistrz Magicznych Urządzeń
                                  Rasa: Tiefling
                                  Klasa: Artificer
                                  Historia: Twórca magicznych urządzeń, wykorzystujący swoje demoniczne zdolności w konstruowaniu.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Wiedza_i_Arkana_Magi'))
                def Tiefling_Wizard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Wizard',
                        'opis': '''Stworzona Postać!
                                  Imię: Malphas Zaklęty Czarownik
                                  Rasa: Tiefling
                                  Klasa: Wizard
                                  Historia: Zafascynowany magią, poszukujący tajemnic demonicznych mocy.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Narodzony_z_Magia'))
                def Tiefling_Sorcerer(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Sorcerer',
                        'opis': '''Stworzona Postać!
                                  Imię: Beelzebub Potężny Zaklinacz
                                  Rasa: Tiefling
                                  Klasa: Sorcerer
                                  Historia: Posiadający wrodzoną moc magiczną, kontrolujący magię w demonicznych otchłaniach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Muzyka_i_Magia'))
                def Tiefling_Bard(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Bard',
                        'opis': '''Stworzona Postać!
                                  Imię: Diablo Melodyjny Zaczarowiciel
                                  Rasa: Tiefling
                                  Klasa: Bard
                                  Historia: Muzyk i opowieścista, używający magii w swojej sztuce, oczarowujący publiczność i wrogów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Zrecznosc_i_Bron_dystansowa'))
                def Tiefling_Ranger(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Ranger',
                        'opis': '''Stworzona Postać!
                                  Imię: Asmodaj Strzelec z Piekielnych Puszczy
                                  Rasa: Tiefling
                                  Klasa: Ranger
                                  Historia: Łowca, który wykorzystuje swoje piekielne dziedzictwo w walce z odległości.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Magia_paktow_i_Cienie'))
                def Tiefling_Warlock(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Warlock',
                        'opis': '''Stworzona Postać!
                                  Imię: Mammon Uwięziony w Umowie
                                  Rasa: Tiefling
                                  Klasa: Warlock
                                  Historia: Posiadający umowę z mrocznym bytem, wykorzystujący demoniczne moce w służbie swoich celów.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all((m.rasa == 'Tiefling') & (m.klasa == 'Przywiazanie_do_natury'))
                def Tiefling_Druid(c):
                    characters[c.m.ktora] = {
                        'wynik': 'Tiefling Druid',
                        'opis': '''Stworzona Postać!
                        Imię: Belphegor Strażnik Piekła
                        Rasa: Tiefling
                        Klasa: Druid
                        Historia: Oddany naturze, poszukujący równowagi w demonicznych korzeniach.'''
                    }
                    c.assert_fact({'ktora': c.m.ktora})

                @when_all(+m.ktora)
                def output(c):
                    character_info = characters.get(c.m.ktora)
                    if character_info:
                        formatted_info = (
                            f"Postać: {character_info['wynik']}\n\n"
                            f"Opis postaci:\n"
                            f"Imię: {character_info['opis'].split('\n')[1].split(': ')[1]}\n"
                            f"Rasa: {character_info['opis'].split('\n')[2].split(': ')[1]}\n"
                            f"Klasa: {character_info['opis'].split('\n')[3].split(': ')[1]}\n"
                            f"{'Historia: ' + character_info['opis'].split('\n')[4].split(': ')[1]}"
                        )
                        self.character_info.setText(formatted_info)

            post('tworzenie_postaci', {'ktora': '1', 'rasa': race, 'klasa': char_class})
            self.rule_set_created = True
            self.race_label.setText("Race:")
            self.class_label.setText("Class:")
            self.race_combo.hide()
            self.class_combo.hide()
            self.character_info_label.show()
            self.display_button.hide()
            self.reload_button.show()
        
    def restart(self):
        sys.exit()
            
def main():
    app = QApplication(sys.argv)
    window = CharacterCreator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
