def calculate(days):
    if days < 14:
        return 200*days
    elif days >= 14 and days < 30:
        return (200*days) + 50*(days - 14) 
    elif days >= 30 and days < 60:
        return (200*days) + 80*(days - 14)
    else:
        return (200*days) + 100*(days - 14)