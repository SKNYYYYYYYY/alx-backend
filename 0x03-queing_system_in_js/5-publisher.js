const redis = require('redis');

const client = redis.createClient()

client.on('connect', () => { console.log('Redis client connected to the server'); });
client.on("error", (error) => console.log(`Redis client not coonnected to the server: ${error}`))

function publishMessage(message, time) {
  setTimeout(async () => {
    console.log(`About to send ${message}`);
    await client.publish('ALX channel', message)
  }, time)
}

publishMessage("ALX Student #1 starts course", 100)
publishMessage("ALX Student #2 starts course", 200)
publishMessage("KILL_SERVER", 300)
publishMessage("ALX Student #3 starts course", 400)
