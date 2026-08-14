class TextProcessor:

    def format_text(self, w1: str, w2: str = None)-> str:
        if w2 is None:
            return w1.upper()
        return w1 + w2

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))