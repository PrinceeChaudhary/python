countries = [
{"name": "Nepal", "population":656780},
{"name": "India", "population":576890},
{"name": "France", "population":67890},
]
for country in countries:
    print(f"Name:{country["name"]} - population: {country["population"]}")
 # Add a if to compare country with biggest_country
 # if bigger population we want to store this country in biggest_country
 # After the loop, we display the biggest country
 print(f"The biggest country is {biggest_country["name"]} with a population of {biggest_country["population"]}")
