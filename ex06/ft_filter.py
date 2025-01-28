def ft_filter(function_to_apply, list_of_inputs):
    final_list = []
    for element in list_of_inputs:
        if function_to_apply(element) == True:
            final_list.insert(element)
    print(final_list)