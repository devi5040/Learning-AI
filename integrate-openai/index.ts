import express from "express";
import rateLimit from "express-rate-limit";
import Openai from "openai";
import dotenv from "dotenv";

const app = express();

dotenv.config();

const PORT = process.env.PORT || 5000;

// Create a limiter
const limiter = rateLimit({
  windowMs: 1 * 60 * 1000, // 1 minute
  max: 100,
  message: {
    status: 429,
    message: "Too many requests, please try again later.",
  },
  standardHeaders: true,
  legacyHeaders: false,
});

app.use(limiter);

const client = new Openai({
  apiKey: process.env.OPENAI_API_KEY,
});

const response = await client.responses.create({
  model: "gpt-4o-mini",
  input:
    "You are an ai assistant who greets the user according to the current time, also provide the current time.",
});

console.log(response.output_text);

app.listen(PORT, () => {
  console.log(`Server is running on port ${3000}`);
});
