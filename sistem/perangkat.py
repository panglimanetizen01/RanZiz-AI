"""Kendali dasar perangkat Termux/Android"""
import subprocess
import shutil

class KendaliPerangkat:
    @staticmethod
    def jalankan_perintah(perintah: str) -> str:
        alat = perintah.split()[0]
        if not shutil.which(alat):
            return f"❌ Tidak ditemukan: {alat}"
        try:
            hasil = subprocess.run(
                perintah, shell=True, capture_output=True,
                text=True, timeout=15
            )
            keluar = hasil.stdout.strip() or hasil.stderr.strip()
            return keluar[:300] + ("..." if len(keluar) > 300 else "")
        except subprocess.TimeoutExpired:
            return "⏱️ Terlalu lama"
        except Exception as e:
            return f"❌ Gagal: {str(e)}"
