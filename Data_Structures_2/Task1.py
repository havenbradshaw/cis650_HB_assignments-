countries = {'Afghanistan': 'Kabul',
'Albania': 'Tirana',
'Algeria': 'Algiers',
'Andorra': 'Andorra la Vella',
'Angola': 'Luanda',
'Antigua and Barbuda': 'Saint John',
'Austria': 'Vienna',
'Azerbaijan': 'Baku',
'Bahamas': 'Nassau',
'Bahrain': 'Manama',
'Bangladesh': 'Dhaka',
'Barbados': 'Bridgetown',
'Belarus': 'Minsk',
'Belgium': 'Brussels',
'Belize': 'Belmopan',
'Benin': 'Porto-Novo',
'Bhutan': 'Thimphu',
'Bolivia': 'Sucre (de jure)',
'Bosnia and Herzegovina': 'Sarajevo',
'Botswana': 'Gaborone',
'Brazil': 'Brasilia'}

while True:
    user_country = input("Enter a country (or 'quit' to exit' : ")
    if user_country == 'quit':
        break
    if user_country in countries:
        print(countries[user_country])
    else:
        print("Country not found")