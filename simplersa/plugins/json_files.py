import json

def export_public_key(n: int, e: int) -> str:
    public_key = {
        "n": n,
        "e": e
    }
    return json.dumps(public_key, indent=4)

def export_private_key(n: int, d: int, e: int, p: int, q: int) -> str:
    private_key = {
        "n": n,
        "d": d,
        "e": e,
        "p": p,
        "q": q
    }

    return json.dumps(private_key, indent=4)

def import_public_key(filename: str) -> tuple:
    with open(filename, "r") as f:
        data = json.load(f)
        n = data["n"]
        e = data["e"]
    return n, e

def import_private_key(filename: str) -> tuple:
    with open(filename, "r") as f:
        data = json.load(f)
        n = data["n"]
        d = data["d"]
        e = data["e"]
        p = data["p"]
        q = data["q"]
    return n, d, e, p, q