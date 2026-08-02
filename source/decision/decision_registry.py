"""
RanZiz AI Decision Registry
Version 1.0
"""


class DecisionRegistry:


    def __init__(self):

        self.rules = []



    def register(

        self,

        rule

    ):

        self.rules.append(
            rule
        )



    def all(self):

        return self.rules



    def clear(self):

        self.rules.clear()