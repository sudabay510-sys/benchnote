# Benchnote

A listing, photo, and launch cadence for handmade sellers.

Quiz → personalized plan preview → email capture → Gumroad checkout (Monthly or Quarterly). Payments processed by Gumroad. Renews automatically. Cancel anytime from your Gumroad library.

## Run locally
```bash
pip install -r requirements.txt
python app.py   # http://127.0.0.1:5109
```

## Deploy (Render)
- Build: `pip install -r requirements.txt`
- Start: `gunicorn -b 0.0.0.0:$PORT app:app`
- Env: `SECRET_KEY`, `ADMIN_PASSWORD` (owner-only `/admin`), `DATABASE_URL` (pooled Neon Postgres URL), `DATABASE_SCHEMA=benchnote`. Without `DATABASE_URL` it falls back to SQLite (`DATABASE_PATH`).

## Tests
```bash
pytest -q
```

Plans are deterministic rules in `benchnote_brand.py` (`plan()`); swap in an LLM later if wanted.
With `DATABASE_URL` set, leads persist in Postgres. SQLite fallback on free hosting is ephemeral.
