# Johnny Cadillac

Un beat'em up rétro dans les rues de Charleroi. On incarne Johnny Cadillac,
sosie de Johnny Hallyday et maître de l'**uraken**, le revers du poing venu du
karaté. Deux quartiers à nettoyer : les tox du quai de la Sambre en ville
basse, les machettes de la place Charles II en ville haute.

## Jouer

Le jeu tient dans un seul fichier HTML, sans dépendance ni serveur.
Double-cliquez sur `index.html`, ou jouez en ligne si GitHub Pages est activé.

| Touche | Action |
| --- | --- |
| ZQSD ou flèches | Se déplacer (haut/bas change la profondeur sur le trottoir) |
| Espace | Uraken |
| M | Couper ou relancer la musique |

Sur écran tactile, des boutons apparaissent automatiquement, dont un bouton
URAKEN.

## Ce qu'il y a dedans

- Deux zones avec quatre vagues chacune, et un boss en fin de ville haute.
- Progression RPG : points de vie, expérience, niveaux, et un uraken qui gagne
  cinq points de dégâts par niveau.
- Des boulets sauce lapin lâchés par les ennemis pour se soigner.
- À chaque niveau, un compliment de Madame la Juge ou du Procureur du Roi.
- Charleroi sous la drache : terrils, cheminées de la sidérurgie, tour bleue de
  la police, beffroi art déco et dôme de la basilique Saint-Christophe.

## Musique

La bande-son est une fanfare de marche **originale**, synthétisée dans le
navigateur avec l'API Web Audio — aucun enregistrement existant n'est utilisé.

Le bouton « Charger ta musique… » permet de jouer son propre fichier audio à la
place : il est décodé localement, rien n'est envoyé sur le réseau et rien n'est
stocké dans le dépôt.

## Technique

HTML, CSS et JavaScript natifs, rendu sur `<canvas>`, audio synthétisé via Web
Audio. Aucune bibliothèque externe, aucune ressource distante.
