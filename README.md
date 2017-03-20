# PISTE: Referentiels exogènes

## Objectifs
 1. Mise à jour et gestion des versions de l'ensemble des référentiels externes
 2. Report de forme automatique pour l'ensemble des valeurs définies par les réferentiels exogènes pour une notice

## Datasets

Nous disposons de plusieurs datasets:
* Un document **master** qui liste l'ensemble des référentiels externes pour chaque zone, sous zone position et type de notice concernée ainsi que la date de dernière modification
* Un ensemble de document **spécifiques pour chaque référentiels**. Ils listent
le code attribué et la valeur correspondante. Selon le référentiel, on peut trouver en sus:
  * le détail de la  modification d'une valeur (date, remplacement)
  * la norme sur laquelle repose le référentiel
  * les valeurs locales (spécifique à la BNF) qui remplacent les valeurs globales

    ` A noter: les normes ISO sont disponibles en ligne et pourraient etre mise à jour automatiquement
    en respectant la priorité des données locales (soit les valeurs spécifiques figées par la BNF)
    `
* L'**ensemble des notices concernées** par ses référentiels exogènes: l'information est qualifiée par chaque zone,sous-zone, position et "type"  de notice et la valeur  peut être présente à plusieurs endroits

## BackLog

* Création d'une base de connaissance qui croise chaque référentiel externe avec le document master:
`tag:master_ref`
* Création d'une API de requetage de ces données pour chaque valeur controlée `tag:requete`
* API de requetage des référentiels exogènes `tag:exo_api`
* Gestion des versions/modifications: stockage dans une BDD `tag:versionning`
