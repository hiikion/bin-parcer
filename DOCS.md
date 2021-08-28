# pastebinOmatic docs

- <a href='#'>pastebin</a>
- <a href='#'>ghostbin</a>


## pastebin

importing and calling the class
```python
import pastebinOmatic as pom

p = pom.pastebin('https://pastebin.com/XrXxjtWw')
```

### get_content()
```python
content = p.get_content()
```
returns paste content <br>
type: str

### get_title()
```python
title = p.get_title()
```
returns paste title <br>
type: str

### get_author()
```python
author = p.get_author()
```
returns paste author <br>
type: str

### get_date()
```python
date = p.get_date()
```
returns paste creation date <br>
type: str

### get_views()
```python
views = p.get_views()
```
returns paste views <br>
type: int

### get_expire_date()
```python
expire_date = p.get_expire_date()
```
reurns pate expire date <br>
type: str

### get_syntax_hilight()
```python
syntax_hilight = p.get_syntax_hilight()
```
returns pate syntax hilight <br>
if none returns `text` <br>
type: str

### password_check()
```python
password_check = p.password_check
```
returns true if paste has password false if dosent
type: bool
<a href='#'>BACK</a>
