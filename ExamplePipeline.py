from module1.ExampleModule import ExampleModule

from Pipeline import Pipeline
if __name__ == "__main__":
    modules = [ExampleModule()]
    pipeline = Pipeline("Abel's Example", modules)
    pipeline.run()
