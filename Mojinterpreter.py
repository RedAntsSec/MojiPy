# MojiPy program. Written by Darcy from @RedAntsSec(Github), @RedAntsS3c(Telegram)

# Emojies dictionary
keys = {
        "🖨": "print",
        "❗️": "(",
        "❕": ")",
        "⛓": "\"",
        "🌀": "for",
        "⏩": ">",
        "⏪": "<",
        "⏭": ">=",
        "⏮": "<=",
        "🍆": "in",
        "🕯": "while",
        "🧨": "break",
        "💣": "exit()",
        "⚖️" : "if",
        "💤": "sleep",
        "❌": "not",
        "⛔️": "!",
        "✅": "=",
        "❇️" : "is",
        "➡️" : "elif",
        "🛑": "else",
        "🇮🇷": "def",
        "🛂": "pass",
        "🚶‍♂️": "return",
        "📈": "range",
        "💁‍♂️": "try",
        "🤦‍♂️": "except",
        "😫": "and",
        "😮": "or",
        "🤬": "raise",
        "👫": "with",
        "🤥": "False",
        "🤐": "True",
        "👽": "global",
        "👩‍🏫": "class"
        }

# Converts python keywords to emojies.
def dinterpret(string):
    string = string.strip()
    x = 0
   
    for count in range(65,91):
        if chr(count) in string or chr(count).lower() in string:
            x = 1
            break
    if x == 0:
        return "NotMoji"

    result = ""
    x = 0

    if "\'" in string:
        x += 1
        ans = string.split("\'")
        for part in ans:
            index = ans.index(part)
            
            if index % 2 == 0:
                for keychar, valchar in keys.items():
                    part = part.replace(valchar,keychar)
                result += part 
            else:
                result += "⛓" + part + "⛓" 
    
    if '\"' in string:
        x += 1
        ans = string.split("\"")
        for part in ans:
            if ans.index(part) % 2 == 0:
                for keychar, valchar in keys.items():
                    part = part.replace(valchar,keychar)
                result += part
            else:
                result += "⛓" + part + "⛓"
    if x == 0:
        for keychar, valchar in keys.items():
            string = string.replace(valchar,keychar)
        return string
    else:
        return result

# Converts emojies to python keywords
def interpret(string):
    string = string.strip()
    x = 0
    for char in keys.keys():
        if char in string:
            x = 1
            break
    if x == 0:
        return "NotMoji"
    for keychar , valchar in keys.items():
        string = string.replace(keychar , valchar)
    return string

    if "\'" in string:
        x += 1
        ans = string.split("\'")
        for part in ans:
            index = ans.index(part)
            
            if index % 2 == 0:
                for keychar, valchar in keys.items():
                    part = part.replace(valchar,keychar)
                result += part 
            else:
                result += "⛓" + part + "⛓" 
    
    if '\"' in string:
        x += 1
        ans = string.split("\"")
        for part in ans:
            if ans.index(part) % 2 == 0:
                for keychar, valchar in keys.items():
                    part = part.replace(valchar,keychar)
                result += part
            else:
                result += "⛓" + part + "⛓"
    if x == 0:
        for keychar, valchar in keys.items():
            string = string.replace(valchar,keychar)
        return string
    else:
        return result

# Converts emojies to python keywords
def interpret(string):
    string = string.strip()
    x = 0
    for char in keys.keys():
        if char in string:
            x = 1
            break
    for count in range(65,91):
        if chr(count) in string:
            x += 1
            break

    if x != 2:
        return "NotMoji"
    for keychar , valchar in keys.items():
        string = string.replace(keychar , valchar)
    return string

