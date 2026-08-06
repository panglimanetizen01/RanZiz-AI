"""Enkripsi sederhana aman - pas di Termux"""
import base64
from hashlib import sha256

class PelindungSandi:
    def __init__(self, kunci_dasar: str = ""):
        kunci = kunci_dasar or "RANZIZ_RAHASIA_DASAR_2026"
        self.kunci = sha256(kunci.encode()).digest()

    def kunci_teks(self, teks: str) -> str:
        teks_byte = teks.encode("utf-8")
        hasil = bytearray()
        kunci_len = len(self.kunci)
        for i, b in enumerate(teks_byte):
            hasil.append(b ^ self.kunci[i % kunci_len])
        return base64.b64encode(hasil).decode("ascii")

    def buka_teks(self, sandi: str) -> str:
        try:
            sandi_byte = base64.b64decode(sandi)
            hasil = bytearray()
            kunci_len = len(self.kunci)
            for i, b in enumerate(sandi_byte):
                hasil.append(b ^ self.kunci[i % kunci_len])
            return hasil.decode("utf-8")
        except Exception:
            return "Gagal buka sandi"
