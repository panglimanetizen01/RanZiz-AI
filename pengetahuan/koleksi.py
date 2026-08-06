"""Basis data pengetahuan khusus milik Bos"""

KOLEKSI = {
    "proyek": "RanZiz AI - sistem cerdas buatan sendiri, berjalan di Termux & siap VPS",
    "aturan_nama": "Selalu tulis nama persis: RanZiz AI",
    "bahasa": "Gunakan bahasa Indonesia gaul yang sopan, singkat dan padat",
    "keamanan": "Segala informasi rahasia tidak boleh disebarkan ke siapa pun"
}

def cari_isi(kata_kunci: str):
    kata_kunci = kata_kunci.lower()
    for judul, isi in KOLEKSI.items():
        if kata_kunci in judul.lower() or kata_kunci in isi.lower():
            return f"📚 Pengetahuan Khusus: {isi}"
    return None
