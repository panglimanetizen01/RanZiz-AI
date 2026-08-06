from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
import hashlib

from ..planner import PlanObject
from ..capability import CapabilityDispatcher, CapabilityRequest

class AgentResult(BaseModel):
    """Hasil akhir pelaksanaan alur kerja oleh Agen"""
    id_rencana: str
    sukses: bool
    pesan_umum: str
    hasil_tugas: Dict[int, Dict[str, Any]] = Field(default_factory=dict)
    total_langkah_dijalankan: int = 0
    tanda_selesai: str = Field(..., description="Bukti pelaksanaan sah")

class BaseAgent(ABC):
    """Kelas dasar semua jenis Agen"""
    jenis: str = "dasar_agen"
    versi: str = "1.0.0"

    @abstractmethod
    def jalankan_rencana(self, rencana: PlanObject) -> AgentResult:
        """Setiap Agen wajib melaksanakan fungsi ini saja"""
        pass

    def buat_tanda_sah(self, isi: str) -> str:
        return hashlib.sha256(f"{isi}:{self.jenis}:RANZIZ_AGENT".encode()).hexdigest()[:32]
