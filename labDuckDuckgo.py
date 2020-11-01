#CSC-256-0002 Lab Duckduckgo
# #Problem description
#Find out if the name of presidents
#printing them using json
## name of the file labDuckDuckgo.py
### Sandhya Joshi
## date : Oct 24,2020


import requests
presidents =[]


# Get the requests from the url provided in the main
def getRequest(url):
    return requests.get(url).json()

def parseResponse(response):
    data=[]
    for element in response['RelatedTopics']: # loop through the RelatedTopics
        # this function takes the first url
        # split it based on the / character, get the last element and replace '_' with the blank spaces
        data.append(element['FirstURL'].split('/')[-1].replace('_',' '))
    print (data)
    return data

def displayResults(results):
    for element in results:
        print(element)

def main():
    URL = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1%22'
    response = getRequest(URL)
    presidents = parseResponse(response)
    displayResults(presidents)
"""
list = []
for pres in presidents:
    list.append((pres))
#print(list)
"""
if __name__ == '__main__':
    main()

