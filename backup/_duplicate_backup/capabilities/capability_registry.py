from typing import Dict, Type, Optional
from .base_capability import BaseCapability, CapabilityRequest, CapabilityResponse

class CapabilityRegistry:
    """Satu-satunya daftar resmi semua kemampuan"""
    _daftar: Dict[str, Type[BaseCapability]] = {}

    @classmethod
    def daftarkan(cls, nama: str, kelas_kemampuan: Type[BaseCapability]):
        """Daftarkan kemampuan baru, cegah nama bentrok"""
        nama = nama.lower().strip()
        if nama in cls._daftar:
            raise ValueError(f"Kemampuan '{nama}' sudah terdaftar! Tidak boleh ganda.")
        cls._daftar[nama] = kelas_kemampuan

    @classmethod
    def dapatkan(cls, nama: str) -> Optional[Type[BaseCapability]]:
        """Ambil kemampuan terdaftar saja"""
        return cls._daftar.get(nama.lower().strip())

    @classmethod
    def daftar_semua(cls) -> list[str]:
        return list(cls._daftar.keys())

class CapabilityDispatcher:
    """Satu-satunya gerbang resmi untuk menjalankan kemampuan"""

    @staticmethod
    def kirim(permintaan: CapabilityRequest) -> CapabilityResponse:
        # Langkah keamanan dasar
        kelas = CapabilityRegistry.dapatkan(permintaan.nama_kemampuan)
        if not kelas:
            return CapabilityResponse(
                sukses=False,
                pesan=f"Kemampuan '{permintaan.nama_kemampuan}' tidak ditemukan",
                data_hasil={},
                kode=404,
                tanda_verifikasi=""
            )

        try:
            instansi = kelas()
            return instansi.jalankan(permintaan)
        except Exception as e:
            return CapabilityResponse(
                sukses=False,
                pesan=f"Kesalahan eksekusi: {str(e)[:200]}",
                data_hasil={},
                kode=500,
                tanda_verifikasi=""
            )
