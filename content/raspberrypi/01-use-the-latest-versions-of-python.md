+++
title = "01: Use the latest versions of Python"
description = "This guide demonstrates the best way to install and manage the latest versions of Python."
date = 2017-09-16
draft = false
+++
The Raspberry Pi's [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) operating system uses default versions of Python that are out of date. Using the open source [pyenv](https://github.com/pyenv/pyenv) tool you can easily install and manage the latest versions. I use it, almost daily, for development projects at work and home. Having worked in Python both with and without `pyenv`, I can confidently say using it makes life much better.


### Install and update pyenv
Using the official [pyenv-installer](https://github.com/pyenv/pyenv-installer) you can get started with `pyenv` in just a few steps. First, download the install script and execute it in bash.

```bash
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

At the end of the installer's output, you will see a warning message telling you to add some configuration to the `~/.bash_profile` file. On the Raspberry Pi, you will add this to the end of the `~/.bashrc` file instead.

Finally, log out and back in before issuing the command to update `pyenv`.

```bash
$ pyenv update
```

At this point, you are ready to use `pyenv` to install new versions of Python.


### Install the latest Python versions
Use the `install` command to download and install any version of Python. At the time of this writing, the latest release for Python 2 was 2.7.13. The following command installs that version.

```bash
$ pyenv install 2.7.13
```

Don't be alarmed if the install process takes a while to complete; this is normal. Once it finishes, repeat the command above using the latest release of Python 3.

```bash
$ pyenv install 3.6.2
```

With both versions of Python installed, you can use `pyenv` to switch between them as needed.


### Switch between Python versions
Use the `versions` command to see all versions of Python installed on the Raspberry Pi, including the system default.

```bash
$ pyenv versions
```

You can switch Python versions locally at the directory level. If you have a Python 3 project at the path `~/whatever`, use the `local` command inside that path to set the version. After doing so, any Python code executed in this location will use the specified version instead of the system default.

```bash
$ cd ~/whatever
~/whatever $ pyenv local 3.6.2
```

To change Python versions globally, across the entire system, use the `global` command.

```bash
$ pyenv global 3.6.2
```
