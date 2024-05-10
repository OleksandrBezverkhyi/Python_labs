import json
import matplotlib.pyplot as plt

with open('DataBase.json') as f:
    data = json.load(f)

birth_year_count = {}

for person in data:
    birth_year = int(person['Birthdate'].split('-')[0])
    if birth_year in birth_year_count:
        birth_year_count[birth_year] += 1
    else:
        birth_year_count[birth_year] = 1

sorted_years = sorted(birth_year_count.keys())

labels = [str(year) for year in sorted_years]
sizes = [birth_year_count[year] for year in sorted_years]
colors = plt.cm.tab20c.colors  
explode = [0] * len(sorted_years)  

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  
ax.legend()
plt.title('Birth Year Distribution')
plt.show()
