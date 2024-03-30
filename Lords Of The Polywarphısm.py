# coding: latin-1

class Dunya:
    def __init__(self, n_satir, n_sutun):
        self.n_satir = n_satir
        self.n_sutun = n_sutun
        self.dunya = self.init_dunya()

    def init_dunya(self):
        matris = []
        for satir in range(self.n_satir):
            matris.append(["-"] * self.n_sutun)
        return matris

    def __str__(self):
        dunya_str = "      "
        for i in range(self.n_sutun):
            dunya_str += f"{i + 1:<5} "
        dunya_str += "\n"

        for i in range(self.n_satir):
            dunya_str += f"{i + 1:<3}|  "
            for j in range(self.n_sutun):
                dunya_str += f"{self.dunya[i][j]:<3}|  "
            dunya_str += "\n"
            if i < self.n_satir - 1:
                dunya_str += "   |" + "_____|" * (self.n_sutun - 1) + "_____|\n"
        return dunya_str.replace("-", ".")

    def yerlestir(self, oyuncu, x, y, savasci):
        if self.dunya[x][y] == "-":
            self.dunya[x][y] = savasci.isim[0]
            oyuncu.savascilar.append(savasci)
        else:
            print("Bu h�cre dolu, l�tfen ba�ka bir h�cre se�in.")

    def oyunculari_yerlestir(self, oyuncular):
        for oyuncu in oyuncular:
            if oyuncu.isim == "m1":
                self.yerlestir(oyuncu, 0, 0, Muhafiz())
            elif oyuncu.isim == "m2":
                self.yerlestir(oyuncu, 0, self.n_sutun - 1, Muhafiz())
            elif oyuncu.isim == "m3":
                self.yerlestir(oyuncu, self.n_satir - 1, 0, Muhafiz())
            elif oyuncu.isim == "m4":
                self.yerlestir(oyuncu, self.n_satir - 1, self.n_sutun - 1, Muhafiz())


class Oyuncu:
    def __init__(self, isim):
        self.isim = isim
        self.savascilar = []


class Warrior:
    def __init__(self, kaynak, can, menzil):
        self.kaynak = kaynak
        self.can = can
        self.menzil = menzil

    def attack(self, dusmanlar):
        pass


class Muhafiz(Warrior):
    def __init__(self):
        super().__init__(kaynak=10, can=80, menzil=1)
        self.isim = "Muhafiz"


class Okcu(Warrior):
    def __init__(self):
        super().__init__(kaynak=20, can=30, menzil=2)
        self.isim = "Ok�u"


class Topcu(Warrior):
    def __init__(self):
        super().__init__(kaynak=50, can=30, menzil=2)
        self.isim = "Top�u"


class Atli(Warrior):
    def __init__(self):
        super().__init__(kaynak=30, can=40, menzil=0)
        self.isim = "Atl�"


class Saglikci(Warrior):
    def __init__(self):
        super().__init__(kaynak=10, can=100, menzil=2)
        self.isim = "Sa�l�k��"


# Kullan�c�dan d�nya boyutunu al
def dunya_boyutu_al():
    while True:
        try:
            boyut = int(input("D�nya boyutunu girin (�rn. 16, 24, 32): "))
            if boyut not in [16, 24, 32]:
                print("Ge�ersiz boyut! L�tfen 16, 24 veya 32 girin.")
                continue
            return boyut
        except ValueError:
            print("Ge�ersiz giri�! L�tfen bir tam say� girin.")


# Oyuncu olu�turma
m1 = Oyuncu("m1")
m2 = Oyuncu("m2")
m3 = Oyuncu("m3")
m4 = Oyuncu("m4")

oyuncular = [m1, m2, m3, m4]

# D�nya boyutunu al ve d�nyay� olu�turma
dunya_boyutu = dunya_boyutu_al()
dunya = Dunya(dunya_boyutu, dunya_boyutu)
dunya.oyunculari_yerlestir(oyuncular)

# Oyuncular�n s�ras�yla hamle yap
def oyuncu_hamleleri(oyuncular, dunya):
    while True:
        for oyuncu in oyuncular:
            print(f"\nSe�en oyuncu: {oyuncu.isim}")
            print("�u anda Muhaf�z karakteri se�ilmi�tir.")
            print("1. Ok�u\n2. Atl�\n3. Top�u\n4. Muhaf�z")
            secim = input("Se�iminizi yap�n (1-4 veya 'bitir'): ")

            if secim.lower() == "bitir":
                return
            elif secim == "1":
                karakter = Okcu()
            elif secim == "2":
                karakter = Atli()
            elif secim == "3":
                karakter = Topcu()
            elif secim == "4":
                karakter = Muhafiz()
            else:
                print("Ge�ersiz se�im! L�tfen 1-4 aras�nda bir say� girin veya 'bitir' yaz�n.")
                continue

            while True:
                try:
                    satir = int(input("�stedi�iniz sat�r� se�in (1-{}): ".format(dunya.n_satir))) - 1
                    sutun = int(input("�stedi�iniz s�tunu se�in (1-{}): ".format(dunya.n_sutun))) - 1

                    if 0 <= satir < dunya.n_satir and 0 <= sutun < dunya.n_sutun and dunya.dunya[satir][sutun] == "-":
                        dunya.yerlestir(oyuncu, satir, sutun, karakter)
                        break
                    else:
                        print(f"Ge�ersiz pozisyon! L�tfen bo� bir h�cre se�in ve 1 ile {dunya.n_satir} aras�nda bir sat�r ve s�tun girin.")
                except ValueError:
                    print("Ge�ersiz giri�! L�tfen tam say� bir de�er girin.")

# Oyun ba�lang�c�
oyuncu_hamleleri(oyuncular, dunya)

# Son durumu g�ster
print("\nSon durum:")
for oyuncu in oyuncular:
    print(f"\n{oyuncu.isim}'in durumu:")
    for savasci in oyuncu.savascilar:
        print(f"{savasci.isim}: {savasci.kaynak=}, {savasci.can=}, {savasci.menzil=}")
print(dunya)

# Yeni bir tur i�in devam etmek isteyip istemedi�ini sor
while True:
    devam = input("\nYeni bir tur yapmak istiyor musunuz? (Evet/Hay�r): ").lower()
    if devam == "evet":
        # Her oyuncunun savascilar listesini s�f�rla
        for oyuncu in oyuncular:
            oyuncu.savascilar = []
        # Yeni bir tur ba�lat
        oyuncu_hamleleri(oyuncular, dunya)
        # Son durumu g�ster
        print("\nSon durum:")
        for oyuncu in oyuncular:
            print(f"\n{oyuncu.isim}'in durumu:")
            for savasci in oyuncu.savascilar:
                print(f"{savasci.isim}: {savasci.kaynak=}, {savasci.can=}, {savasci.menzil=}")
        print(dunya)
    elif devam == "hay�r":
        print("Oyun sona erdi. �yi g�nler!")
        break
    else:
        print("Ge�ersiz giri�! L�tfen 'Evet' veya 'Hay�r' yaz�n.")
