import re

content = """
Some text.

***Question 1?***

Answer 1.

***Question 2?***
Answer 2.

## Header
"""

def process(content):
    def faq_replacer(match):
        question = match.group(1)
        answer = match.group(2).strip()
        return f'<details class="faq-accordion"><summary>{question}</summary><p>{answer}</p></details>'

    # Match ***Question*** followed by text until next *** or Header (#) or EOF
    pattern = r'\*\*\*(.*?)\*\*\*\s*\n(.*?)(?=\n\*\*\*|\n#|$)'
    content = re.sub(pattern, faq_replacer, content, flags=re.DOTALL)
    return content

print(process(content))
