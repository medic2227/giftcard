import os
import random
import sys
import string as strg

try:
    from luhn import verify
except ImportError:
    os.system('pip install luhn')
    from luhn import verify

try:
    from colorama import init, Fore
except ImportError:
    os.system('pip install colorama')
    from colorama import init, Fore

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

try:
    from art import text2art
except ImportError:
    os.system('pip install art')
    from art import text2art

headers = {'User-Agent': 'TikTok 17.4.0 rv:17yellow_to_red14 (iPhone; iOS 13.6.1; sv_SE) Cronet',
           'Connection': 'keep-alive'}

timeout = 60

def issue():
    os.system('clear')
    print(Fore.GREEN + text2art("Giftcard  Generator"))
    print(' ')
    print(Fore.GREEN + 'Giftcard Types:',
          Fore.GREEN + '\n1.  PSN Card\n2.  Playstore Giftcard\n3.  Roblox Giftcard\n4.  Amazon Giftcard\n5.  Netflix Giftcard\n6.  XBOX Giftcard\n7.  Itunes\n8.  Nitro-Gen\n9.  Tiktok\n10. EXIT')
    print(' ')
    gen = input(Fore.YELLOW + '[?] Which Giftcard type do you want to generate: ')
    print(' ')
    if gen == '1':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_psn in range(amount):
            psn_card = "".join(random.choices(character, k=12))
            url_code_psn = "https://web.np.playstation.com/api/graphql/v1/transact/wallets/vouchers/" + psn_card
            status = requests.get(url_code_psn)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {psn_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {psn_card}\n')
        sys.exit()

    elif gen == '2':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_playstore in range(amount):
            playstore_card = "".join(random.choices(character, k=12))
            url_code_playstore = "https://play.google.com/store/code/" + playstore_card
            status = requests.get(url_code_playstore)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {playstore_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {playstore_card}\n')
        sys.exit()

    elif gen == '3':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_roblox in range(amount):
            roblox_card = "".join(random.choices(character, k=12))
            url_code_roblox = "https://www.roblox.com/giftcards/redeem/" + roblox_card
            status = requests.get(url_code_roblox)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {roblox_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {roblox_card}\n')
        sys.exit()

    elif gen == '4':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_amazon in range(amount):
            amazon_card = "".join(random.choices(character, k=12))
            url_code_amazon = "https://www.amazon.com/gp/css/gc/balance?claimCode=" + amazon_card
            status = requests.get(url_code_amazon)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {amazon_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {amazon_card}\n')
        sys.exit()

    elif gen == '5':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_netflix in range(amount):
            netflix_card = "".join(random.choices(character, k=12))
            url_code_netflix = "https://www.netflix.com/redeem/" + netflix_card
            status = requests.get(url_code_netflix)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {netflix_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {netflix_card}\n')
        sys.exit()

    elif gen == '6':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_xbox in range(amount):
            xbox_card = "".join(random.choices(character, k=12))
            url_code_xbox = "https://www.microsoft.com/en-us/redeem/" + xbox_card
            status = requests.get(url_code_xbox)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {xbox_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {xbox_card}\n')
        sys.exit()

    elif gen == '7':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_itunes in range(amount):
            itunes_card = "".join(random.choices(character, k=12))
            url_code_itunes = "https://www.apple.com/redeem/" + itunes_card
            status = requests.get(url_code_itunes)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {itunes_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {itunes_card}\n')
        sys.exit()

    elif gen == '8':
        amount = input(Fore.YELLOW + '[?] How many links do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_nitro in range(amount):
            nitro_card = "".join(random.choices(character, k=12))
            url_code_nitro = "https://discord.com/billing/promotions/" + nitro_card
            status = requests.get(url_code_nitro)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {nitro_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {nitro_card}\n')
        sys.exit()

    elif gen == '9':
        amount = input(Fore.YELLOW + '[?] How many giftcards do you want to generate and check: ')
        print(' ')
        amount = int(amount)
        character = strg.ascii_letters + strg.digits
        for gen_tiktok in range(amount):
            tiktok_card = "".join(random.choices(character, k=12))
            url_code_tiktok = "https://www.tiktok.com/redeem/" + tiktok_card
            status = requests.get(url_code_tiktok)
            if status.status_code == 403:
                print(Fore.GREEN + f'VALID | {tiktok_card}\n')
                break
            else:
                print(Fore.RED + f'INVALID | {tiktok_card}\n')
        sys.exit()

    elif gen == '10':
        sys.exit()

    else:
        print(Fore.RED + 'Enter a valid number!')

if __name__ == "__main__":
    issue()
