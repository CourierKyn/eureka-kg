import re
import json
import minecart

def get50_leading_company_name(text):
    patternOfName = re.compile(r'\d\d(.+)')
    try:
        Name = patternOfName.findall(text)[0]
    except:
        Name =None
    return {'Name': Name}

def get50_emerging_company_name(text):
    patternOfName = re.compile(r'\ue801(.+)')
    try:
        Name = patternOfName.findall(text)[0]
    except:
        Name =None
    return {'Name':Name}

def get_description_investors(text):
    patternOfDescription = re.compile(r'Company Description([\s\S]+)Notable Investors')
    patternOfInvestors = re.compile(r'Notable Investors([\s\S]+)')
    patternOfDescription_1 = re.compile(r'Company Description([\s\S]+)')
    patternOfDescription_2 = re.compile(r'Company Description([\s\S]+)  Notable investors')
    patternOfInvestors_2 = re.compile(r'  Notable investors([\s\S]+)')
    try:
        Description = patternOfDescription.findall(text)[0]
    except:
        if patternOfDescription_1.findall(text)[0]:
            Description = patternOfDescription_1.findall(text)[0]
        else:
            Description = None
    try:
        Investors = patternOfInvestors.findall(text)[0]
    except:
        # if patternOfInvestors_new.findall(text)[0]:
        #     Investors = patternOfInvestors_new.findall(text)[0]
        # else:
        Investors = None
    return {'Description':Description,'Investors':Investors}

def get_other_information(text):
    patternOfYear = re.compile(r'Year Founded  (.+)Key People')
    patternOfLocation = re.compile(r'Located  (.+)Year Founded')
    patternOfWebsite = re.compile(r'Website  (.+)Category')
    patternOfCategory = re.compile(r'Category  (.+)Ownership')
    patternOfOwnership = re.compile(r'Ownership  (.+)Rank')
    patternOfOwnership_1 = re.compile(r'Ownership  (.+)Staff')
    patternOfKeyPeople = re.compile(r'Key People  ([\s\S]+)Website')
    patternOfKeyPeople_1 = re.compile(r'Key People ([\s\S]+)Website')
    try:
        Year = patternOfYear.findall(text)[0]
    except:
        Year = None
    try:
        Location = patternOfLocation.findall(text)[0]
    except:
        Location = None
    try:
        Website = patternOfWebsite.findall(text)[0]
    except:
        Website = None
    try:
        Category = patternOfCategory.findall(text)[0]
    except:
        Category = None
    try:
        Ownership = patternOfOwnership.findall(text)[0]
    except:
        if patternOfOwnership_1.findall(text)[0]:
            Ownership = patternOfOwnership_1.findall(text)[0]
        else:
            Ownership = None
    try:
        Keypeople = ','.join(re.split(r'(?<=[a-z])(?=[A-Z])', patternOfKeyPeople.findall(text)[0]))
    except:
        if patternOfKeyPeople_1.findall(text)[0]:
            Keypeople = ','.join(re.split(r'(?<=[a-z])(?=[A-Z])', patternOfKeyPeople_1.findall(text)[0]))
        else:
            Keypeople = None
    return {'Year': Year,'Location': Location,'Website': Website,'Category':Category,'Ownership':Ownership,'Keypeople':Keypeople}

if __name__ == '__main__':
    name_box = (0, 688, 288, 835)
    description_investor_box = (30, 30, 300, 376)
    glance_box = (288, 41, 576, 376)

    file = open("Fintech100-12-111.pdf", 'rb')
    doc = minecart.Document(file)

    Company100Information = []
    a = 0
    while a < 100:
        page = doc.get_page(a)
        if a < 50:
            name = get50_leading_company_name("".join(page.letterings.iter_in_bbox(name_box)))
        else:
            name = get50_emerging_company_name("".join(page.letterings.iter_in_bbox(name_box)))
        description_investor = get_description_investors("".join(page.letterings.iter_in_bbox(description_investor_box)))
        other_information = get_other_information("".join(page.letterings.iter_in_bbox(glance_box)))
        Company100Information.append(dict((dict(name, **description_investor)),**other_information))
        a += 1
    with open('Company100Information.json', 'w') as f:
            json.dump(Company100Information, f, indent=4)