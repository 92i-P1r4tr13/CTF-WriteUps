# Baby stegano

## Sujet (100 points)

Baby Steganography
Chelinka

Syndicat agents did not protect their exchanges between them about a future attack and we were able to recover in their messages an image. It’s up to you to know what was targeted by the future attack and retrieve the information hidden in this image.
Des agents du syndicat n'ont pas protégé leurs échanges entre eux à propos d'une future attaque et nous avons pu récupérer dans leurs messages une image. A vous de savoir ce qui était ciblé par la future attaque et récupérez les informations dissimulées dans cette image. Récupérez l'image et trouver l'information ! Download the picture and uncover the information inside ! 

[Voir l'image](./zebra.jpg)

## Solve

Les barres obliques sont organisées: tout à gauche, toutes dans le même sens. Sur chaque ligne, il y a 8 barres, comme le nombre de bits dans un octet.

Connaissant la table ASCII, on sait que tous les caractères de celle-ci ont 0 pour bit de poids fort.

On en déduit que les \ sont des 0 et les / sont des 1.

Retranscription:

```
01000001
01000011
01001011
01000100
01000001
01011001
01111011
01110100
00110000
01110101
01110010
01011111
01100100
01100101
01011111
01100011
01101000
01100001
01110101
01100110
01100110
01100101
01111101
```

Soit HACKDAY{t0ur_de_chauffe}
