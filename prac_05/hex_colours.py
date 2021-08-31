

HEX_COLOURS = {"Black": "#000000", "Brown": "#a52a2a", "CadetBlue1": "#98f5ff", "Chatreuse1": "#7fff00", "Cyan1": "#00ffff",
               "DarkGoldenRod1": "#ffb90f", "DarkGreen": "#006400", "DarkOrchid": "#9932cc", "DodgerBlue1": "#1e90ff", "White": "#ffffff"}
print(HEX_COLOURS)

for key, value in HEX_COLOURS.items():
    print(f"{key:<14} is {value}")

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(colour_name, "is", HEX_COLOURS[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
