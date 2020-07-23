var pg = require(‘pg’);
var connectionString = "postgres://nikclarks:kevinsayslittleword@sPostgresql/ip:5432/officedb";
var pgClient = new pg.Client(connectionString)
pgClient.connect();
var query = pgClient.query("SELECT id from officedb");
