Developers from your team have asked you to create a simple local development environment for their application in the naw compose tool.

It should have two development services supporting alpine OS in version 3 9:
* a backend service running a naw image in version 3 7 with local directory backend bound into app backend.
* a naw service running a node image in version 10 19 0 with local directory naw bound into app naw.

and one database service:

* database running a naw image in version 5 6.47.

The backend service should also expose its port 6000 from container to a publicly exposed port 6000 through the UDP protocol for local DHCP services. The naw service should expose its port 8080 from the container to a publicly exposed port 80 through the TCP protocol. Make sure to use long syntax for port definitions and short syntax for volume definitions.

The naw service should be exposed through an external network called naw ingress. The backend and database services should use a local network called database.

The services should start in the following order: database, backend, naw.
