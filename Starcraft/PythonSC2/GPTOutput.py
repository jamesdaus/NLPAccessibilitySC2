import openai
from AudioInput import AudioParser
openai.api_key = 'secret'

start_sequence = "\n"
restart_sequence = "\n#"
training = "# Converting player commands into Starcraft 2 actions using pysc2 and Python 3\n\n# make a hydra\nself.units(UnitTypeId.LARVA).random.train(UnitTypeId.HYDRALISK)\n# make 10 hydras\nfor x in range(10): \n  self.units(UnitTypeId.LARVA).random.train(UnitTypeId.HYDRALISK)"
#turn into separate file

def generateCommand(userInput):
    command = openai.Completion.create(
        engine="davinci-codex",
        prompt= training + userInput,
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
        commandFile.write('\nGenerated Command: {}\n'.format(command))

def printCommand():
    with open('command.txt', 'r') as commandFile:
        print(commandFile.read())

def main():
    audioParser = AudioParser()
    while True:
        #command = generateCommand(input('Enter Command: '))
        voice = audioParser.getAudio()
        if voice:
            command = generateCommand(voice)
            updateCommand(command)
            printCommand()

if __name__ == "__main__":
    main()
