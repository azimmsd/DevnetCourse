from lxml import etree as ET 
#Get the XML file data
stream=open('NameSample.xml','r')

#Parse the data into am ElementTree object
xml=ET.parse(stream)

#Get the 'root' Element object from the ElementTree
root=xml.getroot()

#Iterate through each child of the root element
for e in root:
    #print the stringified version of the element
    print(ET.tostring(e))
    #print the 'id' attribute of the element object
    print(e.get("id"))
    