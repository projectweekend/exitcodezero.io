+++
title = 'Compile a Go Executable for Raspberry Pi'
date = 2018-06-16
draft = false
tags = ["raspberry-pi", "go"]
description = "This shows how to compile a Go executable for the Raspberry Pi"
+++

Run the following command, in the root of your Go project, to compile an executable for the Raspberry Pi:

```
$ env GOOS=linux GOARCH=arm GOARM=7 go build
```
