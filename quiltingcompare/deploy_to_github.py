#!/usr/bin/env python3
"""
QuiltingCompare.com — One-shot GitHub deploy
Run this once: python3 deploy_to_github.py YOUR_TOKEN
It creates the repo, pushes every file, and enables GitHub Pages.
"""

import sys, os, json, base64, time
from urllib import request, error

# ── Config ────────────────────────────────────────────────────
USERNAME = "potomacfallspublishing-code"
REPO     = "quiltingcompare"
BRANCH   = "main"
# ──────────────────────────────────────────────────────────────

if len(sys.argv) < 2:
    TOKEN = input("Paste your GitHub token: ").strip()
else:
    TOKEN = sys.argv[1].strip()

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json",
    "User-Agent": "QuiltingCompare-Deploy"
}

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

def api(method, path, data=None):
    url = f"https://api.github.com{path}"
    body = json.dumps(data).encode("utf-8") if data else None
    req = request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode("utf-8"))
    except error.HTTPError as e:
        msg = e.read().decode("utf-8")
        if e.code in (409, 422) and ("already exists" in msg or "already initialized" in msg):
            return {"__already_exists": True}
        print(f"  API error {e.code} on {method} {path}: {msg[:120]}")
        return {}

def push_file(abs_path):
    rel = os.path.relpath(abs_path, SITE_DIR).replace("\\", "/")
    with open(abs_path, "rb") as f:
        content_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Check if file already exists (need its SHA to update)
    existing = api("GET", f"/repos/{USERNAME}/{REPO}/contents/{rel}")
    sha = existing.get("sha") if isinstance(existing, dict) else None

    payload = {"message": f"Add {rel}", "content": content_b64, "branch": BRANCH}
    if sha:
        payload["sha"] = sha

    result = api("PUT", f"/repos/{USERNAME}/{REPO}/contents/{rel}", payload)
    status = "updated" if sha else "added"
    print(f"  ✓  {rel}  ({status})")
    return result

# ── Step 1: create repo ────────────────────────────────────────
print(f"\n1/3  Creating repository '{REPO}' on GitHub…")
result = api("POST", "/user/repos", {
    "name": REPO,
    "description": "Quilt batting price comparison — QuiltingCompare.com",
    "private": False,
    "auto_init": False
})
if result.get("__already_exists"):
    print("     Repo already exists — continuing.")
elif result.get("html_url"):
    print(f"     Created: {result['html_url']}")
else:
    print("     (check your token if you see errors below)")

# ── Step 2: push files ─────────────────────────────────────────
print(f"\n2/3  Pushing files…")
skip_names = {os.path.basename(__file__), "deploy_to_github.py", "quiltingcompare-site.zip"}

for root, dirs, files in os.walk(SITE_DIR):
    dirs[:] = sorted([d for d in dirs if d != "__pycache__"])
    for filename in sorted(files):
        if filename in skip_names:
            continue
        if filename.startswith(".") and filename != ".nojekyll":
            continue
        full_path = os.path.join(root, filename)
        push_file(full_path)
        time.sleep(0.25)   # stay inside GitHub's rate limit

# ── Step 3: enable GitHub Pages ────────────────────────────────
print(f"\n3/3  Enabling GitHub Pages…")
pages = api("POST", f"/repos/{USERNAME}/{REPO}/pages", {
    "source": {"branch": BRANCH, "path": "/"}
})
if pages.get("__already_exists") or pages.get("url"):
    print("     GitHub Pages enabled!")
elif pages.get("html_url"):
    print(f"     Live at: {pages['html_url']}")
else:
    print("     (Pages may already be on — check repo Settings → Pages)")

# ── Done ───────────────────────────────────────────────────────
print(f"""
✅  All done!

Your site will be live in ~60 seconds at:
   https://{USERNAME}.github.io/{REPO}/

To connect quiltingcompare.com:
   Add these 4 A records at Porkbun for quiltingcompare.com:
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
   Then add a CNAME:  www  →  {USERNAME}.github.io
   Then in GitHub repo Settings → Pages → Custom domain → type quiltingcompare.com

That's it. Never touch GitHub again — everything else is automated.
""")
