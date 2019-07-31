import androidhelper
import os
droid = androidhelper.Android()
path = os.getcwd()
message = "Hi {}. I hope you are well. \n this message is just a trial \n We will get in touch with you soon."
with (path + "/details.txt", "r") as f :
    while True:
        line = f.readline()
        if line == "" :
            break
        name = line.split(",")[0]
        no = line.split(",")[1].replace("\n", "")
        droid.smsSend(no, message.format(name))