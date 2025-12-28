def temperature_status(temp):
    """
    Classifies body temperature into medical categories.

    Parameters:
        temp (float): Body temperature in Celsius.

    Returns:
        str: Temperature status.
    """
    if temp < 0 or temp > 45:
        return "invalid"
    elif temp < 35:
        return "hypothermia"
    elif temp < 37:
        return "normal"
    elif temp < 39:
        return "fever"
    else:
        return "high fever"


temps = [36.5, 38.2, 34, 40, -5, 37, 45, 50]
results = []

for temp in temps:
    results.append(temperature_status(temp))

print(results)
