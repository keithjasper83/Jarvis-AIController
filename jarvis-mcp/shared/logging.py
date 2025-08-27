import logging
import uuid
import json

class JsonLogger:
    def __init__(self, name="mcp"):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    def log(self, event, **kwargs):
        entry = {
            "event": event,
            "request_id": str(uuid.uuid4()),
            **kwargs
        }
        self.logger.info(json.dumps(entry))

logger = JsonLogger()
