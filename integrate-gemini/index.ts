import express from "express";
import dotenv from "dotenv";
import rateLimit from "express-rate-limit";
import { GoogleGenAI } from "@google/genai";

dotenv.config();

const app = express();

const PORT = process.env.PORT || 5050;

const limiter = rateLimit({
  windowMs: 1 * 60 * 1000,
  max: 10,
  message: {
    status: 429,
    message: "Too many requests. Please try again later.",
  },
  standardHeaders: true,
  legacyHeaders: false,
});

app.use(limiter);

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY! });

const currentTime = new Date();

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash-lite",
  contents: `You are an ai assistant who greets the user according to the current time. The current time is ${currentTime}`,
});

if (response.candidates && response.candidates[0]?.content?.parts) {
  console.log(response.candidates[0]?.content?.parts[0]?.text);
} else {
  console.log("No response");
}

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
