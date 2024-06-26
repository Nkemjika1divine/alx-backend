import { createClient } from "redis";
import { promisify } from "util";
const redis = require("redis");

const client = createClient().on("error", (err) =>
  console.log("Redis client not connected to the server:", err.message)
);
console.log("Redis client connected to the server");

const HS = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (let key in HS) client.hmset("HolbertonSchools", key, HS[key], redis.print);

client.hgetall("HolbertonSchools", (err, res) => console.log(res));
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           