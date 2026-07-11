# Biomech Wild Studio — System Changelog

This file records improvements to the same Biomech Wild Studio system. We do not create a replacement system for each iteration.

## 2026-07-11 — Strict SEO Instagram Caption Rule

Change:

- Added a hard Instagram caption rule to the generator.
- Updated Main Studio and Pets Studio existing captions.
- Captions are now SEO descriptions.
- Captions now always contain exactly 5 hashtags.
- One hashtag is always the animal name, normalized without spaces.
- Main Studio hashtag set: `#biomechwild #biomechanical #aicreatures #wildlifeart #{animalname}`.
- Pets Studio hashtag set: `#biomechpets #biomechanical #aipets #creaturedesign #{animalname}`.

Verification:

- Checked `data/cards.json` and `data/pets_cards.json`: 0 hashtag-count errors.
- Backend syntax check passed.

## 2026-07-11 — No-Text Rule and Duplicate Active Set Fix

Change:

- Added a strict Studio-wide prompt rule: generated images/videos must contain no text, no logo, no watermark, no captions, and no letters anywhere.
- Removed `National Geographic` / `NatGeo` wording from Main Studio, Pets Studio, TEST data, and generator output to prevent logos, watermarks, or branded text appearing in images.
- Changed visible prompt button label from `NatGeo` to `Encounter`.
- Removed the duplicated luminescent active Main set from production flow:
  - `101` Luminous Manta Ray
  - `102` Glowfin Starfish
  - `103` Lantern Firefly
  - `104` Abyssal Whale
  - `105` Nocturne Octopus
  - `106` Neon Reef Cuttlefish
  - `107` Aurora Jellyfish
  - `108` Ember Salamander
  - `109` Moonlit Snow Owl
  - `110` Prismatic Beetle
- These duplicate cards are now marked as `rejected` / `не использовать`, not deleted.
- Created a new Main active set that does not reuse TEST leader species:
  - `111` Opal Koi
  - `112` Lumen Gecko
  - `113` Tideglass Horseshoe Crab
  - `114` Mangrove Mudskipper Unit
  - `115` Frostline Arctic Fox
  - `116` Amber Leafcutter Ant
  - `117` River Otter Frame
  - `118` Desert Viper Coil
  - `119` Alpine Ibex Mechanism
  - `120` Glass Reef Shrimp
- Updated generator pool so future Main cards avoid the TEST-leader duplication pattern.

Verification:

- Checked Main, Pets, and TEST data: no `National Geographic` / `NatGeo` text remains.
- Checked Main, Pets, and TEST data: no-text/no-logo/no-watermark rules are present.
- Current Main counts: 120 total, 10 active, 50 ready, 50 published, 10 rejected.

## 2026-07-11 — Refresh Active Cards and Add Luminescent Variants

Change:

- Added luminescent card variants to the local backend generator as biological/material texture, not decorative light effects.
- Expanded Main Studio subject pool with luminous biomechanical creatures.
- Expanded Pets Studio subject pool while keeping the allowed categories: cats, dogs, chinchillas, ferrets.
- Moved all current active Main cards to ready and created a new active set:
  - `101` Luminous Manta Ray
  - `102` Glowfin Starfish
  - `103` Lantern Firefly
  - `104` Abyssal Whale
  - `105` Nocturne Octopus
  - `106` Neon Reef Cuttlefish
  - `107` Aurora Jellyfish
  - `108` Ember Salamander
  - `109` Moonlit Snow Owl
  - `110` Prismatic Beetle
- Moved all current active Pets cards to ready and created a new active set:
  - `11` Copper House Dog
  - `12` Ferret Cable Runner
  - `13` Lumen Collar Cat
  - `14` Porcelain Toy Dog
  - `15` Velvet Chinchilla Unit
  - `16` Copper Mask Ferret
  - `17` Tuxedo Servo Cat
  - `18` Dachshund Spine Unit
  - `19` Blue Chinchilla Rotor
  - `20` Albino Ferret Relay
- Marked all TEST characters as `READY_FOR_VARIATION`.
- Added `PLATFORM_ROADMAP.md` for the independent linked platform path.

Verification:

- Main Studio now has 110 cards: 10 active, 50 ready, 50 published.
- Pets Studio now has 20 cards: 10 active, 10 ready.
- TEST has 8 characters, all source-ready.
- Backend syntax check passed.

Next:

- Restart local backend to load the updated generator code.
- Add visible action log / done-today list.
- Decide hosted persistence: Supabase, Firebase, or Railway backend.

## 2026-07-11 — Document Current Working Architecture

Change:

- Added `README.md` as the current project entrypoint.
- Added `ARCHITECTURE.md` to describe the real static HTML + JSON architecture.
- Documented the distinction between static viewing mode and working status-changing mode.
- Recorded current data counts: Main Studio 100 cards, Pets Studio 10 cards, TEST 8 characters.

Reason:

- Prevent future iterations from confusing `SECOND_BRAIN_2026`, the old `site/` folder notes, GitHub Pages static preview, and the current working publish project.
- Make it clear that `/api/...` status actions require backend support and cannot persist on GitHub Pages or plain static preview.

Verification:

- Inspected current files and JSON data.
- Confirmed data sources:
  - `data/cards.json`
  - `data/pets_cards.json`
  - `data/test_characters.json`
- Confirmed Git state only had untracked local `launchers/` before this documentation update.

Next:

- Decide the next concrete implementation target: backend/persistent status actions, active-card refill logic, or public/private interface split.

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
