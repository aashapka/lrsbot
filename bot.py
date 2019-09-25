import config
import utils
import socket
import re
import time
import threading
from time import sleep
print('bot started')


s = socket.socket()
s.connect((config.HOST , config.PORT))
s.send('PASS {}\r\n'.format(config.PASS).encode('utf-8'))
s.send('NICK {}\r\n'.format(config.NICK).encode('utf-8'))
s.send('JOIN #{}\r\n'.format(config.CHAN).encode('utf-8'))
chat_msg = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
while True:
    res = s.recv(4096).decode('utf-8')

    if res == 'PING :tmi.twitch.tv\r\n':
        s.send(('PONG :tmi.twitch.tv\r\n').encode('utf-8'))
    else:
       try:
            name = re.search(r"\w+", res).group(0)
            msg = chat_msg.sub('', res)
            print(res)
            #if msg.strip() == '++' and (name in mods):
            #    utils.rip_plus(s)
            #elif msg.strip() == '--' and (name in mods):
            #    utils.rip_minus(s)
            #elif msg.strip() == '!r':
            #    utils.rip_print(s, name)
            #elif msg.strip().startswith('!mod+') and (name in mods):
            #    utils.addmod(s, name, msg.strip())
            #elif msg.strip().startswith('!boss') and (name in mods):
            #    utils.boss(s, msg.strip())
            if (msg.strip() == "гык" and name == 'aashapka'):
                s.send('PRIVMSG #{} : Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited Jebaited Jebaited Jebaited\r\n'.format(config.CHAN,name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
                s.send('PRIVMSG #{} : Jebaited\r\n'.format(config.CHAN, name).encode('utf-8'))
            if (msg.strip() == "!правила"):
                s.send('PRIVMSG #{} : Первое Правило чата Марадона 1-марадон всегда лох . Второе правило чата марадона 2-если я назвал тебя куколдом то я долбаеб\r\n'.format(config.CHAN, name).encode('utf-8'))
        except:
            None

        #i = 0
        #for x in msg.strip():
        #    if x.isupper():
        #        i+=1
        #percent = i/len(msg.strip())
        #print(percent)
        #if (percent > 0.49) and (msg.strip() not in smiles):
           # utils.timeout(s, name) 
        
        
        
        #if msg.strip() == 'grav+' and (name in mods):
        #    utils.rip_plus(s)
        #elif msg.strip() == 'grav-' and (name in mods):
        #    utils.rip_minus(s)
        #elif msg.strip() == '!rip':
        #    utils.rip_print(s, name)
        #elif msg.strip() == '!pasha' and (name in sosat):
         #   utils.pxs(s, name)
        #elif msg.strip().startswith('!хуй') == True:
        #    utils.fuck(s, name, msg)