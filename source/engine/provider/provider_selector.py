# RanZiz AI - Provider Selector
# Versi: 1.0.0 | Tidak ada hardcode, berbasis aturan

from typing import Dict, List, Optional

CAPABILITY_TO_PROVIDER: Dict[str, Dict[str, List[str]]] = {
    "ChatCapability": {
        "utama": ["gemini"],
        "cadangan": ["claude", "deepseek"]
    },
    "CodeCapability": {
        "utama": ["deepseek"],
        "cadangan": ["gemini", "claude"]
    },
    "LyricCapability": {
        "utama": ["gemini"],
        "cadangan": ["claude"]
    },
    "ComposerCapability": {
        "utama": ["gemini"],
        "cadangan": ["claude"]
    },
    "AudioCapability": {
        "utama": ["gemini"],
        "cadangan": []
    },
    "ResearchCapability": {
        "utama": ["claude"],
        "cadangan": ["gemini", "deepseek"]
    }
}

class ProviderSelector:
    @staticmethod
    def pilih(capability_nama: str) -> Optional[List[str]]:
        """Kembalikan daftar provider urutan prioritas untuk kemampuan tertentu"""
        aturan = CAPABILITY_TO_PROVIDER.get(capability_nama)
        if not aturan:
            return CAPABILITY_TO_PROVIDER.get("ChatCapability", {}).get("utama", [])
        return aturan.get("utama", []) + aturan.get("cadangan", [])
