#!/usr/bin/env python3

"""
A silly idea I had to track the Wifi uptime of Vancouver's SkyTrain
"""

from enum import Enum
import subprocess as sp


class STLine(Enum):
    EXPO = 1
    MILLENIUM = 2


class STGen(Enum):
    MKI = 1  # Original SkyTrain model from the 1980s
    MKII = 2  # SkyTrain model from the 2000s
    MKIII = 3  # SkyTrain model from the 2010s


class Train:
    def __init__(self, id, gen, line, wifi_reported, total_reported):
        self.id: int = id  # Train number
        self.gen: STGen = gen  # Train generation
        self.line: STLine = line  # SkyTrain line
        self.wifi_reported: int = (
            wifi_reported  # The number of times wifi was reported working
        )
        self.total_reported: int = (
            total_reported  # The number of times this train was reported on
        )
        self.wifi_uptime: int = int((self.wifi_reported / self.total_reported) * 100)


class Menu:
    def main_menu(trains: [Train], msg: str = "") -> str:
        """Draw the main menu and return user input"""
        sp.run("clear")
        print("=========================================")
        print("  Welcome to the SkyTrain Wifi Tracker!")
        print("=========================================")
        if msg != "":
            print(msg)
        print("  1. Report train status")
        print("  2. Get train status")
        print("  3. See overall stats")
        print("  4. Quit")

        return input("-> ")

    def report_menu(trains: [Train]) -> [Train]:
        """Draw the report menu and record user input to memory"""
        sp.run("clear")
        print("=========================================")
        print("          Report Train Status")
        print("=========================================")
        print("Enter train #:")
        train_id: int = int(input("-> "))

        previously_reported: bool = any(t for t in trains if t.id == train_id)

        if not previously_reported:
            # These menus will only be shown if the train has not been
            # previously reported on
            sp.run("clear")
            print("=========================================")
            print("          Report Train Status")
            print("=========================================")
            print("Train generation:")
            print("  1. MKI   (From the 1980s)")
            print("  2. MKII  (From the 2000s)")
            print("  3. MKIII (From the 2010s)")
            print("Enter answer(1, 2, 3)")
            train_gen: STGen = int(input("-> "))

            sp.run("clear")
            print("=========================================")
            print("          Report Train Status")
            print("=========================================")
            print("SkyTrain line:")
            print("  1. Expo Line")
            print("  2. Millenium Line")
            print("Enter answer (1, 2):")
            train_line: STLine = int(input("-> "))

        sp.run("clear")
        print("=========================================")
        print("          Report Train Status")
        print("=========================================")
        print("Does this train have working Wifi?")
        print("  1. No")
        print("  2. Yes")
        print("Enter answer (1, 2)")
        has_wifi: int = int(input("-> ")) - 1

        if previously_reported:
            # If this train was previously reported on, update its stats
            train_idx: int = [train.id for train in trains].index(train_id)
            train = trains[train_idx]
            train.wifi_reported += has_wifi
            train.total_reported += 1
            train.wifi_uptime = int((train.wifi_reported / train.total_reported) * 100)
        else:
            # If this is a new train, create a new train and add it to the list
            train: Train = Train(train_id, train_gen, train_line, has_wifi, 1)
            trains += [train]

        return trains

    def get_train_stats_menu(trains: [Train]):
        """Show the Wifi status of a given train"""
        sp.run("clear")
        print("=========================================")
        print("            Get Train Status")
        print("=========================================")
        print("Enter train #:")
        train_id: int = int(input("-> "))

        train_idx: int = [train.id for train in trains].index(train_id)
        train = trains[train_idx]

        sp.run("clear")
        print("=========================================")
        print("            Get Train Status")
        print("=========================================")
        print(f"Train #{train_id}:")
        print(f"  Generation:  {STGen(train.gen).name}")
        print(f"  Line:        {STLine(train.line).name}")
        print(
            f"  Wifi uptime: {train.wifi_uptime}% ({train.wifi_reported}/{train.total_reported})"
        )
        print("")
        input("Press RETURN to continue...")

    def get_overall_stats_menu(trains: [Train]):
        """Show the overall stats for the whole skytrain system"""
        expo: [Train] = [t for t in trains if t.line == 1]
        mil: [Train] = [t for t in trains if t.line == 2]
        mki: [Train] = [t for t in trains if t.gen == 1]
        mkii: [Train] = [t for t in trains if t.gen == 2]
        mkiii: [Train] = [t for t in trains if t.gen == 3]
        total_uptime_lst: [int] = [train.wifi_uptime for train in trains]
        total_uptime: int = int(sum(total_uptime_lst) / len(trains))
        mki_uptime_lst: [int] = [train.wifi_uptime for train in mki]
        mki_uptime: int = int(sum(mki_uptime_lst) / len(mki))
        mkii_uptime_lst: [int] = [train.wifi_uptime for train in mkii]
        mkii_uptime: [int] = int(sum(mkii_uptime_lst) / len(mkii))
        mkiii_uptime_lst: [int] = [train.wifi_uptime for train in mkiii]
        mkiii_uptime: int = int(sum(mkiii_uptime_lst) / len(mkiii))
        expo_uptime_lst: [int] = [train.wifi_uptime for train in expo]
        expo_uptime: int = int(sum(expo_uptime_lst) / len(expo))
        mil_uptime_lst: [int] = [train.wifi_uptime for train in mil]
        mil_uptime: int = int(sum(mil_uptime_lst) / len(mil))

        sp.run("clear")
        print("=========================================")
        print("            Get Overall Stats")
        print("=========================================")
        print("----- Train Count -----")
        print(f"Total trains:             {len(trains)}")
        print(f"MKI/MKII/MKIII:           {len(mki)}/{len(mkii)}/{len(mkiii)}")
        print(f"Expo Line/Millenium Line: {len(expo)}/{len(mil)}")
        print("")
        print("----- Wifi Uptime -----")
        print(f"Total Wifi uptime:        {total_uptime}%")
        print(f"MKI/MKII/MKIII:           {mki_uptime}%/{mkii_uptime}%/{mkiii_uptime}%")
        print(f"Expo Line/Millenium line: {expo_uptime}%/{mil_uptime}%")
        print("")
        input("Press RETURN to continue...")


if __name__ == "__main__":
    sp.run("clear")
    has_quit = False
    trains: [Train] = [
        Train(100, 2, 1, 2, 3),
        Train(101, 1, 1, 0, 2),
        Train(102, 3, 1, 4, 4),
        Train(103, 2, 2, 3, 3),
        Train(104, 2, 2, 1, 4),
        Train(105, 3, 2, 0, 2),
    ]

    while not has_quit:
        selection: str = Menu.main_menu(trains)

        if selection == "1":  # Report on train's wifi
            trains = Menu.report_menu(trains)
        elif selection == "2":  # See specific train's wifi stats
            Menu.get_train_stats_menu(trains)
        elif selection == "3":  # See overall wifi stats
            Menu.get_overall_stats_menu(trains)
        elif selection == "4":  # Quit app
            has_quit = True
            sp.run("clear")
        else:
            Menu.main_menu("Invalid input. Please enter 1, 2, 3, or 4")
