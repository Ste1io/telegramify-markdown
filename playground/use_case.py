import re

import telegramify_markdown
from telegramify_markdown.customize import markdown_symbol

markdown_symbol.head_level_1 = "📌"  # If you want, Customizing the head level 1 symbol
markdown_symbol.link = "🔗"  # If you want, Customizing the link symbol
md = """*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
~strikethrough~
"""
quote = """>test"""
task = """
- [x] task1?
-- [x] task2?

\\\\( T\\(n\\) \\= 100^\\{10\\} \\\\) 用大 O 记号表示。\\~\\[RULE\\]\n\n观察此函数可知，它是一个常数

>1231

"""
test_md = """
**bold text**
||spoiler||
"""
math = r"""
\[
\begin{aligned}
\text{Let } f(x) &= \frac{1}{x} \\
\text{Then } f'(x) &= -\frac{1}{x^2} \\
\text{And } f''(x) &= \frac{2}{x^3}
\end{aligned}
\]

$ f(x) = \frac{1}{x} $
"""

converted = telegramify_markdown.convert(math)
print(converted)


