# Baby web

## Sujet (100 points)

Baby Web
Chelinka

Our mole has risked infiltrating the Syndicate but has managed to inform us that they have hidden a project within a web platform. You need to connect to the instance and retrieve the secret project via the platform.
Notre agent double a risqué son infiltration au sein du Syndicat mais à réussi à nous informer que ces dernier ont caché un projet au sein d'une plateforme web. Vous devez donc vous connecter à l'instance et récupérez le projet secret au travers de la plateforme. Atteignez le projet secret. Get access to the secret project. http://challenges.hackday.fr:50399

## Solve

On arrive sur une page "vide": dans le HTML se trouve un indice qui nous emmène à la deuxième étape: ` There is nothing at /SuperSecretProject`.

Sur cette page, on nous dit "You are not the USER : DS Bandit". Il suffit alors de modifier les cookies pour en ajouter un clé:valeur / `USER : DS Bandit`.

Enfin, `You need to be connecting from the DS Mobile`. Il suffit de modifier le User-Agent pour qu'il soit "DS Mobile".

=> `<!--HACKDAY{WEB101}-->`
