#!/usr/bin/python3
from mcstatus import JavaServer


def directCheck(ip, port):
    server = JavaServer(ip, port)

    try:

        try:
            ping = server.ping()
        except:
            ping = "???"

        status = server.status()

        players_online = status.players.online
        players_max = status.players.max
        player_list = status.players.sample
        message_of_the_day = status.description
        version = status.version.name

        print(f"\nPlayers online: {players_online}/{players_max}\nLatency: {ping} ms\nVersion: {version}\n\nMOTD:\n{message_of_the_day}\n")

        #I am not proud of this
        print("Players:")
        if player_list is not None:
            for player in player_list:
                print(f"{player.name} | {player.id}")
        else:
            print("No players online.")

        print("\n")

    except:
        print("Failed to get status (connection may have been refused).\n")


directCheck(input("\nMinecraft server IP: "), int(input("\nPort: ")))
