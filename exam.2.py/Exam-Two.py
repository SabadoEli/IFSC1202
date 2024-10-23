import csv
def read_properties(input_file):
    properties = []
    
    with open (input_file, mode='r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line:
                address = line[0]
                city = line[1]
                state = line[2]
                zipcode = line[3]
                price = float (line[4])
                properties.append([address, city, state, zipcode, price])
    return properties

def analyze_properties(properties):
    zipcodes =[]
    for property_data in properties:
            zipcode = property_data[3]
            price = property_data[4]
            
            found = False
            for zipcode_row in zipcodes: 
                if zipcode_row[0] == zipcode:
                    zipcode_row[1] += 1
                    zipcode_row[2] += price
                    found = True
                    break 
                
            if not found:
                zipcodes.append([zipcode, 1, price])
    return zipcodes
            
def format_output(zipcodes):
    print (f"{'Zipcode':>10} {'Count':>10} {'Average':>15}")    
    for zipcode_row in zipcodes:
        zipcode = zipcode_row[0]
        count = zipcode_row[1]
        total_price = zipcode_row[2]
        average = total_price / count
        print(f"{zipcode:>10} {count:>10} ${average:>14,.2f}")

input_file_path = 'exam.2.py/Exam-Two-Properties.csv'
properties = read_properties(input_file_path)
if properties: 
    zipcodes = analyze_properties (properties)
    format_output(zipcodes)
        
    