"""
RanZiz AI Observability Service
Version 1.3
"""


from source.logging.diagnostic_report import DiagnosticReport
from source.logging.health_monitor import HealthMonitor
from source.logging.request_summary import RequestSummary
from source.logging.trace_analyzer import TraceAnalyzer
from source.logging.trace_storage import TraceStorage
from source.observability.diagnostic_engine import DiagnosticEngine


class ObservabilityService:



    def __init__(self):

        self.storage = TraceStorage()

        self.analyzer = TraceAnalyzer()

        self.summary = RequestSummary()

        self.report = DiagnosticReport()

        self.health = HealthMonitor()

        self.diagnostic = DiagnosticEngine()



    def process(

        self,

        context

    ):

        trace = context.get_trace()



        self.storage.save(

            context.get_id(),

            trace

        )



        analysis = self.analyzer.analyze(

            trace

        )



        summary = self.summary.build(

            analysis,

            trace

        )



        health = self.health.check(

            trace

        )



        diagnosis = self.diagnostic.analyze(

            trace

        )



        report = self.report.build(

            summary,

            diagnosis

        )



        return {


            "analysis": analysis,


            "summary": summary,


            "health": health,


            "report": report,


            "diagnosis": diagnosis

        }



    def __repr__(self):

        return "ObservabilityService()"