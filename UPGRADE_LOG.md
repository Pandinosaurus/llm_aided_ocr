# Dependency Upgrade Log

**Date:** 2026-01-18  |  **Project:** llm_aided_ocr  |  **Language:** Python (requirements.txt)

## Summary
- **Updated:** N/A (uses requirements.txt, not pyproject.toml)
- **Skipped:** 0
- **Failed:** 0
- **Needs attention:** 0

## Notes

This project uses `requirements.txt` without pinned versions (just package names).
Dependencies are pulled at latest compatible versions at install time.

Current dependencies:
- anthropic, openai (LLM providers)
- transformers, llama-cpp-python
- opencv-python-headless, pillow, pdf2image, pytesseract
- numpy, scikit-learn
- tiktoken, langdetect
