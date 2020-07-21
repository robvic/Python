import requests
from requests.exceptions import HTTPError

apiKey = "82XyiwnujAR3AFBUH6neAWZjEtSvZkXbPEFdiRlKMCelEyryyQYecbjVVXbH"
realAPI = "https://api.worldtradingdata.com/api/v1/history?symbol=AAPL&sort=newest&api_token="
dummyAPI = "http://dummy.restapiexample.com/api/v1/employees"
response = requests.get(realAPI + apiKey)
if response:
    print('Success!')
else:
    print('An error has occurred.')

fileOutput = open("data.txt", "w")
fileOutput.writelines(response.text)
fileOutput.close()

