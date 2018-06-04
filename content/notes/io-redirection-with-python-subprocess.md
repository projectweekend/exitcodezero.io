+++
title = "IO Redirection With Python's Subprocess Module"
date = 2018-06-03
draft = false
tags = ["python", "subprocess"]
description = "This example shows how to chain commands, via IO redirection, using Python's subprocess module."
+++

The example code below demonstrates the following concepts using Python's [subprocess](https://docs.python.org/3/library/subprocess.html) module.

* Launching two processes, piping `stdout` from the first to `stdin` of the second
* Waiting for both to finish with a timeout in case either process takes too long
* Checking the exit code for each process independently

```python
from subprocess import PIPE, Popen, TimeoutExpired


ls = Popen(['ls', '-la'], stdout=PIPE)
grep = Popen(['grep', 'Pipfile'], stdin=ls.stdout, stdout=PIPE)

for process in [ls, grep]:
    try:
        process.wait(timeout=5)
    except TimeoutExpired:
        # You could raise a different exception, or log and re-raise
        msg = 'This process ran longer than expected: {0}'
        print(msg.format(' '.join(process.args)))
        raise

    if process.returncode != 0:
      # You could rasie an exception here indicating which process failed
      msg = 'This process did not return a 0 exit code: {0}'
      print(msg.format(' '.join(process.args)))

# This loop is just to show the final output from the grep process
for line in grep.stdout:
    print(line)
```

**Remember:**

* In order for a process to make its `stdout` stream available to another, it needs to receive `subprocess.PIPE` for the `stdout` argument in the `Popen` constructor.
* Processes launched with `Popen` release the [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) and execute without blocking. In the example above, we use the `wait()` method to block our code until both finish execution.
