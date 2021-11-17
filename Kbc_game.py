print("welcome to K.B.C")
questions=[ "How many continents are there?",  "What is the capital of India?", "NG mei kaun se course padhaya jaata hai?" 
]
options= [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
answer=["Seven","Delhi","Software Engineering"]
i=0
while i<len(questions):
	print("Your question is in your screen")
	print(questions[i])
	print(options[i])
	choice=input("choose one option :  ")
	if choice==answer[i]:
		print("correct")
	else:
		print("sorry!!!,wrong answer") 
		print("Thank you,try next time")
		break
	i=i+1