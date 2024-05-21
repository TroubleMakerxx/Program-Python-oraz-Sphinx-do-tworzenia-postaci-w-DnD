from durable.lang import *

characters = {}

with ruleset('tworzenie_postaci'):
    @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Furia_i_Wscieklosc') & (~m.ktora))
    def Dragonborn_Barbarian(c):
        ktora = str(len(characters) + 1)
        characters[ktora] = {
            'wynik': 'Dragonborn Barbarian',
            'opis': '''Stworzona Postać! 
                      Imie: Roland Barns
                      Rasa: Dragonborn
                      Klasa: Barbarian
                      Historia: Smoczy wojownik który opuścił swoje rodzinne miasto Nemfis w poszukiwaniu przygód.'''
        }
        c.assert_fact({'ktora': ktora})

    # Add checks and definitions for other race-class combinations
    @when_all((m.rasa == 'Dragonborn') & (m.klasa == 'Mistrz_Miecza') & (~m.ktora))
    def Dragonborn_Fighter(c):
        ktora = str(len(characters) + 1)
        characters[ktora] = {
            'wynik': 'Dragonborn Fighter',
            'opis': '''Stworzona Postać!
                      Imię: Dragan Żelazna Dłoń
                      Rasa: Dragonborn
                      Klasa: Fighter
                      Historia: Wytrawny wojownik, opuścił swoją rodzinę i ojczyznę, by zdobyć sławę i szacunek w brutalnym świecie walki.'''
        }
        c.assert_fact({'ktora': ktora})

    # Add more character combinations as needed...

    @when_all(+m.ktora)
    def output(c):
        character_info = characters.get(c.m.ktora)
        if character_info:
            print("Postać:", character_info['wynik'])
            print("Opis postaci:")
            print("Imie:", character_info['opis'].split('\n')[1].split(': ')[1])
            print("Rasa:", character_info['opis'].split('\n')[2].split(': ')[1])
            print("Klasa:", character_info['opis'].split('\n')[3].split(': ')[1])
            print("Historia:", character_info['opis'].split('\n')[4].split(': ')[1])
            print('\n')

# Your post() calls remain unchanged
post('tworzenie_postaci', {'rasa': 'Dragonborn', 'klasa': 'Furia_i_Wscieklosc'})
# Include other post() calls for different character combinations as needed
