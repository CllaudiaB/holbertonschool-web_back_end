const redis = require('redis');
const client = redis.createClient();

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
    client.get(schoolName, redis.print)
};

client.on('connect', function() {
    console.log('Redis client connected to the server');
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
});

client.on("error", function(err){ 
    console.log(`Redis client not connected to the server: ${err}`);
});
