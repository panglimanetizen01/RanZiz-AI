# RanZiz AI - Intent Analyzer
# Versi: 1.1.1 | Logika pengecekan disesuaikan sempurna

from typing import Dict, Any, List
from source.capability.selector.intent_mapper import INTENT_TO_CAPABILITY, ATURAN_DETEKSI

class IntentAnalyzer:
    @staticmethod
    def analisis(pesan: str) -> Dict[str, Any]:
        pesan = pesan.lower().strip()
        intent_terpilih = "chat_umum"

        # Cek satu per satu aturan
        for daftar_kata, nama_intent in ATURAN_DETEKSI:
            for kata in daftar_kata:
                if kata in pesan:
                    intent_terpilih = nama_intent
                    break
            if intent_terpilih != "chat_umum":
                break

        return {
            "intent": intent_terpilih,
            "keyakinan": 1.0 if intent_terpilih != "chat_umum" else 0.7,
            "kemampuan_dipilih": INTENT_TO_CAPABILITY.get(intent_terpilih, ["ChatCapability"])
        }
