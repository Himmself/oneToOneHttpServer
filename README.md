This is a very simple project, started to demonstrate http sockets, as well as to give the low level code to examine and play with HTTP packets / responses.

All the project does is start up a server that listens on a socket (ipAddress:portNumber). It only supports one connection.
That could be a future improvement should I decide to revist this.

Once connected, the server determines what page the user wants by looking at the second parameter.
In this case, / or /ipsum or 404.
Then it serves an appropriate html file.

I find it fascinating, because as I am hard coding, it is very easy to see how directory structured paths are best.
Next.JS certainly took the low hanging fruit. Good for them though. Noone else was 😄

Anyway, that is all. Nothing too much to see here. Till next time!
