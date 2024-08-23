![image](https://github.com/user-attachments/assets/76adb78e-8326-4a27-a3fc-ca8bc37a1313)

# MinecraftDiscordBot
A Simple Discord Bot to show how many players are on your Minecraft Server

# Instructions
You can host this discord bot on your own computer or use a cheap vps like one on https://www.eugamehost.com/ or if your in the USA https://www.hetzner.com/cloud/

# Windows
On your windows pc make sure you have python installed
Make a file and put your discord bot in that file
cmd into the file and run
```bash
pip install discord.py requests
python main.py
```
# Linux
If you are running this on a vps using linux here is how to run the bot on there
use sftp software like winzip or filezilla
drag and drop main.py into your servers sftp you can make a file or keep it in the root directory
make sure you have python installed on your linux vps/machine
in the directory with the python file run python main.py or do screen -S mcbot python main.py make sure you have screen installed on your linux machine
Screen is like running the bot but it runs in the background after you close your machines termanal
```bash
python main.py
screen -S mcbot python main.py
```
After you ran the command Congratulations the bot is now running. Don't forget to edit the code to your likeing
