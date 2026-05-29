# Python OOP Exam Prep (Senior SDET)

Self-contained study package for **Python OOP** interviews and trace-the-output exams at senior SDET level (8+ years).

## Prerequisites

- Python 3.10+
- No Selenium required for core modules

## Quick start

```bash
cd Python_OOPS

# Run any concept demo
python concepts/01_classes_and_objects/demo.py

# Practice predict-the-output (predict first, then run)
python exercises/predict_output/easy/q01_instance_vs_class_attr.py
```

## Study path

1. Read [docs/STUDY_GUIDE.md](docs/STUDY_GUIDE.md) — pillars, cram sheet, checklist.
2. Work through `concepts/01_*` … `concepts/10_*` (README → `demo.py`).
3. Map ideas to your Selenium lab: [docs/SDET_MAPPINGS.md](docs/SDET_MAPPINGS.md).
4. Do `exercises/predict_output/` **without running** first; verify; read commented answers at file bottom.
5. Mock interview: [docs/INTERVIEW_QA.md](docs/INTERVIEW_QA.md) — start with **HIGH_LIKELIHOOD** tags.
6. Review [patterns_for_sdet/](patterns_for_sdet/) then re-read `learning_project/pages/` and `core/base_page.py`.

## Layout

| Path | Purpose |
|------|---------|
| `docs/` | Study guide, SDET mappings, 55+ interview Q&A |
| `concepts/` | One folder per OOP topic (theory + runnable demo) |
| `exercises/predict_output/` | easy / medium / hard trace questions |
| `patterns_for_sdet/` | Factory, strategy, page object sketch |

## Related project

Your [learning_project](../learning_project/) already uses inheritance (`LoginPage(BasePage)`), encapsulation (locators), and a driver factory — use it as the live example after this module.
