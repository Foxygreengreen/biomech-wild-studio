# Biomech Wild Studio — Platform Roadmap

Date: 2026-07-11

Goal: turn the current local/static Biomech Wild Studio into an independent private platform available by link and not dependent on the laptop being awake.

## Current State

The current project is a strong local working prototype:

- static HTML interface;
- JSON card data;
- local Python backend for status actions;
- GitHub Pages-compatible public preview;
- Main, Pets, and TEST sections.

Current limitation:

- persistent actions work only when the local backend is running;
- GitHub Pages cannot save status changes;
- there is no authentication or hosted database yet.

## Target Product

Private content-factory platform:

- works by link;
- has login/private access;
- stores cards in a hosted database;
- keeps active cards at 10;
- moves cards through `active → ready → published`;
- has separate workspaces/series;
- can later support crossposting and API integrations.

## Recommended Stages

### Stage 1 — Stabilize Local Studio

- Keep current HTML interface.
- Keep JSON data while workflows are still changing.
- Improve local backend actions.
- Add action log / done-today list.
- Add stronger card generator rules.
- Keep backups before data writes.

### Stage 2 — Hosted Data Layer

Choose one:

- Supabase for database + auth.
- Firebase for quick hosted data.
- Small custom backend on Railway/Render/Fly.

Recommended: Supabase + small backend or serverless functions.

Why:

- status changes persist online;
- can be private;
- future crossposting and user accounts are easier;
- not tied to the laptop.

### Stage 3 — Private Working App

- Deploy working app to Vercel/Netlify/Railway.
- Add auth.
- Separate private work interface from public showcase.
- Hide or disable action buttons in public demo.

### Stage 4 — Content Factory Product

- Add workspaces.
- Add custom content themes.
- Add prompt templates.
- Add creator onboarding.
- Add export/crossposting.
- Add paid access or client installs.

## Immediate Next Technical Decision

Pick data persistence:

1. Supabase.
2. Firebase.
3. Railway backend with JSON/database.

Best first choice: Supabase, because it gives database + auth + API and can grow into a paid product.

