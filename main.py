try:
  from colorama import Fore
  import discord
  
else:
  os.system("pip install colorama")
  os.system("pip install py-cord")
  
"""
Create a File called 'config.json' and copy n paste the following 4 lines:
{
  "token": "ADD YOUR TOKEN HERE",
  "prefix": "."
}
/////\\\\\
CHANGE LINE 46 IF NEEDED !!!!!!!!!!!!!!!
"""

def get_config(name):
    with open("config.json", "r") as f:
        json_file = json.load(f)
        return json_file[name]

client = bridge.Bot(
    command_prefix=get_config('token'),
    intents=discord.Intents.all(),
    help_command=None
)


def load():
    os.system("cls")
    print(Fore.RED + " ____________________________________")
    print(Fore.RED + "/                                    \ ")
    print(Fore.RED + "|      _ _         _____             |")
    print(Fore.RED + "|     | | |       |  __ \            |")
    print(Fore.RED + "|   __| | |____  _| |  | | _____   __|")
    print(Fore.RED + "|  / _` | '_ \ \/ / |  | |/ _ \ \ / /|")
    print(Fore.RED + "| | (_| | |_) >  <| |__| |  __/\ V / |")
    print(Fore.RED + "|  \__,_|_.__/_/\_\_____/ \___| \_/  |")
    print(Fore.RED + "|                                    |")
    print(Fore.RED + f"|              " + Fore.BLUE + f"made by dbx" + Fore.RED + "           |")
    print(Fore.RED + "\____________________________________/\n" + Fore.GREEN + "|")

    folders = [
        "If your using Cogs, add your Folder name here || If you not using any cogs, remove line 45 - 53"
        ]
    for folder in folders:
        for file in os.listdir(f"./{folder}"):
            if file.endswith(".py"):
                client.load_extension(f"{folder.replace('/', '.')}.{file[:-3]}")
                print(Fore.GREEN + f'| {file} was loaded')
    print(Fore.GREEN + f'\_______________________________')


if __name__ == '__main__':
    load()
    client.run(get_config('token'))
