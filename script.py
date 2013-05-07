email = 'akshay_ratan@yahoo.com'

# Include the Dwolla REST Client
from dwolla import DwollaUser

# Instantiate a new Dwolla User client
# And, Seed a previously generated access token
Dwolla = DwollaUser('OAUTH_TOKEN')

transaction = Dwolla.send_funds(0.01, email, 'PIN', dest_type='Email')
print('Transaction ID: %s' % transaction)
