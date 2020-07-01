pets=('birds,','snake','dog','turtle','cat','hamster')

pet_list_capitalize=[pet.capitalize() for pet in pets]
print(pet_list_capitalize)

pet_list_upper=[pet.upper() for pet in pets]
print(pet_list_upper)

prime_number=[2,3,5,7,11,13,17,19,23,29]
squared_primes=[x**2 for x in prime_number if x%10 == 3]
print(squared_primes)

def has_four_legs(pet):
    return pet in ('dog','cat','pig','turtle','hamster')

four_legged_pet=[pet for pet in pets if has_four_legs(pet)]
print(four_legged_pet)

numbers1=[1,2,3,4,5,6]
list1=[number*number for number in numbers1]

#set_comprehension
numbers=(1,34,5,8,10,12,3,90,70,70,90)
unique_number_set ={number for number in numbers if number%2 ==0 }
print(unique_number_set)

#dict_comprehension
words=('python','is','a','big','snake')
dict1={word:len(word) for word in words}
print(dict1)



