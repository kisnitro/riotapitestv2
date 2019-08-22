import RiotAPI
from RiotAPI import RiotAPI
import requests
import RiotConsts as Consts

#development_api_key = input("Enter your api-key: ")
development_api_key = 'RGAPI-cd1d3fcf-c2ae-4c92-9eb8-f8b24a943ea7'
#matchlist request
def request_matchlist(accountId, champion, region=Consts.REGIONS['europe_nordic_and_east'], version=Consts.API_VERSION['summoner']):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v' + version + '/matchlists/by-account/' + accountId + '?champion=' + champion + "&api_key=" + development_api_key
    print (URL)
    response = requests.get(URL)
    return response.json()
#main
def main():
    api = RiotAPI(development_api_key)
    r = api.get_summoner_by_name('ArmandHUN')
    accountId = r['accountId']
    print ('AccountID:', r['accountId'], '\n', 'id:', r['id'] )
    print("1 => Tovább")
    gomb = int(input())
#Kilépési lehetőség
    if gomb == 1:
        print ("AccountId: " + accountId) 
        champion = int(input("Champion's code: "))
        r = request_matchlist(accountId, champion)
        lista = r['matches']
        lista2 = lista[0]
        gameId = lista2['gameId']
        print (gameId)
        f = open(champion + ".txt", "a")
        new_gameId = str(gameId) + '\n'
        newline = str(new_gameId)
        f.write(newline)
        f.close()
        print ("Total games played with this champion: ", r['totalGames'])

    else:
        exit()
   

if __name__ == "__main__":
    main()




"""
        f = open(champion + ".txt", "w+")
        f.write(str(r['matches']))
        f.close()

"""
