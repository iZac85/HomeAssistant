# Script to return interpolated limit for mold growth at given
# temperature and humidity
#
# From https://www.lfs-web.se/mogel.htm
# Förenklad framställning av forskning framkommen risk för mögeltillväxt:
# Relativ Fuktighet – RF      Risk för mögeltillvä
# Under 75 %                    Ingen risk
# Mellan 75 – 85 %              Liten risk
# Mellan 85 – 95 %          Medelstor risk
# Över 95 %                       Hög risk
#
# Run script from Developer Tools with Service Data: {"temperature" : 10,"humidity" : 20}

def check_mold_growth_level(temperature=None, humidity=None):
    """check_mold_growth_level scrript to check if temperature and humidity is above level for mold growth."""

    print(
        "check_mold_growth_level: Got temperature: {} deg, humidity: {} %".format(temperature, humidity))

    # Limit for mold growth in one day
    oneDay_growth_temp = [0,  10, 15, 20, 25, 30]
    oneDay_growth_humidity = [100, 100, 97, 95, 94, 94]
    y_interp = interpolate(
        oneDay_growth_temp, oneDay_growth_humidity, temperature)
    print("One day mold limit at {} degrees is: {} %".format(temperature, y_interp))

    # Check if current temperature and humidity is above limit for one day mold growth
    if humidity >= y_interp:
        print("check_mold_growth_level: Humidity is ABOVE one day mold growth limit!")
        return 0
    else:
        print("check_mold_growth_level: Humidity is BELOW one day mold growth limit.")
        return 1


def interpolate(x_array, y_array, x):
    """Return interpolated y value using x_array, y_array and x.
    https://en.wikipedia.org/wiki/Linear_interpolation
    """
    for k in range(0, len(x_array)):
        if x_array[k] > x:
            y_interp = (y_array[k-1] * (x_array[k] - x) + y_array[k] *
                        (x - x_array[k-1])) / (x_array[k] - x_array[k-1])
            break
    return y_interp


if __name__ == "__main__":
    temperature = 25
    humidity = 94
    check_mold_growth_level(temperature, humidity)
