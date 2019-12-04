def read_file(filename):
    with open(filename) as f:
        line = f.readline()

    program = [int(item) for item in line.split(',')]
    return program


def op_grabber(instructions):
    size = len(instructions)
    def inner(n):
        idx0 = 4 * n
        idx1 = idx0 + 4
        ret = instructions[idx0:idx1]
        if idx1 > size:
            ret += [None] * (4 - len(ret))
        return ret
    return inner


def op_applier(instructions, op_map):
    def inner(op):
        instruction = op[0]
        noun, verb, output = instructions[op[1]], instructions[op[2]], op[3]
        instructions[output] =  op_map[instruction](noun, verb)
    return inner


class IntCode:
    op_map = {1: lambda x, y: x + y,
              2: lambda x, y: x * y}

    halt_code = 99

    @classmethod
    def process_instructions(cls, instructions):
        noun, verb = instructions[1], instructions[2]
        op_grab = op_grabber(instructions)
        op_apply = op_applier(instructions, cls.op_map)
        pointer = 0
        op = op_grab(pointer)
        while op[0] != cls.halt_code:
            op_apply(op)
            pointer += 1
            op = op_grab(pointer)

        return instructions[0]


# part 2
def noun_verb_generator(min_val=0, max_val=99):
    from itertools import product
    vals = list(range(min_val, max_val + 1))
    for combination in product(vals, vals):
        yield combination


def program_search(instructions, target):
    for noun, verb in noun_verb_generator(0, 99):
        instrucs = instructions.copy()
        instrucs[1] = noun
        instrucs[2] = verb
        output = IntCode.process_instructions(instrucs)
        if output == target:
            break

    if output != target:
        raise Exception('Didnt find noun/verb combo')

    return noun, verb


if __name__ == '__main__':
    test_instructions = [1,0,0,0,99]
    result = IntCode.process_instructions(test_instructions)
    assert result == 2, result

    test_instructions = [1,1,1,4,99,5,6,0,99]
    result = IntCode.process_instructions(test_instructions)
    assert result == 30, result

    original_instructions = read_file('input')
    instructions = original_instructions.copy()
    instructions[1] = 12
    instructions[2] = 2
    result = IntCode.process_instructions(instructions)
    print(f'Part 1 output: {result}')

    noun, verb = program_search(original_instructions.copy(), 19690720)
    print(f'Part 2 output: noun = {noun}, verb = {verb}, output={100 * noun + verb}')
