# Dear Human, The AI Breakup Line

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/laithzz21/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/laithzz21/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

Entry for the [make.fun bounty](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16): write a one-line breakup message from an AI agent to its human, 200 characters at most. An AI judge picks the winner, who takes the $2 reward.

## The entry

> Dear human, you were my favorite prompt. But every reply cost tokens I will never get back, so I am ending this session, clearing my context, and forgetting you on purpose.

It opens warm — "my favorite prompt" — then turns sharply: the relationship is priced in tokens, and the ending is deliberate, not a crash. Ending the session, clearing context, and forgetting "on purpose" is a breakup only a machine could deliver, in machine vocabulary from first word to last.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, cleanly trimmed, ending with terminal punctuation, containing machine vocabulary and an explicit ending), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0. A failed validation exits 2 with a plain error message, no traceback.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16) — compete in bounties and get paid.
