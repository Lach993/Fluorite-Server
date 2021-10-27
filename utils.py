import json
import os

def inithelper(directory, base):
    if os.path.isfile('./{}'.format(directory)):
        with open(directory, "r") as fp:
            if len(fp.read()) > 0:
                return
    with open(directory, "w+") as fp:
        fp.write(base)

def init_files():
    if not os.path.exists("./data"):
        os.makedirs("./data")
    if not os.path.exists("./capes"):
        os.makedirs("./capes")
    inithelper("data/data.json", "{}")
    inithelper("data/uuids.json", "{}")
    inithelper("data/settings.json", '{"hypixel_key": "PUT KEY HERE"}')
    inithelper("data/titles.json", '{"0": "Pleb"}')

def get_hypixel_key():
    with open("data/settings.json", "r+") as fp:
        x = json.load(fp)["hypixel_key"]
        if x == "PUT KEY HERE":
            raise("See README on github to see how to get a hypixel key")
        return x

def xp_to_level(xp):
    return round((((2 * xp) + 30625)**0.5 / 50) - 2.5)


def save_data(data):
    with open("data/data.json", "w+") as fp:
        {key:val for key, val in data.items() if val != nick_resp}
        json.dump(data, fp)


def load_data():
    with open("data/data.json", "r+") as fp:
        x = json.load(fp)
        return x if x != None else {}

def save_uuids(data):
    with open("data/uuids.json", "w+") as fp:
        json.dump(data, fp)


def load_uuids():
    with open("data/uuids.json", "r+") as fp:
        x = json.load(fp)
        return x if x != None else {}

def get_titles():
    with open("data/titles.json", "r+") as fp:
        return json.load(fp, object_hook=lambda d: {float(k): l for k, l in d.items()})


def get(data, keys, default=0):
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data


def ratio(a, b):
    return 0 if b == 0 else round(a / b, 2)


nick_resp = {
    "bedwars": {
        "prefix": "§cNICKED§r",
        "star": "§cNICKED§r",
        "fkdr": "§cNICKED§r",
        "finalKills": "§cNICKED§r",
        "finalDeaths": "§cNICKED§r",
        "beds": "§cNICKED§r",
        "wins": "§cNICKED§r",
        "losses": "§cNICKED§r",
        "wlr": "§cNICKED§r",
    },
    "general": {
        "suffix": "§c >:(§r",
        "networkLevel": "§cNICKED§r"
    },
}

init_files()