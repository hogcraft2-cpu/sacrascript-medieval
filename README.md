# SacraScript Medieval

A historically conscious toolkit for drafting prayers, blessings, sermon outlines, and parish blog posts inspired by Latin Christian writing around **1400 CE**.

> **Important:** SacraScript creates new, historically inspired texts. It does not certify them as authentic medieval sources or approved liturgical texts. Generated material must not be used as an official Mass text without review by the appropriate Church authority.

## Quick start

Requires Python 3.10+. The starter version uses only the standard library.

```bash
python -m sacrascript --kind prayer --occasion peace --language latin
python -m sacrascript --kind blessing --occasion harvest --language polish
python -m sacrascript --kind sermon --occasion mercy --language bilingual
python -m sacrascript --kind blog --occasion feast-day --language polish
```

Run tests with `python -m unittest discover -s tests -v`.

## Features
- Draft prayers, blessings, sermon outlines, and parish blog posts.
- Latin, Polish, or bilingual output.
- Custom occasion and audience fields.
- Clear distinction between modern compositions and verified historical sources.

This is a **template-based prototype**, not yet an AI model. See `docs/llm-integration.md` for a safe path to add a language-model provider.

## Safeguards
1. Never label generated text an authentic medieval source unless verified against a reliable edition or manuscript catalogue.
2. Do not present generated text as an approved Missal, sacramental formula, or official liturgy.
3. Have Latin and historical claims reviewed by qualified experts.
4. Keep citations and provenance separate from generated compositions.

## License
MIT. See `LICENSE`.
