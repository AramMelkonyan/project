from solution import Solution


class Evaluator(Solution):
    def __init__(self, out):
        super().__init__()
        self.out = out

    def test(self, args):
        # parse arguments string as needed
        args = args.split()
        return self.sum(eval(args[0]), eval(args[1]))
 
    def evaluate(self, args):
        result = self.test(args)
        self.out.write(str(result))
        self.out.write('\n')
