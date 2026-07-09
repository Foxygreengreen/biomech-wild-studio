# Biomech Wild Studio — System Changelog

This file records improvements to the same Biomech Wild Studio system. We do not create a replacement system for each iteration.

## 2026-07-09 — Restore Unified Studio Boundary

Working product/project:

- `/Users/evgenijarazguljaeva/Documents/Codex/biomech-wild-studio-publish`

Archive/source of truth:

- `SECOND_BRAIN_2026`

Rules:

- `SECOND_BRAIN_2026` is a knowledge archive, not the working deployed Studio.
- `index.html`, `pets.html`, and `test/index.html` are sections of one Studio system.
- `data/cards.json`, `data/pets_cards.json`, and `data/test_characters.json` are the current visible content sources.
- Every future improvement should be recorded here.

Current content state:

- Main Studio: 90 cards total, 10 new/in work, 30 ready, 50 published.
- Pets Studio: 10 cards, all new/in work.
- TEST: 5 selected character leaders.

Change:

- Fixed local and GitHub Pages data loading by changing absolute `/data/...` fetch paths to relative `data/...` paths on the main and pets pages.
- Added `SYSTEM_REQUIREMENTS.md` as the system passport for the intended Biomech Wild Studio behavior.

Next iteration queue:

- Restore clear navigation between Main Studio, Pets Studio, and TEST.
- Keep the full prompt button set visible: Image, Veo, Seedance, Kling, 8s, 15s, Storyboard, NatGeo, Text, Caption.
- Keep card logic as one system: ready, published, replace to 10 active cards.
- Add visible “published” stability so published cards do not jump back into ready.
