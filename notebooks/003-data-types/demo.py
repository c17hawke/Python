"""
Author: SUNNY BHAVEEN CHANDRA

For more information - 
- [1] Python notes-
    https://c17hawke.github.io/Python/

- [2] Python YouTube Playlist- 
    https://youtube.com/playlist?list=PLrdaCCBhU_hnxIzB7EJlY-pfYOMGRycAK

"""

# Data-types in Python

# | Category | Common Data Types        |
# |----------|--------------------------|
# | Text     | `str`                    |
# | Numeric  | `int`, `float`, `complex`|
# | Sequence | `list`, `tuple`,         |
# | Mapping  | `dict`                   |
# | Set      | `set`                    |
# | Boolean  | `bool`                   |
# | None     | `NoneType`               |

# Text     | `str` 

name = "Sunny"
print(name)
print(type(name))

sentence = "Sunny is a life long student"
print(sentence)
print(type(sentence))

sentence = 'single quote example'
print(sentence)
print(type(sentence))

character = "S"
print(character)
print(type(character))

x = "1234"
print(x)
print(type(x))

x = "12.34"
print(x)
print(type(x))

# | Numeric  | `int`

x = 1234
print(x)
print(type(x))

x = -1234
print(x)
print(type(x))

x = 0
print(x)
print(type(x))

# | Numeric  | `float`

x = 12.34
print(x)
print(type(x))

x = -12.34
print(x)
print(type(x))

x = 0.0
print(x)
print(type(x))

# | Numeric  | `complex`|

z = 1 + 2j
print(z)
print(type(z))
print(f"real part of {z} => {z.real}")
print(f"imaginary part of {z} => {z.imag}")

# | Sequence | `list`

x = [1,2,3,4,5,6,7,8,9,10]
print(x)
print(type(x))


# | Sequence | `tuple` |
x = (1,2,3,4,5,6,7,8,9,10)
print(x)
print(type(x))

# | Set      | `set` 
x = {1,2,3,4,5,6,7,8,9,10}
print(x)
print(type(x))

x = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,10}
print(x)
print(type(x))


# | Boolean  | `bool`                   |

x = True
print(x)
print(type(x))

x = False
print(x)
print(type(x))

# | None     | `NoneType`               |

x = None
print(x)
print(type(x))

# School records example

name_of_student = "Sunny"
print(name_of_student)
print(type(name_of_student))

roll_no = 12
print(roll_no)
print(type(roll_no))

percentage_of_marks = 75.2
print(percentage_of_marks)
print(type(percentage_of_marks))

student_1_data = {
    "name_of_student": "Sunny",
    "roll_no": 12,
    "percentage_of_marks": 75.2
}

print(student_1_data)
print(type(student_1_data))

list_of_subjects = [
    "English", 
    "Maths", 
    "Science", 
    "Social Science", 
    "Hindi"
    ]

print(list_of_subjects)
print(type(list_of_subjects))

passing_status = False
print(passing_status)
print(type(passing_status))

practical_marks_in_English = None
print(practical_marks_in_English)
print(type(practical_marks_in_English))

# Ecommerce or Amazon example

name_of_product = "Hands on Machine Learning"
cost_of_product = 3000
one_day_delivery = False
rating_of_product = 4.7
reviews_of_product = [
    "Book is good",
    "Book is average",
    "Book is excellent"
]

product_info = {
    "name_of_product": "Hands on Machine Learning",
    "cost_of_product": 3000,
    "one_day_delivery": False,
    "rating_of_product": 4.7,
    "reviews_of_product": [
                        "Book is good",
                        "Book is average",
                        "Book is excellent"
                    ]
}
