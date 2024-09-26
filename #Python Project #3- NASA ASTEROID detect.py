#Python Project #3- NASA ASTEROID detector
import requests # Library to make HTTP requests
import json 

#Make sure to always add an endpoint when setting an API 
def NASA_api_setup():
    API_KeY = 'aWpeM64caG5zNZiWOVu4al9csjcFjVTUOCmDsJX5' 
    #(When adding to GITHUB get rid of API key and put a substitute)
    NASA_URL = 'https://api.nasa.gov/neo/rest/v1/feed'
    return API_KeY, NASA_URL #Returns the API Key and URL which will be used later on in the code

# Part of the code that gets the asteroid data from the NASA API
def asteroid_data(API_Key, NASA_URL, start_date, end_date):
    # Dictionary for the request parameters which sets up values for each key
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'API_key': API_Key
    }
# HTTP GET requests to the NASA API
    response = requests.get(NASA_URL, params=params)
#Establish if or else statements
#If the requests is successful ie. status code 200, the code will save the data on json and return that an asteroid is near and if not then data is not recieved
    if response.status_code == 200:
        data = response.json() 
        return data['NEO']
    else:
        print((f"Error: Unable to retrieve data. Status Code: f{response.status_code}"))
        return None
#Main function of code that sets the start and end data strings
def main():
    API_Key, NASA_URL = NASA_api_setup() #calls NASA_api_setup to retrieve the API key and the url. The variables API_Key and NASA_URL now hold these values
    #Specify the range of time for which data needs to be obtained regarding NEO(near eatrth objects/asteroids)
    start_date = '2016-08-04' #Date is changed whenever you want the data
    end_date = '2016-08-16' #Data is changed whenever you want the data
#Calls the asteroid_data() function that was defined earlier make an HTTP GET requests to the NASA API, and if sucessful will return the data about the NEO's for the dates
    neo_data = asteroid_data(API_Key, start_date, NASA_URL, end_date)
#printing asteroid data
#After data is fetched, this is now checking if asteroid_data is not empty. If the data is valid then its enters this line of code to process and print info.
    if neo_data:  #checks if asteroid_data is not empty
        for date, asteroids in asteroid_data.items(): #intiates a loop that repeats over the ietms in the dictionary
            print(f"Date: {date}") #prints the key date for the repetition of the loop #the f-string allows the data var into the output text, giving you Date: 2022-08-04.
        for asteroid in asteroids: #another loop that repeats through each asteroid in the list of asteroids
            name = asteroid['name'] #retrieves the name of the asteroid by accessing the anme key in the dictionary
            estimated_diameter = asteroid['estimated diameter'] #retrieves the estimated diameter dictionary from the asteroid
            meters = estimated_diameter['meters']['estimated'] #lists the estimated diameter in meters by using the estimated diameter dictionary
            print(f" Name: {name}', Diamter: {meters:.2f} m") #prints info about the asteroid using an f-string to format the output

if __name__ == "__main__":
    main()
