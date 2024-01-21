# Sound zero

## Sujet (162 points)

Sound Zero
162
Didouad

Nous venons de recevoir un rapport surprenant de nos équipes de terrains. En fouillant un criminel qu’elles venaient d’appréhender, ils ont trouvé un disque dur sur le coup jugé intéressant. Cependant, après un interrogatoire ce criminel a révélé qu’il faisait partie d’une organisation qui pourrait bien être le SYNDICAT ! À en juger par le contenu du disque dur pour le moins singulier, il contient certainement un message caché. Et vous l’avez compris, votre job va être de le découvrir !
We have just received a surprising report from our field teams. While searching for a recently apprehended criminal, they found an interesting hard drive on the scene. However, after interrogation, this criminal revealed that he is part of an organization that could very well be SYNDICAT! Judging by the rather peculiar content on the hard drive, it certainly contains a hidden message. And, as you have guessed, your job is to uncover it! Téléchargez le fichier sonore, et récupérez le drapeau caché dedans ! Download the music, and recover the flag hidden inside ! 

## Solve

En observant le fichier, on remarque une grande quantité de bytes de valeur zéro au début du fichier (`xxd -p challenge.wav| tr -d '\n' | tail -c +88 > out.txt && python parse.py > parsed.txt`, [challenge.wav](challenge.wav), [out.txt](out.txt)).

`01001000010000010100001101001011010001000100000101011001011110110101001100110000011101010110111001100100010111110110110000110001011010110011001101011111011000010101111101100111001100000100111101100100010111110111000001101100001101000110111001111101`

HACKDAY{S0und_l1k3_a_g0Od_pl4n}
