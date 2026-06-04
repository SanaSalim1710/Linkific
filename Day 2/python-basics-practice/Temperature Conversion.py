# convert celsius to fahrenheit 
def c_to_f(temperature):
    return (temperature * 9/5) + 32

# convert fahrenheit to celsius
def f_to_c(temperature):
    return (temperature - 32) * 5/9

# convert celsius to kelvin 
def c_to_k(temperature):
    return temperature + 273.15

# convert kelvin to celsius
def k_to_c(temperature):
    return temperature - 273.15

# convert fahrenheit to kelvin
def f_to_k(temperature):
    #return (temperature + 459.67) * 5/9
    celsius = f_to_c(temperature)
    return c_to_k(celsius)

# convert kelvin to fahrenheit
def k_to_f(temperature):
    celsius = k_to_c(temperature)
    return c_to_f(celsius)

def convert_temp(unit, temperature):
    if unit == "C":
        print(f"{temperature}°C is {c_to_f(temperature):.2f}°F")
        print(f"{temperature}°C is {c_to_k(temperature):.2f}°K")
    elif unit == "F":
        print(f"{temperature}°F is {f_to_c(temperature):.2f}°C")
        print(f"{temperature}°F is {f_to_k(temperature):.2f}°K")
    else:
        print(f"{temperature}°K is {k_to_c(temperature):.2f}°C")
        print(f"{temperature}°K is {k_to_f(temperature):.2f}°F")

convert_temp("F",100)
convert_temp("C",25)
convert_temp("K",300)
