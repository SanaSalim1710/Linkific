# Regex Cheatsheet


| Pattern | Matches |
|---------|---------|
| `\d` | Any digit `[0-9]` |
| `\D` | Any non-digit |
| `\w` | Alphanumeric character `[a-zA-Z0-9_]` |
| `\W` | Non-alphanumeric character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `\b` | Word boundary |
| `[abc]` | Any of a, b, or c |
| `[^abc]` | Anything except a, b, c |
| `[a-z]` | Any lowercase letter |
| `[a-zA-Z0-9]` | Any letter or digit |

 Syntax | Description | 
|--------|---------|
| `.` | Any character except newline |
| `*` | 0 or more of previous | 
| `+` | 1 or more of previous | 
| `?` | 0 or 1 of previous (optional) | 
| `^` | Start of string | 
| `$` | End of string | 
| `\|` | OR | 
| `{n}` | Exactly n times | 
| `{n,m}` | Between n and m times | 

```python
import re

re.search(pattern, text)     # find first match 
re.match(pattern, text)      # match only at start of text
re.findall(pattern, text)    # return list of all matches
re.sub(pattern, a, text)     # replace matches with a
re.split(pattern, text)      # return list str split at each match
