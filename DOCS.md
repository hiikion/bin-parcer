# bin parcer docs

- <a href='#pastebin'>pastebin</a>
- <a href='#ghostbin'>ghostbin</a>


## pastebin

importing and calling the class
```python
import bin_parcer as bp

p = bp.pastebin('https://pastebin.com/XrXxjtWw')
```
### get_all()
```python
p.get_all('json')
```
returns all paste stuff <br>
format: dict, json <br>
type dict || str <br>

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
returns true if paste has password false if dosent <br>
type: bool <br> <br>
<a href='#pastebinOmatic-docs'>BACK</a>


## ghostbin

importing and calling the class
```python
import bin_parcer as bp

g = bp.ghostbin('https://ghostbin.com/paste/ymgve')
```
### get_all()
```python
g.get_all('json')
```
### get_content()
```python
content = g.get_content()
```
returns paste content <br>
type: str <br>

### get_title()
```python
title = g.get_title()
```
returns paste title if none returns `None` <br>
type: str <br>
returns all paste stuff <br>
format: dict, json <br>
type dict || str <br>

### password_check()
```python
password_check = g.password_check()
```
returns true if paste has password false if dosent <br>
type: bool

<a href='#bin-parcer-docs'>BACK</a>
