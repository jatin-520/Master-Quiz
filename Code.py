import random

print("Welcome to Master Quiz game!")
print("What should I call you?")
name = input("")
print(f"Ok {name}, So let's start the game")
print("Answer these question fast!")

print("Every correct question will give you 1 point and incorrect will deduct 1 point")
print("Let's start the game")

point = 0

q1 = "Which country is the largest producer of coal in the world?"
q2 = "What is the world's longest railway tunnel in use?"
q3 = "What is the full form of UPSC?"
q4 = "What is the name of ISRO's new humanoid robot that will go to space next?"
q5 = "Who was the first female president of India?"
q6 = "Where is the headquarters of ISRO located?"
q7 = "Giddha is the folk dance of?"
q8 = "Who is the founder of ALIBABA?"
q9 = "Who was the first man to be given NOBLE PRIZE?"
q10 = "Which country gives the noble prize?"

c1 = "A: India    B: USA\nC: China    D: Japan"
c2 = "A: Gotthard tunnel  B: Bee Tunnel-Roaring Branch Trail\nC: None of the above    D: Both"
c3 = "A: Union Public Service Community B: Union Public Service Commision\nC: United Public Service Communists    D: None of the above"
c4 = "A: Vyommitra    B: Nagarjuna\nC: Tachikomas     D: None of the above"
c5 = "A: Nupur Shashtri    B: Pratibha Patil\nC: Indra Gandhi    D: None of the above"
c6 = "A: Bengaluru    B: New Delhi\nC: Chennai    D: Mumbai"
c7 = "A: Kerela    B: Tamil Nadu\nC: Punjab    D: None of the above"
c8 = "A: Jack ma    B: Jeff Bezos\nC: Sunil Aggrawal    D: None of the above"
c9 = "A: Sachin Tendulkar     B: Abdul Kalam\nC: Frédéric Passy    D: None of the above"
c10 = "A: India    B: Switzerland\nC: Sweden    D: Australia"

print(q1)
print(c1)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "c":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1

print(q2)
print(c2)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "a":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q3)
print(c3)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "b":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q4)
print(c4)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "a":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q5)
print(c5)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "b":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q6)
print(c6)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "a":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q7)
print(c7)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "c":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q8)
print(c8)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "a":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q9)
print(c9)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "c":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1
print(q10)
print(c10)

ch1 = input("Choose the correct option:\n")

if ch1.lower() == "c":
    print("Correct")
    point += 1

else:
    print("Wrong answer")
    point -= 1

if point<0:
    point=0
print(f"Your score was {point}")
print("Hope you enjoyed!")
print("Thanks for playing!")