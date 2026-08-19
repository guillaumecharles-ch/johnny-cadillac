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

Sur écran tactile, une croix directionnelle complète et un bouton URAKEN
apparaissent, jamais par-dessus le jeu : **sous** la scène en portrait, et
**de part et d'autre** en paysage, où la hauteur d'écran manque. La scène est
bornée en hauteur autant qu'en largeur, pour que tout reste dans le cadre.

## Ce qu'il y a dedans

- **Trois zones.** Ville basse et ville haute comptent quatre vagues chacune ;
  entre les deux, une descente de la Sambre en gondole où il faut slalomer
  entre pneus, palettes, caddies, bidons et ce qui flotte à côté. Un uraken
  bien placé dégage un débris de la proue — mais pas un bateau-promenade, qui
  passe indifférent avec son couple enlacé à la proue. Sur la berge d'en face,
  on attend le client sous les lampadaires.
- **Un boss qui se défend.** Il encaisse quatorze urakens, lance ses lames par
  gerbes de trois, enchaîne les coups deux fois plus vite que ses hommes, et
  surtout il **décroche sur le côté quand il voit l'uraken partir** : environ
  une esquive sur deux, signalée par une image rémanente.
- **Des ennemis qui tirent.** Les tox lancent des seringues, les chômeurs
  balancent leurs canettes de Carapils et de 8.6, les machettes lancent leur
  lame. Un bandeau turquoise annonce le tir : l'uraken dévie le projectile si
  le timing est bon.
- **Trois adversaires au sol.** Le tox, voûté et tremblant, frappe faible mais
  vient toujours. Le chômeur, jogging à bandes, claquettes-chaussettes et sac
  de canettes, reste à distance et arrose. La machette, en survêt rouge, est
  rapide et fait mal.
- **Pita-mitraillettes sauce andalouse**, coca sans sucre compris : deux par
  zone, posées au sol et rien d'autre — les ennemis n'en lâchent aucune. On les
  ramasse avec Espace pour 30 points de vie. À pleine santé, Espace frappe au
  lieu de ramasser. Six pitas pour toute la partie : il faut les mériter.
- **Pas de niveaux, pas d'expérience.** Johnny a 120 points de vie du début à
  la fin et son uraken frappe toujours à 25. Ce qui progresse, c'est le joueur.
- Tous les huit adversaires, un compliment de Madame la Juge ou du Procureur
  du Roi.
- **Score et classement.** La partie est chronométrée : le score récompense la
  vitesse, les adversaires mis au tapis et les dégâts évités. En fin de partie
  on entre son nom, et le classement du Pays Noir est conservé sur l'appareil.
- **Un classement commun, sans serveur.** Le jeu lit `scores.json`, servi à
  côté de lui : tout le monde voit le même tableau. Les scores encore locaux y
  apparaissent marqués « local » jusqu'à publication. Hors ligne, ou ouvert
  depuis un fichier, le jeu retombe sans bruit sur les scores de l'appareil.
- **Comparer sans passer par GitHub.** Chaque score produit aussi un code
  `JC1-…`. Collé chez un ami, il entre directement dans son classement.
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

## Le classement commun

`scores.json` est un simple fichier du dépôt, lu par le jeu. Trois façons de
l'alimenter, aucune n'expose de secret.

**Le joueur publie lui-même.** Le bouton « Publier au classement commun » ouvre
un ticket pré-rempli avec son code. Le robot `.github/workflows/scores.yml` le
valide, met `scores.json` à jour, répond le rang obtenu et referme le ticket.
Il faut un compte GitHub.

**Tu ajoutes un code reçu par message**, pour les amis sans compte GitHub :

```bash
./ajouter-score.sh JC1-eyJuIjoi…
```

**Vous échangez les codes entre vous**, sans rien publier : chacun colle les
codes des autres dans son propre classement.

### Pourquoi le jeu n'écrit pas directement

Écrire dans le dépôt depuis la page demanderait un jeton d'écriture dans du
JavaScript public : n'importe qui pourrait s'en servir pour modifier ou effacer
le dépôt. Le robot, lui, s'authentifie côté GitHub avec un jeton qui ne quitte
jamais le runner.

Le classement reste déclaratif : un code est fabricable à la main. Le script
refuse les scores dépassant le maximum atteignable et enregistre le compte
GitHub de l'auteur, ce qui suffit entre amis — pas contre un tricheur motivé.
