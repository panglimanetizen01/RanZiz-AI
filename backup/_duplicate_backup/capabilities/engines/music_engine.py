from ..base_capability import BaseCapability, CapabilityRequest, CapabilityResponse
from ..capability_registry import CapabilityRegistry

class MusicEngine(BaseCapability):
    nama = "music_engine"
    versi = "1.0.0"

    def jalankan(self, permintaan: CapabilityRequest) -> CapabilityResponse:
        tujuan = permintaan.data_masukan.get("tujuan", "")
        hasil = f"Kerangka lagu untuk: {tujuan}"
        tanda = self.buat_tanda(hasil)
        
        return CapabilityResponse(
            sukses=True,
            pesan="Kemampuan musik diproses",
            data_hasil={"isi_kerangka": hasil},
            kode=200,
            tanda_verifikasi=tanda
        )

# Daftarkan otomatis saat dimuat
CapabilityRegistry.daftarkan(MusicEngine.nama, MusicEngine)
