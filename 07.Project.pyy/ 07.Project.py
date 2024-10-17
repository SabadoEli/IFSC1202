def ParseDegreeString(ddmmss):
    degree_sym = chr(176)
    minutes_sym = "'"
    second_sym = '"'
    
    degrees_str = ddmmss.split(degree_sym)[0]
    minutes_str = ddmmss.split(degree_sym)[1].split (minutes_sym)[0]
    seconds_str = ddmmss.split(minutes_sym)[1].split (second_sym)[0]
    degrees = float(degrees_str.strip())
    minutes = float(minutes_str.strip())
    seconds = float(seconds_str.strip())
    
    return degrees, minutes, seconds 

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes/60)+(seconds/3600)
    return decimal_degrees
    
def convert_angles(input_file, output_file):
    print("Starting conversion...")
    with open(input_file,'r')as infile, open(output_file, 'w')as outfile:
        for line in infile:
            line=line.strip()
            if line:
                try:
                    degrees, minutes, seconds = ParseDegreeString(line)
                    decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
                    outfile.write(f"{decimal_degrees:.6f}\n")
                    print(f"Converted: {line} -> {decimal_degrees:.6f}°")
                except (ValueError, IndexError):
                    print(f"Invalid entry skipped: {line}")
                
    print("Conversion complete! Output written to", output_file)
                    
                    
                
input_file_path = '07.Project_Angles_Input.txt'
output_file_path = '07.Project Angles Output.txt'
convert_angles(input_file_path, output_file_path)