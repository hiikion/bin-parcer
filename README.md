# pastebinOmatic v1.1
pastebinOmatic is a utility lib for working with pastebin.com

## instolation
```
pip install pastebinOmatic
```

## examples

```python
import pastebinOmatic as pom 


p = pom.parce("https://pastebin.com/XrXxjtWw")

paste_title = p.get_title()

print(paste_title)
# output: hiiiiiiiiiiiiiiiiiiiiiiiiiii
```
## TODO
- api stuff
- scrapper

## links
<a href="https://github.com/hiikion/pastebinOmatic/blob/main/DOCS.md">DOCS</a> | <a href="https://pypi.org/project/pastebinOmatic/">PyPi</a>
