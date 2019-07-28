with open("details.txt", "r") as f :
	while True :
		line = f.readline()
		if line == "" :
			break
		name = line.split(",")[0]
		no = line.split(",")[1].replace("\n", "")
		