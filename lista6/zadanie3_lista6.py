def look_and_say(n):
    counter = 1 #licznik
    lookandsay = "" #tymczasowa zmienna
    sequence = "1" #początkowy wyraz
    elements = ["1"] #tablica z elementami ciagu
    for _ in range(n): #ile elementow
        for i in range(len(sequence)): #iteruje po kazdym znaku obecnego wyrazu
            if i != len(sequence)-1: #jezeli iterujemy do znaku przedostatniego
                if sequence[i] == sequence[i+1]: #jezeli dwa kolejne znaki sa takie same
                    counter += 1 #licznik +1
                else: #jezeli nie to wypisuje licznik plus ten wyraz i przechodze do kolejnego znaku
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