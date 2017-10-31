# created by raymond
# created on october 31
# created for isc3u

def temperature(temperature_celcius):
    temperature_fahrenheight = 1.8 * temperature_celcius + 32
    print("It is " + str(temperature_fahrenheight) + " degrees in fahrenheigt")
    
temperature_celcius = raw_input("Please enter the degrees in Celsius :")
temperature_celcius =   float(temperature_celcius)
temperature(temperature_celcius)
