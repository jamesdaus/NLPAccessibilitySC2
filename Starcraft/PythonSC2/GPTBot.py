import AudioInput
import GPTOutput

import sc2
from sc2 import run_game, maps, Race, Difficulty
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
        self.audioParser = AudioInput.AudioParser()
        self.audioParser.listenBackground()
        print('Listening :)')

    async def on_step(self, iteration):
        command = ''
        try:
            print('in try')
            parsedAudio = self.get_audio()
            print(f"parsed audio: {parsedAudio}")
            if parsedAudio:
                command = self.create_command(parsedAudio)
            if (self.state.chat):
                pass
                #Insert chat commands
        except Exception as e:
            print("Error is {0}".format(e))
        if (iteration % 5 == 0):
            if command:
                try:
                    print(command)
                    exec(command)
                except:
                    Client.debug_text_simple(self.client, f'Error in {command}')

    def create_command(self, audio):
        command = GPTOutput.generateCommand(audio)
        with open('log.txt', 'a') as logFile:
            logFile.write('Command: {}\n'.format(command))
        return command

    def get_audio(self):
        with open('voice.txt', 'r+') as audioFile: #read, log, clear
            print('pre-read')
            parsedAudio = audioFile.read()
            print(f"in get_audio: {parsedAudio}")
            if parsedAudio:
                with open('log.txt', 'a') as logFile:
                    logFile.write('Audio: {}\n'.format(parsedAudio))
                audioFile.truncate(0)
        return parsedAudio


#This script controls and calls everything, imports AudioInput and GPTOutput to call gather audio data,
#send convert call, and exec.

def main():
    run_game(
        maps.get("BlackburnAIE"),
        [Bot(Race.Zerg, GPTBot()), Computer(Race.Protoss, Difficulty.Easy)],
        realtime=True,
        save_replay_as="GPTBot.SC2Replay",
    )
    #self.audioParser.stopListening()


if __name__ == "__main__":
    main()
