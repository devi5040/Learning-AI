import express from "express";
import rateLimit from "express-rate-limit";
import Openai from "openai";
import dotenv from "dotenv";
import fs from "fs";

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

// Analyze images and files
const response_image = await client.responses.create({
  model: "gpt-4",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "What is in this image?" },
        {
          type: "input_image",
          image_url:
            "https://openai-documentation.vercel.app/images/cat_and_otter.png",
          detail: "auto",
        },
      ],
    },
  ],
});

console.log(response_image.output_text);

// Uploading the file
const file = await client.files.create({
  file: fs.createReadStream("image.png"),
  purpose: "user_data",
});

const response_upload_file = await client.responses.create({
  model: "chatgpt-4o-latest",
  input: [
    {
      role: "user",
      content: [
        {
          type: "input_file",
          file_id: file.id,
        },
        {
          type: "input_text",
          text: "What is the first dragon in the book?",
        },
      ],
    },
  ],
});

console.log(response_upload_file.output_text);

app.listen(PORT, () => {
  console.log(`Server is running on port ${3000}`);
});
