import json

continent_dict = {}

with open("static/fuel_gdp.csv", "r") as gdp:
  gdp_import = gdp.readlines()
  for i in range(1, len(gdp_import)):
    gdp_row = gdp_import[i].strip().split(",")
    entity = gdp_row[0]
    continent = gdp_row[6]
    if continent != "":
      continent_dict[entity] = continent

with open("continents.json", "w") as f:
  json.dump(continent_dict, f)

# get a list of unique continent names
continents = continent_dict.values()
continents = list(set(continents))
print(continents)