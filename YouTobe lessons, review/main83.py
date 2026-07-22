#large dictionari

people = {
    'user_1':{
        'name':'John',
        'age':27,
        'address': ('Seattle', 'Some street', 6635),
        'grades': {
            'math':5,'physics':2, }
    },
    'user_2':{
        'surname': 'Doe',
        'name':'Alex',
    }
}

print(people['user_1']['address'][1])