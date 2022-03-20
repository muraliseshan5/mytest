import xml.etree.ElementTree as ET

tree = ET.parse('../data/sample.xml')
root = tree.getroot()
country_list = []
rank_list = []
for child in root:
    name = child.attrib.get('name')
    rank = child.find('rank').text
    country_list.append(name)
    rank_list.append(child.find('rank').text)
    print(name, rank)
print (country_list, rank_list)

for country in root.findall('country'):
    gdp = country.find('gdppc').text
    name = country.get('name')
    print(name, gdp)
