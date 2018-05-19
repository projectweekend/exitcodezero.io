+++
title = 'Bash History Tips'
date = 2018-05-19
draft = false
tags = ["bash", "linux"]
description = "These are some tips for navigating Bash command history."
+++

### Run the last command with `sudo`
```
$ sudo !!
```

### Run a command by line number in history
Commands displayed using the `history` command each have a line number:
```
$ history
2004  sudo apt update
2005  sudo apt upgrade
2006  ls
2007  cat some-file.txt
```
Using the example output above, we can run the command on line `2005` like this:
```
$ !2005
```

### Use reverse search
Launch a reverse history search with `ctrl-r`, then start typing part of a command to find. The most recently used commands are displayed first. In this example, we are searching for commands that contain `sudo`:
```
(reverse-i-search)`sudo': sudo apt upgrade
```
Continue pressing `ctrl-r` to see the next matching command:
```
(reverse-i-search)`sudo': sudo apt update
```
