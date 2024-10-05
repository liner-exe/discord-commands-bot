import configparser
from shutil import copy

print("""## Welcome to bot setup ##

If you have additional questions type 'help' on each of answers.
If you wanna abort the setting up just close the program.
Please make sure that you will input the right data.
""")

while True:
    token = input('Please enter your token here: ')

    if token.lower() == 'help':
        print("""Open the discord developer portal, create your application and copy your token.
        https://discord.com/developers/applications""")

    elif token == '':
        continue

    else:
        break

while True:
    owner_id = input('\nPlease enter your discord id: ')

    if owner_id.lower() == 'help':
        print("""Turn on developer mode in discord app settings. Then copy your id in the profile.
        It will need for some commands.""")

    elif owner_id == '':
        continue

    else:
        break

while True:
    prefix = input('\nPlease enter bot prefix: ')

    if prefix.lower() == 'help':
        print("""Prefix will be used for some ctx commands.""")

    elif prefix == '':
        continue

    else:
        break

while True:
    admin_guild = input('\nPlease enter admin guild id: ')

    if admin_guild.lower() == 'help':
        print("""Admin guild id used for some commands.""")

    elif admin_guild == '':
        continue

    else:
        break

while True:
    openweather_token = input('\nPlease enter openweather token (type "skip" for skip): ')

    if openweather_token.lower() == 'help':
        print("""Open https://openweathermap.org/ then login. Create token, copy and paste there.""")

    elif openweather_token.lower() == 'skip':
        break

    elif openweather_token == '':
        continue

    else:
        break

while True:
    is_save = input('\nSave settings? (Yes/No): ')

    if is_save.lower() == 'yes':
        break

    elif is_save.lower() == 'no':
        exit('\nOkay. Try again.')

    else:
        continue

copy('config.ini.sample', 'config.ini')

config = configparser.ConfigParser()
config.read('config.ini')


config['bot']['token'] = token
config['bot']['owner_id'] = owner_id
config['bot']['prefix'] = prefix

config['settings']['admin_guild'] = admin_guild

config['weather']['openweather_token'] = '' if openweather_token == 'skip' else openweather_token

with open('config.ini', 'w') as f:
    config.write(f)

print('\nDone. Now you can run the bot.')
