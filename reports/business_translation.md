# Business translation — from model score to bank action

## The problem in plain English
Santander has 76,000 customers.
About 3,000 of them are unhappy right now.
They will not tell the bank. They will just quietly close their account.
Our model gives each customer a score from 0 to 1.
0 means very likely satisfied. 1 means very likely dissatisfied.
The bank uses that score to decide what to do.

## What the score means and what the bank should do

| Score | What it means | What the bank should do |
|---|---|---|
| 0.7 or above | High risk of leaving | Call the customer within 24 hours. Assign a dedicated relationship manager. Offer a loyalty package or fee waiver. |
| 0.4 to 0.7 | Moderate risk | Send a personalised satisfaction survey. Offer a product upgrade. |
| 0.2 to 0.4 | Low risk | Include in next monthly customer outreach. Monitor for changes. |
| Below 0.2 | Satisfied | No action needed. |

## Business sub-questions this model answers

Q1: Which customers are at risk right now?
All customers with a score above 0.4 — roughly 3-5% of the base.

Q2: What are the earliest warning signs?
Zero cash balance (saldo_var30=0), zero average balance in last
3 months, low number of products, age above 80.
These signals appear 1-3 months before typical churn behaviour.

Q3: How early can we detect it?
The model uses data from the last 1 and 3 months.
Detection is possible roughly 1-3 months before the customer leaves.

Q4: Why not just use accuracy?
Because accuracy = 96% if we predict everyone is satisfied.
That is useless. AUC-ROC measures how well we separate the two groups.
Our target is AUC above 0.84.

Q5: What is the financial impact?
If the model catches 50% of at-risk customers:
3,000 unhappy customers × 50% caught = 1,500 interventions
If 40% of those interventions retain the customer = 600 saved
At $3,000 average customer lifetime value = $1.8M retained revenue
This is conservative and for one customer cohort only.

## For the presentation
Lead with the business problem and impact.
Show the score-to-action table as a visual.
Only introduce the technical details after the business case is clear.
The professor wants to see that you understand why this matters,
not just that you can run a model.
