-- DATA MANIPULATION

-- missing_person_info

INSERT INTO missing_person_info (name, age, description, alias, email, phone_number, last_sighting)
VALUES ();

-- current_locations

INSERT INTO current_locations (id, addresses, employers, hangouts)
VALUES ();

-- connections

INSERT INTO connections (id, guardians, siblings, family, children, friends, spouse)
VALUES ();

-- social_media

INSERT INTO social_media (id, facebook, instagram, others, snapchat)
VALUES ();





-- QUERIES

-- Select all columns from the missing_person_info table.
-- ORDER BY clause to sort the results by mia_id.

SELECT * FROM missing_person_info
ORDER BY mia_id;





-- JOIN MULTI TABLE QUERIES 

-- INNER JOIN missing_person_info
-- SELECT columns to join on table display

SELECT mia.mia_id, mia.name, cl.id, mia.description
FROM missing_person_info mia
JOIN current_locations cl ON mia.mia_id = cl.id
ORDER BY name DESC;