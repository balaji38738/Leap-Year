import json

with open('india_covid_data.json') as covid_data_file:
  covid_data = json.load(covid_data_file)
  print(covid_data)