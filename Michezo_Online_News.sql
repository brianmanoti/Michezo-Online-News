USE Michezo_Online_News ---select the database
--- create the first table(players)
CREATE TABLE players (
    jersey INT PRIMARY KEY,
    name VARCHAR(256),
    age INT
    nationality VARCAHR(256),
    team_id INT,
    strong_foot VARCHAR(256),
    FOREIGN KEY (team_id) REFERENCES Teams(id)
); 

--- create the second table(teams)
CREATE TABLE teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(256),
    team_nickname VARCHAR(256),
    stadium VARCHAR(256),
    city VARCHAR(256),
    coach VARCHAR(256),
    jersey INT, -- the jersey column to reference
    FOREIGN KEY (jersey) REFERENCES players(jersey)
);

--- create the users table

CREATE TABLE users (
	user_id INT,
	user_name VARCHAR(256),
	email VARCHAR(256),
	password VARCHAR(256)
);
