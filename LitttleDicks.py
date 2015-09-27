def main():
	myList = [69, 20]
	thirdNumber = 7
	myList.append(thirdNumber)
	print (getLargestNumber(myList))



def getLargestNumber(numberList):
	largest = numberList[0]
	
	for i in range(len(numberList)):
		if numberList[i] > largest:
			largest = numberList[i]

	return largest 

if __name__ == '__main__':
	main()	