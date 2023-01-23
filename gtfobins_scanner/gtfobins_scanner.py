import asyncio
from bs4 import BeautifulSoup
import aiohttp

# Asynchronous function that checks if a command has SUID on GTFOBins website
async def check_gtfobins(session, command):
    url = 'https://gtfobins.github.io/gtfobins/' + command
    async with session.get(url) as resp:
        if resp.status == 200:
            soup = BeautifulSoup(await resp.text(), 'html.parser')
            available = soup.find('h2', {'id': 'suid', 'class': 'function-name'})
            if available and available.text == 'SUID':
                return command, url
            
# Runs check_gtfobins function concurrently for multiple commands
async def main(commands):
    async with aiohttp.ClientSession() as session:
        # Running tasks concurrently, collecting results
        tasks = []
        for cmd in commands:
            tasks.append(asyncio.ensure_future(check_gtfobins(session, cmd)))
        results = await asyncio.gather(*tasks)
        # Filtering results
        commands_available = []
        for x in results:
            if x is not None:
                commands_available.append(x)
    if commands_available:
        print("\033[1;34mSUID Found in GTFOBins:\033[m")
        for cmd, url in commands_available:
            print(f"\033[0;34m[+]\033[m \033[1;32;48m{cmd}\033[m - {url}")
    else:
        print("\033[1;31;40mNo SUID Found in GTFOBins\033[m")

if __name__ == '__main__':
    # Reading commands from a file and appending them to a list
    with open('./SUID.txt', 'r') as f:
        commands = []
        for line in f:
            command = line.strip().split("/")[-1]
            commands.append(command)
    # Setting up event loop and running the main function with the commands list      
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(commands))