
file=open("devices.txt","a")

while True: 
    newItem = input("What is the name of the new device? ")

    if newItem != "exit": 
        file.write(newItem + "\n")
    else: 
        print("All done!")
        break

file.close()