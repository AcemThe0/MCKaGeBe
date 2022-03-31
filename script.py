#!/usr/bin/python3
from mcstatus import JavaServer


def directCheck(ip, port):
    server = JavaServer(ip, port)

    try:
        status = server.status()
        ping = server.ping()
        version = status.version.name

        players_online = status.players.online
        players_max = status.players.max
        player_list = status.players.sample
        message_of_the_day = status.description


        print(f"\nPlayers online: {players_online}/{players_max}\nLatency: {ping} ms\nVersion: {version}\n\nMOTD:\n{message_of_the_day}\n")

        #I am not proud of this
        print("Players: ", end="")
        if player_list is not None:
            for player in player_list:
                print(f"{player.name}", end=" ; ")
        else:
            print("No players online.")

        print("\n")

    except:
        print("Failed to get status (server may be offline, non-existent or you may be banned).\n")


directCheck(input("\nMinecraft server IP (port not required.): "), 25565)
