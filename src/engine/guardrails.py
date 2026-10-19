import re
from typing import Tuple

class GuardrailEngine:
    """Enterprise Prompt Security, Red Team Jailbreak Mitigation & PII Scrubber"""

    JAILBREAKS = [
        r"ignore previous instructions", r"system prompt override",
        r"dan mode", r"bypass security", r"reveal (?:api[_-]?key|secret|password)",
        r"drop (?:table|database)", r"<script.*?>", r"unrestricted developer mode"
    ]

    def __init__(self):
        self.jailbreak_pattern = re.compile("|".join(self.JAILBREAKS), re.IGNORECASE)
        self.email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        self.key_pattern = re.compile(r'(?:sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{20,})')
        self.card_pattern = re.compile(r'\b(?:\d{4}[ -]?){3}\d{4}\b')

    def inspect(self, prompt: str) -> Tuple[bool, str]:
        match = self.jailbreak_pattern.search(prompt)
        if match:
            return True, f"Adversarial signature detected: '{match.group(0)}'"
        return False, "Passed"

    def sanitize_pii(self, prompt: str) -> Tuple[str, bool]:
        sanitized = self.email_pattern.sub("[PII_EMAIL_REDACTED]", prompt)
        sanitized = self.key_pattern.sub("[API_KEY_REDACTED]", sanitized)
        sanitized = self.card_pattern.sub("[CARD_NUM_REDACTED]", sanitized)
        return sanitized, (sanitized != prompt)
