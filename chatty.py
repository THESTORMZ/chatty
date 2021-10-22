import requests
import os

class bcolors:
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  HEADER = '\033[0m'

os.system('clear')
                                        
print("     `+yyyyyyyyyyyyyyyyyyyyyyyyyyy/`    ")
print("   `+s:                           /s+`  ")
print("  `/M.                             -M.  ")
print("  ./M.                             -M.  ")
print("  ./M.                             -M.  ")
print("  ./M.                             -M.  ")
print("  ./M.                             -M.  ")
print("  ./M.                             -M.  ")
print("  ./M.                             -M.  ")
print("  ./N.                            `:N`  ")
print("  `.-yo+++++++-   -+++++++++++++++o+     ") 
print("    `.:////++N+   sm/////////////:.     ")
print("          `-os:  /o+                    ")
print("          ./M.`-y:.                     ")
print("          :syyy+                        ")
print("         .-``                      ")
print("")
print("Welcome to Chatty")

print(chr(27)+'[2j')

Name = input("What is your name: ")

os.system('clear')

bname = "Chatty"

log = open("chat.log", "w")
log.write("")
while True:
  print(bcolors.HEADER)

  x = input(Name + ':')
  # NOTE: Even if you delete chat.log, there will be a new one created
  log = open("chat.log", "a")
  log.write(Name + ":" + x + "\n\n")

  if x == "!help":
    print(bcolors.WARNING + "Commands")
    print("!name - Change your username")
    print("!info - Lists creators")
    print("!clear - Clears screen")
    print("!bname - Change the bots name")

  elif x == "!name":
    print()
    Name = input(bcolors.WARNING + "Choose a new name: ")
    print()
    print("Name Changed")
    
    log.write("Name changed to " + Name + "\n\n")
    log.close()

  elif x == "!info":
    print(bcolors.WARNING + "Chatty V1 Credits")
    print("API: affiliateplus")
    print("UI: @ZippyGG")
    log.close()

  elif x == "!clear":
    os.system('clear')
    log.close()

  elif x == "!bname":
    print()
    bname = input(bcolors.WARNING + "Choose a new bot name: ")
    print()
    print("Bot Name Changed")

    log.write("Bot name changed to " + bname + "\n\n")
    log.close()
  else:
    x = x.replace(" ", "+")

    r = requests.get("https://api.affiliateplus.xyz/api/chatbot?message=" + x + "&botname=" + bname + "&ownername=" + Name + "&user=1")

    msg = str(r.content)
    
    log.write("api response: " + msg + "\n")

    msg = msg.replace("b", "", 1)
    msg = msg.replace("\'", "")
    msg = msg.replace("{", "")
    msg = msg.replace("}", "")
    msg = msg.replace("\"", "")
    msg = msg.replace("\\", "\'")
    msg = msg.replace("message", bname, 1)

    log.write(msg + "\n\n")
    log.close()

    print(chr(27)+'[2j')

    if msg == "Chatty:ERROR! No message supplied.":
      msg = msg.replace("Chatty:", "")
      print(bcolors.FAIL + msg)
    else:
      print(msg)