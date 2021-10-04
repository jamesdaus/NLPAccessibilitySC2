import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

#import ast
import GPTOutput

currentCommand = ''

class GPTBot(sc2.BotAI):
    async def on_step(self, iteration):
        if (iteration % 50 == 0):
            with open('command.txt', 'r') as commandFile:
                print(commandFile.read())

def updateCommands(newCommand):
    currentCommand = newCommand

def main():
    run_game(
        maps.get("BlackburnAIE"),
        [Bot(Race.Zerg, GPTBot()), Computer(Race.Protoss, Difficulty.Easy)],
        realtime=True,
        save_replay_as="GPTBot.SC2Replay",
    )


if __name__ == "__main__":
    main()
