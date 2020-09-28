from BaseModule import BaseModule

class ExampleModule(BaseModule):
    def __init__(self):
        super().__init__("Example Module")

    def run(self):
        prereqs = self.__load_prereq__()
        print(self.config)

    def __load_prereq__(self):
        pass
