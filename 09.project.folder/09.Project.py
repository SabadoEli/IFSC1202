import csv

def load_distances(input_file):
    with open(input_file, mode = 'r') as file:
        reader = csv.reader(file)
        distances = list(reader)
    return distances

def print_distances(distances):
    for row in distances:
        print("\t".join(row))
        
def get_city_index(city_list, city):
    try:
        return city_list.index(city)
    except ValueError:
        return -1
    
def main():
    input_file = '09.project.folder/09.Project-Distances.csv'
    distances = load_distances(input_file)
    print_distances(distances)
    from_city = input("Enter From City: ")
    to_city = input("Enter To City: ")
    from_index = get_city_index([row[0]for row in distances], from_city)
    to_index = get_city_index(distances[0], to_city)
    
    if from_index == -1:
        print("Invalid From City")
    elif to_index == -1:
        print("Invalid To City")
    else:
        distance = distances[from_index][to_index]
        print(f"{from_city} to {to_city} - {distance} miles")