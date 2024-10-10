def ParseDegreeString(ddmmss):
    degree_sym = chr(176)
    minute_sym = "'"
    second_sym = '"'
    
    degrees_str = ddmmss.split(degree_sym)[0]
    minute_str = ddmmss.split(degree_sym)[1].split (minute_sym)[0]
    seconds_str = ddmmss.split(minute_sym)[1].split (second_sym)[0]
    degrees = float(degrees_str.strip())
    minutes = float(minutes_str.strip())
    seconds = float(seconds_str.strip())
    
    return degrees, minutes, seconds 


    