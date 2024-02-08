git # Implement funny reverse, skipping serious words (words with !).

def funny2(s):
   return ' '.join([item[::-1] for item in s.split() if '!' not in item])

print(funny2('i am cute!'))


# Using list comprehension, create a function that returns an html unordered list:

def ul(items):
    return f"<ul>{''.join([f'<li>{item}</li>' for item in items])}</ul>"


assert "<ul><li>One</li><li>Two</li><li>Three</li></ul>" == ul(['One', 'Two', 'Three'])


# dictionary_exercise.py

def word_length_dict(s):
    return {len(item):item for item in s.split()}

print(word_length_dict("i am  very sed and nerves"))


# complex_dict_exercise.py

def word_stats(s):
  return {item:{'length':len(item),'is_vowel_start':True if item.lower()==item else False,'contains_digit':True if item.isdigit() else False} for item in s.split()}
print(word_stats("Complex 123 exercise with multiple words!"))

