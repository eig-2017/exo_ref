# PISTE: Referentiels exogènes

## Objectifs
 1. Mise à jour de l'ensemble des référentiels externes
 2. En figeant les valeurs spécifiques liés au catalogage interne
 3. En proposant une interface pour gérer les conflits de merge
 4. En mettant à jour les notices BIB et AUT concernées


## Datasets

Nous disposons de plusieurs datasets:
* Un document **master** qui liste l'ensemble des référentiels externes pour chaque format(type de notice), zone, sous zone position et type de notice concernée ainsi que la date de dernière modification
* Un ensemble de document **spécifiques pour chaque référentiels**. Ils listent
le code attribué et la valeur correspondante. Selon le référentiel, on peut trouver des informations complémentaires telles que:
  * le détail de la  modification d'une valeur (date, remplacement)
  * la norme sur laquelle repose le référentiel
  * les valeurs locales (spécifique à la BNF) qui remplacent les valeurs globales

    ` A noter: les normes ISO sont disponibles en ligne et pourraient etre mise à jour automatiquement
    en respectant la priorité des données locales (soit les valeurs spécifiques figées par la BNF)
    `
* L'**ensemble des notices concernées** par ses référentiels exogènes: l'information est qualifiée par chaque zone,sous-zone, position et "type"  de notice et la valeur  peut être présente à plusieurs endroits.

## BackLog

* Création d'une base de connaissance qui croise chaque référentiel externe avec les valeurs du document master (format, zone, sous-zone, position)
`tag:master_ref`
* Création d'une API de requetage de ces données pour chaque valeur controlée `tag:requete`
* API de requetage des référentiels exogènes `tag:exo_api`
* Gestion des versions/modifications: stockage dans une BDD `tag:versionning`
