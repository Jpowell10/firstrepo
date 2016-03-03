# Get car A Name
A= raw_input ('please enter the name of the hybrid car: ')

B = raw_input ('please enter the name of the non hybrid car: ')
# Get car A price store as float variable 
PA=input('please enter the price of ' + A + ".")
# Get car B price store as float variable
PB=input('please enter the price of ' + B +".")
# subtract car B price from car A price store as retail cost difference variable 
CD=PA-PB
# Get average gas price variable store as average price variable
GP=input('please enter the average price of gasoline per gallon for your area ')
# Get combined mpg for car A store as variable
mpgA=input('please enter the average mpg for ' + A +".")
# Get combined mpg for car B store as variable
mpgB=input('please enter the average mpg for ' + B +".")
# Calculate average cost/mile for car A store as variable ACM
ACM= GP/mpgA
BCM= GP/mpgB
CMD= BCM-ACM
BEPM= CD/CMD
BEPMi=int(BEPM)
print('in order to get your money back by driving a' + A + " you have to drive %s miles." % (BEPMi))