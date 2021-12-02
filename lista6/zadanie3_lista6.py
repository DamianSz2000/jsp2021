def look_and_say(n):
    counter = 1
    lookandsay = ""
    sequence = "1"
    elements = ["1"]
    for _ in range(n):
        for i in range(len(sequence)):
            if i != len(sequence)-1:
                if sequence[i] == sequence[i+1]:
                    counter += 1
                else:
                    lookandsay += str(counter) + sequence[i]
                    counter = 1
            else:
                lookandsay += str(counter) + sequence[i]
                counter = 1
        elements.append(lookandsay)
        sequence = lookandsay
        lookandsay = ""
    return elements
        

sequence = int(input("Podaj ilosc elementow ciagu look and say: "))
print(look_and_say(sequence))