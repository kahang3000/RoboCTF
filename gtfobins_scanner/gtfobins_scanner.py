import asyncio
from bs4 import BeautifulSoup
import aiohttp

# Asynchronous function runs in a non-blocking manner, allowing other code to execute while it's running
async def check_gtfobins(session, command):
    url = 'https://gtfobins.github.io/gtfobins/' + command
    async with session.get(url) as resp:
        if resp.status == 200:
            soup = BeautifulSoup(await resp.text(), 'html.parser')
            available = soup.find('h2', {'id': 'suid', 'class': 'function-name'})
            if available and available.text == 'SUID':
                return command, url

async def main(commands):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(check_gtfobins(session, cmd) for cmd in commands))
    commands_available = [x for x in results if x is not None]
    if commands_available:
        print("\033[1;34mSUID Found in GTFOBins:\033[m")
        for cmd, url in commands_available:
            print(f"\033[0;34m[+]\033[m \033[1;32;48m{cmd}\033[m - {url}")
    else:
        print("\033[1;31;40mNo SUID Found in GTFOBins\033[m")

if __name__ == '__main__':
    with open('./SUID.txt', 'r') as f:
        commands = []
        for line in f:
            command = line.strip().split("/")[-1]
            commands.append(command)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(commands))