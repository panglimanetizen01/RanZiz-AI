# 11_Capability_System.md
**Versi Dokumen:** 1.0.0
**Status:** Final Sesuai Konsep
**Sesuai:** Visi & Filosofi RanZiz AI

Capability adalah kemampuan spesifik yang dimiliki RanZiz AI untuk menyelesaikan suatu pekerjaan. Ibaratnya, kalau Brain adalah otaknya, maka capability adalah "alat" atau "keahlian" yang dipilih otak untuk menyelesaikan tugas tertentu.

Misalnya pengguna berkata:
> "Buat lagu pop tentang hujan."

Brain tidak langsung membuat lagu. Alurnya idealnya seperti ini:
User → Brain → Decision Engine → Capability Selection → Task Executor → Hasil

Jadi capability adalah daftar kemampuan yang dipilih sesuai kebutuhan.

## Capability Terdaftar
### 1. Code Engine
- Buat kode, perbaiki bug, rapikan, jelaskan
### 2. Research Engine
- Riset, analisis, rangkum, jawab berbasis data
### 3. Lyric Engine
- Tulis lirik lagu
### 4. Composer
- Tentukan struktur, susun bagian lagu
### 5. Audio Engine
- Instruksi produksi, aransemen, pengaturan suara
### 6. Image Engine
- Hasilkan & proses gambar

## Kenapa Dipisah?
Hindari tumpukan `if-else` di Brain. Tambah fitur tak rusak yang lama.

## Beda Agent vs Capability
- **Agent**: Pengarah & perencana tugas
- **Capability**: Pelaksana teknis tugas

## Rencana Pengembangan
Siap tambah: Chat, Visi, Suara, Terjemah, Dokumen, Pencarian, Browser, Memori, Perencana, Otomatisasi.
