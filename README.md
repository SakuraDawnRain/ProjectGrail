# ProjectGrail

# run app
$env:FLASK_APP = "server.py"
python -m flask run

# player
- HP (0, 10]
- MP (0, 10]
Each player get a card at the beginning of his round.
Each player can equip with one weapon.
Each player can give one card to other palyer in one round.
Each player can receive one card in one round.
Giving will be processed in the beginning of the receiver's round.

# cards
- Action 行动
- Thing 物品
 - Emblem 纹章
 - Weapon/Relic 武器/圣器
 - Container 容器
 - Grail 圣杯
 - Potion 药水


# emblem
## 

# grail
grails can only get by synthesizing
grails are so powerful enough that only one grail can appear in one game
grail owner becomes the enemy of all other players

# weapon / relic
relic = weapon + enlightenment
enlightenment can be 

# container
no use but to synthesis a grail

# action
- attack
- enlighten
- synthesis

## attack
simple attack with brings HP damage
attack with magic cost MP
the value may be varied when equipped with weapons and emblems

## enlighten
player can enlighten container or weapon
enlightened weapons becomes a relic with strong power

## synthesis
grail = emblem + enlightened container 
or
grail = emblem + container + relic 

Warning: If a relic is used to synthesis a grail, it will disappear!

# Potion
## HP potion
+2 HP
## MP potion
+2 MP