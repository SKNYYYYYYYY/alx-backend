const redis = require('redis');

const client = redis.createClient()

client.on('connect', () => { console.log('Redis client connected to the server'); });
client.on("error", (error) => console.log(`Redis client not coonnected to the server: ${error}`))


const subscriber = client.duplicate()

subscriber.subscribe('ALX channel'), 
subscriber.on('message', (channel, message) => {
    console.log(message)
    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe();
      subscriber.quit();
      client.quit()
    }
})
