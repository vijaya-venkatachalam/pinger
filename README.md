# pinger
Pings a UDP server and computes RTT.
Pinger is the client side application.
The server is in the ponger repo.
To run the pinger application, follow the steps below
1. docker build -t pinger .
2. docker run -d --net=host --name ping pinger


