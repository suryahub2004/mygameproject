answer = input("do yo want to play a this adventurous game? [yes/no] ")

if answer == "yes":
    
    print("that's great")
    print()
    answer = input("do you want to explore a cave or jungle [cave/jungle] ")

    if answer == "cave":
      print("you gone into cave and there is a aleeping bear")
      print()
      answer = input("do you want to run or fight [run/fight]")

      if answer == "fight":
          print("the bear is really strong and you died!")

      elif answer == "run":
          print("you ran away and you win")

      else:
          print("invalid option , you lose!")

    elif answer == "jungle":
        print("you meet  tiger and got eaten , you lose!")

    else:
        print("invalid option!")
    

else:
    print("but this is really a awesome game")
