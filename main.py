def get_denominator(file_name):
    try:
        with open(file_name, 'r') as f:
                denominator = int(f.read())
        try:
            5 % denominator
        except ZeroDivisionError:
            print('Ha-ha, we can`t divide by zero')
        return denominator
    except FileNotFoundError:
        print('Oops, file not found')
    except ValueError:
        print('Oops, it`s not a number in file')


def get_list_of_numbers(denominator):
    list_of_numbers = list(map(int, input().split()))
    list_of_numbers = list(filter(lambda x: x % denominator == 0, list_of_numbers))
    return list_of_numbers


def get_sum(list_of_numbers):
    sum_of_numbers = sum(list_of_numbers)
    return sum_of_numbers


def write_result (number, name_of_result_file):
    with open(name_of_result_file, 'w') as f:
        f.write(str(number))


write_result(get_sum(get_list_of_numbers((get_denominator('d.txt')))), 'result_file.txt')
