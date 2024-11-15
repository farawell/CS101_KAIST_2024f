# Author: Yohan Park (farawell777@kaist.ac.kr)

def parser(line):
    # ex) line: "KR","Korea, Republic of",37,127.5
    # latitude: 위도, longitude: 경도 
    chunks = line.strip().split(',') # ['"KR"', '"Korea', 'Republic of"','37', '127.5']

    # Helper function
    def strip_chunk(chunk):
        return chunk.strip().strip('"').strip("'")

    country_code = strip_chunk(chunks[0])
    country_name = strip_chunk(','.join(chunks[1 : -2]))
    latitude = float(chunks[-2])
    longitude = float(chunks[-1])

    if not (-90.0 <= latitude <= 90.0) or not (-180.0 <= longitude <= 180.0):
        print("Wrong latitude or longitude")
        return
    
    return country_code, country_name, latitude, longitude

def handle_csv(file_name):
    list_code_name, list_code_loc, list_name_loc = [], [], []
    dict_code_name = {}

    with open(file_name, 'r') as csv_file:
        next(csv_file)
        for line in csv_file:
            code, name, lat, lon = parser(str(line))
            list_code_name.append((code, name))
            list_code_loc.append((code, (lat, lon)))
            list_name_loc.append((name, (lat, lon)))
            dict_code_name[code] = name
    
    for _list in [list_code_name, list_code_loc]:
        print(_list)
        print()
    
    return list_code_name, list_code_loc, list_name_loc, dict_code_name

def print_south(list_name_loc):
    for item in list_name_loc:
        latitude = item[1][0]
        if latitude < 0:
            name = item[0]
            print(name)
    print()

def get_full_name(dict_code_name):
    while (True):
        code = str(input('Enter country code: '))
        print(dict_code_name.get(code, "-----Wrong country code-----"))

def main():
    info_csv = 'average-latitude-longitude-countries.csv'

    # Make two lists and print them
    _, _, list_name_loc, dict_code_name = handle_csv(info_csv)

    # Print the names of all countries whose 
    # location lies in the south of the equator
    print_south(list_name_loc)

    # Let the user enter a country code, 
    # and then print the full name of the corresponding country
    get_full_name(dict_code_name)

main()
