# pinger
pings a UDP server and computes RTT

docker build -t pinger .

docker run --net=mynet --name client -d pinger

# display the statistics output from the client app
docker logs -f client
