import openai

openai.api_key = OPENAI_API_KEY

import CommandParser

def generateCommand(userInput):
    command = userInput
    command = openai.Completion.create(engine="ada", prompt=command)
    #engine="davinci"
    #print(completion.choices[0].text)
    return command

def parseCommand(command):
    return CommandParser.parse(command)

def updateCommand(parsedCommand):
    with open('command.txt', 'w') as commandFile:
        commandFile.write(parsedCommand)

def main():
    command = generateCommand('attack workers')
    parsed = parseCommand(command)
    updateCommand(command)



if __name__ == "__main__":
    main()
