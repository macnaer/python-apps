exit = False
while not exit:
    choice = int(input("1. Youtube\n0. Exit\n=:->> "))
    if choice == 1:
        from lib.Youtube import Youtube
        youtube = Youtube()
        youtube.start()
    elif choice == 0:
        exit = True
        print("Bye!")
    else:
        print("Whong choice.")
