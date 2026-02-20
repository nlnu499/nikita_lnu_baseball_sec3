import csv
from objects import Player

FILE_NAME = "players.csv"

def load_players():
    players = []

    try:
        with open(FILE_NAME, newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) != 5:
                    continue

                first, last, pos, ab, hits = row

                player = Player(
                    first,
                    last,
                    pos,
                    int(ab),
                    int(hits)
                )

                players.append(player)

    except FileNotFoundError:
        print("No data file found. Starting empty lineup.")

    return players

def save_players(lineup):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        for player in lineup:
            writer.writerow([
                player.first_name,
                player.last_name,
                player.position,
                player.at_bats,
                player.hits
            ])