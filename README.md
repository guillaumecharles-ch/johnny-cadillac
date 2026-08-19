# Johnny Cadillac

Un beat'em up rétro dans les rues de Charleroi. On incarne Johnny Cadillac,
sosie de Johnny Hallyday et maître de l'**uraken**, le revers du poing venu du
karaté. Trois étapes : les tox du quai de la Sambre en ville basse, une
traversée de la Sambre en gondole, puis les machettes de la place Charles II
en ville haute.

## Jouer

Le jeu tient dans un seul fichier HTML, sans dépendance ni serveur.
Double-cliquez sur `index.html`, ou jouez en ligne si GitHub Pages est activé.

| Touche | Action |
| --- | --- |
| ZQSD ou flèches | Se déplacer (haut/bas change la profondeur sur le trottoir) |
| Espace | Uraken, et ramasser une pita-mitraillette |
| M | Couper ou relancer la musique |

Sur écran tactile, des boutons apparaissent automatiquement, dont un bouton
URAKEN.

## Ce qu'il y a dedans

- **Trois zones.** Ville basse et ville haute comptent quatre vagues chacune,
  avec un boss pour finir ; entre les deux, une descente de la Sambre en
  gondole où il faut slalomer entre pneus, palettes, caddies, bidons et ce qui
  flotte à côté. Un uraken bien placé dégage un débris de la proue.
- **Des ennemis qui tirent.** Les tox lancent des seringues, les machettes
  lancent leur lame. Un bandeau turquoise annonce le tir : l'uraken dévie le
  projectile si le timing est bon.
- **Pita-mitraillettes sauce andalouse**, coca sans sucre compris, posées au
  sol et lâchées par les ennemis. On les ramasse avec Espace et elles rendent
  30 points de vie. À pleine santé, Espace frappe au lieu de ramasser.
- **Progression RPG** : points de vie, expérience, niveaux, et un uraken qui
  gagne cinq points de dégâts par niveau.
- À chaque niveau, un compliment de Madame la Juge ou du Procureur du Roi.
- **Score et classement.** La partie est chronométrée : le score récompense la
  vitesse, les adversaires mis au tapis, le niveau atteint et les dégâts
  évités. En fin de partie on entre son nom, et le classement du Pays Noir est
  conservé sur l'appareil.
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
