-- This ists all cities contained in the database hbtn_0d_usa where each record should display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id;
