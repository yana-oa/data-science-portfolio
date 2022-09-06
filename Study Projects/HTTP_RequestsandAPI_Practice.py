import requests
url='https://www.ibm.com/'
r=requests.get(url)

# r is the response object
#here it shows the request information
r.status_code
print(r.request.headers)
print("request body:", r.request.body)

#This is the HTTP response information
header = r.headers
print(r.headers)

#Terminal
#header['date']
#header['Content-Type']

##As the Content-Type is text/html                    ##
##we can use the attribute text to display the HTML   ##
##in the body. We can review the first 100 characters:##

print(r.text[0:100])

#################
#Fruitvice API HTTP request
print("FRUITVICE API")
import requests
import json
import pandas as pd

fv_data = requests.get("https://www.fruityvice.com/api/fruit/all")
results = json.loads(fv_data.text)

fv_df = pd.DataFrame(results)
print(fv_df)

fv_df2 = pd.json_normalize(results)
print(fv_df2)

#getting scientific name function
#fruit = fv_df2.loc[fv_df2["name"] == 'Cherry']
#(fruit.iloc[0]['family']) , (fruit.iloc[0]['genus'])

a = 'Orange'

def sci_name_getter(a):
    fruit = fv_df2.loc[fv_df2["name"] == a]
    print((fruit.iloc[0]['family']) , (fruit.iloc[0]['genus']))
    return

sci_name_getter(a)

#################
#RandomUser API to Dataframe
print("RANDOMUSER API")
from randomuser import RandomUser
import pandas as pd

r = RandomUser()

users_list = r.generate_users(12)
print(users_list)

#Creating Dataset
name = r.get_full_name()
for user in users_list:
    print (user.get_full_name()," ",user.get_email())

def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),
                     "Gender":user.get_gender(),
                     "City":user.get_city(),
                     "State":user.get_state(),
                     "Email":user.get_email()})
    return pd.DataFrame(users)

Users_DF = get_users()
print(Users_DF)

##Now we have a pandas dataframe!


        
        
        
        
        
        
        
        
        
        
        
        