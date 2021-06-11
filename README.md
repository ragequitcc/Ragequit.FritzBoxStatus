### Ragequit.FritzBoxStatus

This is a "microservice" to get your WAN IP from an AVM Fritz.Box (common router in Germany).

It just returns the IPv4 via HTTP.

Since it used only on an internal network we won't add HTTPS. If you need HTTPS, feel free to implement it add create a PR :)

Build:

```
docker build -t <name> .
```

Run:

```
docker run <name> -p <customport>:8080 -e FritzBoxUri="" -e FritzBoxUser="" -e FritzBoxPassword=""
```

Then visit `127.0.0.1:<customport>`
