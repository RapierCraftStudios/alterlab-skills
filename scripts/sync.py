"""Mirror the published AlterLab agent skills from alterlab.io.

Only files served publicly by https://alterlab.io/.well-known/agent-skills/index.json
are fetched. Each SKILL.md is verified against its digest in the index.
"""
import hashlib
import json
import pathlib
import sys
import urllib.error
import urllib.request

BASE = "https://alterlab.io"
ROOT = pathlib.Path(__file__).resolve().parent.parent


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "alterlab-skills-mirror"})
    return urllib.request.urlopen(req, timeout=30).read()


def main():
    index = json.loads(get(f"{BASE}/.well-known/agent-skills/index.json"))
    skills = index["skills"]
    if len(skills) < 5:
        sys.exit("index lists fewer than 5 skills; refusing to mirror")
    for s in skills:
        name = s["name"]
        body = get(s["url"])
        if "sha256:" + hashlib.sha256(body).hexdigest() != s["digest"]:
            sys.exit(f"digest mismatch for {name}")
        d = ROOT / "agent-skills" / name
        (d / "scripts").mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_bytes(body)
        script = name.split("-", 1)[1] + ".py"
        try:
            (d / "scripts" / script).write_bytes(get(f"{BASE}/agent-skills/{name}/scripts/{script}"))
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise


main()
