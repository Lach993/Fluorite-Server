# Fluorite Server
The api which stores and distributes the cosmetic, cape, and levelhead information for the Fluorite minecraft client
please note that this requires some knowledge of python and if preferable knowledge of deploying servers.
running this server as is will launch it in a "development" environment, instead i recomend you [Run as an ASGI Server](#Installing-Hypercorn)

# Installation
This app requires python (tested with 3.9+, should work on older versions) which can be downloaded here [Python](https://www.python.org/downloads/)
Go to the [GitHub Repo](https://github.com/Lach993/Fluorite-Server) and download the file and unzip.
After download and installation you need to install the required libraries:
    + run cmd in the Fluorite server directory
    + type in `pip install -r requirements.txt`
    + if that doesnt work try these variations `py -m pip install -r requirements.txt` or `python -m pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`
run utils.py by running the command `py utils.py` (`py` may need to be changed to `python` or `python3`)
open the file data/settings.json and replace "PUT YOUR KEY HERE" with the key you get from [Here](#Get-Hypixel-Key)
go to Fluorite client, click settings -> mods -> api and change the ip address to localhost or the ip to the computer it is hosted on.
run main.py using `py main.py`


# Open to the Public
When not to open this server to the public:
    + If you are not familiar with networking and security in any way. 
    + If you are not going to download an external ASGI server to run it.
    + If you don't have enough knowledge to modify python code 
If you would like to open your server to the public it is recomended that you get [priviliged API access](https://api.hypixel.net/#section/Introduction/Limits)
I recomend you [Run as an ASGI Server](#Installing-Hypercorn)
enable port forwarding in router settings and give your public ip adress to the people you want to give it to
i would recomend setting up a dynamic ip and give that to people as if your public ip adress is not static then it will change


# Get Hypixel Key
log into minecraft with the account you want to be associated with the key
join the server `mc.hypixel.net`
type in chat `/api`
you will see `Your new API key is xxxxxxxxxxxxxxxx`
click the key, press `ctrl`+`A` then `ctrl`+`C`, then backspace. DO NOT SEND THIS KEY IN CHAT, keep this key secret.
you now have the key in your clipboard, you can paste it into any file you want using `ctrl`+`V`

# Installing Hypercorn
documentation for Hypercorn [Here](https://gitlab.com/pgjones/hypercorn)
Install hypercorn with pip `pip install hypercorn`
edit main.py and put a # (hashtag) infront of the last 2 lines.
open command prompt in the working directory and run hypercorn module:main. 
p.s. no idea if this will work cause im too tired to test it
