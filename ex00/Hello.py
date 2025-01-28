ft_list = ["Hello", "tata!"]    # Tableau classique
ft_tuple = ("Hello", "toto!")   # Non modifiable
ft_set = {"Hello", "tutu!"}     # Non ordonné
ft_dict = {"Hello": "titi!"}    # Clé : Valeur

ft_list[1] = "World!"

tuple_to_list = list(ft_tuple)
tuple_to_list[1] = "France!"
ft_tuple = tuple(tuple_to_list)

ft_set.remove("tutu!")
ft_set.add("Nice!")

ft_dict["Hello"] = "42Nice!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
