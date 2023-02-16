# korisnik unosi termin sastanka
# aplikacija pokazuje koliko je vremena do početka termina
# potrebno to prikazati unutar vremenske zone korisnika
# korisnik treba specificirati vremensku zonu pri unosu termina sastanka

import datetime as dt
from dateutil import tz

sastanci = []


def unos_termina_sastanka():
    while True:
        termin_sastanka = input("Molimo Vas da unesete termin sastanka u formatu DD-MM-YYYY HH:MM\n")
        vremenska_zone_korisnika = input("Unesite Vašu vremensku zonu u formatu Kontinent/Grad:\n")
        try:
            sastanak_objekt = dt.datetime.strptime(termin_sastanka, "%d-%m-%Y %H:%M")
            sadasnji_trenutak = dt.datetime.now()
            tz_korisnik = tz.gettz(vremenska_zone_korisnika)
            sastanak_tz_korisnika = sastanak_objekt.astimezone(tz_korisnik)
            do_termina = sastanak_objekt - sadasnji_trenutak
            sastanci.append(sastanak_objekt)
            print(f"Uspješno ste zakazali termin sastanka za {sastanak_objekt}")
            print(f"Do početka sastanka: {do_termina.days} dana, {do_termina.seconds // 3600} sati i {do_termina.seconds // 60 % 60} minuta")
            print(f"Termin sastanka za vremensku zonu {vremenska_zone_korisnika} je {sastanak_tz_korisnika}")
        except Exception as e:
            print(f"Došlo je do pogreške: {e}")
        finally:
            if input("Želite li unijeti još jedan termin? (da/ne)\n").lower() != "da":
                break






