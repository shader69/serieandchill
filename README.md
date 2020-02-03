<h1>Projet : SerieAndChill</h1>
<p>
    Ceci est mon projet de site en Django.
    Voici les fonctionnalités disnonibles :
</p>

<h4>Fonctionnalités sans être connecté :</h4>
<ul>
    <li>Voir les séries proposées par les utilisateurs et leurs résumés</li>
    <li>Voir les commentaires postés sur les séries</li>
    <li>Filtrer les séries par nationalités, genre et en faisant une recherche</li>
    <li>Changer la langue du site (entre anglais et français)</li>
</ul>

<h4>Fonctionnalités en étant connecté :</h4>
<ul>
    <li>Poster une série en ligne (titre, résumé, photo, nombre de saison / épisodes...)</li>
    <li>Commenter une série / Supprimer un commentaire posté</li>
    <li>Modifier ses infos de compte (nom / prénom, email, mot de passe...)</li>
</ul>

<hr>

<h4>Explications sur certains choix :</h4>
<ul>
    <li>Concernant les formulaires utilisateurs (login, logout, passeword change etc..) j'ai choisi de 
    créer mes propres formulaires à partir des formulaires de Django pour pouvoir gérer les champs à 
    afficher lors des requêtes des formulaires</li>
    <li>Le bouton permettant de switcher entre les languages utilise l'URL 'set language' défini par
    Django qui sert à passer d'un language à l'autre</li>
    <li>Je n'ai volontairement pas crée de fonction de suppression de série car je ne voulais
    pas que les utilisateurs aient cette possibilté et cela devait être reservé à l'administrateur</li>
</ul>
