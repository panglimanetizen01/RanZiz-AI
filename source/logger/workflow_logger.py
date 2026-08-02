"""
RanZiz AI Workflow Logger
Version 1.0
"""

from source.logger.logger import Logger


class WorkflowLogger:


    def __init__(self):

        self.logger = Logger()


    def started(
        self,
        workflow
    ):

        return self.logger.info(
            f"Workflow dimulai: {workflow}"
        )


    def finished(
        self,
        workflow
    ):

        return self.logger.info(
            f"Workflow selesai: {workflow}"
        )


    def failed(
        self,
        workflow,
        reason
    ):

        return self.logger.error(
            f"Workflow gagal: {workflow} | reason={reason}"
        )


    def all(self):

        return self.logger.all()
