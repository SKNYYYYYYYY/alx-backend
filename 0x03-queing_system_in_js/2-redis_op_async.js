import { createClient } from "redis";

const client = await createClient()
  .on('error', (error) => console.log(`Redis client not coonnected to the server: ${error}`))
  .connect();
console.log('Redis client connected to the server')
async function setNewSchool(schoolName, Name) {
  await client.set(schoolName, Name);
  console.log('Reply: OK')
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value)
}

displaySchoolValue('ALX')
setNewSchool('ALXSan', '100')
displaySchoolValue('ALXSan')