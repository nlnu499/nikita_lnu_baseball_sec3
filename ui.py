# ui.py

def display_menu():
    print("=" * 64)
    print("Baseball Team Manager")
    print("=" * 64)
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit")
    print("=" * 64)


def display_lineup(lineup):
    print("\n#  Player                     POS   AB   H   AVG")
    print("-" * 64)

    for i, player in enumerate(lineup, start=1):
        print(f"{i:<3}"
              f"{player.full_name:<25}"
              f"{player.position:<5}"
              f"{player.at_bats:<5}"
              f"{player.hits:<5}"
              f"{player.batting_average:.3f}")