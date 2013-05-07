######Copyright 2013 by Akshay Ratan <akshayratan@gmail.com>
     
from dwolla import DwollaUser
Dwolla = DwollaUser('OAUTH_TOKEN')
Dwolla.send_funds(1.00,'akshay_ratan@gmail.com', '812-734-7288',dest_type='Email')
