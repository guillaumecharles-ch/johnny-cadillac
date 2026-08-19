#!/usr/bin/env python3
"""Ajoute un score au classement commun à partir d'un code JC1-.

Lit le code sur l'entrée standard ou en argument, valide tout ce qui vient de
l'extérieur, et réécrit scores.json trié. Aucun secret n'est manipulé ici : le
robot GitHub s'authentifie tout seul, et en local c'est ta propre session git.
"""
import base64, json, os, re, sys, datetime

FICHIER = "scores.json"
MAX_SCORE = 130000          # plafond théorique atteignable, marge comprise
MAX_ENTREES = 200
MOTIF = re.compile(r"JC1-[A-Za-z0-9_-]+")


def decoder(code):
    corps = code[4:].replace("-", "+").replace("_", "/")
    corps += "=" * (-len(corps) % 4)
    donnees = json.loads(base64.b64decode(corps).decode("utf-8"))
    score = donnees.get("s")
    if not isinstance(score, (int, float)) or not 0 <= score <= MAX_SCORE:
        raise ValueError("score hors limites")
    nom = str(donnees.get("n") or "—")[:14]
    nom = "".join(c for c in nom if c.isprintable()).strip() or "—"
    return {
        "nom": nom,
        "score": int(round(score)),
        "temps": max(0, int(donnees.get("t") or 0)),
        "kills": max(0, int(donnees.get("k") or 0)),
        "gagne": bool(donnees.get("g")),
    }


def sortie(**champs):
    """Transmet le résultat au workflow, s'il y en a un."""
    env = os.environ.get("GITHUB_ENV")
    if not env:
        return
    with open(env, "a", encoding="utf-8") as f:
        for cle, valeur in champs.items():
            f.write(f"{cle}={valeur}\n")


def charger():
    if not os.path.exists(FICHIER):
        return {"scores": []}
    with open(FICHIER, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data.get("scores"), list):
        data["scores"] = []
    return data


def main():
    brut = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read()
    trouve = MOTIF.search(brut or "")
    if not trouve:
        print("::error::aucun code JC1- trouvé dans le message")
        return 1
    try:
        entree = decoder(trouve.group(0))
    except Exception as err:
        print(f"::error::code illisible ({err})")
        return 1

    auteur = os.environ.get("AUTEUR", "").strip()
    if auteur:
        entree["github"] = auteur[:39]

    data = charger()
    cle = (entree["nom"], entree["score"], entree["temps"])
    if any((e.get("nom"), e.get("score"), e.get("temps")) == cle for e in data["scores"]):
        print(f"::notice::score déjà présent pour {entree['nom']}")
        sortie(RESULTAT="doublon", JOUEUR=entree["nom"])
        return 0

    data["scores"].append(entree)
    data["scores"].sort(key=lambda e: -e.get("score", 0))
    data["scores"] = data["scores"][:MAX_ENTREES]
    data["maj"] = datetime.date.today().isoformat()

    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    rang = next(i for i, e in enumerate(data["scores"], 1)
                if (e.get("nom"), e.get("score"), e.get("temps")) == cle)
    print(f"{entree['nom']} entre au classement : {entree['score']} points, rang {rang}")
    sortie(RESULTAT="ajoute", JOUEUR=entree["nom"],
           POINTS=entree["score"], RANG=rang)
    return 0


if __name__ == "__main__":
    sys.exit(main())
