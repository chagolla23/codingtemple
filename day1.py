# Datatypes

# Strings
my_string = "Hello world!"
my_string = 'Hello world!'
# my_string = "Hello world!' # ILLEGAL

my_string = "What's up"
# my_string = 'What's up' # ILLEGAL
my_string = 'he said "hello"'
my_string = 'he said, "what\'s up?"'
my_string = "he said, \"what's up?\""

print(my_string)
print(type(my_string))


# Intergers
my_int = 12
print(type(my_int))

# Floats <-- Doubles  Decimal Numbers!
my_float = 12.
print(type(my_float))


print(my_int*my_float) # type float
print(my_int*my_int)   # type int

print(type(6/6)) # Divide you always get a float

print(5/2)

# Floor division ... Interger division
print(5//2) # integer

# Modulo % Remainder of Division
print(5%2) #integer if you start with 2 ints
print(6%2==0)

# Booleans <-- Floats
my_bool = True
my_bool = False
print(my_bool)
# Boolean expressions
# == < > <= >= != .. link together with and/or in keyword
print(not 5!=4)
print(5>=5)

# 
# [] brackets/square brackets
# {} braces /curly brackets
# () para
# ! bang, not


# Lists
my_list = [1,2,3]

foods = ["pizza","tacos","dumsum","sushi"]
print(foods[1])

print(type(foods))
print(type(foods[1]))
print(foods[1].upper())


my_list = [1,2,3,[["Jim","Jack","Johnny","Jose"],"a","b","c"],4]

["a","b","c"][1]

print(
    my_list[3][0][2]
)

# list[index]

# Dictionaries!!!!!!!
my_dict = {"Key":"Value"}

vanessa = {
    "name":"Vanessa",
    "age":28,
    "weight":72.8,
    "foods":["ice cream", "pizza", "noodles"],
    "ice_cream":{
        "vanilla":True,
        "chocolate":True,
        "strawberry":True
    }
}

print(
    vanessa["ice_cream"]["chocolate"]
)
if  vanessa["ice_cream"]["chocolate"]:
    print("Vanessa Shove your face with this carton of Death by Chocolate!")


# Tuples immutable lists

# Sets Hash Tables



my_int = 5
my_string = "5"

print(my_string+str(my_int))

# Casting to covert datatype:
# bool() list() int() float() str() dict() ... more

print(
    bool(' ')
)