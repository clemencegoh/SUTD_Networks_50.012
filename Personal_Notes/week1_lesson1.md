Important slides:
    slide 25 -  
        OSI vs TCP/IP
        OSI not as popular.
        Transmission Control Protocol/Internet Protocol

    slide 26 -
        layers: Application -> Transport -> Network -> Link -> Physical

    slide 27 -
        views: High level, Medium level, and Low level.
        Each layer is applicable to programmers, sysadmins, and electrical engineers respectively.

    slide 28 - 
        note the alternative names to each layer
        ---- From Wiki ----
        *Datagram* is the basic transfer unit associated with a packet-switched network. These datagrams are typically structured in header and payload sections. Datagrams provide a connectionless communication service across a packet-switched network. The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network.   
        ----

    slides 31-33 - 
        On Network core and important layers for transfer 

    slide 34 - 
        For homework, on how lines each layer adds more bytes of data on the application data, which causes overall data to be quite large.

    slide 36 - 
        Throughput, Latency, and Loss.
        Bandwidth availability vs throughput,concepts must be strong.

    slide 37 - 
        4 sources of delay
        [!Important!]
        This will help in optimisation.

    slide 38 (explained in slide 41) - 
        understand packet switching vs circuit switching
        Currently we use packet switching for the internet.
        Packet switching: 
            - Main reason for packet switching is to eliminate "dead air", unused amounts of time where server is doing nothing when we have multiple users.
            - Allows us to take on bursty traffic (internet browsing, loading of data from server -> client)
            - Allows more users
            - Does not guarantee transmission, potential queueing loss of data
            - Simpler, no call setup

*Note, mathematical models will not be tested as heavily in Networks.