county_towns = {
    "Antrim" : "BELFAST",
    "Armagh" : "ARMAGH",
    "Carlow" : "CARLOW",
    "Cavan" : "CAVAN",
    "Clare" : "ENNIS",
    "Cork" : "CORK",
    "Derry" : "DERRY",
    "Donegal" : "LIFFORD",
    "Down" : "DOWNPATRICK",
    "Dublin" : "DUBLIN",
    "Fermanagh" : "ENNISKILLEN",
    "Galway" : "GALWAY",
    "Kerry" : "TRALEE",
    "Kildare" : "NAAS",
    "Kilkenny" : "KILKENNY",
    "Laois" : "PORTLAOIS",
    "Leitrim" : "CARRICK-ON-SHANNON",
    "Limerick" : "LIMERICK",
    "Longford" : "LONGFORD",
    "Louth" : "DUNDALK",
    "Mayo" : "CASTLEBAR",
    "Meath" : "NAVAN",
    "Monaghan" : "MONAGHAN",
    "Offaly" : "TULLAMORE",
    "Roscommon" : "ROSCOMMON",
    "Sligo" : "SLIGO",
    "Tipperary" : "CLONMEL",
    "Tyrone" : "OMAGH",
    "Waterford" : "WATERFORD",
    "Westmeath" : "MULLINGAR",
    "Wexford" : "WEXFORD",
    "Wicklow" : "WICKLOW"
}

correct_answers = 0

for county, town in county_towns.items():
    answer = input(f"What is the County Town of County {county} ? ").upper()
    if answer == town:
        correct_answers += 1
        print("Great job !")
    elif answer != town:
        print(f"Incorrect, the County Town of County {county} is {town}")

percentage = int((correct_answers/len(county_towns)) * 100)

if percentage == 100:
    print(f"Outstanding, you have found all {correct_answers} County Towns of Ireland !")
elif percentage >= 90 and percentage <= 99:
    print(f"Really good, you have found {correct_answers} County Towns of Ireland, only a few to make it a PERFECT !")
elif percentage >= 75 and percentage <= 89:
    print(f"Pretty good, you have found {correct_answers} County Towns of Ireland, keep learning and you'll be there soon !")
elif percentage >= 50 and percentage <= 74:
    print(f"Not bad, you have found {correct_answers} County Towns of Ireland. You can do better though !")
elif percentage >= 25 and percentage <= 49:
    print(f"Not your best performance, you have found {correct_answers} County Towns of Ireland. You'll do better next time !")
elif percentage <= 24:
    print(f"Not great, you have only found {correct_answers} County Towns of Ireland.")

