# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The first time the hint banner and the attempts was responsive, though the hints were wrong
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The banner stating that I won and should start a new game never was updated after the first win
  The attempts variable never increased after the first game
  The hints were backwards

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 19 |    Go higher           Go lower          None
| 99 |    Go lower            Go higher         None
| New game |  Reset score+history   Score+history carried from previous game    None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude, specifically Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I didn't catch it, but apparently the first iteration of the game starts the user with 1 attempt
already completed. It suggested me to standardize this, and offered the solution of setting it to 0 here. I verified that the other games started at 0 and this made the most sense, because it also matched the attempts left logic.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Technically not incorrect, but the AI wanted to suggest adjustments to the logic of the game. It said fix the invalid input logic to make it not cost the user an attempt, but maybe this was the intended effect by the creator of the game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested its use case, and went through the tests file to also ensure that if that case was in that
file, it ran properly.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  After fixing the new game logic, I tried it out manually with base and edge cases, starting a new game before, during and after a game. It showed me that (fingers crossed) my code was fully functional throughout different user behaviors
- Did AI help you design or understand any tests? How?
It suggested some tests to make, citing different inputs or behaviors worth considering. Manually, I did use some of its tests, and validated some tests on my own

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns appears to execute the given script after every interaction. Session states are like values that are stored across reruns. I see them similarly to a recursive function and its parameters, stored across recalls.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Carefully reviewing the suggested fixes given to me by an AI tool. Sometimes I accept them blindly, assuming it knows better than me, which is not always the case.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Narrow context to reduce token usage and get more precise answers.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project began to change my relationship with AI dev tools, and it made me more confident I could drive a powerful engine like Claude Code or Github Copilot