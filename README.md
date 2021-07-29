# pastebinOmatic v1.0
pastebinOmatic is a utility lib for working with pastebin.com

## instolation
```
pip install pastebinOmatic
```

## examples

```python
from pastebinOmatic import *
p = parce("https://pastebin.com/XrXxjtWw")

paste_title = p.get_title()

print(paste_title)
# output: hiiiiiiiiiiiiiiiiiiiiiiiiiii
```
