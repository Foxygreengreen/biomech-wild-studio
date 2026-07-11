# Biomech Wild Studio Architecture

Date: 2026-07-11

This document describes the current architecture so future changes improve the existing system instead of replacing it.

## 1. Project Boundary

Working project:

`/Users/evgenijarazguljaeva/Documents/Codex/biomech-wild-studio-publish`

Knowledge archive:

`/Users/evgenijarazguljaeva/Documents/SECOND_BRAIN_2026`

The working Studio is not the master archive. The archive can inform methodology and prompt rules, but the live Studio interface should stay separate.

## 2. Runtime Type

Current runtime: static HTML + JSON.

There is no committed backend in this folder right now.

The pages contain JavaScript that calls API routes such as:

- `/api/mark-ready`
- `/api/mark-ready-only`
- `/api/mark-active`
- `/api/mark-published`
- `/api/ensure-active`

Those routes are not provided by plain `python3 -m http.server` or GitHub Pages.

Result:

- viewing works;
- copying prompts works;
- status-changing buttons need backend support.

## 3. Files

| File | Role |
|---|---|
| `index.html` | Main production interface for living beings |
| `pets.html` | Domestic pets production interface |
| `test/index.html` | Controlled TEST prompt experiments |
| `data/cards.json` | Main Studio card data |
| `data/pets_cards.json` | Pets Studio card data |
| `data/test_characters.json` | TEST character data |
| `SYSTEM_REQUIREMENTS.md` | Product behavior requirements |
| `SYSTEM_CHANGELOG.md` | Iteration history |
| `README_DEPLOY.md` | Older deploy notes; partially outdated |
| `README.md` | Current project entrypoint |
| `ARCHITECTURE.md` | Current architecture map |

## 4. Data Model

### Main / Pets Cards

Data files:

- `data/cards.json`
- `data/pets_cards.json`

Top-level shape:

```json
{
  "cards": []
}
```

Observed card fields:

- `num`
- `name`
- `hook`
- `file`
- `videoFile`
- `date`
- `group`
- `groupLabel`
- `status`
- `imagePrompt`
- `videoPrompt`
- `videoPromptVeo`
- `videoPromptSeedance`
- `videoPromptKling`
- `scene8s`
- `scene15s`
- `storyboard30s`
- `natgeoEncounter`
- `overlay`
- `caption`
- `notes`
- `platforms`

### Groups

Current UI group values:

- `active`
- `ready`
- `published`

Expected behavior:

- `active` means visible new/in-work card.
- `ready` means ready to publish.
- `published` means already published and should stay published.

### Status Text

Current observed status labels:

- `💡 идея`
- `🟢 готово к публикации`
- `✅ опубликовано`

The UI mostly relies on `group`, while status is the human label.

## 5. Current Counts

As of inspection on 2026-07-11:

| Data file | Total | Active | Ready | Published |
|---|---:|---:|---:|---:|
| `cards.json` | 100 | 10 | 40 | 50 |
| `pets_cards.json` | 10 | 10 | 0 | 0 |

TEST:

- `test_characters.json`: 8 characters.
- Statuses: `READY_FOR_VARIATION`, `NEEDS_SOURCE`.

## 6. UI Actions

Current intended UI actions:

- Active card: `Готово → заменить новой`.
- Ready card: `Вернуть в новые`, `Опубликовано`.
- Published card: `Вернуть в готово`.
- Main page: `Добрать до 10`.

Important product decision:

Published cards should not accidentally return to ready in normal workflow. Any "return" action should be deliberate and clearly labeled as an exception.

## 7. Static vs Working Modes

### Static Mode

Used by:

- GitHub Pages.
- `python3 -m http.server`.

Good for:

- browsing;
- copying prompts;
- showing public/demo interface;
- sharing a link.

Not enough for:

- saving card status changes;
- generating new cards;
- refilling active cards;
- background automation.

### Working Mode Needed

To fully work as intended, the Studio needs one of:

- local backend script;
- hosted backend;
- serverless functions;
- hosted database;
- app platform with persistent storage.

## 8. Prompt System Requirements

All production cards should include:

- Image prompt.
- Veo prompt.
- Seedance prompt.
- Kling prompt.
- 8s scene.
- 15s scene.
- Storyboard.
- NatGeo encounter.
- Text/overlay.
- Instagram caption with SEO description and no more than 5 hashtags.

Video prompt constraints:

- no light effects as event;
- no falling trees;
- no fur growing/shedding/disappearing;
- no sudden transformations;
- no sudden location changes;
- biomechanics must remain stable and visible;
- camera should be smooth, controlled, cinematic;
- normal prompts use one creature;
- NatGeo prompts can use two biomechanical species in the same habitat.

## 9. Known Risks

1. Static pages expose buttons that cannot persist changes without backend.
2. `README_DEPLOY.md` mentions a `site/` folder and build scripts that are not present in this publish project.
3. Local and public versions can diverge.
4. Manual JSON edits can break counts or statuses.
5. Generated content can drift from prompt rules unless generation logic is centralized.

## 10. Recommended Next Steps

Short term:

1. Add a small working backend or choose hosted storage.
2. Make status actions actually persist.
3. Ensure active cards refill to 10.
4. Hide or soften status-changing buttons on public GitHub Pages if no backend is present.
5. Keep updating `SYSTEM_CHANGELOG.md`.

Medium term:

1. Move card generation rules into one generator module.
2. Add validation for JSON fields and statuses.
3. Add a private working interface and a public showcase interface.
4. Add crossposting workflow.
5. Prepare reusable content-factory template for other creators.

