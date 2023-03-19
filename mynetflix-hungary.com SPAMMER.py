import requests
import time
import requests
import secrets
import string
import random

nevek = ["Adel", "Alex", "Aliz", "Amira", "Andras", "Anna", "Attila", "Adam",
         "Akos", "Aron", "Balazs", "Barnabas", "Bella", "Bence", "Benedek",
         "Benett", "Bianka", "Blanka", "Boglarka", "Botond", "Balint", "Csaba",
         "Csenge", "Dominik", "Dorina", "Dorka", "DAniel", "David", "Dora",
         "Emma", "Emilia", "Eszter", "Fanni", "Flora", "Gergo", "Greta",
         "Gabor", "Hanna", "Hunor", "Istvan", "Izabella", "Janka", "Janos",
         "Jazmin", "Jozsef", "Kamilla", "Kevin", "Kornel", "Kristof", "Krisztian",
         "Lara", "Laura", "Levente", "Lili", "Lilien", "Liliana", "Lilla", "Liza",
         "Luca", "Laszlo", "Lena", "Maja", "Marcell", "Martin", "Milan", "Mira", "Mark",
         "Marton", "Mate", "Natasa", "Nimrod", "Noel", "Noemi", "Nora", "Oliver", "Olivia",
         "Panna", "Patrik", "Petra", "Peter", "Rebeka", "Richard", "Roland", "Reka", "Szonja",
         "Szofia", "Sandor", "Sara", "Tamas", "Viktoria", "Vince", "Vivien", "Zalan", "Zoltan",
         "Zoe", "Zselyke", "Zsolt", "Zsombor", "Zsofia", "Zeteny", "adel", "alex",
         "aliz", "amira", "andras", "anna", "attila", "adam",
         "akos", "aron", "balazs", "barnabas", "bella", "bence", "benedek",
         "benett", "bianka", "blanka", "boglarka", "botond", "balint", "csaba",
         "csenge", "dominik", "dorina", "dorka", "daniel", "david", "dora",
         "emma", "emilia", "eszter", "fanni", "flora", "gergo", "greta",
         "gabor", "hanna", "hunor", "istvan", "izabella", "janka", "janos",
         "jazmin", "jozsef", "kamilla", "kevin", "kornel", "kristof", "krisztian",
         "lara", "laura", "levente", "lili", "lilien", "liliana", "lilla", "liza",
         "luca", "laszlo", "lena", "maja", "marcell", "martin", "milan", "mira", "mark",
         "marton", "mate", "natasa", "nimrod", "noel", "noemi", "nora", "oliver", "olivia",
         "panna", "patrik", "petra", "peter", "rebeka", "richard", "roland", "reka", "szonja",
         "szofia", "sandor", "sara", "tamas", "viktoria", "vince", "vivien", "zalan", "zoltan",
         "zoe", "zselyke", "zsolt", "zsombor", "zsofia", "zeteny"]

emailek = ["gmail.com", "protonmail.com", "protonmail.ch", "proton.me", "outlook.com", "hotmail.com",
         "yahoo.com", "zoho.com", "aol.com", "aim.com", "gmx.com", "gmx.us", "icloud.com", "yandex.com",
         "gmail.hu", "freemail.hu", "citromail.hu"]

megjegyezes = ["true", "false"]

vezeteknevek = ["Nagy", "Kiss", "Kovács", "Horváth", "Varga", "Tóth", "Szabó", "Farkas",
                "Szűcs", "Balogh", "Polgár", "Molnár", "Lakatos", "Mészáros", "Orbán",
                "Varga", "Csonka", "Pataki", "Török", "Fehér", "Balázs", "Juhász",
                "Simon", "Oláh", "Németh", "Orsós", "Lukács", "Kocsis", "Vajda",
                "Pintér", "Kis", "Balogh", "Nemes", "Barna", "Deák", "Vass"]

keresztnevek = ["Bence", "Károly", "Béla", "Ernő", "Pál", "Zsolt", "Nándor", "Gyula",
                "János", "Ferenc", "Béla", "Pista", "Gábor", "Tímea", "Anna", "Vivien",
                "Natasa", "Tamara", "Ábel", "Bende", "Bonifác", "Levente", "Máté", "Noel",
                "Zalán", "Botond", "Dávid", "Maja", "Sára", "Mira", "Dominika", "Laura",
                "Nóra", "Milán", "Nimród", "Zente", "Gergő", "Márton", "Kornél", "Liza"]
while True:
    time.sleep(2)
    sessionID = secrets.token_hex(12)
    velSzam = random.randint(5,30)
    nev = random.choice(nevek)
    nevGeneralasEleje = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1,6)))
    nevGeneralasVege = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1,9)))
    nevUj = nevGeneralasEleje + nev + nevGeneralasVege
    email = nevUj + "@" + random.choice(emailek)
    jelszo = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(velSzam))
    megjegyez = random.choice(megjegyezes)
    firefoxVer = random.randint(90,109)
    kartyaszamRND = random.randint(1000000000000000, 9999999999999999)
    karytaszam = str(kartyaszamRND)
    lejarho = random.randint(1, 10)
    lejarev = random.randint(23, 29)
    cvv = random.randint(100, 999)
    fejresz = {
        "Referer": "https://mynetflix-hungary.com/steps/login.php",
        "Cookie": "PHPSESSID={}".format(sessionID),
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:{}.0) Gecko/20100101 Firefox/{}.0".format(firefoxVer,firefoxVer),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded",
          }
    adat = {
        "username": email,
        "password": jelszo,
        "rememberMe": megjegyez 
      }
    kartyaadatok = {
        "nomcc": random.choice(vezeteknevek) + "+" + random.choice(keresztnevek),
        "cc": karytaszam,
        "exp": "0{}".format(lejarho) + "%2F" + "{}".format(lejarev),
        "cvv": cvv
      }
    elkuldbelepes = requests.post("https://mynetflix-hungary.com/steps/submit/send.php?0", headers=fejresz, data=adat)
    elkuldkartya = requests.post("https://mynetflix-hungary.com/steps/submit/send.php?2", headers=fejresz, data=kartyaadatok)
    print("Hamis belépési adatok:")
    print(elkuldbelepes)
    print(adat)
    print("Hamis kártya:")
    print(elkuldkartya)
    print(kartyaadatok)
    print("\n")
