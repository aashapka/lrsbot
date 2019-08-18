import config
import urllib
import json
import time
#import thread
from time import sleep


def rip_plus(sock):
    file = open(r'grav.txt', 'r')
    rip_count = int(file.read())
    rip_count +=1
    file = open(r'grav.txt', 'w')
    file.write(str(rip_count));
    file.close()
    file = open(r'boss.txt', 'r')
    boss = file.read()
    file.close()
    #print('PRIVMSG #{} : {}:Саехель - {}:0\r\n'.format(config.CHAN, boss, rip_count))
    sock.send('PRIVMSG #{} : {}:Саэхель - {}:0 NotLikeThis\r\n'.format(config.CHAN , boss,  rip_count).encode('utf-8'))

def rip_minus(sock):
    file = open(r'grav.txt', 'r')
    rip_count = int(file.read())
    rip_count -= 1
    file = open(r'grav.txt', 'w')
    file.write(str(rip_count));
    file.close()
    file = open(r'boss.txt', 'r')
    boss = file.read()
    file.close()
    sock.send('PRIVMSG #{} : {}:Саэхель - {}:0 NotLikeThis \r\n'.format(config.CHAN, boss, rip_count).encode('utf-8'))

def rip_print(sock, name):
    file = open(r'grav.txt', 'r')
    rip_count = int(file.read())
    file.close()
    boss = open(r'boss.txt', 'r').read()
    sock.send('PRIVMSG #{} : @{}, {}:Саэхель - {}:0 NotLikeThis\r\n'.format(config.CHAN, name, boss,  rip_count).encode('utf-8'))


def timeout(sock, name):
     sock.send('PRIVMSG #{} :.timeout {} 1\r\n'.format(config.CHAN, name).encode('utf-8'))
     sock.send('PRIVMSG #{} : @{} не капси PixelBob\r\n'.format(config.CHAN, name).encode('utf-8'))
     
     
def addmod(sock, name, msg):
        newmod = msg[7:].lower()
        list = open(r'mods.txt', 'a')
        list.write(newmod + '\n')
        list.close()
        
        sock.send('PRIVMSG #{} : {}, теперь я подчиняюсь {}\r\n'.format(config.CHAN, name, newmod).encode('utf-8'))
        
def boss(sock, msg):
        bossname = msg[6:]
        list = open(r'boss.txt', 'w')
        list.write(bossname)
        list.close()
        file = open(r'grav.txt', 'w')
        file.write('0')
        file.close()
        sock.send('PRIVMSG #{} : Новый босс - {}\r\n'.format(config.CHAN, bossname).encode('utf-8'))