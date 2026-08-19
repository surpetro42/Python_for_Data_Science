ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# "Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello
# «name of your campus»"

ft_list[1] = "World!"
ft_tuple = ("Hello", "Armenia!")
ft_set.add("Yerevan!")
ft_set.remove("tutu!")
ft_dict["Hello"] = "42YErevan!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)



# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>