# Returns smallest integer greater than X, 
# the sum of whose digits is twice as big as the sum of digits N

input_data = [14,99]

def compute(X):
    def digit_sum(num):
        return sum(map(int, str(num)))

    target_sum = 2 * digit_sum(X)
    current_num = X + 1

    while digit_sum(current_num) != target_sum:
        current_num += 1

    return current_num

for i in input_data:
    print(compute(i))