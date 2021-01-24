import json
import functools

class BaseModule:
    def __init__(self, name, config_path='./module1/config.json'):
        self.name = name
        with open(config_path) as f:
            self.config = json.load(f)

    # Should Update Results to location specified on CONFIG
    def run(self):
        pass
