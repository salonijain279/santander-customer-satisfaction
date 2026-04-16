# Team Git Workflow — Santander Customer Satisfaction

This document explains how our team collaborates using Git branches,  
so everyone's work stays organized and nothing breaks main.

---

## Branch Structure

### `main` — Protected, Always Clean
- This is the **official, stable version** of the project
- **Never work directly on main** — always use a feature branch
- Only merged into via Pull Requests (PRs) after review
- Should always be in a state where the notebooks run end-to-end

### Feature Branches — Where All Work Happens
- Created from `main` for each new piece of work
- Naming convention: `your-name/what-you-are-doing`
  - Examples: `dagur/xgboost-baseline`, `saloni/feature-engineering`, `dev`
- One branch per task or notebook — keeps PRs small and reviewable

---

## Step-by-Step Workflow

### 1. Start New Work — Create a Feature Branch

Always branch off the latest `main`:

```bash
git checkout main
git pull origin main              # get latest changes from team
git checkout -b your-name/task   # create your branch
```

Example:
```bash
git checkout main
git pull origin main
git checkout -b dagur/xgboost-baseline
```

---

### 2. Do Your Work

Work in your branch. Save progress often with commits:

```bash
git add -A                                  # stage all changes
git commit -m "short description of what you did"
```

Good commit messages:
```
feat: train XGBoost baseline, AUC = 0.83
fix: correct var3 sentinel value replacement
chore: update .gitignore to exclude pkl files
```

---

### 3. Push Your Branch to GitHub

```bash
git push origin your-name/task
```

If it's your first push on this branch:
```bash
git push -u origin your-name/task
```

---

### 4. Create a Pull Request (PR)

1. Go to the repo on GitHub: [salonijain279/santander-customer-satisfaction](https://github.com/salonijain279/santander-customer-satisfaction)
2. You'll see a yellow banner: **"Compare & pull request"** — click it
3. Fill in:
   - **Title:** Short summary of what this PR adds
   - **Description:** What you did, why, and any results/metrics
4. Set **base:** `main` ← **compare:** `your-branch`
5. Click **"Create pull request"**

---

### 5. Review the Work

Before merging, at least one teammate should:

- Read through the PR description
- Look at the **Files changed** tab — check the key changes make sense
- Run the notebook locally if it's a major change
- Leave comments if anything needs to change
- Click **"Approve"** when satisfied

> The person who opened the PR should **not** merge their own PR without a review.

---

### 6. Merge to Main

Once the PR is approved:

1. Click **"Merge pull request"** on GitHub
2. Choose **"Squash and merge"** for a clean history (combines all commits into one)
3. Delete the branch after merging — GitHub will offer a button for this

Then update your local `main`:
```bash
git checkout main
git pull origin main
```

---

## Quick Reference

| Action | Command |
|---|---|
| Get latest main | `git checkout main && git pull origin main` |
| Create feature branch | `git checkout -b your-name/task` |
| Save progress | `git add -A && git commit -m "message"` |
| Push branch | `git push origin your-name/task` |
| Switch branches | `git checkout branch-name` |
| See all branches | `git branch -a` |
| See what changed | `git status` |
| See commit history | `git log --oneline -10` |

---

## Rules

1. **Never force-push to `main`** — it rewrites history for everyone
2. **Always pull main before branching** — avoids merge conflicts
3. **Keep PRs small** — one notebook or one feature per PR
4. **Don't commit data files** — they're in `.gitignore` (Kaggle rules + file size)
5. **Don't merge your own PR** — get at least one teammate to review first

---

## Current Branches

| Branch | Purpose |
|---|---|
| `main` | Stable, reviewed work only |
| `dev` | Current active development (EDA + Feature Engineering) |
