with open("shop.txt") as file:
    for line in file:
        line = line.strip().split()
        
        if len(line) != 0:
            #print(line)
            if line[0] == "Weapons:":
                weapons = {}
                mode = 'w'
            elif line[0] == "Armor:":
                armour = {}
                mode = 'a'
            elif line[0] == "Rings:":
                rings = {}
                mode = 'r'
            elif mode == 'w':
                weapons[line[0]] = {'cost': int(line[1]), 'damage': int(line[2]), 'armour': int(line[3])}
            elif mode == 'a':
                armour[line[0]] = {'cost': int(line[1]), 'damage': int(line[2]), 'armour': int(line[3])}
            elif mode == 'r':
               rings[line[0]+ line[1]] = {'cost': int(line[2]), 'damage': int(line[3]), 'armour': int(line[4])}
print(weapons,armour, rings)

boss = {'hit': 104, 'damage': 8, 'armour': 1}
me = {'hit': 100, 'damage': 0, 'armour': 0}
#test
#boss = {'hit': 12, 'damage': 7, 'armour': 2}
#me = {'hit': 8, 'damage': 5, 'armour': 5}

def battle(boss,me):
    print(boss, me)
    boss['hit'] = 104
    me['hit'] = 100
    while boss['hit'] > 0 and me['hit'] > 0:
        # my go
        boss_damage = me['damage'] - boss['armour']
        if boss_damage < 1:
            boss_damage = 1
        boss['hit'] = boss['hit'] - boss_damage
        # boss go
        if boss['hit'] > 0 and me['hit'] > 0: # check nobody has lost
            me_damage = boss['damage'] - me['armour']
            if me_damage < 1:
                me_damage = 1
            me['hit'] = me['hit'] - me_damage
        else: # only boss hit has changed so I must have won
            print("I win")
            return('me')
        print("scores:",boss['hit'], me['hit'])
    print("boss wins")
    return('boss')
       # print(boss['hit'], me['hit'])

# pick weapon
wins = []
gold_spent = 0
for w in weapons.keys():
    print(w)
    gold_spent = weapons[w]['cost']
    me['damage'] = weapons[w]['damage']
    me['armour'] = 0
    if battle(boss,me) == 'me':
        wins.append(gold_spent)
        print(gold_spent)
    else: #  didn't win with a weapon so add just some armour
        for a in armour.keys():
            print("----",a)
            gold_spent = weapons[w]['cost'] + armour[a]['cost']
            me['armour'] = armour[a]['armour']
            
            if battle(boss,me) == 'me':
                wins.append(gold_spent)
                print(gold_spent)
            else: # still didn't win so now add a ring
                for r in rings.keys():
                    print("+++++++++++++", r)
                    gold_spent = weapons[w]['cost'] + armour[a]['cost'] + rings[r]['cost']
                    me['damage'] = weapons[w]['damage'] + rings[r]['damage']
                    me['armour'] = armour[a]['armour'] + rings[r]['armour']
                    
                    if battle(boss,me) == 'me':
                        wins.append(gold_spent)
                        print(gold_spent)
                    else: # still didn't win so add a second ring
                        for r2 in rings.keys():
                            if r2 != r: # can't have two of same ring
                                print("++++++++++++++++++++++++++++", r2)
                                gold_spent = weapons[w]['cost'] + armour[a]['cost'] + rings[r]['cost'] + rings[r2]['cost']
                                me['damage'] = weapons[w]['damage'] + rings[r]['damage'] + rings[r2]['damage']
                                me['armour'] = armour[a]['armour'] + rings[r]['armour'] + rings[r2]['armour']
                                
                                if battle(boss,me) == 'me':
                                    wins.append(gold_spent)
                                    print(gold_spent)
        # now try rings but no armour
        for r in rings.keys():
            gold_spent = weapons[w]['cost'] + rings[r]['cost']
            me['damage'] = weapons[w]['damage'] + rings[r]['damage']
            me['armour'] = rings[r]['armour']
            if battle(boss,me) == 'me':
                wins.append(gold_spent)
                print(gold_spent)
            else: # didn't win so add a second ring
                for r2 in rings.keys():
                    if r2 != r: # can't have two of same ring
                        gold_spent = weapons[w]['cost'] + rings[r]['cost'] + rings[r2]['cost']
                        me['damage'] = weapons[w]['damage'] + rings[r]['damage'] + rings[r2]['damage']
                        me['armour'] = rings[r]['armour'] + rings[r2]['armour']
                        if battle(boss,me) == 'me':
                            wins.append(gold_spent)
                            print(gold_spent)
        # now try rings but no armour                        
print(wins)
print(min(wins))



#print("winner:",battle(boss,me))
