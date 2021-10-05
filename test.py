players = [
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 16.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 4.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 16.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 4.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 12.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 0.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 12.0},
    {"name": "4 4", "birthday": "4", "gender": "4", "rank": 4, "scores": 0.0},
]


def serialize_match(
    player_name,
    player_score,
    player_two_name,
    player_two_score,
):
    the_match = {
        "first_player_name": player_name,
        "first_player_score": player_score,
        "second_player_name": player_two_name,
        "second_player_score": player_two_score,
    }
    return the_match


def creer_match(the_match, nom1, score1, nom2, score2):
    the_match = serialize_match(
        nom1,
        float(score1),
        nom2,
        float(score2),
    )
    return the_match


list_matchs = []
match = {}

for j, k, l in zip(range(0, 4), range(4, 8), range(1, 5)):
    print(f"\nmatch {l}\n")
    list_matchs.append(
        creer_match(
            match,
            players[j]["name"],
            input(f"score de {players[j]['name']}\n"),
            players[k]["name"],
            input(f"score de {players[k]['name']}\n"),
        )
    )
    players[j]["scores"] = list_matchs[j]["first_player_score"]
    players[k]["scores"] = list_matchs[j]["second_player_score"]

print(list_matchs)
