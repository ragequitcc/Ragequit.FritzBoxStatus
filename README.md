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
docker run <name> -p <customport>:8080 -e FritzBoxUri="uri" -e FritzBoxUser="user" -e FritzBoxPassword="pass"
```

Or

Unix / MacOS

```
export FritzBoxUri=<uri>
export FritzBoxUser=<user>
export FritzBoxPassword=<password>
```

Windows Powershell

```
$Env:FritzBoxUri = "<uri>"
$Env:FritzBoxUser = "<user>"
$Env:FritzBoxPassword = "<password>"
```

And then run `pyton main.py`

Visit `127.0.0.1:<customport>` to get the WAN IPv4.
