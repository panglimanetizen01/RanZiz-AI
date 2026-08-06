import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PenyediaCerdas:
    def __init__(self):
        self.aktif = False
        self.url = os.getenv("RANZIZ_API_URL", "").strip()
        self.kunci = os.getenv("RANZIZ_API_KUNCI", "").strip()
        self.model = os.getenv("RANZIZ_MODEL", "").strip()
        if self.url and self.kunci:
            self.aktif = True

    def tanya_dengan_konteks(self, daftar_pesan: list) -> str:
        if not self.aktif:
            return "🔌 Belum terhubung ke layanan."
        try:
            kepala = {
                "Authorization": f"Bearer {self.kunci}",
                "Content-Type": "application/json"
            }
            badan = {
                "model": self.model,
                "messages": daftar_pesan,
                "temperature": 0.4,
                "max_tokens": 1024
            }
            respon = requests.post(self.url, headers=kepala, json=badan, timeout=20)
            if respon.status_code == 200:
                hasil = respon.json()["choices"][0]["message"]["content"].strip()
                # PAKSA GANTI SEMUA VARIASI NAMA YANG SALAH
                hasil = hasil.replace("RANZIZ AI", "RanZiz AI")
                hasil = hasil.replace("ranziz ai", "RanZiz AI")
                hasil = hasil.replace("Ranziz ai", "RanZiz AI")
                hasil = hasil.replace("RANZIZ ai", "RanZiz AI")
                return hasil
            return f"⚠️ Gangguan layanan, coba lagi nanti ya."
        except Exception:
            return "⚠️ Sedang tidak bisa terhubung, cek koneksi atau kunci API."
