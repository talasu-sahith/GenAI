seatType = input("please enter seat type : ").lower()

match seatType :
    case "sleeper":
        print("only non ac beds available")
    case "ac":
        print("only AC beds available")
    case "general":
        print("idi general ra puka")
    case "luxury":
        print("lux soap raasko aadapilla laga")
    case _:
        print("erripoooka")