import os

filepath = "04_Arsitektur.md"  # Sesuaikan path file jika berada di folder lain

# Teks kelanjutan bagian 16.6 Alerting dan Bab 17 yang lengkap
tambahan_teks = """
### 16.6 Alerting (Lanjutan)

Sistem *alerting* otomatis dikonfigurasi untuk mendeteksi anomali dan masalah performa sebelum berdampak luas kepada pengguna. Peringatan akan dikirimkan ke tim pengembang atau operasional melalui saluran prioritas berdasarkan tingkat keparahannya (*severity level*).

Contoh kondisi yang memicu peringatan meliputi:

* **Latensi Tinggi**: Waktu respons API atau AI melebihi SLA yang ditentukan (Warning / Critical)
* **Peningkatan Error Rate**: Persentase *error* HTTP 5xx atau kegagalan plugin melonjak (Critical)
* **Kegagalan AI Provider**: Model AI utama gagal merespons dan mekanisme *fallback* aktif (Warning)
* **Lonjakan Penggunaan Memori**: Konsumsi RAM atau *Vector Store* melewati batas aman (Critical)
* **Crash Plugin Berulang**: Sebuah plugin mengalami *crash* atau *health check* gagal berkali-kali (Warning)
* **Antrean Pesan Menumpuk**: *Message Queue length* melebihi ambang batas kapasitas normal (Warning)

---

## 17. Penutup Arsitektur Sistem

Arsitektur sistem RanZiz AI dirancang dengan prinsip modularitas, pemisahan domain yang ketat (*domain separation*), serta kesiapan menghadapi skala enterprise. Dengan membagi sistem ke dalam berbagai lapisan (*presentation, gateway, application, domain, infrastructure*) serta mengadopsi pendekatan *model-agnostic* untuk kecerdasan buatan, platform ini mampu beradaptasi terhadap perubahan teknologi jangka panjang tanpa mengorbankan stabilitas dan keamanan. Dokumen `04_Arsitektur.md` ini menjadi landasan teknis utama bagi implementasi spesifikasi komponen, basis data, API, serta mesin AI selanjutnya.
"""

if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Menghapus sisa potongan teks terakhir jika ada, lalu menambahkan versi lengkapnya
    # Atau langsung append jika file memang berhenti di situ
    updated_content = content.strip() + "\n" + tambahan_teks
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Sukses! File 04_Arsitektur.md berhasil diperbarui.")
else:
    print(f"File {filepath} tidak ditemukan. Pastikan posisi terminal berada di folder yang benar.")
