import pyautogui, time
from pathlib import Path

sign = "██████████████████████████████████████████████████████████████████████████████████████\n█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█▄─██─▄█▄─▄▄▀█▄─▄▄─███─▄▄▄─█─▄▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█\n██─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─██─██─███─▄─▄██─▄█▀███─███▀█─██─█─██─██─▄▀███─▄█▀██─▄─▄█\n▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀"

def pressureCooker(nightmare):

    permutations = int(input("How many times do you wish to repeat this input? "))
    permutations = 1 if permutations < 0 else permutations
    finality = input("\nLast chance to change your mind!\nIf you enter \"y\" you will proceed and will have 12 seconds to select the text box of which you wish to enter into!\nEnter anything else to exit: ")

    if finality == "y":
        print("Hop to it! The 12 seconds start now!")
        time.sleep(12)

        if nightmare == "txtfile":
            script_location = Path(__file__).absolute().parent
            file_location = script_location / 'query.txt'
            try:
                for x in range(permutations):
                    for line in file_location.open("r"):
                        pyautogui.typewrite(line)
                        pyautogui.press("enter")
            except:
                print("problem is with the loop")

        else:
            for x in range(permutations):
                pyautogui.typewrite(nightmare)
                pyautogui.press("enter")

    else:
        print("Understandable, have a good day")

def main():

    print(sign + "\nby Carter Slade\n\nGreetings, user of this lovely software!")

    while(True):
        try:
            query = input("I must ask, do you wish to use input from (type corresponding letter):\na)typing it in\nb)from text file\n")

            if query == "a":
                query = input("Lively, type below your desired query:\n")
                pressureCooker(query)

            elif query == "b":
                print("Delightful! Before we start, ensure query.txt is in the same folder as this program!")
                pressureCooker("txtfile")

            else:
                print("Exiting due to typing something other than listed inputs.\nUnderstandable, have a good day!")
                time.sleep(7)
                
            break

        except:
            print("ERROR DETECTED: Incorrect Input type.\nI kindly ask you apply the correct type of input when prompted!\n\n")

main()