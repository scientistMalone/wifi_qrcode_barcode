from countryinfo import CountryInfo

#user input
count = input("Enter your country: ")
country = CountryInfo(count)

print("Capital city:", country.capital())
print("Currencies: ", country.currencies())
print("Languages: ", country.languages())
print("Borders: ", country.borders())
print("Timezones: ", country.timezones())
