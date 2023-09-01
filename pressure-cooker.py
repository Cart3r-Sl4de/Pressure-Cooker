import pyautogui, time, sys
from pathlib import Path

## The sign/banner that displays when running (make the terminal aesthetic look delightful)
sign = "██████████████████████████████████████████████████████████████████████████████████████\n█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█▄─██─▄█▄─▄▄▀█▄─▄▄─███─▄▄▄─█─▄▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█\n██─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─██─██─███─▄─▄██─▄█▀███─███▀█─██─█─██─██─▄▀███─▄█▀██─▄─▄█\n▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀"

## Where the magic happens
def pressureCooker(nightmare):

    ## Ask if the user wants to have the program send the message with the enter key or mouse click
    ## Of course have a loop preventing incorrect query
    while True:
        clickOrEnter = input("Do you want the program to enter the input by pressing\na)enter\nb)mouse click\n[?] ")
        if clickOrEnter == "a" or clickOrEnter == "b":
            break
        else:
            print("[!] ERROR DETECTED: Incorrect input. Please input a or b\n\n")

    ## ask permutations and timing with input validator function
    permutations = input_validator_int("How many times do you wish to repeat this input?\n[?] ")
    timing = input_validator_int("Should there be a delay with the repeated input? If so, enter any amount of seconds. If not, just type 0\n[?] ")
    ## 
    finality = input("\nLast chance to change your mind!\nIf you enter \"y\" you will proceed and will have 12 seconds to select the text box of which you wish to enter into!\nEnter anything else to exit:\n[?] ")

    if finality == "y":
        print("Hop to it! The 12 seconds start now!")
        time.sleep(12)

        ## if the person asked that the query be from the text file, do the following
        if nightmare == "txtfile":
            script_location = Path(__file__).absolute().parent
            file_location = script_location / 'query.txt'
            try:
                ## for the range of requested permutations, write the query, and IF they want it to be entered with enter key,
                ## do so, but IF they prefer a mouse click, then mouse click
                for x in range(permutations):
                    for line in file_location.open("r"):
                        pyautogui.typewrite(line)
                        if clickOrEnter == "a":
                            pyautogui.press("enter")
                        elif clickOrEnter == "b":
                            pyautogui.click()
                        time.sleep(timing)
            except Exception as e:
                print(f"[!] ERROR DETECTED: {e}\n\n")
                sys.exit()

        ## if the user asked for just the line written when prompted to be what repeats, do the following
        else:
            ## for the range of requested permutations, write the query, and IF they want it to be entered with enter key,
            ## do so, but IF they prefer a mouse click, then mouse click
            for x in range(permutations):
                pyautogui.typewrite(nightmare)
                if clickOrEnter == "a":
                    pyautogui.press("enter")
                elif clickOrEnter == "b":
                    pyautogui.click()

                time.sleep(timing)

    else:
        print("Understandable, have a good day\n[!] EXITING")

## to prevent unnecessary redundancy, made a function to ensure that input is an integer
def input_validator_int(question):
    while True:
        try:
            result = int(input(question))
            ## if the result is less than 0, return 1. If not, return amount requested
            return 1 if result < 0 else result
        except KeyboardInterrupt:
            print("\n[!] EXITING DUE TO: User Termination")
            time.sleep(5)
            sys.exit()
        except:
            print("[!] ERROR DETECTED: Please input a number when asked\n\n")

def main():

    print(sign + "\nby Carter Slade\n\nGreetings, user of this lovely software!")

    while(True):
        try:
            query = input("I must ask, do you wish to source input from (type corresponding letter):\na)typing it in\nb)text file\n[?] ")

            if query == "a":
                query = input("Lively, type below your desired query (aka what you want repeated):\n[?] ")
                pressureCooker(query)

            elif query == "b":
                print("Delightful! Before we start, ensure query.txt is in the same folder as this program!")
                pressureCooker("txtfile")

            else:
                print("\n[!] EXITING DUE TO: typing something other than listed inputs.\nUnderstandable, have a good day!")
                time.sleep(7)
                
            break

        except KeyboardInterrupt:
            print("\n[!] EXITING DUE TO: User Termination")
            time.sleep(5)
            sys.exit()

        except:
            print("[!] ERROR DETECTED: Incorrect Input type.\nI kindly ask you apply the correct type of input when prompted!\n\n")

main()