class Interpreter:
    def __init__(self, input):
        self.execute(input)

    def execute(self, input):
        exec(input)
