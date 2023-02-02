import random
import string

characters_list = string.ascii_letters + string.digits

user_accounts = {
    "admin": {
        "username": "admin",
        "firstName": "Admin",
        "lastName": "McAdminFace",
        "password": "12345asdfg" 
    },
    
    "mhorvat": {
        "username": "mhorvat",
        "firstName": "Marko",
        "lastName": "Horvat",
        "password": "12345asdfg" 
    }
}


def login_form(user_accounts):
    login = True
    login_tries = 0
    while login == True:
        username = input("Unesite svoje korisničko ime: ")
        password = input("Unesite svoju lozinku: ")
        login_tries += 1
        if username in user_accounts.keys() and password == user_accounts[username]["password"]:
            firstName = user_accounts[username]["firstName"]
            lastName = user_accounts[username]["lastName"]
            print(f"Prijava uspješna. Dobro došli, {firstName} {lastName}")
            login = False
            return username
        elif login_tries == 3:
            print("Tri neispravna pokušaja prijave. Obratite se administratoru.")
            login =  False
            return False
        else:
            print("Korisničko ime ili lozinka nisu ispravni. Pokušajte ponovno.")
            

    
def add_user(user_accounts):
    firstName = input("Unesite ime korisnika: ")
    lastName = input("Unesite prezime korisnika: ")
    username = firstName[0].lower() + lastName.lower()
    additionalNumber = 0
    while username in user_accounts.keys():
        additionalNumber += 1
        username = username + str(additionalNumber)
    password = ''
    for i in range(10):
        password += random.choice(characters_list)
    user_accounts[username] = {
        "firstName": firstName,
        "lastName": lastName,
        "username": username,
        "password": password,
    }
    print(f"Generirano korisničko ime je {username}, a lozinka je {password}")


def show_account_details(user_accounts, account_choice):
    print(f"Korisnički podaci za {account_choice} ")
    ime = user_accounts[account_choice]["firstName"]
    print(f"1 - Ime: {ime}")
    prezime = user_accounts[account_choice]["lastName"]
    print(f"2 - Prezime: {prezime}")
    lozinka = user_accounts[account_choice]["password"]
    print(f"3 - Lozinka: {lozinka}")

def change_account_details(user_accounts):
    print("Popis korisničkih računa je:")
    for key in user_accounts.keys():
        print(key)
    while True:
        account_choice = input("Odaberite korisnički račun koji želite urediti ili unesite 'end' za kraj uređivanja: ")
        if account_choice in user_accounts.keys():
            show_account_details(user_accounts, account_choice)
            akcija = input("Odaberite polje 1-3 koje želite urediti: ")
            if akcija == "1":
                new_first_name = input("Unesite ime korisnika: ")
                user_accounts[account_choice]["firstName"] = new_first_name
            elif akcija == "2":
                new_last_name = input("Unesite prezime korisnika: ")
                user_accounts[account_choice]["lastName"] = new_last_name
            elif akcija == "3":
                password_change(user_accounts, account_choice)
        elif account_choice == "end":
            break
        else:
            print(f"Korisnički račun {account_choice} ne postoji.")
    

def password_change(user_accounts, account_choice):
    choice = input("Želite li unijeti lozinku samostalno (1) ili ju automatski generirati (2)? ")
    if choice == "1":
        new_password = ""
        while True:
            new_password = input("Unesite lozinku od 10 znakova: ")
            if len(new_password) < 10:
                print("Lozinka ne sadrži 10 znakova. Pokušajte ponovno.") 
            elif new_password == user_accounts[account_choice]["password"]:
                print("Lozinka koju ste unijeli je jednaka trenutnoj. Pokušajte ponovno.")
            else:
                user_accounts[account_choice]["password"] = new_password
                print(f"Nova lozinka za korisnički račun {account_choice} je {new_password}")
                break
                        
    if choice == "2":
        for i in range(10):
            new_password += random.choice(characters_list)
        user_accounts[account_choice]["password"] = new_password
        print(f"Nova lozinka za korisnički račun {account_choice} je {new_password}")


def delete_user(user_accounts):
    print("Popis korisničkih računa je:")
    for key in user_accounts.keys():
        print(key)
    while True:
        account_choice = input("Odaberite korisnički račun koji želite obrisati ili unesite 'end' za kraj uređivanja: ")
        if account_choice in user_accounts.keys():
            deleted_account = user_accounts.pop(account_choice)
            print(f"Korisnički račun {deleted_account} je obrisan.")
        elif account_choice == "end":
            break
        else:
            print(f"Korisnički račun {account_choice} ne postoji.")
            

def identity_management(user_accounts):
    logged_in_user = login_form(user_accounts)
    
    if logged_in_user == "admin":
        akcija = "0"
        while akcija != "5":
            akcija = input("""
                Odaberite akciju nad korisnicima:
                1 - dodavanje novog korisnika
                2 - ažuriranje podataka 
                3 - brisanje korisnika
                4 - pregled podataka o korisnicima
                5 - odjava iz sustava
                
                """)
            if akcija == "1":
                add_user(user_accounts)
            
            elif akcija == "2":
                change_account_details(user_accounts)
            
            elif akcija == "3":
                delete_user(user_accounts)
            
            elif akcija == "4":
                for key in user_accounts.keys():
                    show_account_details(user_accounts, key)
            
            elif akcija == "5":
                print(f"Doviđenja {logged_in_user}")
                break
            
            else:
                print("Neispravan unos.")
        
        
    elif logged_in_user in user_accounts.keys():
        akcija = "0"
        while akcija != "4":
            akcija = input("""
                Odaberite akciju nad svojim korisničkim računom:
                1 - pregled podataka
                2 - ažuriranje podataka 
                3 - promjena lozinke
                4 - odjava iz sustava
                
                """)
            
            if akcija == "1":
                show_account_details(user_accounts, logged_in_user)
            elif akcija == "2":
                show_account_details(user_accounts, logged_in_user)
                akcija_promjene = input("Odaberite polje 1-2 koje želite urediti: ")
                if akcija_promjene == "1":
                    new_first_name = input("Unesite ime: ")
                    user_accounts[logged_in_user]["firstName"] = new_first_name
                elif akcija_promjene == "2":
                    new_last_name = input("Unesite prezime: ")
                    user_accounts[logged_in_user]["lastName"] = new_last_name
            elif akcija == "3":
                password_change(user_accounts, logged_in_user)
            elif akcija == "4":
                print(f"Doviđenja {logged_in_user}")
                
    
    else:
        pass
    
            
identity_management(user_accounts)