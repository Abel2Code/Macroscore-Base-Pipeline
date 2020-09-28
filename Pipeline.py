from BaseModule import BaseModule
class Pipeline:
    def __init__(self, name, modules):
        self.name = name
        
        assert(all(isinstance(m, BaseModule) for m in modules))
        self.modules = modules

    def run(self):
        for module in self.modules:
            module.pollRunAndUpload()

            # TODO: Notify whoever needs the output file
