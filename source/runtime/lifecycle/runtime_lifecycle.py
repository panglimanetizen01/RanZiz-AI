"""
RanZiz AI Runtime Lifecycle
Version 1.0
"""


class RuntimeLifecycle:


    def __init__(

        self,

        runtime_manager

    ):

        self.manager = runtime_manager

        self.status = "STOPPED"



    def start(

        self,

        container

    ):

        self.manager.register(

            container

        )

        self.status = "RUNNING"

        return self.status



    def stop(

        self

    ):

        self.manager.clear()

        self.status = "STOPPED"

        return self.status



    def restart(

        self,

        container

    ):

        self.stop()

        return self.start(

            container

        )



    def state(

        self

    ):

        return self.status