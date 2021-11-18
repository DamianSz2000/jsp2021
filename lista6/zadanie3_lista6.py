def look_and_say(n):
    list_of_elements = ["1"]
    last_element = "1"
    for element in range(n):
        counter = 1
        for char in range(len(last_element)-1):
            if(last_element[char+1] == last_element[char]):
                counter += 1
            else:
                counter = 1
                list_of_elements.append(str(counter)+last_element[char])
                last_element = str(counter)+last_element[char]
    return list_of_elements

print(look_and_say(5))


