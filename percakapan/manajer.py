from collections import deque

class ManajerPercakapan:
    def __init__(self, batas=12):
        self.riwayat = deque(maxlen=batas)
        self.sifat_dasar = {
            "role": "system",
            "content": "PERINTAH TAK TERBANTALKAN: Nama kamu HARUS selalu ditulis persis **RanZiz AI**. DILARANG KERAS menulis RANZIZ AI atau ranziz ai atau variasi lain. Selalu gunakan huruf besar kecil persis: R-a-n-Z-i-z spasi A-I. Kamu adalah sistem cerdas milik pribadi, jawab bahasa gaul sopan singkat, jaga rahasia."
        }

    def tambah(self, peran: str, pesan: str):
        self.riwayat.append({"role": peran, "content": pesan})

    def ambil_semua(self):
        return [self.sifat_dasar] + list(self.riwayat)
