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
apparaissent **sous** le canvas : en portrait le jeu ne fait qu'environ 200 px
de haut, des commandes posées par-dessus le masqueraient.

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
- **Comparer avec ses amis sans serveur.** Chaque score enregistré produit un
  code `JC1-…` à envoyer. Collé chez un ami, il fait entrer le score dans son
  classement, marqué d'un point. Les codes s'échangent par message : rien ne
  transite par un serveur, le jeu reste une page statique.
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
