from requests import get
from json import loads
# Interesują nas tylko informacje: uuid (z loginu), imię, nazwisko, login, hasło, e-mail, data rejestracji.
# Interesują nas tylko osoby z narodowościami: CA, DK, FI, GB, IE, NL, NO, US
# Data rejestracji zostanie zapisana w formacie: YYYY/mm/dd HH:MM

def main():
    url = "https://randomuser.me/api"
    response = get(url)

    user_items = [] #lista przechowujaca slownik

    # Sprawdzenie zawartości otrzymanej odpowiedzi
    # print("Otrzymane dane JSON:")
    # print(response.text)
    # print()

    # Parsowanie danych JSON
    data = loads(response.text)

    # Sprawdzenie, czy klucz 'results' istnieje w danych
    if 'results' in data:
        for row in data['results']:
            # Dodanie użytkownika do listy user_items
            user_items.append(row)


    # Iteracja przez elementy user_items
    for user_item in user_items:
        for key, value in user_item.items():
            # Sprawdzenie, czy wartość jest słownikiem
            if isinstance(value, dict):
                # Iteracja przez elementy słownika
                for sub_key, sub_value in value.items():
                    print(f"{sub_key.capitalize()}: {sub_value}") #zamiana na wielka litere .v
            # else:
            #     print(f"{key.capitalize()}: {value}")
        print()  # Pusta linia między użytkownikami


if __name__ == '__main__':
    print('Random users:')
    main()
