#Temperature Converter
def temp():
    temp = float(input("Enter teperature: "))
    unit = input("Celcius(C) or Fahrenheit(F): ").lower()

    if unit == "c":
        res = round(temp *(9/5) + 32, 1)
        print(f"Temperature is around {res}° F.")
    elif unit == "f":
        res = round((temp - 32) * 5/9, 1)
        print(round(res, 2))
        print(f"Temperature is around {res}° C.")
    else:
        print("Unit of measurement must be either Celcius(C) or Fahrenheit(F)!")

if __name__=="__main__":
    temp()



