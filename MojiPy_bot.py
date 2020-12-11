# MojiPy bot, written by Darcy and Mr Nobody. @RedAntsS3c(Telegram), github.com/RedAntsSec

#Imports
from pyrogram import Client , filters
import requests
import json
import Mojinterpreter

#pyrogram api
# You should enter your API details here:
name = ""
api_id = 0
api_hash = ""



helps = """
interpreter's emojis
ایموجی های تفسیر
🖨 print

🌜 (
🌛 )

🕸 "

⏩ >
⏪ <

⏭ >=
⏮ <=

🕯 while
🌀 for

🧨 break

💣 exit()

⚖️ if

💤 sleep

❌ not
⛔️
✅ =
❇️ is

🛂 pass

➡️ elif
🛑 else

🇮🇷 def

🚶 return

📈 range

🍆 in

💁 try
🤦 except

😫 and
😮 or

🤬 raise
👫 with
🤥 False
🤐 True

👽 global
👩‍🏫 class


"""






#App
app = Client(name , api_id = api_id , api_hash = api_hash)

#Rextester
def rextester(code):
    data = {
        "LanguageChoice":"5",
        "Program":code,
        "Input":"",
        "CompileArgs":""
        }
    req = requests.post(url="https://rextester.com/rundotnet/api" , data=data)
    result = json.loads(req.text)
    if result["Errors"] != None and result["Warnings"] != None:
        result = "`**Results: **\n`" + str(result["Result"]) + "`\n**Warnings: **\n" + str(result["Warnings"]) + "Errors: \n" + str(result["Errors"])
    elif result["Errors"] != None and result["Warnings"] == None:
        result = "`**Results: **\n`" + str(result["Result"]) + "`\n**Errors: **\n" + str(result["Errors"])
    elif result["Errors"] == None and result["Warnings"] != None:
        result = "`**Results: **\n`" + str(result["Result"]) + "`\n**Warnings: **\n" + str(result["Warnings"])
    else:
        result = "`**Results: **\n`" + str(result["Result"])
    
    return result




#python to moji
@app.on_message((filters.group | filters.private) & filters.regex("^[Dd]moji$") , group = 1)
def Moji(client , message):
    textl = Mojinterpreter.pytoemoji(message.reply_to_message.text)
    if textl == "NotMoji":
        message.reply_text("**There is not any understandable character in the given code!**")
    else:
        message.reply_text(textl)


#moji to python
@app.on_message((filters.group | filters.private) & filters.regex("^[Mm]oji$") , group = 1)
def Moji(client , message) :
    textl = Mojinterpreter.emojitopy(message.reply_to_message.text)
    if textl == "NotMoji":
        message.reply_text("**There is not any understandable character in the given code!**")
    else:
        result = rextester(textl)
        message.reply_text("**Python Code: ** \n`" + textl + "\n`" + result + "`")

@app.on_message()
def main(client, message):
    if "راهنما" == message.text or "help" == message.text or "about" == message.text:
        message.reply_text(helps)





#Run
app.run()
