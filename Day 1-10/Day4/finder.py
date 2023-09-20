import random

girls_string=input("Enter name of your whores:\n");
girls=girls_string.split(',');

size=int(len(girls))

# choice=int(random.randint(0,size-1))
# print(f"*****************************Today, you are going to fuck {girls[choice]}*****************************")

choice=random.choice(girls)
print(f"*****************************Today, you are going to fuck {choice}*****************************")

# input
# neha,sudanshi,manisha,anjali,hardika,depanshi