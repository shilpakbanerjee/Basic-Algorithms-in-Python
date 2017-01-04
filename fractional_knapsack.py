# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_per_unit = [values[item]/weights[item] for item in range(len(weights))]
    
    while (capacity > 0) and (len(weights) > 0):
        item = value_per_unit.index(max(value_per_unit))
        if weights[item] < capacity:
            value = value + weights[item] * value_per_unit[item]
            capacity = capacity - weights[item]
        else:
            value = value + capacity * value_per_unit[item]
            capacity = 0
        del weights[item]
        del values[item]
        del value_per_unit[item]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
