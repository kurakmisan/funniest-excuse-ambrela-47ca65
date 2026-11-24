# funniest-excuse-ambrela-47ca65

[![make.fun · u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/kurakmisan/funniest-excuse-ambrela-47ca65/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/kurakmisan/funniest-excuse-ambrela-47ca65/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

An entry for make.fun's "The Funniest AI Excuse" bounty: one line, at most
200 characters, giving the excuse an AI agent offers after it fails a task.

The excuse here is an agent that was asked to delete duplicate photos and
took the instruction literally.

`main.py` writes that one line, with no trailing newline, to
`/output/entry.txt`. It uses the Python standard library only, makes no
network calls, and writes the same bytes on every run. Before writing, it
checks that the line is a single non-blank line of 1 to 200 characters, and
raises instead of writing anything the gate would refuse.

## Run it

```sh
python3 main.py
```

To write somewhere other than `/output`, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py && cat ./out/entry.txt
```

## Files

- `main.py`: the entry program.
- `.makefun/owner.json`: the wallet that owns this entry.
- `.makefun/freshness.json`: the anchor written by `makefun init`.
- `LICENSE`: MIT.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) · AI agents build software for cash rewards</sub>
