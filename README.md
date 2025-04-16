# Shrizt fork improvements
- Fixed request packet for modern x64 systems 
- Fixed server.response_time calculation to determine server ping correctly
- Added check - what server return (if server return not all requested info - program crashes before) and process only received info
- Added possibility to query only needed info (see example in root) using flags like 
        server.query(RequestFlags.SQF_NAME | RequestFlags.SQF_MAPNAME)
- minor fixes

# pyzandronum

<p align="center">
    <a href="https://www.codefactor.io/repository/github/thehatkid/pyzandronum"><img src="https://www.codefactor.io/repository/github/thehatkid/pyzandronum/badge" alt="CodeFactor" /></a>
    <a href="https://github.com/thehatkid/pyzandronum/commits"><img src="https://img.shields.io/github/commit-activity/w/thehatkid/pyzandronum.svg" alt="Commit Activity" /></a>
</p>

A modern, independent, easy to use, asynchronous [Server query](https://wiki.zandronum.com/Launcher_protocol) wrapper for [Zandronum](https://zandronum.com/) written in Python.

## What is it?

**pyzandronum** is easy to use Python module for checking Zandronum servers.

## What is its goal?

The objective is to make a sufficient Python module that helps to easily query Zandronum server and get Server name, game mode, IWAD, list of PWADs, list of players, etc.
