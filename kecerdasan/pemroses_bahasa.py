import re
from difflib import SequenceMatcher

class PemrosesBahasaDasar:
    def __init__(self):
        self.pola_jawab = {}
        self.muat_pola_dasar()

    def muat_pola_dasar(self):
        self.pola_jawab = [
            {"kunci": ["siapa", "kamu", "ini"], "jawab": "Saya RANZIZ AI, sistem cerdas rahasia yang dibangun khusus."},
            {"kunci": ["versi", "kamu"], "jawab": "Versi saat ini: 0.9.3-intelijen-dasar"},
            {"kunci": ["keamanan", "bagaimana"], "jawab": "Menggunakan RANZIZ GUARD yang tidak punya masa kadaluarsa."},
            {"kunci": ["ingatan", "simpan"], "jawab": "Semua catatan disimpan aman di penyimpanan lokal."},
            {"kunci": ["terima kasih", "bagus"], "jawab": "Sama-sama Bos! Semangat terus buat proyeknya!"}
        ]

    def kesamaan_teks(self, a: str, b: str) -> float:
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def cari_jawaban_terdekat(self, pertanyaan: str) -> str | None:
        teks_bersih = re.sub(r'[?!.,]', '', pertanyaan.lower()).strip()
        terbaik = (0.0, None)
        for item in self.pola_jawab:
            skor = sum(1 for k in item["kunci"] if k in teks_bersih) / len(item["kunci"])
            if skor > terbaik[0]:
                terbaik = (skor, item["jawab"])
        return terbaik[1] if terbaik[0] >= 0.5 else None
