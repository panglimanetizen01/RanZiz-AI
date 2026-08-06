import os
import shutil
from datetime import datetime

class PengelolaCadangan:
    def __init__(self, folder_data="data", folder_simpan="cadangan"):
        self.data = folder_data
        self.simpan = folder_simpan
        os.makedirs(self.simpan, exist_ok=True)

    def buat(self) -> str:
        waktu = datetime.now().strftime("%Y%m%d_%H%M%S")
        nama = f"ranziz_cadangan_{waktu}"
        arsip = os.path.join(self.simpan, nama)
        if os.path.exists(self.data):
            shutil.make_archive(arsip, "zip", self.data)
            return f"✅ Cadangan jadi: {nama}.zip"
        return "⚠️ Belum ada data untuk dicadangkan"

    def daftar(self) -> str:
        daftar = [f for f in os.listdir(self.simpan) if f.endswith(".zip")]
        return "\n".join(daftar) if daftar else "Belum ada cadangan"
