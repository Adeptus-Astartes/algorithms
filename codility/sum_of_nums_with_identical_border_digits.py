input_data = [
    [405, 45, 300, 300, 300],
    [909, 33, 303, 3993, 959],
    [123, 405, 607],
    [505, 77, 707, 7997, 555, 909, 33, 303, 3993, 959],
    ]

def compute(data):

    # using temp to filter uniq items and keep only duplicates
    temp = {}
    output = {}

    for i in data:
        nums = [int(str(i)[0]), int(str(i)[-1])]

        # use first and last digit as Key
        key = ''.join(map(str,nums))

        if key in temp:
            if key in output:
                output[key] = output[key] + i
            else:
                output[key] = temp[key] + i
        else:
            temp[key] = i

    if not output:
        return -1
    
    result = 0

    # Find the item with the maximum value
    for i in output.values():
        if i > result:
            result = i
    return result

for i in input_data:
    print(compute(i))