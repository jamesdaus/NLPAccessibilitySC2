import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.unit import Unit
from sc2.units import Units
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId

class GPTBot(sc2.BotAI):
    async def on_step(self, iteration):
        if (iteration % 5 == 0):
            with open('command.txt', 'r+') as commandFile: #execute, clear, wait for more input
                command = commandFile.read()
                try:
                    print(command)
                    exec(command)
                except:
                    print(f'Error in {command}')
                commandFile.truncate(0)
def main():
    run_game(
        maps.get("BlackburnAIE"),
        [Bot(Race.Zerg, GPTBot()), Computer(Race.Protoss, Difficulty.Easy)],
        realtime=True,
        save_replay_as="GPTBot.SC2Replay",
    )


if __name__ == "__main__":
    main()
