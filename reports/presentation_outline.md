# Presentation outline

## Format
Confirm slide count with professor.
Suggested: 8-10 slides.
Rule: business perspective first, technical second.
Rule: max 3 bullet points per slide.
Rule: every slide answers one question the professor would ask.

## Slide by slide

Slide 1 — Title
Content: Project name, team names and roles, date.

Slide 2 — The business problem
One sentence: "3,000 of Santander's 76,000 customers are quietly
unhappy and will leave without warning."
Visual: pie chart showing 96% vs 4% split.
Key message: silence does not mean satisfaction.

Slide 3 — Our pipeline
Visual: simple flow diagram
Raw data → EDA → Clean → Engineer features → 5 Models → Ensemble → Score
One sentence per phase. No code on this slide.

Slide 4 — What the data told us (EDA insights)
Three visuals:
- var15 histogram split by TARGET (age under 23 = always satisfied)
- saldo_var30 distribution (zero = dissatisfaction cluster)
- Feature importance bar chart (top 5 features)
Key message: the data itself showed us where to look.

Slide 5 — Features we engineered
Use Table 2 from the write-up.
Columns: Feature | What it captures | AUC impact
Show that EDA findings directly drove feature decisions.

Slide 6 — Five models we tried
Use Table 1 from the write-up.
Columns: Model | Category | CV AUC
Bar chart of CV AUC scores side by side.
Key message: we tried 5 different categories (not just one approach).

Slide 7 — Best model performance
ROC curve of best model.
Confusion matrix at chosen threshold.
Key message: AUC of X means we correctly rank unhappy customers
above happy ones X% of the time.

Slide 8 — Ensemble result
Simple diagram: 5 models → blend → post-processing → final score.
Final AUC vs best single model AUC.
What the ensemble added.

Slide 9 — Business recommendations
Use the score-to-action table from business_translation.md.
Show estimated financial impact.
Key message: this model has real, quantifiable value.

Slide 10 — What we would do next
What additional data would help.
How to deploy this in a real bank system.
One limitation of the current model.

## Design rules
- Business language on slides 1-4 and 9-10
- ML terms only on slides 5-8
- Every number on a slide should answer "so what?"
- Tables over bullet points wherever possible
