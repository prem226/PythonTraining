import xml.etree.ElementTree as ET

mytree = ET.parse("x1.xml")
myroot = mytree.getroot()

for prices in myroot.iter('price'):
    prices.text = str(float(prices.text)+10)
    prices.set('newprices','yes')


ET.SubElement(myroot[0],"tasty")
for temp in myroot.iter('tasty'):
    temp.text = str("Yes")
mytree.write('modified.xml')

# print(myroot[1][0].attrib.pop('name'))
mytree.write('modified.xml')
# print(myroot.remove(myroot[2]))