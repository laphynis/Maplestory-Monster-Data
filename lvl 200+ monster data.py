import requests

from bs4 import BeautifulSoup

import csv


#making a list of the level ranges to use in a loop for the url
urlList = ['201-210', '211-220', '221-230', '231-240', '241-250', '251-275']

#names of each area that will be assigned to a monster
area_names = ['Dark World Tree', 'Scrapyard', 'Vanishing Journey', 'Reverse City',
              'Chu Chu Island', 'Yum Yum Island', 'Lachelein', 'Arcana', 'Morass',
              'Esfera', 'Moonbridge', 'Labyrinth of Suffering', 'Limina']

#create a csv file for writing in. Create the header
consolidatedData = open('Consolidated Data.csv', 'w')
consolidatedData.write('Name,Level,HP,EXP,Area\n')

#use a loop to get data from urls where the only difference is the level range
for level in urlList:
    URL = 'https://strategywiki.org/wiki/MapleStory/Monsters/Level_{}'.format(level)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    #filter the information that contains only the table
    monsters = soup.find(id='mw-content-text')

    #find all information between <tr> and put it into a list
    monsterClass = monsters.find_all('tr')

    #exclude the first item of that list because it is the header
    updatedMonsters = monsterClass[1: ]

    mainList = []

    #loop for each element from the table that we extracted data from
    for monster in updatedMonsters:
        subList = []
        #name of monster is between <b>
        name = monster.find('b')
        #use get_text() function to remove the html tag 
        names = name.get_text()
        subList.append(names)
        
        #stats of the monster is between <li>
        stats = monster.find_all('li')

        #gets the description of the monster which includes its location
        list_desc = monster.find_all('td')
        desc = list_desc[2].get_text()
        
        #extract only level, hp, and exp data
        mainStats = [stats[i] for i in (0, 1, 5)]
        for element in mainStats:
            stat = element.get_text()
            subList.append(stat)

        #assigning the monster's area by checking the description
        for area in area_names:
            if area in desc:
                #moonbridge monsters also have esfera in its description
                if area == 'Esfera' and 'Moonbridge' in desc:
                    subList.append('Moonbridge')
                else:
                    subList.append(area)
            else:
                pass
        mainList.append(subList)

    #using a loop to iterate through each element and cleaning it up
    #for 
    for element in mainList:
        #excludes 'Level:' and returns only the level
        element[1] = element[1][7: ]

        #excludes 'HP:' and returns the HP numerical value without commas
        element[2] = element[2][3: ]
        element[2] = element[2].replace(',', '')

        #checks if the HP is an integer. some entries have non-numeric HP values
        #so this excludes it from the csv file.
        try:
            element[2] = int(element[2])
            
            #excludes 'EXP:' and returns the EXP numerical value without commas
            element[3] = element[3][5: ]
            element[3] = element[3].replace(',', '')

            if int(element[3]) > 1 and int(element[3]) < 1000000 and element[2] < 1000000000:
                consolidatedData.write('{},{},{},{},{}\n'
                                       .format(element[0], element[1],
                                               element[2], element[3],
                                               element[4]))
            else:
                pass
        except ValueError:
            continue

consolidatedData.close()
    
