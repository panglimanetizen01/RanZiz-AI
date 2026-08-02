"""
RanZiz AI Memory Gateway
Version 7.0
"""

from source.memory.decision.decision_learning import DecisionLearning
from source.memory.decision.memory_decision import MemoryDecision
from source.memory.episode.episode_manager import EpisodeManager
from source.memory.episode.episode_recall import EpisodeRecall
from source.memory.importance.memory_importance import MemoryImportance
from source.memory.integration.memory_learning_adapter import MemoryLearningAdapter
from source.memory.integration.memory_recall_adapter import MemoryRecallAdapter
from source.memory.manager.memory_manager import MemoryManager
from source.memory.retrieval.memory_retrieval_pipeline import MemoryRetrievalPipeline


class MemoryGateway:


    def __init__(self):

        self.manager = MemoryManager()

        self.learning = MemoryLearningAdapter()

        self.recall = MemoryRecallAdapter()

        self.retrieval = MemoryRetrievalPipeline()

        self.episodes = EpisodeManager()

        self.episode_recall = EpisodeRecall()

        self.importance = MemoryImportance()

        self.decision = MemoryDecision()

        self.decision_learning = DecisionLearning()



    # ==============================
    # Decision
    # ==============================

    def decide(

        self,

        message

    ):

        return self.decision.decide(

            message

        )



    def learn_decision(

        self,

        decision

    ):

        return self.decision_learning.learn(

            decision

        )



    def decision_pattern(self):

        return self.decision_learning.patterns()



    # ==============================
    # Semantic Learning
    # ==============================

    def learn(

        self,

        message

    ):

        return self.learning.learn(

            message

        )



    # ==============================
    # Semantic Retrieval
    # ==============================

    def retrieve(

        self,

        message

    ):

        return self.retrieval.retrieve(

            message

        )



    # ==============================
    # Profile
    # ==============================

    def profile(self):

        return self.manager.ask(

            "Ceritakan profil saya"

        )


    def about_user(self):

        return self.profile()



    # ==============================
    # Importance
    # ==============================

    def importance_score(

        self,

        key

    ):

        memories = self.manager.all()

        memory = memories.get(

            key

        )

        return self.importance.calculate(

            memory

        )



    def rank_memory(self):

        return self.importance.rank(

            self.manager.all()

        )



    # ==============================
    # Episode
    # ==============================

    def remember(

        self,

        event,

        category="conversation"

    ):

        return self.episodes.remember(

            event,

            category

        )



    def recent(

        self,

        limit=5

    ):

        return self.episodes.recent(

            limit

        )



    def search_episode(

        self,

        keyword

    ):

        return self.episodes.find(

            keyword

        )



    def episode_summary(self):

        return self.episodes.summary()



    # ==============================
    # Episode Recall
    # ==============================

    def recall_episode(

        self,

        message

    ):

        return self.episode_recall.recall(

            message

        )



    def search_episode_memory(

        self,

        keyword

    ):

        return self.episode_recall.search(

            keyword

        )



    # ==============================
    # Direct Manager
    # ==============================

    def save(

        self,

        key,

        value

    ):

        return self.manager.save(

            key,

            value

        )



    def get(

        self,

        key,

        default=None

    ):

        return self.manager.get(

            key,

            default

        )



    def ask(

        self,

        message

    ):

        return self.manager.ask(

            message

        )



    def all(self):

        return self.manager.all()



    def __repr__(self):

        return "MemoryGateway(v7.0)"