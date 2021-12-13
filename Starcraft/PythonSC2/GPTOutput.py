import openai
#import env
openai.api_key = ''
#OPENAI_API_KEY

#start_sequence = "\n"
#restart_sequence = "\n# "
#training = "# Converting player commands into Starcraft 2 actions using pysc2 and Python 3\n\n# make a hydra\nself.units(UnitTypeId.LARVA).random.train(UnitTypeId.HYDRALISK)\n# make 10 hydras\nfor x in range(10): \n  self.units(UnitTypeId.LARVA).random.train(UnitTypeId.HYDRALISK)"

with open('data.txt', 'r') as dataFile:
    training = dataFile.read().replace('\r\n', '\n').replace('\r', '\n')


def generateCommand(userInput):
    with open('command_history.txt', 'r') as dataFile:
        commandHistory = dataFile.read().replace('\r\n', '\n').replace('\r', '\n')
    command = openai.Completion.create(
        engine="davinci-codex",
        prompt= training + commandHistory + '# ' + userInput + '\n', 
        temperature=0,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["#"]
    ).choices[0].text
    return command

def updateCommand(command):
    with open('command.txt', 'w') as commandFile:
        commandFile.write(command)
    with open('log.txt', 'a') as commandFile:
        commandFile.write('\nGenerated Command: {}\n\n'.format(command))

def printCommand():
    with open('command.txt', 'r') as commandFile:
        print(commandFile.read())

def main():
    print(generateCommand("group Base blasters are hydras"))
    with open('command_history.txt', 'a') as dataFile:
        dataFile.write("# group Base blasters are hydras\n")
        dataFile.write("BaseBlasters = {UnitTypeId.HYDRALISK}")
    print(generateCommand("attack enemy base with base blasters"))

if __name__ == "__main__":
    main()
