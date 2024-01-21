# Baby stegano

## Sujet (500 points)

Hackemon
Yam

Un agent infiltré dans le syndicat nous a envoyé un message pour nous indiquer des informations sur le Syndicat. Il faut décrypter le message pour en récupérer les informations. L'agent infiltré a précisé dans son message qu'il voulait vous montrer le dernier pokemon qu'il avait capturé dans son jeu.
An agent who has infiltrated the syndicate has sent us a message giving us information about Syndicate. We need to decrypt the message to retrieve the information. The undercover agent said in his message that he wanted to show you the last pokemon he'd captured in his game. Connect to the instance using netcat to begin the challenge. **There is steganography in this challenge** Connectez-vous à l'instance pour commencer l'épreuve. **Il y a de la stéganographie dans cette épreuve** https://challenges.hackday.fr:50392

## Découverte

En se connectant en nc:

```
Hi friend as a pokemon lover I want to mail you
some of my favourites cards game, what do you think about it?
Email adress: mail@example.com
Email sent successfully.
Okay well
Now I have to confirm your pokemon skills
Can you please specify, in the order you receive them, the Japanese names
of each pokemon that I sent you?
Ex: rattata --> koratta
Pokemon 1:
```

On reçoit un email avec 5 pièces-jointes. Elles s'appellent toutes image.jpg mais seule la première d'entre elles est réellement un jpg. Les autres sont des PNG.

Les pokémons reçus sont:
1. Pidgey
2. Vulpix
3. Charmander
4. Bulbasaur
5. Squirtle

Leurs noms en japonais sont:
1. Poppo
2. Rokon
3. Hitokage
4. Fushigidane
5. Zenigame

## Solve

On reçoit finalement dans la console `nc` un lien vers instagram: https://www.instagram.com/pikhackchuoff/ avec une seule publication: https://www.instagram.com/p/C1WxPyWi3IV/ sous laquelle se trouve un lien: https://ibb.co/q0P0ThX.

On peut y télécharger une [image](final-card.jpg).

En utilisant [Stegseek](https://github.com/RickdeJager/stegseek), on trouve la clé "pikachu".

On extrait avec steghide: `steghide extract --stegofile final-card.jpg`, on obtient un [fichier étrange](./final-card.jpg.out) qui contient du [Pikalang](https://www.dcode.fr/pikalang-language) qu'il est possible de déchiffrer sur dcode :)

`The flag is HACKDAY{reverse_the_name_of_the_Pokemon_above}`

HACKDAY{uhcakip}
