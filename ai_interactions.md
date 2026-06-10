# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude to generate comprehensive test cases for the various game inputs. I told it to include base and edge cases for each user interaction
I also asked it to generate a Guess History sidebar. I told it to make a visual for the user showing their game's guesses and what hint they recieved.

**What did the agent do?**

It ran a few complex bash commands, mostly to view and run the contents of the pytest, and then made multiple code suggestions, writing one each segment of test cases and a brief comment explaining what was being tested.
For the Guess History, it made some adjustments in the app.py code, reran the server and pytests to confirm that the made changes worked as expected.

**What did you have to verify or fix manually?**

I verified that each description matched the functionality of the test case generated, and also worked to minimize unnecessary tests
I also had to review changes to the core app logic to ensure the new code was functional and easy to follow. I also verified that existing features were not modified and test cases still passed.
---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
