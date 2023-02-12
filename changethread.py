#mac version of python script that rewrite all thread xml files increasing hole size by a fixed tolerance
import xml.etree.ElementTree as ET
#how bigger os smaller (negative) holes should be in mm
tolerance_to_add=0.5
#your pc username 
username='mvalenti'

# list all directory
import os
# assign directory
folder_directory = '/Users/'+username+'/Library/Application Support/Autodesk/webdeploy/'
os.chdir(folder_directory)
# iterate over files in
# that directory
app_directory_list = []
for filename in os.listdir('production'):
    f = filename #os.path.join(directory, filename)
    # checking if it is a file
    if(("Autodesk" not in f) and ("." not in f)): 
        app_directory_list.append(f)
#print(app_directory_list)

# List all thread xml files
for files in app_directory_list:
    thread_directory = '/Users/'+username+'/Library/Application Support/Autodesk/webdeploy/production/'+files+'/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/'
    try:
        os.chdir(thread_directory)
    except:
        continue
    # iterate over files in
    # that directory
    xml_files_list = []
    for filename in os.listdir('ThreadData'):
        f = filename #os.path.join(directory, filename)
        # checking if it is a file
        if((".xml" in f) and ("RESIZED" not in f)): 
            xml_files_list.append([files,f])
    #print(xml_files_list)

for [d,f] in xml_files_list:
    directory=d
 
    filexml=f
    filename='/Users/'+username+'/Library/Application Support/Autodesk/webdeploy/production/'+directory+'/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData/'+filexml
    print(filename)
    try:
        tree = ET.parse(filename)
    except:
        continue

    root = tree.getroot()
    unit = root.find('Unit')
    print(unit.text)
    if(unit.text=='in'):
        tolerance_to_add_in_unit=tolerance_to_add/2.54
    else:
        tolerance_to_add_in_unit=tolerance_to_add
    print(tolerance_to_add_in_unit)
    elem=root.find('Name')
    elem.text=elem.text+' RESIZED'
    elem=root.find('CustomName')
    elem.text=elem.text+' RESIZED'
    #start change xml values
    for child in root.iter('Thread'):
        elemento=child.find('MajorDia')
        newDia=float(elemento.text)+tolerance_to_add_in_unit
        elemento.text=str(newDia)
    for child in root.iter('Thread'):
        elemento=child.find('PitchDia')
        newDia=float(elemento.text)+tolerance_to_add_in_unit
        elemento.text=str(newDia)
    for child in root.iter('Thread'):
        elemento=child.find('MinorDia')
        newDia=float(elemento.text)+tolerance_to_add_in_unit
        elemento.text=str(newDia)
    tree.write(filename.removesuffix('.xml')+'RESIZED.xml')