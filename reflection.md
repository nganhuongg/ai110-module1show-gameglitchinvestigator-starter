# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? The attempts did not decrease for the first time. It remained 8.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The hints were wrong because even when I entered 1, it kept said "GO LOWER"

  - When I ran out of attempts, I could not restart the game

  - When the secret number is revealed as 2, I was choosing 14, but the hint said "GO HIGHER"

  - The difficulty level was not applied. Even if the mode is Easy, secret number can be outside the range

  - When changing the difficulty level, the game was not reset

  - When I restart the game, the attempt is not recovered


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Codex
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  It said when I submitted in even attempt, `secret` is changed into `str`, so the comparison is wrong (like "9" > "10" is True), which lead to misleading hint
  I verified it by reading the code line it refered to in the *app.py* and understood the code logic
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  AI can not read icon, so when I ask it to fix my error about string type, it changed all icons into a wrong format, making the website look strange


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I tried to run Streamlit and tested the bug
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I try to change mode in the dashboard and the range is updated to adapt to the chosen difficulty, which means my code successfully fix the mismatch between difficulty and range on dashboard


  When I restart the game, the game is truly restarted
- Did AI help you design or understand any tests? How?
  No

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    The secret number kept changing because for each time of submitting the guess, the code randomized the secret number again
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Streamlit reruns your whole script whenever the user interacts with the app, like clicking a button or typing input. session_state is how the app remembers values between those reruns, so things like scores, attempts, or a secret number do not reset each time.

- What change did you make that finally gave the game a stable secret number?
    I made the secret number live in st.session_state instead of generating it again every time Streamlit reran the script. Specifically, I only create st.session_state.secret if it does not already exist, so clicking Submit no longer changes the number behind the scenes. After that, the secret only changes when I intentionally start a new game, which made the gameplay stable and predictable.



---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    One habit I want to reuse is testing each fix right after I make it instead of changing many things at once. In this project, running the app again after each small change made it easier to tell which fix actually worked. I also want to keep asking AI more specific questions, like pointing to one bug at a time instead of asking it to fix everything at once. That made the answers more useful and easier to verify.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
    Next time, I would double-check the AI suggestions earlier by comparing them with my actual code and testing them right away. In this project, some AI advice was helpful, but some of it also changed things that were not really the problem. I learned that if I trust every suggestion too quickly, I can create new issues. I would use AI more like a helper for ideas, not as something that is always correct.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    This project showed me that AI-generated code can be useful for finding bugs and giving ideas, but it still needs careful checking by the programmer. I now think of AI as a teammate that can help me work faster, but not as something I should trust without testing.
