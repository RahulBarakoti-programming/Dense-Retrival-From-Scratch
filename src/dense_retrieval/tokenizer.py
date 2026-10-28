import re 
from collections import Counter

class SimpleTokenizer:
    """A Basic word-level tokenizer for learning purposes"""
    PAD_TOKEN = "[PAD]"
    UNK_TOKEN = "[UNK]"

    def __init__(self) -> None:
        self.vocab : dict[str, int] = {
            self.PAD_TOKEN: 0,
            self.UNK_TOKEN: 1
        }

    def tokenize(self, text: str) -> list[str]:
        """Convert texts into lowercase word and punctuation tokens."""
        return re.findall(r"\W+|[^\W\s]", text.lower())

    def build_vocab(
            self,
            texts: list[str],
            max_vocab_size: int = 10_000
    ) -> None:
        """Build a vocabulary from a collection of texts."""
        if max_vocab_size < 2