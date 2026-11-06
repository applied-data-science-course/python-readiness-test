# Python Readiness Test

This test shows whether you are ready to start the Professional Certificate in Applied
Data Science. It checks the Python basics the course builds on: decisions, loops,
functions, lists, tuples, sets, dictionaries, handling errors, reading and writing files,
and using Git.

Allow about **2 hours**. You can stop and come back: your work is saved in your repository.

## What to do

You need a free GitHub account. Sign up at [github.com](https://github.com) if you don't
have one.

1. **Make your own copy of this test.** Don't work in this repository directly: you can't
   save changes to it.
   - **If you received a GitHub Classroom invitation link**, open it and click **Accept
     this assignment**. GitHub creates your private copy and shows you its link. Go to
     step 2.
   - **Otherwise**, click the green **Use this template** button at the top of this page,
     then **Create a new repository**. Set the owner to your own account, keep the name
     `python-readiness-test`, choose **Private**, and click **Create repository**. Then,
     in your new repository, go to **Settings → Collaborators → Add people** and add
     your trainer's GitHub username (it is in your invitation email). Without this step,
     your trainer can't see your work.
2. **Open your copy in Codespaces.** Make sure you are on *your* repository's page (the
   name at the top shows your username, not `applied-data-science-course`). Click
   **Code → Codespaces → Create codespace on main**. It takes a minute or two to start.
   Everything you need is already installed.
   *Working on your own computer instead?* Clone your repository, then run
   `pip install -r requirements.txt`.
3. **Complete the 8 tasks** in `readiness_test.py`. Each task says what the function must do
   and gives examples. Replace `raise NotImplementedError` with your code.
4. **Check your work** in the terminal:
   ```
   pytest
   ```
   Each task has its own checks, so you can see which tasks pass. Run `pytest -k task3`
   to check a single task.
5. **Answer the two short questions** in `ANSWERS.md`, in your own words.
6. **Commit and push** at least twice while you work (for example, after Task 4 and at the
   end), with a message that says what you did:
   ```
   git add .
   git commit -m "Complete tasks 1 to 4"
   git push
   ```
   This saves your work to your own repository. Your trainer only sees what you push.

## Rules

- Write the code yourself. You may use your notes, the Python documentation and the
  courses in the Preparation Guide.
- Please **do not use AI tools** (ChatGPT, Copilot and similar). Codespaces has Copilot
  switched off for this reason. The point is to find out what you can do now, so the
  course can start at the right level for you.
- Do not edit the files in `tests/`.

## How it is reviewed

Your trainer looks at three things: which checks pass, whether your code is readable
(clear names, simple logic), and your commit history. You may be asked to walk through
your code on a short call. Passing every check is not required; showing that you can
reason through the tasks is.
