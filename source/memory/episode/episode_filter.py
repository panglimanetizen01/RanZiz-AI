from typing import ClassVar

"""
RanZiz AI Episode Filter
Version 1.0
"""


class EpisodeFilter:


    IMPORTANT_WORDS: ClassVar = [

        "buat",
        "buatkan",
        "lanjutkan",
        "selesai",
        "berhasil",
        "gagal",
        "error",
        "bug",
        "project",
        "ranziz",
        "integrasi",
        "update",
        "ubah",
        "tambah",
        "hapus"

    ]


    def should_record(

        self,

        message

    ):

        text = message.lower()


        for word in self.IMPORTANT_WORDS:

            if word in text:

                return True


        return False



    def category(

        self,

        message

    ):

        text = message.lower()


        if "error" in text or "bug" in text:

            return "problem"


        if "project" in text or "ranziz" in text:

            return "project"


        if "buat" in text or "buatkan" in text:

            return "creation"


        return "conversation"



    def __repr__(self):

        return "EpisodeFilter()"