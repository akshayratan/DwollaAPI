#This is a simple code to get the balance remaining in the Dwolla Account using Python and Dwolla APIs
# @Author:: Akshay Ratan <akshayratan@gmail.com>
from dwolla import DwollaUser
Dwolla = DwollaUser('OAUTH_TOKEN')
print Dwolla.get_balance()   #Dwolla Python package has this command

