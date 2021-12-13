import AudioInput
import GPTOutput

import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.ids.upgrade_id import UpgradeId
from sc2.player import Bot, Computer
from sc2.unit import Unit
from sc2.units import Units
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2 import game_state
from sc2.client import Client

class GPTBot(sc2.BotAI):
    def __init__(self):
        print('init...')
        with open("command_history.txt", 'r+') as f:
            f.truncate(0)
        self.audioParser = AudioInput.AudioParser()
        self.audioParser.listenBackground()
        self.command = ''
        print('Listening :)')

    async def on_step(self, iteration):
        try:
            parsedAudio = self.get_audio()
            
            if parsedAudio:
                self.create_command(parsedAudio)
            elif (self.state.chat):
                #if self.state.chat[0] == 'disable voice':
                #if self.state.chat[0] == 'enable voice':
                #if self.state.chat[0] == 'stop':
                    #self.close()
                self.create_command(str(self.state.chat[0].message))
                with open('log.txt', 'a') as logFile:
                    logFile.write('\n\nChat: {}\n'.format(self.state.chat[0].message))
        except Exception as e:
            print("Error in: {0}".format(e))
        if self.command:
            try:
                print(self.command)
                exec(self.command)
                with open("command_history.txt", 'a') as f:
                    f.write(f'# {self.input}\n')
                    f.write(f'{self.command}')
            except:
                Client.debug_text_simple(self.client, f'Error in {self.command}')
                print(f'Error in {self.command}')
            self.command = ''

    def create_command(self, input):
        self.input = input
        self.command = GPTOutput.generateCommand(input)
        with open('log.txt', 'a') as logFile:
            logFile.write('Command: {}\n'.format(self.command))

    def get_audio(self):
        with open('voice.txt', 'r+') as audioFile: #read, log, clear
            parsedAudio = audioFile.read()
            if parsedAudio:
                with open('log.txt', 'a') as logFile:
                    logFile.write('\n\nAudio: {}\n'.format(parsedAudio))
                audioFile.truncate(0)
        return parsedAudio


#This script controls and calls everything, imports AudioInput and GPTOutput to call gather audio data,
#send convert call, and exec.

def main():
    run_game(
        maps.get("BlackburnAIE"),
        [Bot(Race.Zerg, GPTBot()), Computer(Race.Zerg, Difficulty.Easy)],
        realtime=True,
        save_replay_as="GPTBot.SC2Replay",
    )
    #self.audioParser.stopListening()


if __name__ == "__main__":
    main()
