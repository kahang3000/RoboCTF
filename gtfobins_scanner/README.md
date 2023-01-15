# GTFOBins Scanner

This script is a tool that checks if a command is available on GTFOBins. It reads a list of commands from a file `SUID.txt`, and then checks each command on the GTFOBins website to see if it has the `SUID` function available. If it does, it will print out the command along with its corresponding GTFOBins URL.

## Installation
1. Clone the repository by running **`git clone https://github.com/your-username/gtfobins-suid-scanner.git`**
2. Install the required packages by running **`pip install -r requirements.txt`** 
3. Create a file named **"SUID.txt"** in the same directory as the script, and list all the commands you want to check in this file, one command per line.
4. Run the script by executing **`python gtfobins_suid_scanner.py`**

## Usage

To use the script, simply run it with python and provide the path to the `SUID.txt` file as an argument. Or you can manually change the file name in the given code. 

## Example
```python
$ python gtfobins_suid_scanner.py
[+] GTFOBins available for: env - https://gtfobins.github.io/gtfobins/env
[+] GTFOBins available for: nmap - https://gtfobins.github.io/gtfobins/nmap
```

## Dependencies

This script requires the following python packages to be installed:
- asyncio
- aiohttp
- bs4
