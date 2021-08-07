alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

rotorSettings = [1, 1, 1]

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25]

def rotate(integers, k):
    temp = integers[:k]
    integers = integers[k:] + temp
    return integers

def takeSettings():
    global rotorSettings
    global plugboardSettings

    print("Enter rotor settings (3 space separated integers) (between 1 and 26)")
    rotorSettings = list(map(int, input("Rotor settings: ").split()))
    print("Enter plugboard settings (max 10 pairs of characters) (Format: A/Z T/S O/Y")
    plugboardSettings = input("Plugboard settings: ").split()
    for i in range(len(plugboardSettings)):
        temp = plugboardSettings[i].split("/")
        plugboardSettings[i] = temp
    
def reflector(index):
    if index < 14:
        return index + 13
    return index - 13

def incrementRotor():
    global rotorSettings
    settings = rotorSettings

    if settings[2] < 26:
        settings[2] = settings[2] + 1
    else:
        if settings[1] < 26:
            settings[1] = settings[1] + 1
            settings[2] = 1
        else:
            if settings[0] < 26:
                settings[0] = settings[0] + 1
                settings[1] = 1
                settings[2] = 1
            else:
                settings[0] = settings[1] = settings[2] = 1
    rotorSettings = settings       

def rotorbox(settings, rotor1, rotor2, rotor3, char):
    index = alpha.index(char)

    l1 = rotate(integers, settings[0]-1)
    l2 = rotate(integers, settings[1]-1)
    l3 = rotate(integers, settings[2]-1)

    print("\n\n the integers:\n")
    print(l1)
    print(l2)
    print(l3)
    print('\n')

    print(f"char position: {index}")
    for i in rotor3:
        if i[0] == l3[index]:
            index3 = l3.index(i[1])
            break
    print(f"index3: {index3}")
    for i in rotor2:
        if i[0] == l2[index3]:
            index2 = l2.index(i[1])
            break
    print(f"index2: {index2}")
    for i in rotor1:
        if i[0] == l1[index2]:
            index1 = l1.index(i[1])
            break
    print(f"index1: {index1}")
    index = reflector(index1)
    print(f"reflector index: {index}")
    for i in rotor1:
        if i[1] == l1[index]:
            index1 = l1.index(i[0])
            break
    print(f"index1: {index1}")
    for i in rotor2:
        if i[1] == l2[index1]:
            index2 = l2.index(i[0])
    print(f"index2: {index2}")
    for i in rotor3:
        if i[1] == l3[index2]:
            index3 = l3.index(i[0])
    print(f"index3: {index3}")
    print("\n\n")
    # add a rotor increment function
    incrementRotor()

    return alpha[index3]  

def plugboard(settings, char):
    for i in settings:
        for j in range(2):
            if char == i[j]:
                return i[int(j==0)]
    return char

def encrypt(message, rotor1, rotor2, rotor3):
    st = ""
    for i in message:
        ch = plugboard(plugboardSettings, i)
        ch = rotorbox(rotorSettings, rotor1, rotor2, rotor3, ch)
        ch = plugboard(plugboardSettings, ch)
        st += ch
    return st

def main():
    takeSettings()
    print(plugboardSettings)
    print(rotorSettings)

    rotor1 = [[0, 15], [1, 9], [2, 11], [3, 25], [4, 16], [5, 6], [6, 19], [7, 21], [8, 5], 
              [9, 12], [10, 23], [11, 13], [12, 4], [13, 7], [14, 10], [15, 2], [16, 14], 
              [17, 3], [18, 17], [19, 0], [20, 1], [21, 22], [22, 20], [23, 18], [24, 24], [25, 8]]

    rotor2 = [[0, 7], [1, 0], [2, 12], [3, 6], [4, 2], [5, 21], [6, 14], [7, 20], [8, 18], 
              [9, 24], [10, 17], [11, 15], [12, 19], [13, 23], [14, 3], [15, 10], [16, 13], 
              [17, 16], [18, 9], [19, 1], [20, 11], [21, 22], [22, 25], [23, 4], [24, 8], [25, 5]]

    rotor3 = [[0, 21], [1, 8], [2, 9], [3, 23], [4, 10], [5, 3], [6, 17], [7, 13], [8, 5],
              [9, 11], [10, 25], [11, 24], [12, 15], [13, 1], [14, 14], [15, 7], [16, 18], 
              [17, 19], [18, 2], [19, 6], [20, 16], [21, 22], [22, 0], [23, 20], [24, 12], [25, 4]]

    rotor4 = [[0, 5], [1, 3], [2, 13], [3, 7], [4, 10], [5, 24], [6, 8], [7, 0], [8, 22], 
              [9, 12], [10, 6], [11, 14], [12, 17], [13, 11], [14, 19], [15, 9], [16, 23], 
              [17, 4], [18, 1], [19, 21], [20, 15], [21, 25], [22, 16], [23, 20], [24, 18], [25, 2]]

    rotor5 = [[0, 5], [1, 22], [2, 20], [3, 18], [4, 0], [5, 10], [6, 7], [7, 17], [8, 2], 
              [9, 21], [10, 23], [11, 12], [12, 9], [13, 25], [14, 6], [15, 11], [16, 13], 
              [17, 4], [18, 8], [19, 1], [20, 3], [21, 15], [22, 24], [23, 14], [24, 19], [25, 16]]


    # message = "ALANTURING"
    message = input("Enter message: ")

    rotors = [rotor1, rotor2, rotor3, rotor4, rotor5]

    selectedRotors = list(map(int, input("There are 5 rotors with different wiring, choose any 3: ").split()))

    encryptedMessage = encrypt(message, rotors[selectedRotors[0]-1], rotors[selectedRotors[1]-1], rotors[selectedRotors[2]-1])

    print(encryptedMessage)

if __name__ == "__main__":
    main()