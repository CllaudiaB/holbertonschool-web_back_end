const redis = require('redis');
const client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(err){ 
    console.log(`Redis client not connected to the server: ${err}`); 
});

client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe();
      client.quit();
    }
  });
