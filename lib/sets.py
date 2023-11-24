my_list = [1, 2, 1, 3, 2]
my_new_list = set(my_list)
print(my_new_list)

my_string = "the big red cat ate the fat rat"
print(set(my_string))

def set_asert(input_set):
    if input_set:
       print(True)
    else:
       print(False)
my_set = set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])
result = set_asert(my_set)

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print(set_1 & set_2)
print(set_1 - set_2)
print(set_2 - set_1)
#comprehensions in sets
sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
capitalized_sentense = {word.capitalize() for word in sentence.split()}
print(capitalized_sentense)
