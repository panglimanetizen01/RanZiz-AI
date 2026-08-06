# RanZiz AI - Intent ke Capability Mapper
# Versi: 1.0.2 | Diperiksa struktur data 100% benar

from typing import List, Dict, Tuple

INTENT_TO_CAPABILITY: Dict[str, List[str]] = {
    "chat_umum": ["ChatCapability"],
    "buat_kode": ["CodeCapability"],
    "perbaiki_kode": ["CodeCapability"],
    "jelaskan_kode": ["CodeCapability"],
    "buat_lirik": ["LyricCapability"],
    "buat_lagu": ["ComposerCapability", "AudioCapability"],
    "riset": ["ResearchCapability"],
    "rangkum": ["ResearchCapability"],
    "analisis": ["ResearchCapability"],
    "gambar": ["ImageGeneratorCapability"],
    "suara": ["VoiceSynthesisCapability"]
}

# Format pasti: Tuple(Daftar Kata Kunci, Nama Intent)
ATURAN_DETEKSI: List[Tuple[List[str], str]] = [
    (["buat kode", "buat program", "tolong kode", "fungsi", "python", "javascript", "html", "css", "bug", "error", "perbaiki kode", "tuliskan kode", "contoh kode"], "buat_kode"),
    (["lagu", "lirik", "nada", "iringan", "komposisi", "musik", "bikin lagu", "bikinin lagu", "bikin lirik"], "buat_lagu"),
    (["cari", "jelaskan", "apa itu", "bagaimana", "kenapa", "mengapa", "sejarah", "penjelasan", "rangkumkan", "ringkas", "analisis", "riset"], "riset"),
    (["hai", "halo", "apa kabar", "terima kasih", "makasih", "oke", "ya", "tidak", "siap", "mantap"], "chat_umum")
]
