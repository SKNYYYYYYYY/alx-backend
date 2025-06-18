import { createClient } from "redis";

const client = await createClient()
  .on('error', (error) => console.log(`Redis client not coonnected to the server: ${error}`))
  .connect()
console.log('Redis client connected to the server')
