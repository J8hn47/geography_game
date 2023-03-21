languages = ("ENGLISH", "IRISH")

counties = (
    "ANTRIM",
    "ARMAGH",
    "CARLOW",
    "CAVAN",
    "CLARE",
    "CORK",
    "DERRY",
    "DONEGAL",
    "DOWN",
    "DUBLIN",
    "FERMANAGH",
    "GALWAY",
    "KERRY",
    "KILDARE",
    "KILKENNY",
    "LAOIS",
    "LEITRIM",
    "LIMERICK",
    "LONGFORD",
    "LOUTH",
    "MAYO",
    "MEATH",
    "MONAGHAN",
    "OFFALY",
    "ROSCOMMON",
    "SLIGO",
    "TIPPERARY",
    "TYRONE",
    "WATERFORD",
    "WESTMEATH",
    "WEXFORD",
    "WICKLOW"
)

contaetha = (
    "Aontroim",
    "Ard Mhacha",
    "Ceatharlach",
    "An Cabhán",
    "An Clár",
    "Corcaigh",
    "Doire",
    "Dún na nGall",
    "An Dún",
    "Baile Átha Cliath",
    "Fear Manach",
    "Gaillimh",
    "Ciarraí",
    "Cill Dara",
    "Cill Chainnigh",
    "Laois",
    "Liatroim",
    "Luimneach",
    "An Longfort",
    "Lú",
    "Maigh Eo",
    "An Mhí",
    "Muineachán",
    "Uíbh Fhailí",
    "Ros Comáin",
    "Sligeach",
    "Tiobraid Árann",
    "Tír Eoghain",
    "Port Láirge",
    "An Iarmhí",
    "Loch Garman",
    "Cill Mhantáin"
)


correct_answers = 0
language = ""

# Select language
while language not in languages:
    language = input("Would you like to guess the counties of Ireland in English or in Irish ? ").upper()
    if language == "ENGLISH":
        number_of_counties = len(counties)
        break
    elif language == "IRISH":
        number_of_counties = len(contaetha)
        break
    else:
        print("Sorry, you must select either 'English' or 'Irish' only.")


# Find all counties of Ireland
while correct_answers < number_of_counties:
    if language == "ENGLISH":
        answer = input("Give me a county of Ireland: ").upper()
        if answer in counties:
            correct_answers += 1
            counties_left = number_of_counties - correct_answers
            print(f"Good job ! {answer} is indeed a county of Ireland. You've found {correct_answers} of the {number_of_counties} counties, {counties_left} left !.")
        else:
            print("Try again")
    elif language == "IRISH":
        answer = input("Give me a county of Ireland: ") # In Irish we leave it case sensitive
        if answer in contaetha:
            correct_answers += 1
            counties_left = number_of_counties - correct_answers
            print(f"Good job ! {answer} is indeed a county of Ireland. You've found {correct_answers} of the {number_of_counties} counties, {counties_left} left !.")
        else:
            print("Try again")

if language == "ENGLISH":
    print(f"Well done, you have found all {number_of_counties} counties of Ireland !")
elif language == "IRISH":
    print(f"Well done, you have found all {number_of_counties} counties of Ireland, and in Irish !")