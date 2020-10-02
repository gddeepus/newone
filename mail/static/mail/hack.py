from twilio.rest import Client 
 
account_sid = 'AC5ef024bb202a8fe8a0de728c221a264d' 
auth_token = 'c95f362bac3f90a8fc5c8f0a492e8153' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+16109474264',  
                              body='Dear Ankit,\nYour Video on PornHUB is successfully Uploaded. Your Credits will be stored in wallet. \nThanking you,\nTeam PornHUB',      
                              to='+917033704124' 
                          ) 
 
print(message.sid)