import { createClient } from "redis";

const client = await createClient()
  .on('error', (error) => console.log(`Redis client not coonnected to the server: ${error}`))
  .connect();
console.log('Redis client connected to the server')
function setNewSchool(schoolName, Name) {
  client.set(schoolName, Name);
  console.log('Reply: OK')
}

function displaySchoolValue(schoolName) {
  client.get(schoolName).then((value) => {
  console.log(value)
  });
}

displaySchoolValue('ALX')
setNewSchool('ALXSan', '100')
displaySchoolValue('ALXSan')