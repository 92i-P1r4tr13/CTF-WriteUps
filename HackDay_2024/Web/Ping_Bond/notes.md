# Baby web

## Sujet (100 points)

Ping Bond
100
Lancelot

L'agence a trouvé le service mis en place par un sbire du Syndicat pour récupérer son jeton d'authentification. Votre but, cher agent, est de détourner ce site afin de récupérer les informations envoyées à ces serveurs.
The agency has found the service set up by a Syndicate henchman to recover his authentication token. Your aim, dear agent, is to hijack this site in order to retrieve the information sent to these servers. Connectez-vous à la plateforme web et récupérez le jeton d'authentification. Connect to the web platform and retrieve the authentication token. http://challenges.hackday.fr:50394

## Solve

On a accès au [code source](./app.py) du serveur web.

On arrive sur une page qui nous demande une URL. En lisant le code du serveur web, on remarque que celui-ci "signe" les URLs vers lesquelles il envoie le flag. La processus de signature associe une valeur (en l'occurence 30 et 27) aux URLs. Il suffit alors de créer une URL qui passe le processus de signature. En quelques essais, cette URL fonctionne: https://ens1fg6qhdx0r.x.pipedream.net/aaaaaaaaaaaaaaa

Il suffit de modifier l'URL envoyée depuis la page front, et on récupère sur notre endpoint: 

HACKDAY{Pr3ttY_34Sy_r1Ght?}
