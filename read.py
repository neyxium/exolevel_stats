import json
from operator import truediv
from pickle import TRUE
from re import T
from collections import Counter
import time

  
# Opening JSON file
f = open('data.json')
# Clearing the file
p = open("logs.txt", "w")
p.write("")
p.close 
levels = json.load(f)

# Counting the amount of levels
userLevelCounter = {}
userid_to_username = {}
for level in levels['levels']:
    userid = level['userId']
    username = level['userName']
    if userid not in userLevelCounter:
        userLevelCounter[userid] = 0
        userid_to_username[userid] = username
    userLevelCounter[userid] += 1



# Sorting the dictionary
sorted_dict = sorted(userLevelCounter.items(), key=lambda kv: kv[1], reverse=False)

a = dict(Counter(userLevelCounter.values()))

a = sorted(a.items(), key=lambda kv: kv[0], reverse=False)

total_player = 0
total_maps = 0

# Printing the results
for key, value in dict(sorted_dict).items():
    total_player += 1
    total_maps += value
    file = open('logs.txt', 'a+')
    file.write(str(userid_to_username[key]) + ' : ' + str(value) + "\n")
    file.close()


for levelcount, frequency in a:
    print(levelcount, frequency)


# Typing the total amount of players and maps in file

file = open('logs.txt', 'a+')

file.write("______________________________________" + "\n")
file.write("total players with level editor " + str(total_player) + "\n")
file.write("total map count " + str(total_maps) + "\n")
file.write("avg levels per user " + str(round(total_maps/total_player)) + "\n")
file.write(str(a) + "\n")
file.write("______________________________________" + "\n")
file.close()

# Closing the file
f.close()
    total_player += 1
    total_maps += value
    file = open('logs.txt', 'a+')
    file.write(str(userid_to_username[key]) + ' : ' + str(value) + "\n")
    file.close()


# Typing the total amount of players and maps in file

file = open('logs.txt', 'a+')
file.write("______________________________________" + "\n")
file.write("total players with level editor " + str(total_player) + "\n")
file.write("total map count " + str(total_maps) + "\n")
file.write("avg levels per user " + str(round(total_maps/total_player)) + "\n")
file.write("______________________________________" + "\n")
file.close()

# Closing the file
f.close()
