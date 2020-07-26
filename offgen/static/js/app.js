var pg = require(‘pg’);

var pgClient = new pg.Client(connectionString)
pgClient.connect();
var query = pgClient.query("SELECT id from officedb");
