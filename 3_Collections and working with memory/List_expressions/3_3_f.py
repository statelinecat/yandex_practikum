text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
s = {x: text.lower().count(x) for x in text.lower() if x.isalpha()}
print(s)