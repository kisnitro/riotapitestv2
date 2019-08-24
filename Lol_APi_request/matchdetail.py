import requests
import RiotConsts as Consts

dfile = open("apikey.txt", "r")
development_api_key = dfile.readline()
dfile.close()
summonername = str(input("Your summoner name:"))


#development_api_key = 'RGAPI-cd1d3fcf-c2ae-4c92-9eb8-f8b24a943ea7'
#delimeter
d = ";"

def request_matchdetail(matchId, region=Consts.REGIONS['europe_nordic_and_east'], version=Consts.API_VERSION['summoner']):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v' + version + '/matches/' + matchId + "?api_key=" + development_api_key
    print (URL)
    response = requests.get(URL)
    return response.json()

def main(): 
    filename = input("Champion's code:  ")
    f = filename + ".txt"  
    rownumber = int(input("Row number for the match: "))
    lineList = [line.rstrip('\n') for line in open(f, "r")]
    print(lineList[rownumber])
    r = request_matchdetail(lineList[rownumber])
    lista = r['participantIdentities']
    for x in lista:
        player = x['player']
        partId = x['participantId']       
        sum_name_id = player['summonerName'], partId 
        if sum_name_id == (summonername, partId):
            myid = sum_name_id
            print (myid, "\n")
    lista2 = r['participants']
    for y in lista2:
        ids = y['participantId']
        if ids == myid[1]:
            stats = y['stats']
            visionward = str(stats['visionWardsBoughtInGame'])
            visionScore = str(stats['visionScore'])
            kills = str(stats['kills'])
            wardsKilled = str(stats['wardsKilled'])
            assists = str(stats['assists'])
            win = str(stats['win'])
            deaths = str(stats['deaths'])
            wardsPlaced = str(stats['wardsPlaced']) 
    sor_egy = 'kills'+ d +'deaths'+ d +'assists'+ d +'visionScore'+ d +'wardsPlaced'+ d +'visionWardsBoughtInGame'+ d +'wardsKilled'+ d +'win' + "\n"
    sor_ketto = kills + d + deaths + d + assists + d + visionScore + d + wardsPlaced + d + visionward + d + wardsKilled + d + win+ "\n"
    print('Ready')
    if rownumber == 0:
        with open(filename + ".csv", "a+") as testfile1:
            testfile1.write(sor_egy)
            testfile1.write(sor_ketto)
    else:
        with open(filename + ".csv", "a+") as testfile1:
            testfile1.write(sor_ketto)
    folyt = int(input('1->Ujra 2->kilép'))
    if folyt == 1:
        main()
    else:
        exit()



        """
        testfile1.write(sor_egy)
        testfile1.write(sor_ketto)
        """

        """
        testfile1.write('Champion id: ' + filename + "")
        testfile1.write('kills: ' + kills + "")
        testfile1.write('deaths: ' + deaths + "")
        testfile1.write('assists: ' + assists + "")
        testfile1.write('visionScore: ' + visionScore + "")
        testfile1.write('wardsPlaced: ' + wardsPlaced + "")
        testfile1.write('visionWardsBoughtInGame: ' + visionward + "")
        testfile1.write('wardsKilled: ' + wardsKilled + "")
        testfile1.write('win: ' + win + "")
"""

            

    
          

    

    

"""
for 'summonerName' in player:
            if sum_name == 'ArmandHUN':
                partId = x['participantId']
"""





if __name__ == "__main__":
    main()
