from random import randint
import math
import random
import PokeSelection
movelist = ["tackle", "ember", "water gun", "vine whip", "flamethrower", "thunderbolt"]

moves = [
{
    'name' : "tackle",
    'power' : 40,
    'type' : "normal"
},
{
    'name' : "ember",
    'power' : 40,
    'type' : "fire"
},
{
    'name' : "water gun",
    'power' : 40,
    'type' : "water"
},
{
    'name' : "vine whip",
    'power' : 40,
    'type' : "grass"
},
{
    'name' : "flamethrower",
    'power' : 90,
    'type' : "fire"
},
{
    'name' : "thunderbolt",
    'power' : 90,
    'type' : "electric"
}
]


attackmultiplier = {

    'fire':{
        'fire' : 0.5,
        'grass' : 2,
        'water' : 0.5,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' : 0.5,
        'bug' : 2,
        'ghost' : 1,
        'steel' : 2,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 2,
        'dragon' : 0.5,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1

        },
    'grass':{
        'fire' : 0.5,
        'grass' : 0.5,
        'water' : 2,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 0.5,
        'poison' : 0.5,
        'ground' : 2,
        'rock' : 2,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 1,
        'dragon' : 0.5,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'water':{
        'fire' : 2,
        'grass' : 0.5,
        'water' : 0.5,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 1,
        'ground' : 2,
        'rock' : 2,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 1,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 1,
        'dragon' : 0.5,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'normal':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' : 0.5,
        'bug' : 1,
        'ghost' : 0,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'fighting':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 2,
        'fighting' : 1,
        'flying' : 0.5,
        'poison' : 0.5,
        'ground' : 1,
        'rock' : 2,
        'bug' : 0.5,
        'ghost' : 0,
        'steel' : 2,
        'electric' : 1,
        'psychic' : 0.5,
        'ice' : 2,
        'dragon' : 0.5,
        'dark' : 2,
        'fairy' : 0.5,
        'none' : 1
        },
    'flying':{
        'fire' : 1,
        'grass' : 2,
        'water' : 1,
        'normal' : 1,
        'fighting' : 2,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' :0.5,
        'bug' : 2,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 0.5,
        'psychic' : 0.5,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'poison':{
        'fire' : 1,
        'grass' : 2,
        'water' : 1,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 0.5,
        'ground' : 0.5,
        'rock' : 0.5,
        'bug' : 1,
        'ghost' : 0.5,
        'steel' : 0,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 1,
        'fairy' : 2,
        'none' : 1
        },
    
    'ground':{
        'fire' : 2,
        'grass' : 0.5,
        'water' : 1,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 0,
        'poison' : 2,
        'ground' : 1,
        'rock' : 2,
        'bug' : 0.5,
        'ghost' : 1,
        'steel' : 2,
        'electric' : 2,
        'psychic' : 1,
        'ice' : 2,
        'dragon' : 1,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'rock':{
        'fire' : 2,
        'grass' : 1,
        'water' : 1,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 2,
        'poison' : 1,
        'ground' : 0.5,
        'rock' : 0.5,
        'bug' : 2,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 2,
        'dragon' : 1,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
    },
    'bug':{
        'fire' : 0.5,
        'grass' : 2,
        'water' : 1,
        'normal' : 1,
        'fighting' : 0.5,
        'flying' : 0.5,
        'poison' : 0.5,
        'ground' : 1,
        'rock' : 1,
        'bug' : 1,
        'ghost' : 0.5,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 2,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 2,
        'fairy' : 0.5,
        'none' : 1
        },
    'ghost':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 0,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' : 1,
        'bug' : 1,
        'ghost' : 2,
        'steel' : 1,
        'electric' : 1,
        'psychic' : 2,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 0.5,
        'fairy' : 1,
        'none' : 1
        },
    'steel':{
        'fire' :0.5,
        'grass' : 1,
        'water' : 0.5,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' : 2,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 1,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 2,
        'dragon' : 1,
        'dark' : 1,
        'fairy' : 2,
        'none' : 1
        },
    'electric':{
        'fire' : 1,
        'grass' : 0.5,
        'water' : 2,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 2,
        'poison' : 1,
        'ground' : 0,
        'rock' : 0.5,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 0.5,
        'psychic' : 1,
        'ice' : 1,
        'dragon' : 0.5,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'psychic':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 1,
        'fighting' : 2,
        'flying' : 1,
        'poison' : 2,
        'ground' : 1,
        'rock' : 1,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 0.5,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 0,
        'fairy' : 1,
        'none' : 1
        },
    'ice':{
        'fire' : 0.5,
        'grass' : 2,
        'water' : 0.5,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 2,
        'poison' : 1,
        'ground' : 2,
        'rock' : 2,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 1,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 0.5,
        'dragon' : 2,
        'dark' : 1,
        'fairy' : 1,
        'none' : 1
        },
    'psychic':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 1,
        'fighting' : 2,
        'flying' : 1,
        'poison' : 2,
        'ground' : 1,
        'rock' : 1,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 0.5,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 0,
        'fairy' : 1,
        'none' : 1
        },
    'dragon':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 1,
        'fighting' : 1,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' : 1,
        'bug' : 1,
        'ghost' : 1,
        'steel' : 0.5,
        'electric' : 1,
        'psychic' : 1,
        'ice' : 1,
        'dragon' : 2,
        'dark' : 1,
        'fairy' : 0,
        'none' : 1
        },
    'dark':{
        'fire' : 1,
        'grass' : 1,
        'water' : 1,
        'normal' : 1,
        'fighting' : 0.5,
        'flying' : 1,
        'poison' : 1,
        'ground' : 1,
        'rock' : 1,
        'bug' : 1,
        'ghost' : 2,
        'steel' : 1,
        'electric' : 1,
        'psychic' : 2,
        'ice' : 1,
        'dragon' : 1,
        'dark' : 0.5,
        'fairy' : 0.5,
        'none' : 1
        }
    }
    

    
poke = [

{   'name' : "missingno"


},
{
    'name' : "bulbasaur",
    'num' : 1,
    'baseatk' : 49,
    'basedef' : 49,
    'basesdef' : 50,
    'basesatk' : 65,
    'basehp' : 45,
    'basespeed' : 45,
    'type1' : "grass",
    'type2' : "poison"
    
    
},
{
    'name' : "ivysaur",
    'baseatk' : 62,
    'basedef' : 63,
    'basesdef' : 80,
    'basesatk' : 80,
    'basehp' : 60,
    'basespeed' : 60,
    'type1' : "grass",
    'type2' : "poison",
    'num' : 2
    
},
{
    'name' : "venusaur",
    'baseatk' : 82,
    'basedef' : 83,
    'basesdef' : 100,
    'basesatk' : 100,
    'basehp' : 80,
    'basespeed' : 80,
    'type1' : "grass",
    'type2' : "poison",
    'num' : 3
    
},
{
    'name' : "charmander",
    'baseatk' : 52,
    'basedef' : 43,
    'basesdef' : 50,
    'basesatk' : 60,
    'basehp' : 39,
    'basespeed' : 65,
    'type1' : "fire",
    'type2' : "none",
    'num' : 4
},
{
    'name' : "charmeleon",
    'baseatk' : 64,
    'basedef' : 58,
    'basesdef' : 65,
    'basesatk' : 80,
    'basehp' : 58,
    'basespeed' : 80,
    'type1' : "fire",
    'type2' : "none",
    'num' : 5
},
{
    'name' : "charizard",
    'baseatk' : 84,
    'basedef' : 78,
    'basesdef' : 85,
    'basesatk' : 109,
    'basehp' : 78,
    'basespeed' : 100,
    'type1' : "fire",
    'type2' : "flying",
    'num' : 6
},
{
    'name' : "squirtle",
    'baseatk' : 48,
    'basedef' : 65,
    'basesdef' : 64,
    'basesatk' : 50,
    'basehp' : 44,
    'basespeed' : 43,
    'type1' : "water",
    'type2' : "none",
    'num' : 7
},
{
    'name' : "wartortle",
    'baseatk' : 63,
    'basedef' : 80,
    'basesdef' : 80,
    'basesatk' : 65,
    'basehp' : 59,
    'basespeed' : 58,
    'type1' : "water",
    'type2' : "none",
    'num' : 8
},
{
    'name' : "blastoise",
    'baseatk' : 83,
    'basedef' : 100,
    'basesdef' : 105,
    'basesatk' : 85,
    'basehp' : 79,
    'basespeed' : 78,
    'type1' : "water",
    'type2' : "none",
    'num' : 9
},
{
    'name' : "caterpie",
    'baseatk' : 30,
    'basedef' : 35,
    'basesdef' : 20,
    'basesatk' : 20,
    'basehp' : 45,
    'basespeed' : 45,
    'type1' : "bug",
    'type2' : "none",
    'num' : 10
},
{
    'name' : "metapod",
    'baseatk' : 20,
    'basedef' : 55,
    'basesdef' : 25,
    'basesatk' : 25,
    'basehp' : 50,
    'basespeed' : 30,
    'type1' : "bug",
    'type2' : "none",
    'num' : 11
},
{
    'name' : "butterfree",
    'baseatk' : 45,
    'basedef' : 50,
    'basesdef' : 80,
    'basesatk' : 90,
    'basehp' : 60,
    'basespeed' : 70,
    'type1' : "bug",
    'type2' : "flying",
    'num' : 12
},
{
    'name' : "weedle",
    'baseatk' : 35,
    'basedef' : 30,
    'basesdef' : 20,
    'basesatk' : 20,
    'basehp' : 40,
    'basespeed' : 50,
    'type1' : "bug",
    'type2' : "poison",
    'num' : 13
},
{
    'name' : "kakuna",
    'baseatk' : 25,
    'basedef' : 50,
    'basesdef' : 25,
    'basesatk' : 25,
    'basehp' : 45,
    'basespeed' : 35,
    'type1' : "bug",
    'type2' : "poison",
    'num' : 14
},
{
    'name' : "beedrill",
    'baseatk' : 90,
    'basedef' : 40,
    'basesdef' : 80,
    'basesatk' : 45,
    'basehp' : 65,
    'basespeed' : 75,
    'type1' : "bug",
    'type2' : "poison",
    'num' : 15
},
{
    'name' : "pidgey",
    'baseatk' : 45,
    'basedef' : 40,
    'basesdef' : 35,
    'basesatk' : 35,
    'basehp' : 40,
    'basespeed' : 56,
    'type1' : "normal",
    'type2' : "flying",
    'num' : 16
},
{
    'name' : "pidgeotto",
    'baseatk' : 60,
    'basedef' : 55,
    'basesdef' : 50,
    'basesatk' : 50,
    'basehp' : 63,
    'basespeed' : 71,
    'type1' : "normal",
    'type2' : "flying",
    'num' : 17
},
{
    'name' : "pidgeot",
    'baseatk' : 80,
    'basedef' : 75,
    'basesdef' : 70,
    'basesatk' : 70,
    'basehp' : 83,
    'basespeed' : 101,
    'type1' : "normal",
    'type2' : "flying",
    'num' : 18
},
{
    'name' : "rattata",
    'baseatk' : 56,
    'basedef' : 35,
    'basesdef' : 35,
    'basesatk' : 25,
    'basehp' : 30,
    'basespeed' : 72,
    'type1' : "normal",
    'type2' : "none",
    'num' : 19
},
{
    'name' : "raticate",
    'baseatk' : 81,
    'basedef' : 60,
    'basesdef' : 70,
    'basesatk' : 50,
    'basehp' : 55,
    'basespeed' : 97,
    'type1' : "normal",
    'type2' : "none",
    'num' : 20
},
{
    'name' : "spearow",
    'baseatk' : 60,
    'basedef' : 30,
    'basesdef' : 31,
    'basesatk' : 31,
    'basehp' : 40,
    'basespeed' : 70,
    'type1' : "normal",
    'type2' : "flying",
    'num' : 21
},
{
    'name' : "fearow",
    'baseatk' : 90,
    'basedef' : 65,
    'basesdef' : 61,
    'basesatk' : 61,
    'basehp' : 65,
    'basespeed' : 100,
    'type1' : "normal",
    'type2' : "flying",
    'num' : 22
},
{
    'name' : "ekans",
    'baseatk' : 60,
    'basedef' : 44,
    'basesdef' : 54,
    'basesatk' : 40,
    'basehp' : 35,
    'basespeed' : 55,
    'type1' : "poison",
    'type2' : "none",
    'num' : 23
},
{
    'name' : "arbok",
    'baseatk' : 95,
    'basedef' : 69,
    'basesdef' : 79,
    'basesatk' : 65,
    'basehp' : 60,
    'basespeed' : 80,
    'type1' : "poison",
    'type2' : "none",
    'num' : 24
},
{
    'name' : "pikachu",
    'baseatk' : 55,
    'basedef' : 40,
    'basesdef' : 50,
    'basesatk' : 50,
    'basehp' : 35,
    'basespeed' : 90,
    'type1' : "electric",
    'type2' : "none",
    'num' : 25
},
{
    'name' : "raichu",
    'baseatk' : 90,
    'basedef' : 55,
    'basesdef' : 80,
    'basesatk' : 90,
    'basehp' : 60,
    'basespeed' : 110,
    'type1' : "electric",
    'type2' : "none",
    'num' : 26
},
{
    'name' : "sandshrew",
    'baseatk' : 75,
    'basedef' : 85,
    'basesdef' : 30,
    'basesatk' : 20,
    'basehp' : 50,
    'basespeed' : 40,
    'type1' : "ground",
    'type2' : "none",
    'num' : 27
},
{
    'name' : "sandslash",
    'baseatk' : 100,
    'basedef' : 110,
    'basesdef' : 55,
    'basesatk' : 45,
    'basehp' : 75,
    'basespeed' : 65,
    'type1' : "ground",
    'type2' : "none",
    'num' : 28
},
{
    'name' : "nidoranf",
    'baseatk' : 47,
    'basedef' : 52,
    'basesdef' : 40,
    'basesatk' : 40,
    'basehp' : 55,
    'basespeed' : 41,
    'type1' : "poison",
    'type2' : "none",
    'num' : 29
},
{
    'name' : "nidorana",
    'baseatk' : 47,
    'basedef' : 52,
    'basesdef' : 40,
    'basesatk' : 40,
    'basehp' : 55,
    'basespeed' : 41,
    'type1' : "poison",
    'type2' : "none",
    'num' : 30
}
]

def calculatedamage(power, attack, defense, modifier, level):
    damage = ((((2 * level) / 5) + 2) * power * (attack / defense) / 50 + 2) * modifier
    damage = math.floor(damage)
    return damage

def calculatestat(base, level, iv, nature, ev):
    stat = ((((2 * base + iv + (ev / 4)) * level) / 100) + 5) * nature
    stat = math.floor(stat)
    return stat

def calculatehp(base, level, iv, ev):
    stat = (((2 * base + iv + (ev / 4)) * level) / 100) + level + 10
    stat = math.floor(stat)
    return stat
    

def calculatestatlightball(base, level, iv, nature, ev):
    stat = ((((2 * base + iv + (ev / 4)) * level) / 100) + 5) * nature
    stat = math.floor(stat)
    stat = stat * 2
    print(stat)

def effectiveness(movetype, type1, type2):
    effect = attackmultiplier[movetype][type1] * attackmultiplier[movetype][type2]
    return effect

def printeffectiveness(movetype, type1, type2):
    effect = attackmultiplier[movetype][type1] * attackmultiplier[movetype][type2]
    if effect >= 2:
        print("It's super effective!")
    elif effect <= 0.5:
        print("It's not very effective.")
    elif effect == 0:
        print("It didn't effect the enemy pokemon!")
    else:
        print("")
    return effect


def getPokeNum(name):
  for i in poke:
    if i ['name'] == name:
      return i['num']

def statget(name, stat):
    for i in poke:
        if i ['name'] == name:
            return i[stat]

def statGetAtk(name):
    for i in poke:
        if i ['name'] == name:
            return i['baseatk']

def statGetDef(name):
    for i in poke:
        if i ['name'] == name:
            return i['basedef']

def statGetSAtk(name):
    for i in poke:
        if i ['name'] == name:
            return i['basesatk']

def statGetSDef(name):
    for i in poke:
        if i ['name'] == name:
            return i['basesdef']

def statGetSpeed(name):
    for i in poke:
        if i ['name'] == name:
            return i['basespeed']

def statgethp(name):
    for i in poke:
        if i ['name'] == name:
            return i['basehp']
        
def GetEnemyPokemon(num):
    return poke[num]['name']
    
def getmovepower(name):
    for i in moves:
        if i ['name'] == name:
            return i['power']

def getmovetype(name):
    for i in moves:
        if i ['name'] == name:
            return i['type']

def getpoketype1stab(num, type1):
    stab = poke[num]['type1']
    if stab == type1:
        return 1.5
    else:
        return 1

def getpoketype2stab(num, type2):
    stab = poke[num]['type2']
    if stab == type2:
        return 1.5
    else:
        return 1


def getpoketype1(num):
    return poke[num]['type1']

def getpoketype2(num):
    return poke[num]['type2']

def setupGame():
    pokemon = PokeSelection.pokemon
    pokemonlevel = randint(1,100)
