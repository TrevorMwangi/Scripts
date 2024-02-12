# pip install countryinfo in terminal

from countryinfo import CountryInfo

try:
    count = input("Enter your country: ")
    country = CountryInfo(count)
    print("Capital is:", country.capital())
    print("Currency is:", country.currencies())
    print("Language is:", country.languages())
    print("Bordering countries are:", country.borders())
    print("Other names:", country.alt_spellings())
except KeyError:
    print("Sorry, that is not a recognized country.")
except Exception as e:
    print("An error occurred:", str(e))