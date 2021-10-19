samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
litera = input("Podaj jakas litere: ")
if litera in samogloski: #Sprawdzam czy podana litera znajduje sie w tablicy z samogloskami
    print("Litera",litera,"jest samogloska.",sep=" ")
else:
    print("Litera",litera,"jest spolgloska.",sep=" ")