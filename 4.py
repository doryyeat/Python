People = {'Kate': 12, 'Dasha': 18, 'Oleg': 34,
          'Nastya': 10, 'Liza': 27, 'Yana': 20,
          'Polina': 19, 'Zhenya': 25, 'Nina': 40}

print('Изначальный словарь: ')
for key, value in People.items():
    print(f"{key}: {value}")

# в порядке возрастания

sorted_people_ascending = dict(sorted(People.items(), key=lambda x: x[1]))

print("\nСортировка словаря по значению в порядке возрастания:")
for key, value in sorted_people_ascending.items():
    print(f"{key}: {value}")

# в порядке убывания

sorted_people_descending = dict(sorted(People.items(), key=lambda x: x[1], reverse=True))

print("\nСортировка словаря по значению в порядке убывания:")
for key, value in sorted_people_descending.items():
    print(f"{key}: {value}")