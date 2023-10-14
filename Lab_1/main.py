import os, subprocess, json, psutil, shutil

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Детальное задание
"""
1. Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.
"""
print("Part 1")
inp = input("Skip part 1(y/N)?:").lower()
if inp == "n" or inp == "no" or inp == '':
    # proc = subprocess.Popen('C:\\Windows\\system32\\cmd.exe /k "wmic logicaldisk list brief"', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    # stdout, stderr = proc.communicate()
    # stdout = stdout.decode("utf-8").split("\n")
    # stdout.pop()
    # for item in stdout:
    #     print(item.replace("\r",''))
    # Disk Information
    print("=" * 40, "Disk Information", "=" * 40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  Drive type: {partition.opts}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

"""
2.Работа с файлами
Создать файл
Записать в файл строку, введённую пользователем
Прочитать файл в консоль
Удалить файл
"""
print("Part 2")
inp = input("Skip part 2(y/N)?:").lower()
if inp == "n" or inp == "no" or inp == '':
    fileName = input("Input file name:")
    fileRecords = input("Input text:")

    #write file
    with open(fileName, "w") as file:
        file.write(fileRecords)
    print("Writing completed")

    #read file
    with open(fileName, "r") as file:
        for line in file:
            print(line)

    #delete file
    inp = input("Delete file(Y/n)?:").lower()
    if  inp == "y" or inp == "yes" or inp == '':
        os.remove(fileName)
        print("File deleted")
"""
3. Работа с форматом JSON
Создать файл формате JSON в любом редакторе или с использованием данных, введенных пользователем
Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл.
Прочитать файл в консоль
Удалить файл
"""
print("Part 3")
inp = input("Skip part 3(y/N)?:").lower()
if inp == "n" or inp == "no" or inp == '':
    fileName = input("Input JSON file name(jsondata.json):")
    print("Default json data")
    data = '[ {"studentid": 1, "name": "ABC", \
"subjects": ["Python", "Data Structures"]}, \
                {"studentid": 2, "name": "PQR",\
                "subjects": ["Java", "Operating System"]} ]'

    # Create Python object from JSON string data
    obj = json.loads(data)

    # Pretty Print JSON
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)

    inp = input(("1) Use default JSON data\n2) Enter yourself JSON format text?:"))
    if inp == "2":
        data = input("Enter yourself JSON format text:")
        # Serializing json and
        # Writing json file
        with open(fileName, "w") as write:
            json.dump(data, write)
        print("Writing completed")

    else:
        # Serializing json and
        # Writing json file
        with open(fileName, "w") as write:
            json.dump(data, write)
        print("Writing completed")

    # opening the JSON file
    data = open(fileName, "r")
    # deserializing the data
    data = json.load(data)

    obj = json.loads(data)

    # Pretty Print JSON
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)

    #delete file
    inp = input("Delete json file(Y/n)?:").lower()
    if  inp == "y" or inp == "yes" or inp == '':
        os.remove(fileName)
        print("Json file deleted")

"""
4.Работа с форматом XML
Создать файл формате XML из редактора
Записать в файл новые данные из консоли.
Прочитать файл в консоль.
Удалить файл.
"""
print("Part 4")
inp = input("Skip part 4(y/N)?:").lower()
if inp == "n" or inp == "no" or inp == '':
    import xml.etree.ElementTree as ET
    import xml.dom.minidom

    tree = ET.parse('country_data.xml')
    root = tree.getroot()

    country = input("Input country:")
    rank = input("Input rank:")
    year = input("Input year:")
    gdppc = input("Input gdppc:")

    if country:
        _country = ET.Element('country')
        _country.attrib = {'name': country}
        root.append(_country)
        if rank:
            _rank = ET.SubElement(_country, "rank")
            _rank.text = rank
        if year:
            _year = ET.SubElement(_country, "year")
            _year.text = year
        if gdppc:
            _gdppc = ET.SubElement(_country, "gdppc")
            _gdppc.text = gdppc

        tree.write('country_data.xml')

    dom = xml.dom.minidom.parse('country_data.xml')
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
    #delete file
    inp = input("Delete xml file(Y/n)?:").lower()
    if  inp == "y" or inp == "yes" or inp == '':
        os.remove('country_data.xml')
        print("Json file deleted")
"""
5.Создание zip архива, добавление туда файла, определение размера архива
Создать архив в форматер zip
Добавить файл, выбранный пользователем, в архив
Разархивировать файл и вывести данные о нем
Удалить файл и архив
"""
print("Part 5")
inp = input("Skip part 5(y/N)?:").lower()
if inp == "n" or inp == "no" or inp == '':
    from zipfile import ZipFile
    import pprint
    curr_dir = os.getcwd()
    zip_name = input("Input zip name (archive.zip):")

    # Create a ZipFile Object
    zip_file = curr_dir + '\\' + zip_name
    with ZipFile(zip_file, 'w') as zip_object:
        from os import listdir
        from os.path import isfile, join

        onlyfiles = {}
        list_dir = [f for f in listdir(curr_dir) if isfile(join(curr_dir, f))]

        for i,f in zip(range(1, list_dir.__len__() + 1), list_dir):
            if isfile(join(curr_dir, f)):
                onlyfiles[i] = f

        for keys, values in onlyfiles.items():
            print(keys, values)
        zip_file_number = int(input('Select file number(1 or 2 or 3...):'))
        # Adding files that need to be zipped
        zip_object.write(onlyfiles[zip_file_number])

    # Check to see if the zip file is created
    if os.path.exists(zip_file):
        print("ZIP file created")
        print(listdir(curr_dir))
        print(f'File Size in Bytes is {os.stat(zip_file).st_size}')
    else:
        print("ZIP file not created")

    with ZipFile(zip_file, 'r') as zip_ref:
        zip_name_without_extension = os.path.splitext(zip_name)[0]
        zip_ref.extractall(curr_dir + '\\' + zip_name_without_extension)
        print('Contents of folder \"' + zip_name_without_extension + '\"' + '\n',
              [f for f in listdir(curr_dir + '\\' + zip_name_without_extension) if isfile(join(curr_dir + '\\' + zip_name_without_extension, f))])

    os.remove(zip_file)
    shutil.rmtree(curr_dir + '\\' + zip_name_without_extension)



