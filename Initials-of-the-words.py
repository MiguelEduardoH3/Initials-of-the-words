def initial_word(name):
    separate_name = name.split()
    acronym = ""
    for initial_letter in separate_name:
        acronym += initial_letter[0].upper()
    return acronym

print(initial_word('Fédération Internationale Football Association'))
print(initial_word('Central Intelligence Agency'))
print(initial_word('As Soon As Possible'))
print(initial_word('Absent Without Official Leave'))