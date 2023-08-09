-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'mia_portfolio' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS mia_portfolio;
CREATE DATABASE mia_portfolio;
-- connect via psql
\c mia_portfolio

-- Primary Key Table
CREATE TABLE IF NOT EXISTS public.missing_person_info
(
    mia_id SERIAL PRIMARY KEY,
	name text COLLATE pg_catalog."default" NOT NULL,
    age integer NOT NULL,
    description character varying COLLATE pg_catalog."default" NOT NULL,
    alias character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    phone_number VARCHAR(20),
    last_sighting date
);

CREATE TABLE IF NOT EXISTS public.connections
(
    id integer NOT NULL,
    guardians text COLLATE pg_catalog."default",
    siblings text COLLATE pg_catalog."default",
    family text COLLATE pg_catalog."default",
    children text COLLATE pg_catalog."default",
    friends text COLLATE pg_catalog."default",
    spouse text COLLATE pg_catalog."default",
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.current_locations
(
    id integer NOT NULL,
    addresses character varying COLLATE pg_catalog."default",
    employers character varying COLLATE pg_catalog."default",
    hangouts character varying COLLATE pg_catalog."default",
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.social_media
(
    id integer NOT NULL,
    facebook text COLLATE pg_catalog."default",
    instagram text COLLATE pg_catalog."default",
    others character varying COLLATE pg_catalog."default",
    snapchat text COLLATE pg_catalog."default",
    PRIMARY KEY (id)
);

-- one to many table
CREATE TABLE IF NOT EXISTS public.missing_person_info_connections
(
    mia_id integer NOT NULL,
    connections_id integer NOT NULL,
    CONSTRAINT missing_person_info_connections_pkey PRIMARY KEY (mia_id, connections_id),
    CONSTRAINT fk_missing_person_info_connections_connections FOREIGN KEY (connections_id)
        REFERENCES public.connections (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

-- one to many table
CREATE TABLE IF NOT EXISTS public.missing_person_info_current_locations
(
    mia_id integer NOT NULL,
    current_locations_id integer NOT NULL,
    CONSTRAINT missing_person_info_current_locations_pkey PRIMARY KEY (mia_id, current_locations_id),
    CONSTRAINT fk_missing_person_info_current_locations_current_locations FOREIGN KEY (current_locations_id)
        REFERENCES public.current_locations (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

-- one to many table
CREATE TABLE IF NOT EXISTS public.missing_person_info_social_media
(
    mia_id integer NOT NULL,
    social_media_id integer NOT NULL,
    CONSTRAINT missing_person_info_social_media_pkey PRIMARY KEY (mia_id, social_media_id),
    CONSTRAINT fk_missing_person_info_social_media_social_media FOREIGN KEY (social_media_id)
        REFERENCES public.social_media (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
