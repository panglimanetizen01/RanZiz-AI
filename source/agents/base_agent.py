"""
RanZiz AI Base Agent
Version 1.0
"""

from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def can_handle(self, message):
        pass

    @abstractmethod
    def execute(self, message):
        pass