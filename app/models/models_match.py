# class Match:
#     def __init__(
#         self,
#         first_player,
#         second_player,
#         first_player_score,
#         second_player_score,
#     ):
#         self.first_player = first_player
#         self.second_player = second_player
#         self.first_player_score = first_player_score
#         self.second_player_score = second_player_score

#     def generate_pair(self):
#         pair = {
#             "Joueur1": [
#                 self.first_player.name + self.first_player_score.scores,
#             ],
#             "Joueur2": [
#                 self.second_player_score.scores + self.second_player.name,
#             ],
#         }
#         self.serialize_match(pair)

#     def serialize_match(self, the_pair):
#         the_match = {the_pair.Joueur1 + "Contre" + the_pair.Joueur2}
#         return the_match
