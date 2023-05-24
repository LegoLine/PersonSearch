####################################################################################

# importing required module
import urllib.parse
import requests
import json




class PersonSearch:

    # setting the base URL value
#baseUrl = "https://v6.exchangerate-api.com/v6/0f215802f0c83392e64ee40d/pair/"

    baseUrl = "https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&search="
    formatJson = "format=json"


    FirstName = input("Enter firstname: ")
    LastName = input("Enter  lastname: ")
    
    result = FirstName+"+"+LastName+"&"+formatJson
    final_url = baseUrl+result
    
    def personId():

    # retrieving data from JSON Data
        json_data = requests.get(PersonSearch.final_url).json()
        Final_result = json_data['search'][0]['id']
        
        #print("Conversion rate from "+FirstName+" to "+LastName+" = ", Final_result)
        print("Søkeresultat: "+PersonSearch.FirstName+" "+PersonSearch.LastName+" = ", json.dumps(Final_result, indent=4))

    def personDisplayInfo():

    # retrieving data from JSON Data
        json_data = requests.get(PersonSearch.final_url).json()
        Final_result = json_data['search']#[0]['display']
            
        #print("Conversion rate from "+FirstName+" to "+LastName+" = ", Final_result)
        print("Søkeresultat: "+PersonSearch.FirstName+" "+PersonSearch.LastName+" = ", json.dumps(Final_result, indent=4))


#PersonSearch.personId()

    def testingOut():

    # retrieving data from JSON Data
        json_data = requests.get(PersonSearch.final_url).json()
        #input_search = input("Enter searchlevel info you want to get: ")
#        search_result = json_data['search'][0][input_search]
        search_result = json_data  #['search'][0][input_search]
        Final_result = search_result

        for x in Final_result:
            print("xxxxxxxxxxxxxxxxxxxxx\nSøkeresultat: "+PersonSearch.FirstName+" "+PersonSearch.LastName+" =\n", json.dumps(Final_result, indent=4))


'''
            print(""Søkeresultat: "+PersonSearch.FirstName+" "+PersonSearch.LastName+" "+str(search_result)+" =", Final_result)


        if Final_result == False: 
            print("Søkeresultat: "+PersonSearch.FirstName+" "+PersonSearch.LastName+" "+str(search_result)+" =", Final_result)
        else:
            print("Sorry, you've got to try again")
'''

#PersonSearch.testingOut()
#PersonSearch.personId()
PersonSearch.personDisplayInfo()