+++
title = 'Basic Screen Usage'
date = 2018-06-12
draft = false
tags = ["linux", "screen"]
description = "This demonstrates some basic usage of the screen program."
+++

Screen is handy if you need to start a long-running process and don't want to lose control of your current terminal session. While on an `ssh` connection, you can also run processes in a `screen` session and log off without killing them.

### Start a named `screen`
```
$ screen -R nameofsession
```

### Detach from a `screen`
Use the following while inside a `screen` session to return to the parent session
```
ctrl + a d
```

### List detached `screen` sessions
```
$ screen -list
```

### Reconnect to a detached `screen`
This is the same command that is used to start a named `screen` session. If an existing, detached session does not exist with the name, a new one is created.
```
$ screen -R nameofsession
```
