from .metric_producer_bindings import *
from os import getenv

class MetricProducer():
    def __init__(self):
        if not self._verify_environment():
            raise ValueError("Environment variables are not set")
        
        self._impl = MetricProducerBindings()

    def produce(self, application_name: str, metric_name: str) -> bool:
        return self._impl.produce(application_name, metric_name)

    def _verify_environment(self) -> bool:
        environment_variables: list[str] = [
            "BOOTSTRAP_SERVERS",
            "SECURITY_PROTOCOL",
            "SASL_MECHANISM",
            "SASL_PLAIN_USERNAME",
            "SASL_PLAIN_PASSWORD",
            "TOPIC_NAME"
        ]
        
        for variable in environment_variables:
            if not getenv(variable):
                return False
        
        