import androidhelper
import os
droid = androidhelper.Android()
path = os.path.realpath(__file__)
path = path.replace(".last_tmp.py", "")
fileName = str(path + "details.txt")
message = "Hi {}. I hope you are well. \n this message is just a trial \n We will get in touch with you soon."

with open(fileName, "r") as f :
    while True:
        line = f.readline()
        if line == "" :
            break
        name = line.split(",")[0]
        no = line.split(",")[1].replace("\n", "")
        droid.smsSend(no, message.format(name))