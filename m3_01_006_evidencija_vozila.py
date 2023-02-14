class Vozilo:
    def __init__(self, proizvodac, model, registracija):
        self.proizvodac = proizvodac
        self.model = model
        self.registracija = registracija

    def ispis(self):
        print()
        print(f"Marka vozila: {self.proizvodac} {self.model}")
        print(f"Registracija vozila: {self.registracija}")


class Automobil(Vozilo):
    def __init__(self, proizvodac, model, registracija, tip_motora):
        super().__init__(proizvodac, model, registracija)
        self.tip_motora = tip_motora

    def ispis(self):
        super().ispis()
        print(f"Tip motora: {self.tip_motora}")


class Kamion(Vozilo):
    def __init__(self, proizvodac, model, registracija, max_tezina):
        super().__init__(proizvodac, model, registracija)
        self.max_tezina = max_tezina

    def ispis(self):
        super().ispis()
        print(f"Maksimalna težina tereta: {self.max_tezina}")


class RadniStroj(Vozilo):
    def __init__(self, proizvodac, model, registracija, svrha):
        super().__init__(proizvodac, model, registracija)
        self.svrha = svrha

    def ispis(self):
        super().ispis()
        print(f"Svrha vozila: {self.svrha}")

vozila = {
    "automobili": [],
    "kamioni": [],
    "radni strojevi": [],
}

while True:
    print("Odaberite tip vozila koje želite unijeti:\n1-automobil\n2-kamion\n3-radni stroj")
    odabir = input()
    if odabir == "1":
        proizvodac = input("Unesite ime proizvodaca vozila: ")
        model = input("Unesite ime modela vozila: ")
        registracija = input("Unesite registraciju vozila: ")
        tip_motora = input("Unesite tip motora vozila: ")

        automobil = Automobil(proizvodac, model, registracija, tip_motora)
        vozila["automobili"].append(automobil)
    elif odabir == "2":
        proizvodac = input("Unesite ime proizvodaca vozila: ")
        model = input("Unesite ime modela vozila: ")
        registracija = input("Unesite registraciju vozila: ")
        max_tezina = input("Unesite maksimalnu težinu tereta vozila: ")

        kamion = Kamion(proizvodac, model, registracija, max_tezina)
        vozila["kamioni"].append(kamion)
    elif odabir == "3":
        proizvodac = input("Unesite ime proizvodaca vozila: ")
        model = input("Unesite ime modela vozila: ")
        registracija = input("Unesite registraciju vozila: ")
        svrha = input("Unesite svrhu vozila: ")

        radni_stroj = RadniStroj(proizvodac, model, registracija, svrha)
        vozila["radni strojevi"].append(radni_stroj)
    else:
        print("Neispravan unos.")

    if input("Želite li unijeti još jedno vozilo? (d/n) ").lower() == 'n':
        break
