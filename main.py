# Interesują nas tylko informacje: uuid (z loginu), imię, nazwisko, login, hasło, e-mail, data rejestracji.
# Interesują nas tylko osoby z narodowościami: CA, DK, FI, GB, IE, NL, NO, US
# Data rejestracji zostanie zapisana w formacie: YYYY/mm/dd HH:MM
# Na koniec zapisujemy nasze dane do pliku, którego format możemy wybrać w funkcji. Dostępne opcje to: txt i csv.
#
# Dla csv zapisujemy dane z separatorem ";" oraz z nagłówkiem.
# Dla txt zapisujemy dane z separatorem oraz bez nagłówka.
# Nazwa pliku jest zgodna z formatem: <yyyy_mm_dd_HH_MM_SS>.<csv|txt>


from requests import get
from json import loads
from datetime import datetime
import time
import csv




def fetch_random_users():
    url = "https://randomuser.me/api"
    response = get(url)
    user_items = []  # Lista przechowująca słownik
    nationality = ['CA', 'DK', 'FI', 'GB', 'IE', 'NL', 'NO', 'US']
    # Parsowanie danych JSON
    data = loads(response.text)

    # Sprawdzenie, czy klucz 'results' istnieje w danych
    if 'results' in data:
        for row in data['results']:
            if row['nat'] in nationality:
                user_items.append(row)  # Dodanie użytkownika do listy user_items
    return user_items

def main():
    users_number =4
    user_items=[]

    for x in range(users_number): #nie interesuje nas wartość iteratora a ilość iteracji
        fetched_users = fetch_random_users()
        user_items.extend(fetched_users)
        time.sleep(20)

    now = datetime.now()
    file_name_csv = now.strftime("%d_%m_%Y_%H_%M_%S")+ ".csv"
    file_name_txt = now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    with open(file_name_csv, 'w', newline = '') as output_csv: #output_csv jest zmienną, która przechowuje uchwyt pliku do pliku CSV,
        writer = csv.writer(output_csv, delimiter=';') # Utwórz obiekt writer dla pliku CSV
        writer.writerow(['UUID','Imię','Nazwisko','Login','Hasło','E-mail','Narodowość','Data rejestracji']) #nagłówki dla csvd

    # Iteracja przez elementy user_items
        for user_item in user_items:
            writer.writerow([
                user_item['login']['uuid'],  # UUID z loginu
                user_item['name']['first'], # Imię
                user_item['name']['last'], # Nazwisko
                user_item['login']['username'],  # Login
                user_item['login']['password'],  # Hasło
                user_item['email'],  # E-mail
                user_item['nat'],  # Narodowość
        #konwersja daty
                datetime.strptime(user_item['registered']['date'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y/%m/%d %H:%M:%S")
        #parsowanie łańcucha znaków reprezentujące date i czas na obiekt 'datetime'
])
    with open(file_name_txt, 'w', newline='') as output_txt:
                # Iteracja przez elementy user_items i zapis danych do pliku TXT
        for user_item in user_items:
            output_txt.write(';'.join([
                user_item['login']['uuid'],  # UUID z loginu
                user_item['name']['first'],  # Imię
                user_item['name']['last'],  # Nazwisko
                user_item['login']['username'],  # Login
                user_item['login']['password'],  # Hasło
                user_item['email'],  # E-mail
                user_item['nat'],  # Narodowość
                datetime.strptime(user_item['registered']['date'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y/%m/%d %H:%M:%S")]) + '\n')




            print("UUID:", user_item['login']['uuid'])  # UUID z loginu
            print("Imię:", user_item['name']['first'])  # Imię
            print("Nazwisko:", user_item['name']['last'])  # Nazwisko
            print("Login:", user_item['login']['username'])  # Login
            print("Hasło:", user_item['login']['password'])  # Hasło
            print("E-mail:", user_item['email'])  # E-mail
            print("Narodowość:", user_item['nat'])  # Narodowość
        # konwersja daty
            registration_time = datetime.strptime(user_item['registered']['date'], "%Y-%m-%dT%H:%M:%S.%fZ")  # parsowanie łańcucha znaków reprezentujące date i czas na obiekt 'datetime'
            convert_date = registration_time.strftime("%Y/%m/%d %H:%M:%S")
            print("Data rejestracji: ", convert_date)
            print() #przestrzeń między userami






if __name__ == '__main__':
    print('Random users:')
    main()


