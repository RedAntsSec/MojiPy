# MojiPy bot, written by Darcy and Mr Nobody. @RedAntsS3c(Telegram), github.com/RedAntsSec

#Imports
from pyrogram import Client , filters
import requests
import json
import Mojinterpreter

#pyrogram api
# You should enter your API details here:
api_id = 0
api_hash = ""
name = ""

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
        result = "Results: \n" + str(result["Result"]) + "\nWarnings: \n" + str(result["Warnings"]) + "Errors: \n" + str(result["Errors"])
    elif result["Errors"] != None and result["Warnings"] == None:
        result = "Results: \n" + str(result["Result"]) + "\nErrors: \n" + str(result["Errors"])
    elif result["Errors"] == None and result["Warnings"] != None:
        result = "Results: \n" + str(result["Result"]) + "\nWarnings: \n" + str(result["Warnings"])
    else:
        result = "Results: \n" + str(result["Result"])
    
    return result

#python to moji
@app.on_message((filters.group | filters.private) & filters.regex("^[Dd]moji$") , group = 1)
def Moji(client , message) :
	textl = Mojinterpreter.dinterpret(message.reply_to_message.text)
	if textl == "NotMoji":
            app.send_message(message.chat.id , "There is not any understandable character in the given code!")
	else:
		app.send_message(message.chat.id , textl)

#moji to python
@app.on_message((filters.group | filters.private) & filters.regex("^[Mm]oji$") , group = 1)
def Moji(client , message) :
	textl = Mojinterpreter.interpret(message.reply_to_message.text)
        if textl == "NotMoji":
            app.send_message(message.chat.id , "There is not any understandable character in the given code!")
        else:
            result = rextester(textl)
	    app.send_message(message.chat.id , result)
	

#Run
app.run()
