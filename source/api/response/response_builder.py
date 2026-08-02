"""
RanZiz AI Response Builder
Version 1.0
"""


class ResponseBuilder:


    def success(

        self,

        data

    ):

        return {

            "success": True,

            "data": data

        }



    def error(

        self,

        message

    ):

        return {

            "success": False,

            "error": message

        }



    def __repr__(self):

        return "ResponseBuilder()"