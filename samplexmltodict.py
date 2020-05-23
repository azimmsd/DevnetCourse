import xmltodict

#get the xml file data
stream=open('NameSample.xml','r')
#parse the xml file into an "OrderedDict"
xml = xmltodict.parse(stream.read())

for element in xml["people"]["person"]:
        print(element)
