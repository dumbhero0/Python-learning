#WAP to store name of countries in a list and then extract countries that contains substring in another list.
import countryname as c
substr=input("Enter the substring that is associated with countryname:")
Subcountry=[] #country with substring
for country in c.countries:
    if substr.lower() in country.lower():
        Subcountry.append(country)
for x in Subcountry:
    print(x)
