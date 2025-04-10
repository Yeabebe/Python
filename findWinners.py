from collections import defaultdict
class Solution: 
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loss_count = defaultdict(int)
        players = set()

        for winner, loser in matches: 
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        no_losses = []
        one_loss = []

        for player in players:
            if loss_count[player] == 0:
                no_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        return [sorted(no_losses), sorted(one_loss)]