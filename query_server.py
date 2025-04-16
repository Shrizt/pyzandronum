import pyzandronum
from pyzandronum.enums import RequestFlags

# You can put your IP address and port to query.
server = pyzandronum.Server('hb', 10666)

# Get server info by querying only needed info
server.query(RequestFlags.SQF_NAME | RequestFlags.SQF_MAPNAME)
#or query all info (don't query too often - server will ban you)
#server.query()

# Output server info
print('Host Name:', server.name)
print('Current Game Map:', server.map)
print('Online Players: {0}/{1} (max clients: {2})'.format(
    server.number_players,
    server.max_players,
    server.max_clients
))
print('PWADs: {0} (total loaded: {1})'.format(
    server.pwads,
    server.pwads_loaded
))
print('IWAD filename:', server.iwad, '| IWAD name:', server.gamename)
print('Game mode:', server.gamemode)
print('Response time (ms):', server.response_time)

