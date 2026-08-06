import os
from dotenv import load_dotenv

load_dotenv()

class PengaturanSistem:
    MODE = os.getenv("RANZIZ_MODE", "pengembangan")
    IZIN_DEBUG = os.getenv("RANZIZ_IZIN_DEBUG", "tidak")
    SIMPAN_RIWAYAT = os.getenv("RANZIZ_SIMPAN_RIWAYAT", "ya")
    KUNCI_DASAR = os.getenv("RANZIZ_KUNCI_DASAR", "ganti_dulu")
    BATAS_PANJANG_TEKS = 5000
    JUMLAH_HASIL_CARI_MAKS = 5
