# Ceberus — Orbis™ Desktop Console

Ceberus is a desktop UI shell (Electron + Svelte) around a Python backend.
It is meant to host your Orbis™ home sentinel engine and present it as a
cross‑platform neon‑styled command console.

This repo is structured to be pushed directly to GitHub.

## Structure

```text
ceberus/
  package.json          # Electron + Vite + Svelte config
  vite.config.mts       # Vite config
  main.js               # Electron main process
  preload.js            # Preload bridge
  src/                  # Svelte UI
    main.js
    App.svelte
    styles.css
    routes/
      Dashboard.svelte
      Anomalies.svelte
  backend/              # Python FastAPI backend (stub)
    run_backend.py
    requirements.txt
```

The frontend expects a backend on `http://127.0.0.1:5001` with:

- `GET /api/dashboard`
- `GET /api/anomalies`

The included backend is a stub implementation you can later replace
with your full Orbis AI backend.

## Development: backend

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python run_backend.py
```

This starts FastAPI on `http://127.0.0.1:5001`.

## Development: desktop app

In another terminal:

```bash
# from repo root
npm install
npm run dev      # start Vite/Svelte dev server on :5173
npm start        # launch Electron pointing at dev UI
```

The dashboard and anomalies pages will talk to the backend stub.

## Preparing for a frozen, non‑editable backend

When your real Orbis backend is ready, you can:

1. Replace the logic in `backend/run_backend.py` with your full API bridge.
2. Install its dependencies into `backend/venv`.
3. Use PyInstaller to create a one‑file binary, for example:

   ```bash
   cd backend
   pyinstaller --onefile --name ceberus_backend run_backend.py
   ```

4. Create an `embedded_backend/` directory at the repo root and place the
   generated binary there (e.g. `embedded_backend/ceberus_backend.exe`
   or `embedded_backend/ceberus_backend`).

5. Update `main.js` to spawn that binary instead of relying on a dev backend.

From there you can add electron‑builder to `package.json` and build
platform‑specific installers for Windows, macOS, and Linux.
