print(
"""
Fluorite Server 1.0.0 

A lazily written multi-client, asynchronous implementation of the Fluorite API
please see the github for documentation
"""
)




import asyncio, aiohttp, logging, time, threading
from quart import Quart, request, send_file
from utils import *
app = Quart(__name__)
def debug(func):
    async def inner(name, return_value=False):
        try:
            ret = await func(name, return_value)
        finally:
            pass
        if not name in people:
            print(name + "given nicked state")
            people[name] = nick_resp
            ret = nick_resp
        return ret
            
    return inner
@app.get("/api/stats/get")
async def group():
    n = request.args.get("names", type=str).split(",")
    ret = {}
    for player in n:
        if player in people:
            ret[player] = people[player]
        elif player not in loaded:
            loaded.append(player)
            await q.put(player) 
    return ret

@app.get("/api/stats/current")
async def immediate_process_user():
    n = request.args.get("name", type=str)
    data = await process_user(n, True)
    print(data)
    return data


@debug
async def process_user(name, return_result = False):
    async with aiohttp.ClientSession() as session:
        if name in uuids:
            uuid = uuids[name]
        else:
            async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{name}") as mojang_resp:
                try: 
                    uuid = (await mojang_resp.json())["id"]
                    uuids[name] = uuid
                except:
                    uuids[name] = "Nicked"
                    return
        print(uuid)
        async with session.get(f"https://api.hypixel.net/player?key={hypixel_key}&uuid={uuid}") as hypixel_resp:
            user = await (hypixel_resp.json())
            if not user["success"] or not user["player"]: return
            star = get(user, ["player", "achievements", "bedwars_level"])
            finalDeaths = get(user, ["player", "stats", "Bedwars", "final_deaths_bedwars"])
            finalKills = get(user, ["player", "stats", "Bedwars", "final_kills_bedwars"])
            beds = get(user, ["player", "stats", "Bedwars", "beds_broken_bedwars"])
            wins = get(user, ["player", "stats", "Bedwars", "wins_bedwars"])
            losses = get(user, ["player", "stats", "Bedwars", "losses_bedwars"])
            xp = get(user, ["player", "networkExp"])
            playerLevel = xp_to_level(xp)


            fkdr = ratio(finalKills, finalDeaths)
            wlr = ratio(wins, losses)

            
            if uuid.strip() in ["f1c3965e278f457c8e05c41852eb8314","443baadc5349495aa735a7d31c684042"]:
                prefix = "Fluorite"
            else:
                requirements = sorted(titles.keys())
                for f in requirements:
                    if fkdr >= f:
                        prefix = titles[f]
                        break

            bedwarsStats = {
                "prefix": prefix,
                "star": "{}★".format(star),   
                "fkdr": str(fkdr),
                "finalKills": str(finalKills),
                "finalDeaths": str(finalDeaths),
                "beds": str(beds),
                "wins": str(wins),
                "losses": str(losses),
                "wlr": str(wlr)
            }

            generalStats = {"suffix": "<3", "networkLevel": str(playerLevel)}
            stats = {"general": generalStats, "bedwars": bedwarsStats}
            people[name] = stats
            print("lol")
    if return_result:
        print("returning" + str(stats))
        return stats

@app.get('/api/capes/get')
async def cape_get():
    n = request.args.get("name", type=str)
    if n == "_LACH":
        return await send_file("capes/cape2.png", mimetype='image/png')
    elif n == "jh1236":
        return await send_file("capes/cape2.png", mimetype='image/png')
    return "not found"


@app.get("/api/cosmetics/get")
async def temp():
    return "" # unused endpoint (as of now)


async def worker():
    loop = asyncio.get_event_loop()
    while True:
        item = await q.get()
        asyncio.run_coroutine_threadsafe(process_user(item), loop)
        q.task_done()

def timer():
    while True:
        try:
            time.sleep(60)
            save_data(people)
            save_uuids(uuids)
            print(f"saved {len(people)} hypixel people and {len(uuids)} uuids")    
        except Exception as e:
            print(f"{e}")

            
q = asyncio.Queue()
people = load_data()
uuids = load_uuids()
hypixel_key = get_hypixel_key()
loaded = list(people.keys())
titles = get_titles()
threading.Thread(target=timer, daemon=True).start()
loop = asyncio.get_event_loop()
asyncio.run_coroutine_threadsafe(worker(), loop)

if __name__ == "__main__":
    # logging.getLogger("quart.serving").setLevel(logging.ERROR)
    app.run(host="0.0.0.0", port=80, loop=loop)


