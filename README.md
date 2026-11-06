# Python Readiness Test

This short test shows whether you are ready to start the Professional Certificate in
Applied Data Science. You write 4 small Python functions that use decisions, loops,
tuples, dictionaries, error handling and files, then save your work with Git.

**Allow 30 minutes:** about 5 to set up, 20 to code, 5 to save and send.

You need a free GitHub account. Sign up at [github.com](https://github.com) first if you
don't have one.

## 1. Make your own private copy (5 minutes)

Don't work in this repository: it is a template, and you can't save changes to it.

1. Click the green **Use this template** button at the top of this page, then
   **Create a new repository**. (Not the **Code** button, and don't fork.)
2. Set the owner to **your own account**, keep the name `python-readiness-test`, and
   select **Private** before you click **Create repository**.
3. In your new repository, go to **Settings → Collaborators → Add people**, and add
   **`blueconnectorbot`**. This is the grading bot: it reads your test results so your
   trainer can see them. It never changes your code.
4. Open a codespace on **your** repository (the name at the top shows your username):
   **Code → Codespaces → Create codespace on main**. The first start takes 1–2 minutes.

## 2. Complete the 4 tasks (20 minutes)

Open `readiness_test.py`. Each task says what the function must do and gives examples.
Replace `raise NotImplementedError` with your code.

Check your work in the terminal (**Terminal → New Terminal**):

```
pytest
```

Each check names its task (`task1_…` to `task4_…`), so you can see which tasks pass.
Run `pytest -k task3` to check one task.

## 3. Save and send (5 minutes)

Commit and push your work, even if not every task passes:

```
git add .
git commit -m "Readiness test"
git push
```

Each push runs the checks again on GitHub. You can see the result in your repository's
**Actions** tab.

Then reply to your invitation email with the link to your repository (for example
`https://github.com/your-username/python-readiness-test`).

## Rules

- Write the code yourself. You may use your notes and the Python documentation.
- Please **don't use AI tools** (ChatGPT, Copilot and similar). Copilot is switched off
  in the codespace for this reason. The point is to find out what you can do now, so the
  course can start at the right level for you.
- Don't edit the files in `tests/` or `.github/`.

Passing every check isn't required. Your trainer looks at which tasks pass and how you
wrote the code, and may ask you to talk through one task on a short call.
