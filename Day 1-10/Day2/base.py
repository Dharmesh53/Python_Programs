weight=input("Enter your Weight:")
height=input("Enter your Height:")

bmi=int(weight)/float(height)**2
print(int(bmi))

print(round(8/3))
print(round(2.6666,2))
print(8//3)

score=65
result=True
print(f"your Score is {score} ans your winning is {result}")

age=input("Enter your Age:")
days=(90-int(age))*365;
weeks=(90-int(age))*52;
months=(90-int(age))*12;
message=f"You have {days} days,{months} months,{weeks} weeks left"
print(message)
