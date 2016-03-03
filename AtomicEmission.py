# Atomic Emission 
# This is a Ruby program to determine the Atomic Emisssion details 
# around Hydrogen. By exciting the electron into higher energy levels
# and measuring the Energy emitted afterwards when the electron returns 
# to lower energy levels it is possible to determine whether the energy
# levels are characterized by realtively high, medium or low energy.

# First we wish to welcome the user and prompt them for their E value in
# Scientific Notation. This will be a bit tricky since we will prompt for the 
# Numerical part and exponential part of the E value seperately then have the
# program assemble them into a single variable.
print('')
print('Welcome to the Amazing Atomic Emisssion application!')
print('This program will use the E value you measured and recorded in')
print('scientific Notation in order to determine the relative energy of')
print('the energy level transition along with also reporting the wavelength')
print('in meters and frequency in Hertz of the energy emission')
print('')

# First prompt for the significand, the inital number part of the scientific notation.
# and store the value as a variable named significand.
input('Please input the significand value (the number at the beginning) of your E value and press return.')
# Now prompt for the exponential power of the sci notation ans store it as a variable.
input('PLease input the exponential power of your E value ( the number 10 is raised to ) and press return.')

# Use the data inputs from the user to assemble a value for E.
E = significand * 10**exponent

# Now we will declare some variables.
# We will begin by declaring Plank's Constant
h = 6.62606876 * 10**(-34)
# We will also declare the speed of light in m/s to be the variable C.
c = 299792458.0

# Now divide E by h and store the value as v. This value v represents
# the frequency or cycles per second of the energy wave emitted.
v = E / h

# Divide C by v to determine the wavelength of a single cycle in meters.
# This value is then stored as the variable wavelength
wavelength = C / v

# Delaration of Visable Light and UV Limits for wavelength used to determine
# whether the energy emitted is low energy (IR), medium (vis light), or high (uv)
visLimit = 7 * 10**(-7)
uvLimit = 38 * 10**(-8)

# Also two lines to assign some ruby number formatting magic
# the two lines below will provide v and variable wavelength as floats in neat 3 digit scientific notation
vstring = ("%.2E" % (v))
lstring = ("%.2E" % (wavelength))

# Now run the comparisions and set variables based on results
if wavelength > visLimit:
	type = 'Low'          # A new block starts here this is the 'if' block
	range = 'infared'     # You can do lots of different things in a block
elif visLimit > wavelength and wavelength > uvLimit:  # this is the "elseif" block it only runs when the
   	type = 'medium'         # first "if" condition fails
   	range = 'Visable Light'
else:                # This is the "else" block this block is excuted
   type = 'High'         # when the "if" condition and any "elseif" conditions

   range = 'Ultra Violet'
 
                     
 # Return the data for the wavelength and frequency and type
print'' # These space only print statements are just for formatting
print('The frequency of the energy wave emitted was '+ vstring + ' Hertz (cycles/sec)')
print('')
print('The length of each wave was '+ lstring +'meters')
print('')
print('So based on the information above, it is determined')
print('that the energy emitted is ' + type + 'level in the' + range + ' range of the spectrum')
print('')
print('Thanks for using the Amazing Atomic Emisssion application!')
