# exceptions: zerodivisionerror, typeerror, valueerror
# zerodivision: als je iets met 0 probeert te delen
#type: als je een string met een nummer samen telt
#value: als je letters een nummer probeert te maken

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("enter only numbers")
except Exception:
    print("something went wrong")
finally:
    print("do some cleanup here")