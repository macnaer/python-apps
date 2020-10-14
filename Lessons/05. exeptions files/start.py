import datetime

today = datetime.datetime.today()

error_file = open("error.log", "a")
try:
    number1 = int(input("Enter number 1 "))
    number2 = int(input("Enter number 2 "))
    print("Division: ", number1 / number2)
except ValueError as e:
    # print("ValueError ", e)
    date = today.strftime('%Y-%m-%d-%H:%M:%S')
    error_file.write(date + " " + str(e) + "\n")

except ZeroDivisionError as e:
    # print("Zero divisin  error ", e)
    date = today.strftime('%Y-%m-%d-%H:%M:%S')
    error_file.write(date + " " + str(e) + "\n")
except Exception as e:
    # print("Opppps....")
    date = today.strftime('%Y-%m-%d-%H:%M:%S')
    error_file.write(date + " " + str(e) + "\n")

finally:
    # print("All time run")
    error_file.close()
