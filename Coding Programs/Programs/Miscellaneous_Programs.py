# Miscellaneous Programs

""" 
Which of the following would create a list of negative even 
numbers from -100 to 0 (-100 included and 0 not included)? 
"""

list(range(-100, -1, 2))			# Method 1

sorted(set(range(-2, -101, -2)))	# Method 2

l = []
for i in range(-100, 0):			# Method 3
    if(i % 2 == 0):
        l.append(i)


# Min & Max of Dictionary Values

netflix = {'The Debt Collector': 1821195, 'Act of Vengeance': 2804479, 'Paradise Lost': 2195477, "Gerald's Game": 3650626, 'Long Shot': 638440, 'Mak Cun': 1010311, 'Our Souls at Night': 3028705, 'Out of Thin Air': 2681938, "Paul Hollywood's Big Continental Road Trip": 230689, 'Satu Hari': 1012350, 'Monster High: Boo York, Boo York': 1526025, 'Cultivating the Seas: History and Future of the Full-Cycle Cultured Kindai Tuna': 2762103, 'Domino': 872663, 'TUNA GIRL': 2574816, '5CM': 2647713, 'Animal World': 220789, 'Hold the Dark': 2307432, 'Lessons from a School Shooting: Notes from Dunblane': 2419534, 'Made in Mexico': 3653712, 'Single': 239278, 'The 3rd Eye': 196138, 'The Sinking Of Van Der Wijck': 2831856, 'Two Catalonias': 1337119, 'Bobby Sands: 66 Days': 2005623, 'Bard of Blood': 744998, 'Deliha 2': 3638900, 'Dragons: Rescue Riders': 3241239, 'In the Shadow of the Moon': 1213329, 'Skylines': 1840094, 'Sturgill Simpson Presents Sound & Fury': 1915540, 'The Politician': 1019394, 'Weeds on Fire': 2273090, 'Much Loved': 3039852, 'Joseph: King of Dreams': 1734449, 'Malaal': 1926128, 'The Grandmaster': 2549410, 'The Inmate': 130965, 'The Hurricane Heist': 2191538, 'Def Comedy Jam 25': 1392697, 'Restless Creature: Wendy Whelan': 2474412, 'Print the Legend': 548250, 'Birders': 3478883, 'Furie': 2755115, 'Leap!': 1401638, 'Oh! Baby (Malayalam)': 839139, 'Oh! Baby (Tamil)': 2691505, 'USS Indianapolis: Men of Courage': 3286014, 'A Wrinkle in Time': 1258861, 'Teach Us All': 2428947, 'White Island': 1152905, 'Inside Man: Most Wanted': 2812661, 'Jeff Dunham: Beside Himself': 2930368, 'China Salesman': 3377292, 'Swearnet: The Movie': 949689, 'The Bar': 620655, 'Manmadhudu 2': 1842761, 'Team Kaylie': 359856, 'Under the Eiffel Tower': 2298237, 'Audrie & Daisy': 1573055, 'Iliza Shlesinger: Confirmed Kills': 365220, 'BONDING': 1664242, 'Do Paise Ki Dhoop Chaar Aane Ki Baarish': 2770879, '20 Feet From Stardom': 2931730, 'In Darkness': 3248749, 'Gaga: Five Foot Two': 3719550, 'The Bad Batch': 3656264, 'SMOSH: The Movie': 3697506, 'King of Boys': 584112, 'Merry Men: The Real Yoruba Demons': 2035595, "Sarah's Key": 1337902, 'The Wedding Party 2: Destination Dubai': 1471204, 'Vagabond': 1600432, 'Battlefish': 723021, 'DRAGON PILOT: Hisone & Masotan': 602919, 'Hilda': 54948, 'Maniac': 1348196, 'Quincy': 2601704, 'Rafinha Bastos: Ultimatum': 3469996, 'The Good Cop': 2265521, 'Between Two Ferns: The Movie': 3146508, 'Criminal: France': 2021409, 'Criminal: Germany': 658824, 'Criminal: Spain': 3078634, 'Criminal: UK': 2721398, 'Daddy Issues': 2119035, "Inside Bill's Brain: Decoding Bill Gates": 1755104, 'The Hockey Girls': 2000507, 'Travel Mates 2': 707260, 'True: Tricky Treat Day': 3213199, 'Two Sentence Horror Stories': 2438329, 'Mad World': 2281773, 'Mobile Suit Gundam UC': 778879, 'The Bund': 1729892, 'The First Line': 674591, 'Maynard': 84986, 'Monkey Twins': 3277179, 'Bitcoin Heist': 1450158, 'I Am Not Madame Bovary': 2763830, 'Vincent N Roxxy': 1961810, "Chef's Table: France": 2065738} 
print("Most Popular: " + max(netflix, key = netflix.get))
print("Least Popular: " + min(netflix, key = netflix.get))