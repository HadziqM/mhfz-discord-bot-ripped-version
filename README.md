# MHFZ-Moderator-Bot <br />

since there is request about my bot (elzelion bot in Rain Server), i will share my first version of the bot <br />
i m sorry i cant share the full extent of my bot since its fully customized for rain server <br />

## Preparation to make <br />

1. download or clone this repository <br/>
2. then just create your own bot on discord developer portal, there is also many guide to make one <br/>
   https://discord.com/developers/applications there is link to discord's dev portal <br />
3. get your bot token and save it <br />
4. install python in your PC and make sure pip path is in your enviromental variable <br />
   if you have problem pip isnt recognized then you mignt want to visit this site https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/ <br />
5. install module listed in pip_instal_req.txt, you can just copy paste every line on pip_install_req.txt to cmd then enter to install it<br />
6. open database.ini and fill it with your credential(fill postgress section is needed to preceed to next step) <br />
7. open folder query in this repo root folder then open query.py to make new table required in the database<br />
   thats it you fulfilled all the requirement need<br />

## How to deploy bot <br />

i m designing this to make it easier for someone to develope it, so the set-up is easy <br /><br />
for non developer you can just open database ini and fill it with your credential, other detail is self explainatory <br />
to make bot service always active then always open main.py, if the window close then bot will offline, if you prever using discord.py latest version then use mainV2.py instead<br /><br />
for developers you can pretty much extend the code in folder cogs for command and base.py in root folder for database communication <br /><br />
for the command and how to use it is pretty much same with rain server
