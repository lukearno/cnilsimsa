# cNilsimsa

A C implementation of Nilsimsa for Python.

```shell
$ pip install cnilsimsa
```

We are building this module one piece at a time. So far, that means only
`compare_hexdigests` because needing a faster way to do that was the
primary motivation to start this project.

```python
from cnilsimsa import compare_hexdigests
```

It works exactly like the method of the same name from pynilsimsa but
is more than an order of magnitude faster, so if you need to do lots of
deduplication over a large corpus of documents via nilsimsa hex digests
from Python, this should be helpful.

Building out the rest of of the methods for representing and cooking 
LSHs to provide a full drop-in replacement for pynilsimsa is the longer
term goal.

```python
import cnilsimsa as nilsimsa
```

The more complete pure Python implementation is here:

https://code.google.com/p/py-nilsimsa/

Thanks to the authors of the Ruby/C implementation from which our
our `fillpopcount()` function is taken.

https://github.com/jwilkins/nilsimsa

Thanks to the Perl/C implementation that inspired both predecessors.

http://ixazon.dynip.com/~cmeclax/nilsimsa.html

Contributions welcome.