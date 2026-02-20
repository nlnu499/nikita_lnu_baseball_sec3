# Main program controlling application flow
from objects import Player, Lineup
from db import load_players, save_players
from ui import display_menu, display_lineup

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def main():
    lineup = Lineup()

    # Load players from file
    for player in load_players():
        lineup.add_player(player)

    while True:
        display_menu()
        choice = input("Menu option: ")

        # ---------------- DISPLAY ----------------
        if choice == "1":
            display_lineup(lineup)

        # ---------------- ADD ----------------
        elif choice == "2":
            first = input("First name: ")
            last = input("Last name: ")

            while True:
                pos = input("Position: ").upper()
                if pos in POSITIONS:
                    break
                print("Invalid position.")

            try:
                ab = int(input("At bats: "))
                hits = int(input("Hits: "))
            except ValueError:
                print("Invalid integer.")
                continue

            if hits > ab or ab < 0 or hits < 0:
                print("Invalid stats.")
                continue

            lineup.add_player(Player(first, last, pos, ab, hits))
            print(f"{first} {last} was added.")

        # ---------------- REMOVE ----------------
        elif choice == "3":
            try:
                num = int(input("Lineup number: ")) - 1
                if num < 0 or num >= len(lineup):
                    print("Invalid lineup number.")
                    continue

                removed = lineup.remove_player(num)
                print(f"{removed.full_name} was deleted.")

            except ValueError:
                print("Invalid integer.")

        # ---------------- MOVE ----------------
        elif choice == "4":
            try:
                old = int(input("Current lineup number: ")) - 1
                if old < 0 or old >= len(lineup):
                    print("Invalid lineup number.")
                    continue

                player = lineup.get_player(old)
                print(f"{player.full_name} was selected.")

                new = int(input("New lineup number: ")) - 1
                if new < 0 or new >= len(lineup):
                    print("Invalid lineup number.")
                    continue

                lineup.move_player(old, new)
                print(f"{player.full_name} was moved.")

            except ValueError:
                print("Invalid integer.")

        # ---------------- EDIT POSITION ----------------
        elif choice == "5":
            try:
                num = int(input("Lineup number: ")) - 1
                if num < 0 or num >= len(lineup):
                    print("Invalid lineup number.")
                    continue

                player = lineup.get_player(num)
                print(f"You selected {player.full_name} POS={player.position}")

                while True:
                    new_pos = input("Position: ").upper()
                    if new_pos in POSITIONS:
                        break
                    print("Invalid position.")

                player.update_position(new_pos)
                print(f"{player.full_name} was updated.")

            except ValueError:
                print("Invalid integer.")

        # ---------------- EDIT STATS ----------------
        elif choice == "6":
            try:
                num = int(input("Lineup number: ")) - 1
                if num < 0 or num >= len(lineup):
                    print("Invalid lineup number.")
                    continue

                player = lineup.get_player(num)

                ab = int(input("At bats: "))
                hits = int(input("Hits: "))

                if hits > ab or ab < 0 or hits < 0:
                    print("Invalid stats.")
                    continue

                player.update_stats(ab, hits)
                print(f"{player.full_name} stats updated.")

            except ValueError:
                print("Invalid integer.")

        # ---------------- EXIT ----------------
        elif choice == "7":
            save_players(lineup)
            print("Bye!")
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":

    main()
