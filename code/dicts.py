dicta = {
        'a': 'alpha',
        'b': 'beta',
        'c': 'charlie'
         }

for key, value in dicta.items():
        print(key + " means " + value)
# a means alpha
# b means beta
# c means charlie

print(dicta['a'])
# alpha

dicta['d'] = "delta"
print(dicta)
# {'a': 'alpha', 'b': 'beta', 'c': 'charlie', 'd': 'delta'}

dicta.pop('d')
print(dicta)
# {'a': 'alpha', 'b': 'beta', 'c': 'charlie'}

print(dicta.items())
# dict_items([('a', 'alpha'), ('b', 'beta'), ('c', 'charlie')])

print(dicta.keys())
# dict_keys(['a', 'b', 'c'])

print(dicta.values())
# dict_values(['alpha', 'beta', 'charlie'])
