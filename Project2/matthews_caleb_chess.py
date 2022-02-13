print("There is a popular myth about the man who invented chess.\nThe local ruler was so pleased with the invention that he offered the inventor a great reward in gold.")
print("The inventor suggested an alternative reward: he would get one grain of wheat on the first square of the chessboard,")
print("two grains on the second square, four on the third, eight on the fourth, and so on, \ndoubling the number of grains each time.")
print("The ruler saw that this must be a much better deal for him, and accepted. \nThe board has 64 squares.")

squares = 64
#total squares of a chessboard (could change this value for different games)
exponent = 0
#defining variable for exponent calculation
for i in range(0, 64, 1):
    i += 1
    exponent += i
#summing 0+1+2+3+4...64 for each exponent on 2 for each square of the board.

grain_num = 2**exponent
#taking 2 to the precalculated power to find total number of grains
print("The ruler had to pay",grain_num, "grains of wheat.\n\n\n")

#dividing total grains by 20 to get grams
print("This much wheat would weigh approximately",  grain_num//(20),"Grams\n\n\n")

#grain has a volume of .769 grams/cm^3 or 1.3 cm^3/gram so each grain is 0.065 cm^3 (divide by 10^15 for kilometers)
#quantity of grain x65/10^15 gives volume, divided by surface area to give us depth/height.
print("That's enough wheat to cover the state of Oregon", ((grain_num*65)//(10**15)), "kilometers deep.")