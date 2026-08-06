# RanZiz AI - Core Brain
# Versi: 1.2.0 | Alur disambung penuh & keluaran terstandar
# Aturan: Selalu kembalikan teks bersih, tidak ada data mentah

from typing import Dict, Any
from source.decision.intent_analyzer import IntentAnalyzer
from source.capability.service.capability_service import CapabilityService
from source.engine.provider.provider_selector import ProviderSelector

class Brain:
    def __init__(self):
        self.capability_svc = CapabilityService()
        self.provider_selector = ProviderSelector()

    def proses(self, pesan_pengguna: str) -> str:
        """
        Alur proses penuh yang terstandar:
        1. Terima pesan
        2. Analisis maksud
        3. Pilih kemampuan
        4. Pilih penyedia layanan
        5. Hasilkan jawaban akhir berupa teks
        """
        try:
            # Langkah 1 & 2: Analisis maksud
            hasil_analisis = IntentAnalyzer.analisis(pesan_pengguna)
            intent = hasil_analisis["intent"]
            daftar_kemampuan = hasil_analisis["kemampuan_dipilih"]

            # Langkah 3 & 4: Susun ringkasan keputusan
            ringkasan = f"✅ Keputusan RanZiz AI:\n"
            ringkasan += f"🎯 Maksud terdeteksi: {intent}\n"
            ringkasan += f"🛠️ Kemampuan terpilih: {', '.join(daftar_kemampuan)}\n"
            ringkasan += f"🔌 Urutan Penyedia: "

            daftar_provider_terpilih = []
            for nama_cap in daftar_kemampuan:
                urut_provider = self.provider_selector.pilih(nama_cap)
                daftar_provider_terpilih.extend(urut_provider)
            
            # Hapus nama ganda
            daftar_unik = list(dict.fromkeys(daftar_provider_terpilih))
            ringkasan += f"{', '.join(daftar_unik)}\n\n"
            ringkasan += "🧠 Sistem siap memproses permintaan sesuai aturan yang berlaku."

            # Langkah 5: Pastikan selalu mengembalikan teks
            return ringkasan.strip()

        except Exception as e:
            # Tangani kesalahan agar tidak rusak
            return f"⚠️ Peringatan Sistem: Terjadi pengecekan ulang - {str(e)}"

# Inisialisasi satu kali untuk pemakaian umum
otak = Brain()
