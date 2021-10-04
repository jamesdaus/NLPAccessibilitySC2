import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer


class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration):
        if iteration == 0:
            for worker in self.workers:
                worker.attack(self.enemy_start_locations[0])


def main():
    run_game(
        #maps.get("Abyssal Reef LE"),
        maps.get("BlackburnAIE"),
        [Bot(Race.Zerg, WorkerRushBot()), Computer(Race.Protoss, Difficulty.Medium)],
        realtime=True,
        save_replay_as="WorkerRush.SC2Replay",
    )


if __name__ == "__main__":
    main()