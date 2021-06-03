
from datetime import datetime

with open("Path") as f:
    lines = f.readlines()

NewWord= input("New Line here")

lines[2] = "As an admirer of {},\n".format(NewWord) #your word will replaced with {}

lines[-1] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

with open("Path", "w") as f:
    f.writelines(lines)