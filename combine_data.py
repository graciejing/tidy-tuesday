import csv
import copy
import json

header = ["Entity","Code","Year","Access to clean fuels and technologies for cooking (% of population)","GDP per capita, PPP (constant 2017 international $)","Population (historical estimates)","Continent","Deaths - Cause: All causes - Risk: Household air pollution from solid fuels - Sex: Both - Age: Age-standardized (Percent)"]
data = []

with open("static/gdp_data.txt", "r") as gdp_import, open("static/indoor_pollution.csv", "r") as pollution_import, open("static/continents.json", "r") as continents_import:
  gdp = gdp_import.readlines()
  pollution = pollution_import.readlines()
  continents = json.load(continents_import)

  for i in range(1, len(gdp)):
    gdp_row = gdp[i].strip().split(",")
    for j in range(1, len(pollution)):
      pollution_row = pollution[j].strip().split(",")

      entity = gdp_row[0]

      if gdp_row[0] == pollution_row[0] and gdp_row[1] == pollution_row[1] and gdp_row[2] == pollution_row[2] and gdp_row[4] != "":
        if gdp_row[6] == "":
          # continent is empty
          if entity in continents:
            gdp_row[6] = continents[entity]
          else:
            # don't add if it doesn't have a continent
            break
        append_data = gdp_row
        append_data = copy.deepcopy(gdp_row)
        append_data.append(pollution_row[-1])
        append_data = ",".join(append_data) + "\n"
        data.append(append_data)

        break

with open("static/combined_data.txt", "w") as f:
  f.writelines(data)
