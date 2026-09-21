#!/usr/bin/python3
from stats.echo import EchoClient

mon = EchoClient("localhost", 8001)
mon.start()
