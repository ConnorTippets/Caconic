import gc

class Parser:
    def __init__(self, input):
        self.out = self.parse(input)
    
    def parse(self, input):
        parsed = []
        raw = input
        lines = raw.split('\n')
        for index, line in enumerate(lines):
            self.lineno = index+1
            lineparsed = self.parse_syntax(self.parse_comments(line))
            parsed.append(lineparsed)
        return parsed

    def parse_comments(self, line):
        _ = line.split("#")
        __ = line.partition("#")
        if len(_) > 1:
            return _[0]
        try:
            if __ == ('', '#', _[1]):
                return None
        except: pass
        return line

    def parse_syntax(self, line):
        if not line:
            return None
        parsing = line.split(" ")
        objects = []
        for a in gc.get_objects():
            try:
                a.__name__
            except: continue
            objects.append(a.__name__)
        #objects = [a.__name__ for a in gc.get_objects() if hasattr(a, '__name__')]
        if parsing[0] == "func":
            _ = f"def {parsing[1]}({parsing[2].replace(':', '')}):"
            return _
        for object in objects:
            if parsing[0] == object:
                _ = f"{parsing[1]} = {parsing[2]}"
                return _
        return line
