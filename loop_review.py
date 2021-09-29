
fruit = ["apple", ["mango" , "durian" ] ]
        #   0                1


#
# my_index = 0 #starting index
# while (my_index < len(fruit)): #or you can use len of list as :   while (my_index < len(fruit):
#     print(fruit[my_index]) #print the fruit name at my_index
#             #fruit[1]
#     small_list_index = 0
#     while (small_list_index < len(fruit[1])):
#         print( fruit [1] [small_list_index] )
#         small_list_index +=1
#     my_index+=1 #increment my_index by 1 # my_index = my_index + 1
#     #codes here
#     #code here
# for item in fruit:
#     print(item)
#     print(type(item))
#     if isinstance(item, list): #check if the item is an Object list
#         for small_item in item:
#             print(small_item)
#     if isinstance(item, str):
#         print("this item is a string")

Ana = {'English':75,       'Maths':95,       'Science':82,       'Computer':94}
        #0                      1               2                   3
#variable dictionary
Belle = {'English':80,       'Maths':90,       'Science':70,       'Computer':65}
            #0                  1                   2               3
#dictionary variable
my_dictionary = {   #key   :  value (as dictionary)
    'Ana' : {'English':75,       'Maths':95,       'Science':82,       'Computer':94},
    'Belle' : {'English':80,       'Maths':90,       'Science':70,       'Computer':65},
    'Clara' : {'English':60,       'Maths':80,       'Science':65,       'Computer':73}
    }
#
#index = 0
#while index < len(Ana):
    #print(Ana)
for keys, value in my_dictionary.items(): #this is the for loop of big dictionary
    print (f"value of keys : {keys}")
    sum = 0
    for small_key, small_value in value.items():
        print(f"value:  {small_value}")
        sum+=small_value
    print(f"sum of {keys} is {sum}")