import xml.etree.ElementTree as ET

# Read troop names from mod file
while True:
    fname = input("Enter mod troop file path: (Right click the file and copy file path)\n")
    fname = fname.strip('\"')
    try:
        fh = open(fname, encoding="utf-8")
        break
    except:
        print("Please check your input and see if the file name and path is correct.\n")

tree = ET.parse(fh)
root = tree.getroot()

troops = list()
for troop in root:
    troops.append(troop.get('id'))

fh.close()

# Start editing Additional_Troops file
nname = input("Enter the path and name of the file 'Additional Troops'.\n"
              "If left blank, the program will create a new file for you. "
              "Paste the new file into your /Modules/ServeAsSoldier directory:\n")
nname = nname.strip('\"')
if nname == "":
    nname = "Additional_Troops.xml"                                 #New file, new tree
    nroot = ET.Element('ArrayOfRecruit')
    for troop in troops:
        recruit = ET.SubElement(nroot, 'Recruit', Id=troop)
    ntree = ET.ElementTree(nroot)
else:
    while True:
        try:
            ntree = ET.parse(nname)                                 #Adjust existing tree
            break
        except:
            print("Please check your input and see if the file name and path is correct.\n")
            nname = input("Enter the path and name of the file 'Additional Troops'.\n"
                          "If left blank, the program will create a new file for you. "
                          "Paste the new file into your /Modules/ServeAsSoldier directory:\n")
    nroot = ntree.getroot()
    for troop in troops:
        recruit = ET.SubElement(nroot, 'Recruit', Id=troop)

ET.indent(ntree, space="\t", level=0)
ntree.write(nname, encoding='utf-8', method="html")
print("Output successful! Enjoy your game!\n")
