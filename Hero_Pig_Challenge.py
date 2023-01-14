
# 𓃟 HeroPig ⚘️💃.

"""
 Read and write a JSON file.
     
  Hi ❤️
    ┏━╮      ╭━┓
    ┃  ┏ 👑 ┓   ┃
    ╰┓ ■   ■  ┏╯            
 ╭ ━┻ ╮         ┗━━━━━━━╮ ,
 | ▎  ▎ |    ╮                      ┣╯
 ╰ ━┳ ╯  ▬╯                     /
     ╰(  (   )~~(  (   )-╯
      /,,/,,,/  /,,/,,,/  
"""

import json
import logging
import os
import urllib.request as request

logging.basicConfig(level=logging.INFO)

Archive_Name = "pig.json"
Archive_Dir = os.path.dirname(os.path.abspath(__file__)) + os.sep
Archive = Archive_Dir + Archive_Name

# Date a write.

DATA = {
 "hero": [
  {
   "Name": "SwimmerPig 𓃟",
   "Byname": "Spine 𓆡",
   "Skill": "Tsunami  🌊",
   "Task": "Turn a calm ocean into highly destructive waves that destroy everything in their path.",
  },
  {
   "Name": "FlyingPig 𓃟",
   "Byname": "Irritation 𓆦",
   "Skill": "Poop Rain  💩 ",
   "Task": "Bombard and contaminate a large area with very dangerous waste.",
  },
 ]
}

# Opening JSON file to write a dictionary type.

with open(Archive, "w") as pig_json:
 json.dump(DATA, pig_json)
 logging.info("⚠️ A dictionary type was written to a JSON file.\n")

# Opening JSON file.

with open(Archive) as pig_json:

 # Reading from JSON file.
 
 pig = json.load(pig_json)
 logging.info("⚠️ Read from JSON file.\n")
 for hero in pig["hero"]:
  print(f"Name:", hero["Name"])
  print(f"Byname:", hero["Byname"])
  print(f"Skill:", hero["Skill"])
  print(f"Task:\n❌️", hero["Task"],"❗️\n")
  print(f"    🔻 🔻 🔻 🔻 🔻 🔻 🔻\n")
  print(f"📀 Detailed data:\n {hero}\n")
  print(f"    🟢 🟢 🟢 🟢 🟢 🟢 🟢 \n")

urlPig1 = "https://media2.giphy.com/media/0bBOhzYGbD8AtB9dC8/giphy.gif?cid=82a1493b70x9lxuw7233irmyjyizs4mba6sgvl5vs4hqzqa7&rid=giphy.gif&ct=s"

urlPig2 = "https://media2.giphy.com/media/U6isKyHvHvjCySIQE6/giphy.gif?cid=82a1493b61p5t4fzcld1uzf7el490ntrmq8g06077vttorne&rid=giphy.gif&ct=s"

print ("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Mr+Dafoe&display=swap");
 body{
  background-color: oldlace;
  margin: auto;
  border: 5px solid ActiveCaption;
  width: 80%;
  border-radius: 20px;
  box-shadow: 0 25px 30px rgba(0, 0, 0, 0.8); 
  font-family: "Mr Dafoe";
  font-weight: 800;
  font-size:1.4em;
  color:ActiveCaption; 
  padding: .3em .5em 0em 1em;   
  text-shadow:
      0 0 0.5em rgba(0, 0, 0, .5), 
      0 0 0.5em rgba(0, 0, 0, .3), 
      0 0 0.5em rgba(0, 0, 0, .2);   
 }

</style>""")


request.urlretrieve(urlPig1,'pig1.png')
request.urlretrieve(urlPig2,'pig2.png')

