# Biomech Wild Studio — System Requirements

This document describes the intended system, so future iterations improve the same product instead of replacing it.

## Project Boundary

- Biomech Wild Studio is a separate working product.
- `SECOND_BRAIN_2026` is the master knowledge archive and source of truth.
- Studio can use selected knowledge from the archive, but the archive is not the live working interface.

## Core Pages

- Main Studio: biomechanical living beings for Instagram content production.
- Pets Studio: domestic animals as a separate page using the same card logic.
- TEST: controlled character-leader experiments with 5 variations per selected leader.

## Card Logic

- Always keep 10 active/new cards visible.
- When a card is marked done, it should leave the active list.
- The system should refill active cards back to 10.
- Ready cards and published cards must be separate.
- Published cards must stay published and must not return to ready.
- Old completed cards can be marked as published.

## Main Studio Content Scope

- Animals.
- Fish.
- Birds.
- Insects.
- Other living beings.
- All subjects exist in a parallel biomechanical natural world.

## Pets Studio Content Scope

- Cats.
- Dogs.
- Chinchillas.
- Ferrets.
- No other pet categories for now.
- Biomechanics must remain part of the animal structure, not disappear under fur.
- Avoid bones as the main visual language unless explicitly requested.

## Required Prompt Formats

Each production card should provide:

- Image prompt.
- Veo video prompt.
- Seedance video prompt.
- Kling video prompt.
- 8s scene.
- 15s scene.
- Storyboard.
- Documentary encounter.
- Text/overlay.
- Instagram caption with SEO description and exactly 5 hashtags.

## Video Prompt Rules

- No light effects as a decorative event.
- No trees falling.
- No fur growing, melting, shedding, or disappearing.
- No sudden transformations.
- No sudden location changes.
- No strange surprise events unless the rubric explicitly calls for action.
- The camera should be smooth and cinematic.
- Movement should be natural and controlled.
- For normal video prompts: one creature, small movement, natural behavior, possible look to camera, possible subtle play to camera.
- For documentary encounter prompts only: two biomechanical species can interact, attack, stalk, flee, or compete.
- Documentary encounter species must share a believable habitat.
- In documentary encounter prompts both animals must be biomechanical.
- Biomechanical mechanisms must remain stable and visible across the shot.

## Instagram Caption Rules

- Every Instagram caption must be an SEO description, not a casual note.
- Every Instagram caption must include exactly 5 hashtags.
- One hashtag must always be the animal name, normalized without spaces.
- Main Studio default hashtag set: `#biomechwild #biomechanical #aicreatures #wildlifeart #{animalname}`.
- Pets Studio default hashtag set: `#biomechpets #biomechanical #aipets #creaturedesign #{animalname}`.
- Do not add more or fewer than 5 hashtags.

## Product Direction

- First goal: a reliable content-generation assistant for Biomech Wild Instagram.
- Second goal: crossposting and publication workflow.
- Third goal: reusable content-factory platform that can be sold or adapted for other creators.
- Future production system should not depend on the laptop being awake.
- Future version needs a backend, database, authentication, and possibly agents/API integrations.

## Publishing

- GitHub Pages can host the public/demo interface.
- A static GitHub Pages site can show and copy prompts.
- Real status-changing actions require a backend or hosted database.
