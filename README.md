# MHFZ-Moderator-Bot <br />

since there is request about my bot (elzelion bot in Rain Server), i will share my first version of the bot <br />
i m sorry i cant share the full extent of my bot since its fully customized for rain server <br />

## Preparation to make <br />

download or clone this repository <br/>
then just create your own bot on discord developer portal, there is also many guide to make one <br/>
get your bot token and save it <br />
install python in your PC and make sure pip path is in your enviromental variable <br />
install module listed in pip_instal_req.txt <br />
open folder query in this repo root folder then open query.py to make new table required in the database<br />
thats it you fulfilled all the requirement need<br />

## How to deploy bot <br />

i m designing this to make it easier for someone to develope it, so the set-up is easy <br />
for non developer you can just open database ini and fill it with your credential, other detail is self explainatory <br />
to make bot service always active then always open main.py, if the window close then bot will offline <br />
for developers you can pretty much extend the code in folder cogs for command and base.py in root folder for database communication <br />
for the command and how to use it is pretty much same with rain server
