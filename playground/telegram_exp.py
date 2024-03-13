from telebot import formatting


def ignore(a):
    pass


ignore(formatting.mbold("Hello, World!"))
"*Hello, World\!*"
ignore(formatting.mitalic("Hello, World!"))
"_Hello, World\!_"
ignore(formatting.mcode("Hello, World!"))
"""
```
Hello, World\!
```
"""
ignore(formatting.mlink("Hello, World!", "https://www.google.com"))
"""
[Hello, World\!](https://www\.google\.com)
"""
ignore(formatting.mspoiler("Hello, World!"))
"""||Hello, World\!||"""
ignore(formatting.munderline("Hello, World!"))
"""__Hello, World\!__"""
ignore(formatting.mstrikethrough("Hello, World!"))
"""~Hello, World\!~"""
ignore(formatting.mcite("Hello, World!"))
""">Hello, World\!"""
ignore(formatting.escape_markdown("Hello, World!"))
"""Hello, World\!"""
