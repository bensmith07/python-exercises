students_lst = [                                                             #
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# 1. How many students are there?
#    ANSWER: 14

n_students = len(students_lst)

# 2. How many students prefer light coffee? 
#    ANSWER: 3

n_prefer_light = 0
for student in students_lst:
    if student['coffee_preference'] == 'light':
        n_prefer_light += 1 

# 2a. For each type of coffee roast?
#     ANSWER: 3 light, 6 medium, 5 dark

pref_counts = [[],[]]
for student in students_lst:
    if student['coffee_preference'] not in pref_counts[0]:
        pref_counts[0].append(student['coffee_preference'])
        pref_counts[1].append(1)
    else:
        pref_counts[1][pref_counts[0].index(student['coffee_preference'])] += 1


# 3. How many [of each type of pet] are there?
#    ANSWER: 4 horses, 11 cats, 3 dogs
 
species_counts = [[],[]]
for student in students_lst:
    for pet in student['pets']:
        if pet['species'] not in species_counts[0]:
            species_counts[0].append(pet['species'])
            species_counts[1].append(1)
        else:
            species_counts[1][species_counts[0].index(pet['species'])] += 1

# 4. How many grades does each student have? 
#    ANSWER: all have 4 grades

grade_counts = [[],[]]
for student in students_lst:
    grade_counts[0].append(student['id'])
    grade_counts[1].append(len(student['grades'])) 
 
# 4a. Do they all have the same number of grades?
#     ANSWER: yes

same_num_grades = len(set(grade_counts[1])) == 1
# result = True

# 5. What is each student's grade average?

grade_avgs = [[],[]]
for student in students_lst:
    grade_avgs[0].append(student['id'])
    grade_avgs[1].append(sum(student['grades']) / len(student['grades']))

# 6. How many pets does each student have?

pet_counts = [[],[]]
for student in students_lst:
    pet_counts[0].append(student['id'])
    pet_counts[1].append(0)
    for pet in student['pets']:
        pet_counts[1][pet_counts[0].index(student['id'])] += 1

# 7. How many students are in web development? 
#    ANSWER: 7

n_webdev_students = 0
for student in students_lst:
    if student['course'] == 'web development':
        n_webdev_students += 1

# 7a. How many students are in data science?
#     ANSWER: 7

n_ds_students = 0
for student in students_lst:
    if student['course'] == 'data science':
        n_ds_students += 1

# 8. What is the average number of pets for students in web development?
#    ANSWER: 1.3

pet_count_lst = []
for student in students_lst:
    if student['course'] == 'web development':
        pet_count = 0
        for pet in student['pets']:
            pet_count += 1
        pet_count_lst.append(pet_count)

avg_pets = sum(pet_count_lst) / len(pet_count_lst)

# 9. What is the average pet age for students in data science?
#    ANSWER: 5.4

pet_age_lst = []
for student in students_lst:
    if student['course'] == 'data science':
        for pet in student['pets']:
            pet_age_lst.append(pet['age'])
avg_pet_age = sum(pet_age_lst) / len(pet_age_lst)

# 10. What is most frequent coffee preference for data science students?
#     ANSWER: medium

pref_counts = [[],[]]
for student in students_lst:
    if student['course'] == 'data science':
        if student['coffee_preference'] not in pref_counts[0]:
            pref_counts[0].append(student['coffee_preference'])
            pref_counts[1].append(1)
        else:
            pref_counts[1][pref_counts[0].index(student['coffee_preference'])] += 1

ds_best_coffee = []
for idx in range(len(pref_counts[1])):
    if pref_counts[1][idx] == max(pref_counts[1]):
        ds_best_coffee.append(pref_counts[0][idx])



# 11. What is the least frequent coffee preference 
#     for web development students?
#     ANSWER: dark & medium

pref_counts = [[],[]]
for student in students_lst:
    if student['course'] == 'web development':
        if student['coffee_preference'] not in pref_counts[0]:
            pref_counts[0].append(student['coffee_preference'])
            pref_counts[1].append(1)
        else:
            pref_counts[1][pref_counts[0].index(student['coffee_preference'])] += 1

webdev_worst_coffee = []
for idx in range(len(pref_counts[1])):
    if pref_counts[1][idx] == min(pref_counts[1]):
        webdev_worst_coffee.append(pref_counts[0][idx])

# 12. What is the average grade for students with at least 2 pets?
#     ANSWER: 83.8

grade_lst = []

for student in students_lst:

    pet_count = 0
    for pet in student['pets']:
        pet_count += 1

    if pet_count >= 2:
        
        for grade in student['grades']:
            grade_lst.append(grade)

two_pet_avg_grade = sum(grade_lst) / len(grade_lst)

# 13. How many students have 3 pets?
#     ANSWER: 1

three_pet_students_count = 0
for student in students_lst:
    if len(student['pets']) == 3:
        three_pet_students_count += 1

# 14. What is the average grade for students with 0 pets?
#     ANSWER: 82.125

grade_lst = []

for student in students_lst:

    pet_count = 0
    for pet in student['pets']:
        pet_count += 1

    if pet_count == 0:
        
        for grade in student['grades']:
            grade_lst.append(grade)

no_pet_avg_grade = sum(grade_lst) / len(grade_lst)

# 15. What is the average grade for web development students? 
#     ANSWER: 81.179

grade_lst = []

for student in students_lst:

    if student['course'] == 'web development':
        
        for grade in student['grades']:
            grade_lst.append(grade)

webdev_avg_grade = sum(grade_lst) / len(grade_lst)


# 15a. What is the average garde for data science students?
#      ANSWER: 84.679

grade_lst = []

for student in students_lst:

    if student['course'] == 'data science':
        
        for grade in student['grades']:
            grade_lst.append(grade)

ds_avg_grade = sum(grade_lst) / len(grade_lst)

# 16. What is the average grade range (i.e. highest grade - lowest grade) 
#     for dark coffee drinkers?

range_lst = []
for student in students_lst:
    if student['coffee_preference'] == 'dark':
        range_lst.append(max(student['grades']) - min(student['grades']))
dark_avg_range = sum(range_lst) / len(range_lst)

# 17. What is the average number of pets for medium coffee drinkers?