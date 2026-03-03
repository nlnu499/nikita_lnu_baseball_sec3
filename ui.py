"""
ui.py

Handles all user interface display for the Baseball Team Manager.
This module is responsible only for showing menus and displaying lineup data.
"""


def display_menu():
    """
    Displays the main menu options.
    """
    print("\nMENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit")
    print("=" * 64)


def display_positions(positions):
    """
    Displays valid player positions.
    """
    print("\nPOSITIONS")
    print(", ".join(positions))
    print("=" * 64)


def display_lineup(lineup):
    """
    Displays the current lineup in a formatted table.
    """
    print(f"\n{'#':<3}"
          f"{'Player':<25}"
          f"{'POS':<5}"
          f"{'AB':<6}"
          f"{'H':<6}"
          f"{'AVG'}")
    print("-" * 64)

    for i, player in enumerate(lineup, start=1):
        print(f"{i:<3}"
              f"{player.full_name:<25}"
              f"{player.position:<5}"
              f"{player.at_bats:<6}"
              f"{player.hits:<6}"
              f"{player.batting_average:.3f}")

    print("-" * 64)
