# La comprehension de liste est une manière concise d'écrire
# une boucle for qui remplit une liste

def ft_filter(func_to_apply, list_of_inputs):

    '''
    Custom filter function that filters elements of a list based
    on the function_to_apply
    :param function_to_apply: Function that will be applied
    to each element of the list
    :param list_of_inputs: List of elements that will be filtered
    :return: List of elements that satisfy the condition
    '''

    if func_to_apply is None:
        # Comprension de liste qui retourne les elements True
        return [elements for elements in list_of_inputs if elements]
    return [elements for elements in list_of_inputs if func_to_apply(elements)]

# def main():

# 	# Built-in filter
# 	print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
#   # Output: [2, 4, 6]
# 	# Custom ft_filter
# 	print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
#   # Output: [2, 4, 6]

# 	# Built-in filter with None as the function
# 	print(list(filter(None, [0, 1, "", "Hello", None, False, True])))
#   # Output: [1, 'Hello', True]
# 	# Custom ft_filter with None as the function
# 	print(list(ft_filter(None, [0, 1, "", "Hello", None, False, True])))
#   # Output: [1, 'Hello', True]

# 	# Built-in filter
# 	print(list(filter(lambda x: x > 10, [1, 2, 3, 4, 5])))  # Output: []
# 	# Custom ft_filter
# 	print(list(ft_filter(lambda x: x > 10, [1, 2, 3, 4, 5])))  # Output: []

# if __name__ == "__main__":
# 	main()
