import random as rn
import csv 

Trait = {"Height" : 180, 
         "Weight" : 85, 
         "Age": 24, 
         "Sex": "male", 
         "Hair Color": "Blond", 
         "Eye Color": "Blue", 
         "Blood Type": "B+", 
         "Health":"Healthy", 
         "Ethnicity":"German", 
         "Muscle mass distribution": "80%"}


def HeightGenerator(a):
    a['Height'] = rn.randint(165, 195)
    return a['Height']

def WeightGenerator(a):
    a['Weight'] = rn.randint(65, 110)
    return a['Weight']

def AgeGenerator(a):
    a['Age'] = rn.randint(15, 90)
    return a['Age']

def SexGenerator(a):
    a['Sex'] = rn.choice(['Male','Female'])
    return a['Sex']

def HairColorGenerator(a):
    HairColor = ['Blond','Black', 'White', 'Brown']
    rn.shuffle(HairColor)
    a['Hair Color'] = HairColor[1]
    return a['Hair Color']

def EyeColorGenerator(a):
    EyeColor = ['Blue','Black', 'Green', 'Brown']
    rn.shuffle(EyeColor)
    a['Eye Color'] = EyeColor[1]
    return a['Eye Color']

def BloodTypeGenerator(a):
    BloodType = ['A+','A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    rn.shuffle(BloodType)
    a['Blood Type'] = BloodType[1]
    return a['Blood Type']

def HealthGenerator(a):
    Health = ['Too Healthy','Healthy', 'Infectious Disease', 'Deficiency Diseases', 'Hereditary Diseases Genetic', 'Hereditary Diseases Non-Genetic', 'physiological diseases', 'O-']
    rn.shuffle(Health)
    a['Health'] = Health[1]
    return a['Health']

def EthnicityGenerator(a):
    Ethnicity = [
    # North America
    "African American",
    "White American",
    "European American",
    "Hispanic",
    "Latino",
    "Mexican",
    "Puerto Rican",
    "Cuban",
    "Native American",
    "Navajo",
    "Cherokee",
    "Sioux",
    "Inuit",
    "First Nations",

    # South America
    "Mestizo",
    "Indigenous South American",
    "Quechua",
    "Aymara",
    "Mapuche",
    "Afro-Brazilian",
    "Afro-Colombian",
    "White Latin American",

    # Europe
    "German",
    "French",
    "English",
    "British",
    "Irish",
    "Italian",
    "Spanish",
    "Swedish",
    "Danish",
    "Norwegian",
    "Russian",
    "Polish",
    "Ukrainian",
    "Czech",
    "Serbian",
    "Greek",
    "Basque",
    "Roma",
    "Ashkenazi Jewish",
    "Sephardic Jewish",

    # Africa
    "Arab",
    "Berber",
    "Hausa",
    "Yoruba",
    "Igbo",
    "Zulu",
    "Xhosa",
    "Oromo",
    "Amhara",
    "Tutsi",
    "Hutu",
    "Dinka",
    "Somali",
    "Afro-Caribbean",

    # Asia
    "Han Chinese",
    "Tibetan",
    "Uyghur",
    "Japanese",
    "Korean",
    "Mongolian",
    "Vietnamese",
    "Thai",
    "Filipino",
    "Malay",
    "Punjabi",
    "Tamil",
    "Bengali",
    "Gujarati",
    "Pashtun",
    "Sindhi",
    "Arab (Middle Eastern)",
    "Persian",
    "Kurdish",
    "Turkish",
    "Hazara",
    "Tajik",

    # Oceania & Australia
    "Aboriginal Australian",
    "Torres Strait Islander",
    "Māori",
    "Samoan",
    "Tongan",
    "Hawaiian",
    "Fijian",
    "Papua New Guinean",
    "Micronesian"
]

    rn.shuffle(Ethnicity)
    a['Ethnicity'] = Ethnicity[1]
    return a['Ethnicity']

def MuscleMassGenerator(a):
    a['Muscle mass distribution'] = round(rn.uniform(0.30, 0.56), 2)
    return a['Muscle mass distribution']

n = HeightGenerator(Trait), WeightGenerator(Trait), AgeGenerator(Trait), SexGenerator(Trait), HairColorGenerator(Trait), EyeColorGenerator(Trait), BloodTypeGenerator(Trait), HealthGenerator(Trait),EthnicityGenerator(Trait), MuscleMassGenerator(Trait)

with open('TraitsResults.csv', 'w', encoding="utf-8", newline='') as file:
    TraitsHeader = ['Height','Weight', 'Age', 'Sex', 'Hair Color', 'Eye Color', 'Blood Type', 'Health', 'Ethnicity', 'Muscle mass distribution']
    writer = csv.writer(file)
    writer.writerow(TraitsHeader)
    for i in range(1, 1000):
        n = HeightGenerator(Trait), WeightGenerator(Trait), AgeGenerator(Trait), SexGenerator(Trait), HairColorGenerator(Trait), EyeColorGenerator(Trait), BloodTypeGenerator(Trait), HealthGenerator(Trait),EthnicityGenerator(Trait), MuscleMassGenerator(Trait)
        writer.writerow(n)

print(n)