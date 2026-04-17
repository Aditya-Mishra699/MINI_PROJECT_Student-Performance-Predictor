# simple log file writter

with open("log.txt", "a") as f:
    message = input("Enter log message: ")
    f.write(message + "\n")

print("Log saved")