import info,random,art,os

print(art.heading)
score = 0
decision = True

while decision :
    choice1 =random.choice(info.data);
    choice2 = random.choice(info.data);
    if choice1['follower_count'] > choice2['follower_count']:
        answer = 'a'
    else :
        answer = 'b'

    print("==============================================================")
    print("Your current score is ", score);
    print("==============================================================")

    print(f"Compare A : {choice1['name']} , a {choice1['description']} , from {choice1['country']} ")
    print("vs")
    print(f"Compare B : {choice2['name']} , a {choice2['description']} , from {choice2['country']} \n\n")
 
    ans = str(input("Who has more followers ? Type A or B : ")).lower()
 
    if answer != ans :
        decision = False
        print("You Lost!!")
        print("Your score was ", score)
    else :
        score = score + 1
        os.system('cls')

         