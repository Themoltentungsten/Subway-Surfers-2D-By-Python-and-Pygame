# Subway Surfers 2D (Python + Pygame)

An endless-runner inspired by **Subway Surfers**, built as my **2nd-year Python project** with **Pygame**.  
It also ships a **WebAssembly (WASM)** build via **pygbag** so the game can run in the browser.

> 🎮 Dodge trains & blockers across 3 lanes, collect coins, and push your high score!

---

## ✨ Features

- 3-lane endless runner with smooth lane switching
- Trains + blockers with multiple spawn patterns
- Coins, sound effects, score & **persistent High Score**
- Desktop play (Pygame) **and** browser play (pygbag/WASM)
- Pure relative asset paths (`pictures/`, `soundfiles/`) for web hosting

---

## 🕹️ Controls

- **← / →**: switch lanes  
- **Enter**: start from the menu  
- **Mouse click once** inside the page (browser only) to unlock audio

---

## 📦 Project Structure

```
Subway-Surfers-2D-By-Python-and-Pygame/
├─ main.py                 # async entrypoint (required by pygbag)
├─ maingame.py             # main game loop (async + browser-friendly)
├─ mainimg.py              # image/sprite loading & scaling
├─ pictures/               # sprites & backgrounds
├─ soundfiles/             # .ogg/.wav audio (avoid .mp3 for web)
├─ highscore.txt           # desktop high score storage
├─ requirements.txt        # pygbag for CI web builds
├─ vercel.json / netlify.toml (optional)  # hosting config if used
└─ _headers (optional)     # COOP/COEP headers for some static hosts
```

---

## 🖥️ Run Locally (Desktop)

> Requires Python 3.10+.

```bash
# 1) (Recommended) create & activate a virtual env
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install Pygame for desktop play
pip install pygame

# 3) Run the game
python main.py
```

- **High Score** persists to `highscore.txt` in the project root.

---

## 🌐 Build & Play in the Browser (WebAssembly via pygbag)

```bash
# Install pygbag
pip install pygbag

# Quick local test server (opens a browser tab)
python -m pygbag .

# Or produce a static site build
python -m pygbag --build .
# Output goes to: build/web/
# Open build/web/index.html to play
```

> Browsers often require a user gesture: click once inside the page, then press **Enter**.

**Audio format tip:** Prefer **`.ogg`** (or `.wav`). Avoid `.mp3` in the repo for web builds.

---

## 🚀 Deploy (static hosting)

Any static host that serves `build/web/` works. Here are light configs:

### Vercel
- **Build Command:** `python3 -m pygbag --build .`  
- **Output Directory:** `build/web`  
- **Headers** (`vercel.json` in repo root):
  ```json
  {
    "headers": [
      {
        "source": "/(.*)",
        "headers": [
          { "key": "Cross-Origin-Opener-Policy", "value": "same-origin" },
          { "key": "Cross-Origin-Embedder-Policy", "value": "require-corp" },
          { "key": "Cross-Origin-Resource-Policy", "value": "same-origin" },
          { "key": "X-Content-Type-Options", "value": "nosniff" }
        ]
      },
      {
        "source": "/(.*)\.wasm",
        "headers": [{ "key": "Content-Type", "value": "application/wasm" }]
      },
      {
        "source": "/(.*)\.data",
        "headers": [{ "key": "Content-Type", "value": "application/octet-stream" }]
      }
    ]
  }
  ```

### Netlify
- **Build Command:** `python -m pygbag --build . && cp _headers build/web/_headers`  
- **Publish Directory:** `build/web`  
- **Headers**: add a `_headers` file (repo root) and copy it into publish dir:
  ```
  /*
    Cross-Origin-Opener-Policy: same-origin
    Cross-Origin-Embedder-Policy: require-corp
    Cross-Origin-Resource-Policy: same-origin
    X-Content-Type-Options: nosniff

  /*.wasm
    Content-Type: application/wasm

  /*.data
    Content-Type: application/octet-stream
  ```

### Cloudflare Pages
- **Build Command:** `python -m pygbag --build . && cp _headers build/web/_headers`  
- **Output Directory:** `build/web`  
- Cloudflare automatically applies the `_headers` file placed in the output.

> Those COOP/COEP headers enable **cross-origin isolation**, required for pygbag’s WebAssembly threading.

---

## 🧰 Troubleshooting

- **Gray screen / loader stuck:**  
  Ensure COOP/COEP headers are served (see hosting configs). In DevTools Console, `crossOriginIsolated` should be `true`.

- **No audio in browser:**  
  Click once inside the page first; many browsers block audio until a user gesture.

- **404 for assets:**  
  Check that all images and sounds are present under `build/web/pictures/` and `build/web/soundfiles/`. Use **relative** paths (already set in code).

- **pygbag rejects `.mp3`:**  
  Convert to **`.ogg`** with ffmpeg, commit the `.ogg`, and remove `.mp3` from the repo.

---

## 📚 What I Learned (2nd-Year Project)

- Pygame game loop, events, collision checks, and timing
- Asset management (images/audio), basic UI, and HUD
- Porting Python to the web with **pygbag** (WASM)
- Cross-origin isolation (COOP/COEP) and browser quirks

---

## 📸 Screenshots

_Add screenshots/GIFs here when ready._
```
![Menu](pictures/screenshot-menu.png)
![Gameplay](pictures/screenshot-gameplay.png)
```

---

## 📝 License

Educational project. Consider adding an open-source license (e.g., MIT) if you want others to reuse/fork easily.
