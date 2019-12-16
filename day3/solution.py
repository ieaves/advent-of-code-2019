def read_input(file):
    with open(file) as f:
        ret = f.readlines()

    return ';'.join(ret).strip()

def load_instruction_string(input, delim = ';'):
    instructions = [[(instr[0], int(instr[1:])) for instr in instruction_set.split(',')]
                    for instruction_set in input.split(delim)]
    return instructions

instruction_mapper = {
    'R': lambda x, y, num: [(new_coord, y) for new_coord in range(x + 1, x + num + 1)],
    'L': lambda x, y, num: [(new_coord, y) for new_coord in range(x - 1, x - num - 1, -1)],
    'D': lambda x, y, num: [(x, new_coord) for new_coord in range(y - 1, y - num - 1, -1)],
    'U': lambda x, y, num: [(x, new_coord) for new_coord in range(y + 1, y + num + 1)],
}

def process_instruction(instruction, coords):
    x, y = coords
    dir, num = instruction
    return instruction_mapper[dir](x, y, num)


def compute_wire_locations(instructions):
    coordinate = (0, 0) # left/right, up/down
    wire_locations = []
    for instruction in instructions:
        new_wire = process_instruction(instruction, coordinate)
        coordinate = new_wire[-1]
        for wire in new_wire:
            yield wire


def manhattan_distance(coord1, coord2):
    return sum(abs(a - b) for a, b in zip(coord1, coord2))


def closest_distance_intersection(instruction1, instruction2):
    wire_loc1 = compute_wire_locations(instruction1)
    wire_loc2 = compute_wire_locations(instruction2)
    intersections = set(wire_loc2)  & set(wire_loc1)
    distances = [manhattan_distance((0, 0), coord) for coord in intersections]
    return min(distances)


def closest_timing_intersection(instruction1, instruction2):
    wire_loc1 = list(compute_wire_locations(instruction1))
    wire_loc2 = list(compute_wire_locations(instruction2))
    intersections = set(wire_loc2)  & set(wire_loc1)
    timings = [wire_loc1.index(coord) + wire_loc2.index(coord) + 2 for coord in intersections]
    return min(timings)


if __name__ == '__main__':
    test_input = 'R8,U5,L5,D3;U7,R6,D4,L4'
    instructions = load_instruction_string(test_input)
    closest = closest_distance_intersection(*instructions)
    assert closest == 6, closest

    test_input = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51;U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    instructions = load_instruction_string(test_input)
    closest = closest_distance_intersection(*instructions)
    assert closest == 135, closest

    test_input = 'R75,D30,R83,U83,L12,D49,R71,U7,L72;U62,R66,U55,R34,D71,R55,D58,R83'
    instructions = load_instruction_string(test_input)
    closest = closest_distance_intersection(*instructions)
    assert closest == 159, closest

    instructions = load_instruction_string(read_input('input'))
    closest = closest_distance_intersection(*instructions)
    print(f'Part 1: {closest}')

    #  Part 2

    test_input = 'R8,U5,L5,D3;U7,R6,D4,L4'
    instructions = load_instruction_string(test_input)
    closest = closest_timing_intersection(*instructions)
    assert closest == 30, closest

    test_input = 'R75,D30,R83,U83,L12,D49,R71,U7,L72;U62,R66,U55,R34,D71,R55,D58,R83'
    instructions = load_instruction_string(test_input)
    closest = closest_timing_intersection(*instructions)
    assert closest == 610, closest

    test_input = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51;U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    instructions = load_instruction_string(test_input)
    closest = closest_timing_intersection(*instructions)
    assert closest == 410, closest

    instructions = load_instruction_string(read_input('input'))
    closest = closest_timing_intersection(*instructions)
    print(f'Part 2: {closest}')
