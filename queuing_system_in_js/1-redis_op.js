const redis = require('redis');
const client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on("error", function(err){ 
    console.log(`Redis client not connected to the server: ${err}`); 
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
    client.get(schoolName, redis.print)
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
