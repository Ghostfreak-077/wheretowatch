const streamingAvailability = require("streaming-availability");
const dotenv = require("dotenv");
const express = require("express");
const json_data = require('./data.json')

dotenv.configDotenv();
const app = express();

const RAPID_API_KEY = process.env.RAPID_API_KEY;

const search = async (title) => {
//   const client = new streamingAvailability.Client(
//     new streamingAvailability.Configuration({
//       apiKey: process.env.RAPID_API_KEY,
//     })
//   );
//   const data = await client.showsApi.searchShowsByTitle({
//     title: "Batman",
//     country: "in"
//   });
  console.log(title);

  return json_data;
// console.log(json_data);
};

app.get("/search", async (req, res) => {
    const title = req.query.title

    if (!title) return res.status(400).send("Title is required");
    
    const data = await search(title);
    res.send(data);
});

app.listen(process.env.PORT, () => {
  console.log(`Server is running on port http://localhost:${process.env.PORT}`);
});
