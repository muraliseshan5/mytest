import xml.etree.ElementTree as ET

tree = ET.parse('../data/sample.xml')
root = tree.getroot()
for child in root:
    # print(child.tag, child.attrib)
    for grandchild in child:
        # print(grandchild.tag, grandchild.attrib)
        if grandchild.attrib.get('name') == 'Colombia':
            print(child.attrib.get('name'))
            # for country in root.iter('country'):
                # print(country.attrib.get('name'))
# for neighbor in root.iter('neighbor'):
    # print(neighbor.attrib.get('name'))
print("welcome! Gundamma")
