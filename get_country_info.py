# pip install countryinfo in terminal

from countryinfo import CountryInfo

count = input("Enter your country: ")
country = CountryInfo(count)
print("Capital is : ",country.capital())
print("Currency is : ",country.currencies())
print("Language is : ",country.languages())
print("Bordering countries are : ",country.borders())
print("Other names : ",country.alt_spellings())