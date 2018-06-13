from octopus.api.engine import VMstate


class EthereumVMstate(VMstate):

    def __init__(self, gas=1000000):
        self.storage = {}
        self.memory = []

        self.stack = []
        self.ssa_stack = []
        self.symbolic_stack = []

        self.last_returned = []
        self.gas = gas
        self.pc = 0
        self.instr = None

        self.instructions_visited = []

    def details(self):

        return {'storage': self.storage,
                'memory': self.memory,
                'stack': self.stack,
                'ssa_stack': self.ssa_stack,
                'symbolic_stack': self.symbolic_stack,
                'last_returned': self.last_returned,
                'gas': self.gas,
                'pc': self.pc}

    def mem_extend(self, start, sz):

        if (start < 4096 and sz < 4096):

            if sz and start + sz > len(self.memory):

                n_append = start + sz - len(self.memory)

                while n_append > 0:
                    self.memory.append(0)
                    n_append -= 1

        else:
            raise Exception
