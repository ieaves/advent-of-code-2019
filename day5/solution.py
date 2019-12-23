def read_file(filename):
    with open(filename) as f:
        line = f.readline()

    program = [int(item) for item in line.split(',')]
    return program


class exit_code:
    types = {1, 2, 3, 4, 99}

    def __init__(self, type, value):
        assert type in self.types
        self.type = type
        self.value = value


class IntCode:
    skips = {1: 4,
             2: 4,
             3: 2,
             4: 2,
             99: 0}

    def __init__(self, instructions, input=1):
        self.original_instructions = instructions
        self.input = input

        self.instructions = self.original_instructions.copy()
        self.pointer = 0

    def reset(self):
        self.instructions = self.original_instructions.copy()
        self.pointer = 0

    @property
    def instruction(self):
        return self.instructions[self.pointer]

    @property
    def op(self):
        return self.instruction % 100

    @property
    def modes(self):
        instr = str(self.instruction).rjust(3, '0')
        modes = instr[0:-2].rjust(3, '0')[::-1]
        return modes

    def get_val(self, pointer, mode):
        if mode == '0':
            return self.instructions[self.instructions[pointer]]
        elif mode == '1':
            return self.instructions[pointer]
        else:
            raise Exception(f'Unknown mode, {mode}')

    def apply_instructions(self):
        code = self.apply_instruction()

        while not isinstance(code, exit_code):
            code = self.apply_instruction()

        return code.value

    def increment_pointer(self, op):
        self.pointer += self.skips[op]

    def apply_instruction(self):
        op, modes = self.op, self.modes
        #print(op, modes, self.instructions)
        if op == 99:
            return exit_code(99, self.instructions[0])

        if op in set([1, 2]):
            assert len(modes) == 3, self.modes

            val1 = self.get_val(self.pointer + 1, modes[0])
            val2 = self.get_val(self.pointer + 2, modes[1])
            val3 = self.instructions[self.pointer + 3]
            #print(val1, val2, val3, modes)

        if op == 1:
            self.instructions[val3] = val1 + val2
        elif op == 2:
            self.instructions[val3] = val1 * val2
        elif op == 3:
            idx = self.get_val(self.pointer + 1, '1')
            self.instructions[idx] = self.input
        elif op == 4:
            print(self.get_val(self.pointer + 1, '0'))
        else:
            raise Exception('Unknown op')

        self.increment_pointer(op)



test_set = [
    ([1, 0, 0, 0, 99], 2),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], 30),
    ([3, 0, 4, 0, 99], 1),
    ([1002, 4, 3, 4, 33], 1002),
    ([1101, 100, -1, 4, 0], 1101)
]

if __name__ == '__main__':
    day2_instructions = read_file('input_day2')
    day2_instructions[1] = 12
    day2_instructions[2] = 2
    test_set.append((day2_instructions, 3085697))

    for input, expected_result in test_set:
        result = IntCode(input).apply_instructions()
        assert result == expected_result, result
    test_instructions = [3, 0, 4, 0, 99]

    test_instructions = [1101, 100, -1, 4, 0]
    instructions = read_file('input')
    result = IntCode(instructions).apply_instructions()
    print(f'Output day 1: {result}')
