from configparser import ConfigParser
from threading import active_count
from time import sleep as swait
from os import system, name
from telegram import Api
from re import search
from sys import exit


THREADS = 400
LOGO = '''
__     ___                     _____    _
\ \   / (_) _____      _____  |_   _|__| | ___  __ _ _ __ __ _ _ __ ___
 \ \ / /| |/ _ \ \ /\ / / __|   | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \ _____
  \ V / | |  __/\ V  V /\__ \   | |  __/ |  __/ (_| | | | (_| | | | | | |_____|
   \_/  |_|\___| \_/\_/ |___/   |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_|
                                               |___/
                                                    ~ Telegram Auto Views V1 ~
                                                    ~ Dev: eRo HACK ~
                                                    ~ Ch: @EroHack0 ~
'''

error_file = open('errors.txt', 'a+', encoding='utf-8')
logger = lambda error: error_file.write(f'{error}\n')


def config_loader():
    try: 
        cfg = ConfigParser(interpolation=None)
        cfg.read("config.ini", encoding="utf-8")
        return (
            cfg["HTTP"].get("Sources").splitlines(), 
            cfg["SOCKS4"].get("Sources").splitlines(), 
            cfg["SOCKS5"].get("Sources").splitlines()
        )
    except KeyError: 
        print(' [ Error ] config.ini not found!')
        swait(3)
        exit()


def input_loader():
    url_input = search(r'(https?:\/\/t\.me\/)?([^/]+)/(\d+)', input(' [ INPUT ] Enter Post URL: '))
    if url_input: 
        _, channel, post = url_input.groups()
        return channel, post
    else: 
        print(' [ ERROR ] Channel Or Post Not Found!')
        swait(3)
        exit()


def display():
    print(' [ OUTPUT ] Started ( Wait few seconds to run threads )');swait(7)
    while int(active_count()) < THREADS-100: swait(0.05)
    system('cls' if name == 'nt' else 'clear')
    
    def inner():
        print(LOGO)
        print(f'''
    [ Live Views ]: {Api.real_views}

    [ Token Errors ]:   {Api.token_errors}
    [ Proxies Errors ]: {Api.proxy_errors}

    [ Threads ]: {active_count()}
        ''')
    
    return inner


