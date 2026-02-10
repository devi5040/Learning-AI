# Prompt Engineering

- 2 types of LLM:

1. Base LLM - Predicts next word, based on text training data.
2. Instruction based LLM - Tries to follow instructions. Fine tune on instructions and good attempts at following those instructions.
   RLHF - Reinforcement learning with human feedback.

---

## Principles of writing the prompt

1. First principle is to write clear and specific instruction.
2. Second principle is give the model time to think.

### Write clear and specific instructions

1. Use delimeters to clearly indicate distinct parts of the input.
   - Eg: Triple quotes(''') Triple backticks(```) Triple dashes(---) Angle brackets(<>) XML tags(<tag></tag>)
   - It avoids prompt injection.
2. Ask for structured output
   - Eg: HTML, JSON
3. Check whether conditions are satisfied
   - Check assumptions required to do the task
   - Instruct the model how to handle the edge cases to avoid unnecessary error
4. Few-shot prompting
   - Give successful examples of completing the task
   - Then ask model to perform the task

### Give the model time to think

- If we do not give the model sufficient amount of time to think then it might rush into incorrect conclusions or it might not have time to think and make a guess.
  Tactics:

1. Specify the steps required to complete a task.
2. Instruct the model to work out it's own solution before rushing to a conclusion.

---

### Model limitations

1. Hallucination: Makes statements that sound plausible but are not true.
   It doesn't know the boundary of it's knowledge very well.
   Reducing hallucination: First find relevant information from the text, then answer the question based on that.

---

## Iterative Prompt development

Prompt guidelines

- Be clear and specific
- Analyze why result does not give desired output
- Refine the idea and the prompt
- Repeat

---

## Summarizing

- Generating a summary is a very common use case of prompt engineering.

---

## Inferring

Eg prompt:

```sh
"""
What is the sentiment of the following product review,
which is delimited with triple backticks?

Review text: '''{lamp_review}'''
"""
```

---

## Transforming

1. Translation

- ChatGPT is trained with sources in many languages. This gives the model the ability to do translation. Here are some examples of how to use this capability.

```sh
"""
Translate the following English text to Spanish: \
---Hi, I would like to order a blender---
"""
```

- To recognize the language

````sh
"""
Tell me which language this is:
```Combien coûte le lampadaire?```
"""
````

2. Tone transformation

- Writing can vary based on the intended audience. ChatGPT can produce different tones.

```sh
"""
Translate the following from slang to a business letter:
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
```

3. Format conversion

- ChatGPT can translate between formats. The prompt should describe the input and output formats.

```sh
"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
```

4. Spellcheck/Grammar check

```sh
"""Proofread and correct the following text and rewrite the corrected version. If you don't find and errors, just say "No errors found". Don't use any punctuation around the text:{text}"""
```

---

## Expanding

**_Customize the automated reply to a customer email_**

````sh
"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service.
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
````

---

## Temperature

- We will change temperature to change the response(randomness)
- For tasks that require reliability, predictability -> temperature 0
- For tasks that require creativity -> higher temperature
