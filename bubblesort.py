
full_input = input()
full_input = list(full_input)


def bubblesort(input_list):
    while True:
        is_changed = 0 
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                is_changed = 1
        if is_changed == 0:
            return input_list

print(bubblesort(full_input))