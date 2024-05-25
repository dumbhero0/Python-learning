#WAP to create a dictionary that contains districts and their headquarters and then extract the districts for which headquarter names in same as the district name.
data={
    "dolakha":"charikot",
    "kathmandu":"kathmandu",
    "Sindhupalchowk":"Chautara",
    "Ramechhap":"manthali",
    "lalitpur":"Lalitpur",
    "Bhaktapur":"bhaktapur",
    "Rasuwa":"Dhunche",
    "kavre":"Dhulikhel"
}
print("Following District have headquarters with same name as District: ")
for district , headquarter in data.items():
    if district.lower() == headquarter.lower():
        print(district)

