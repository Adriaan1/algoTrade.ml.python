import numpy
from scipy import stats
from modules import controler

# To compile, us Auto Py to Exe:
# Step 1 - install Auto Py to Exe, if not already done
# To install the application run this line in cmd:
# pip install auto-py-to-exe
# To open the application run this line in cmd:
# auto-py-to-exe
# Step 2 - read the rest of the steps here:
# https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi

switch = 2

# Mean, Median, Mode
if switch == 1 :
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    x = numpy.median(speed)
    print(x)
    x = stats.mode(speed)
    print(x)

# Standard Deviation - distance from Mean
elif switch == 2 :
    speed = [86,87,88,86,87,85,86]
    print("speed = [86,87,88,86,87,85,86]")
    print("Mean = ", numpy.mean(speed))
    print("Standard Deviation = ", numpy.std(speed))

    print("")

    speed = [32,111,138,28,59,77,97]
    print("speed = [32,111,138,28,59,77,97]")
    print("Mean = ", numpy.mean(speed))
    print("Standard Deviation = ", numpy.std(speed))

controler.app()