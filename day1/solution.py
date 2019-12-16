def read_file(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            res = int(line.strip())
            yield res


def required_fuel(weight):
    return max((weight // 3) - 2, 0)


# Part 1
def module_fuel_cost(module_weights):
    return sum(required_fuel(module_weight) for module_weight in module_weights)


# Part 2
def total_fuel_cost(weight):
    fuel_weight = required_fuel(weight)
    total_weight = fuel_weight
    while fuel_weight > 2:
        fuel_weight = required_fuel(fuel_weight)
        total_weight += fuel_weight
    return total_weight


def total_module_fuel_cost(module_weights):
    return sum(total_fuel_cost(module_weight) for module_weight in module_weights)


if __name__ == '__main__':
    assert module_fuel_cost([100756]) == 33583
    assert total_module_fuel_cost([100756]) == 50346

    input = [i for i in read_file('input')]
    p1_fuel_cost = module_fuel_cost(input)
    p2_fuel_cost = total_module_fuel_cost(input)
    print(f'Part 1: {p1_fuel_cost}')
    print(f'Part 2: {p2_fuel_cost}')
