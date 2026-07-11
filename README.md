# Biomech Wild Studio

Biomech Wild Studio is the working content-factory interface for Biomech Wild Instagram production.

This project is separate from `SECOND_BRAIN_2026`.

`SECOND_BRAIN_2026` remains the master knowledge archive. This folder is the working Studio/publish project.

## Current Working Folder

`/Users/evgenijarazguljaeva/Documents/Codex/biomech-wild-studio-publish`

## Current Pages

| Page | Purpose | Data source |
|---|---|---|
| `index.html` | Main Biomech Wild production cards | `data/cards.json` |
| `pets.html` | Domestic biomechanical pets | `data/pets_cards.json` |
| `test/index.html` | TEST character-leader prompt experiments | `data/test_characters.json` |

## Current Content State

As of 2026-07-11:

- Main Studio: 100 cards total.
  - 50 published.
  - 40 ready.
  - 10 active/new.
- Pets Studio: 10 active/new cards.
- TEST: 8 character leaders.

## Local Preview

Use the static preview when you only need to view and copy prompts:

```bash
/usr/bin/python3 -m http.server 8788 --bind 127.0.0.1 --directory "/Users/evgenijarazguljaeva/Documents/Codex/biomech-wild-studio-publish"
```

Open:

- `http://127.0.0.1:8788/`
- `http://127.0.0.1:8788/pets.html`
- `http://127.0.0.1:8788/test/`

## Important Limitation

This folder currently contains a static site.

Static preview and GitHub Pages can:

- show cards;
- search cards;
- open/copy prompts;
- show tabs and counts from JSON data.

Static preview and GitHub Pages cannot reliably:

- move cards between statuses;
- create replacement cards;
- persist "ready" or "published" changes;
- call `/api/mark-ready`, `/api/mark-published`, `/api/ensure-active`.

Those actions require a backend or hosted database.

## Product Rules

- Main Studio, Pets Studio, and TEST are sections of one Biomech Wild Studio system.
- Biomech Wild Studio must not be mixed with "Паника, но структурно".
- Biomech Wild Studio must not be moved back into `SECOND_BRAIN_2026` as a working app.
- Published cards must stay published.
- Active/new cards should be refilled to 10.
- Prompt improvements must be recorded in the system, not only in chat.

## Prompt Rules

Normal video prompts:

- one biomechanical creature;
- natural habitat;
- controlled natural movement;
- smooth cinematic camera;
- no sudden transformations;
- no fur growing, melting, shedding, or disappearing;
- no decorative light effects;
- no falling trees;
- no sudden location changes.

NatGeo prompts:

- two biomechanical species are allowed;
- both must share a believable habitat;
- both must be biomechanical;
- interaction can include stalking, attack, escape, competition, or territorial behavior.

## Next Architecture Step

To become a real working system independent of a sleeping laptop, this project needs:

1. Backend or hosted database.
2. Auth / private workspace.
3. Persistent status actions.
4. Server-side card generation/refill logic.
5. Deployment separate from GitHub Pages static preview.

