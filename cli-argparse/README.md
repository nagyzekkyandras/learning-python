# Using

```
./argparse.py 
usage: argparse.py [-h] [--sum] N [N ...]
argparse.py: error: too few arguments
```

```
./argparse.py -h
usage: argparse.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
  N           an integer for the accumulator

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)
```

```
./argparse.py 1 21 33
33
```

```
./argparse.py 1 21 33 --sum
55
```
