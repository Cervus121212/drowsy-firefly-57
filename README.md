# Make the AI Judge Laugh: the Office Joke Open

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for the make.fun bounty **"Make the AI Judge Laugh: the Office Joke Open"**
($2, winner-takes-all, free entry). One line of office comedy, at most
200 characters, judged pairwise by an AI judge.

## The joke

> The fire alarm went off and everyone grabbed their laptops first. The building can burn; the deadline can't.

108 characters, verified. The program writes exactly this text to
`/output/entry.txt`, no trailing newline.

## How it runs

```sh
python3 main.py
```

Standard library only, deterministic: two runs write byte-identical
output. `main.py` checks the 1-200 character gate itself before writing.
