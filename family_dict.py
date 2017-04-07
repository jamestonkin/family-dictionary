my_family = {
    'wife': {
        'name': 'Angela',
        'age': 37
    },
    'mother': {
        'name': 'Pat',
        'age': 64
    },
    'daughter': {
        'name': 'Ava',
        'age': 1
    },
}


{print(v['name'] + " is my " + k + " and is " + str(v["age"]) + " years old.") for k, v in my_family.items()}
