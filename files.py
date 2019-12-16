import os
days = range(2, 26)
files = ['prompt.md', 'solution.py']
for day in days:
    dir = f'day{day}'
    for filename in files:
        file = os.path.join(dir, filename)
        open(file, 'a').close()
