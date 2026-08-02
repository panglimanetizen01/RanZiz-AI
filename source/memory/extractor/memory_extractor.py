from typing import ClassVar

"""
RanZiz AI Memory Extractor
Version 2.0
"""

import re


class MemoryExtractor:

    PATTERNS: ClassVar = [

        # Identitas
        (
            r"(?i)^nama saya (.+)$",
            "nama"
        ),

        (
            r"(?i)^nama aku (.+)$",
            "nama"
        ),

        (
            r"(?i)^saya bernama (.+)$",
            "nama"
        ),

        (
            r"(?i)^umur saya ([0-9]+)$",
            "umur"
        ),

        (
            r"(?i)^usia saya ([0-9]+)$",
            "umur"
        ),

        (
            r"(?i)^saya tinggal di (.+)$",
            "kota"
        ),

        (
            r"(?i)^asal saya dari (.+)$",
            "kota"
        ),

        # Preferensi
        (
            r"(?i)^hobi saya (.+)$",
            "hobi"
        ),

        (
            r"(?i)^warna favorit saya (.+)$",
            "warna_favorit"
        ),

        (
            r"(?i)^makanan favorit saya (.+)$",
            "makanan_favorit"
        ),

        (
            r"(?i)^minuman favorit saya (.+)$",
            "minuman_favorit"
        ),

        (
            r"(?i)^genre favorit saya (.+)$",
            "favorite_genre"
        ),

        (
            r"(?i)^saya suka (.+)$",
            "favorite"
        ),

        # Pekerjaan
        (
            r"(?i)^pekerjaan saya (.+)$",
            "pekerjaan"
        ),

        (
            r"(?i)^saya bekerja sebagai (.+)$",
            "pekerjaan"
        ),

    ]

    def clean(

        self,

        value

    ):

        value = value.strip()

        value = re.sub(
            r"\s+",
            " ",
            value
        )

        return value

    def extract(

        self,

        message

    ):

        if not message:

            return None

        text = message.strip()

        if len(text) > 300:

            # Jangan simpan dokumen panjang,
            # kode program, skripsi, dll.
            return None

        for pattern, key in self.PATTERNS:

            match = re.match(

                pattern,

                text

            )

            if match:

                value = self.clean(

                    match.group(1)

                )

                if not value:

                    return None

                return {

                    "key": key,

                    "value": value

                }

        return None

    def __repr__(self):

        return "MemoryExtractor()"