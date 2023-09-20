print("********************** Welcome to the Tip calculator **********************")
bill=input("Enter your Bill amount:\n")
tipPercent=input("How much percent do you want to give in tip ?\n")
people=input("Enter the number of people:\n")

sum=int(bill)+(int(bill)*int(tipPercent))/100
final=int(sum)/int(people)

message=f"₹ {final} show be seperated among you"
print(message)