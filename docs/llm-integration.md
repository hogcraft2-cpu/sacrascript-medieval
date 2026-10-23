# Integrating a language model

The current prototype is deterministic and uses templates. Add an LLM adapter as a separate module so the CLI remains testable and provider-independent.

Suggested interface:

```python
class TextProvider:
    def generate(self, *, prompt: str) -> str:
        raise NotImplementedError
```

Prompts should specify text type, occasion, audience, language, and length. Require the model to label output as a new composition inspired by Latin Christian writing around 1400, never invent source citations or manuscript provenance, and flag uncertain Latin or historical claims. Do not present output as an approved liturgical formula or official Mass text.

Keep API keys in environment variables, never in source control. Test empty responses, provider failures, provenance labels, and prompt injection. Liturgical use requires review by qualified clergy and relevant language and historical experts.
