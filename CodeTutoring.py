def main():
	print("Hello World")
	myList = ["Suck", "my"]
	thirdWord = "nuts"
	myList.append(thirdWord)
	printAList(myList)

def printAList(listToPrint):
	myStr = ""
	
	for i in range(len(listToPrint)):
		myStr = myStr + " " + listToPrint[i]

	print(myStr)


if __name__ == "__main__":
    main()