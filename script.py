#!/usr/bin/python3
from mcstatus import JavaServer

server_ip = input("\nMinecraft server IP (port not required.): ")
port = 25565
server = JavaServer(server_ip, port)

try:
    status = server.status()
    amount_of_players = status.players.online
    ping = server.ping()
    version = status.version.name
    message_of_the_day = status.description

    print(f"\nPlayers online: {amount_of_players}\nLatency: {ping} ms\nVersion: {version}\n\nMOTD:\n{message_of_the_day}\n")

    try:
        query = server.query()
        print(f"Plugins: {query.software}\nPlayers: {' ; '.join(query.players.names)}")
    except:
        print("Cannot query server.\n")

except:
    print("Failed to get status (server may be offline or non-existent).\n")
