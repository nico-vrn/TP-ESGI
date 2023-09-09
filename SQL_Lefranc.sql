Travail Lefranc Nicolas 

CREATE TABLE "Client" (
    "id_cli" int   NOT NULL,
    "nom" int   NOT NULL,
    "ville" int   NOT NULL,
    "prenom" varchar(200)   NOT NULL,
    CONSTRAINT "pk_Client" PRIMARY KEY (
        "id_cli"
     )
);

CREATE TABLE "Product" (
    "ProductID" int   NOT NULL,
    "Name" varchar(200)   NOT NULL,
    "Price" money   NOT NULL,
    "stock" int   NOT NULL,
    "marque" varchar(200)   NOT NULL,
    CONSTRAINT "pk_Product" PRIMARY KEY (
        "ProductID"
     ),
    CONSTRAINT "uc_Product_Name" UNIQUE (
        "Name"
    )
);

CREATE TABLE "Vente" (
    "id_vente" int   NOT NULL,
    "id_cli" int   NOT NULL,
    "id_pro" int   NOT NULL,
    "date" date   NOT NULL,
    "quantite" int   NOT NULL,
    CONSTRAINT "pk_Vente" PRIMARY KEY (
        "id_vente"
     )
);

ALTER TABLE "Vente" ADD CONSTRAINT "fk_Vente_id_cli" FOREIGN KEY("id_cli")
REFERENCES "Client" ("id_cli");

ALTER TABLE "Vente" ADD CONSTRAINT "fk_Vente_id_pro" FOREIGN KEY("id_pro")
REFERENCES "Product" ("ProductID");

-- Partie 1 : 
-- Ajouter une colonne marque dans la table produit
ALTER TABLE "Product" ADD COLUMN "marque" varchar(200);

-- Ajouter une colonne prenom dans la table client
ALTER TABLE "Client" ADD COLUMN "prenom" varchar(200);

-- Diminuer le prix de 5% dans la table produit
UPDATE "Product" SET "Price" = "Price" * 0.95;

-- Lister les clients dont le nom comporte la lettre L en 3ième position
SELECT * FROM "Client" WHERE SUBSTRING("nom", 3, 1) = 'L';

-- Lister les produits dont le prix est compris entre 500€ et 1100€
SELECT * FROM "Product" WHERE "Price" BETWEEN 500 AND 1100;

-- Lister les produits de marque IBM, Apple ou Dec
SELECT * FROM "Product" WHERE "marque" IN ('IBM', 'Apple', 'Dec');

-- Lister les produits de marque IBM dont le prix est inférieur à 1000€
SELECT * FROM "Product" WHERE "marque" = 'IBM' AND "Price" < 1000;


-- Partie 2 : 

-- Donner les références et les noms des produits vendus
SELECT DISTINCT "ProductID", "Name" FROM "Product" INNER JOIN "Vente" ON "Product"."ProductID" = "Vente"."id_pro";

-- Donner les noms des clients qui ont acheté le produit ‘Auto'
SELECT DISTINCT "nom" FROM "Client" INNER JOIN "Vente" ON "Client"."id_cli" = "Vente"."id_cli" INNER JOIN "Product" ON "Vente"."id_pro" = "Product"."ProductID" WHERE "Product"."Name" = 'Auto';

-- Donner les noms des produits qui n'ont pas été acheté trier par le nom du produit
SELECT "Name" FROM "Product" WHERE "ProductID" NOT IN (SELECT "id_pro" FROM "Vente") ORDER BY "Name";

-- Donner le nombre total de clients ayant acheté des produits
SELECT COUNT(DISTINCT "id_cli") FROM "Vente";

-- Donner le nombre total de produit 'Auto' vendus
SELECT SUM("quantite") FROM "Vente" INNER JOIN "Product" ON "Vente"."id_pro" = "Product"."ProductID" WHERE "Product"."Name" = 'Auto';

-- Donner les noms des produits moins chers que la moyenne des prix de tous les produits
SELECT "Name" FROM "Product" WHERE "Price" < (SELECT AVG("Price") FROM "Product");

-- Donner pour chaque référence de produit la quantité totale vendue
SELECT "id_pro", SUM("quantite") FROM "Vente" GROUP BY "id_pro";

-- Donner les noms des marques dont le prix moyen des produits est < 5000€
SELECT "marque" FROM "Product" GROUP BY "marque" HAVING AVG("Price") < 5000;

-- Donner les noms des produits achetés en qte > 10 par plus de 50 clients
SELECT "Name" FROM "Product" WHERE "ProductID" IN (SELECT "id_pro" FROM "Vente" GROUP BY "id_pro" HAVING COUNT(DISTINCT "id_cli") > 50 AND SUM("quantite") > 10);

-- Augmenter de 30% les prix des produits achetés par des clients de Nice
UPDATE "Product" SET "Price" = "Price" * 1.3 WHERE "ProductID" IN (SELECT DISTINCT "id_pro" FROM "Vente" INNER JOIN "Client" ON "Vente"."id_cli" = "Client"."id_cli" WHERE "Client"."ville" = 'Nice');


