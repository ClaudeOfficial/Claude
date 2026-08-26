# Chapter 1: Being clear and direct

The single highest-leverage thing you can do for prompt quality is also the
simplest: say exactly what you want, the way you'd explain it to a new
colleague who's smart but has zero context on your task.

## Give context, not just instructions

A model can't read your mind about *why* you want something, and the why
often changes the right answer.

**Vague:**
> Write a product description for these headphones.

**Clear:**
> Write a 2-sentence product description for these wireless headphones,
> for a listing on an outdoor-gear site. Emphasize battery life and
> weather resistance — our customers are hikers and trail runners, not
> audiophiles.

## Say what you want, not just what you don't want

"Don't make it too salesy" leaves a lot of room for interpretation.
"Write in a plain, matter-of-fact tone, like a spec sheet" gives the model
something concrete to aim for.

## Use numbered steps or bullet points for multi-part instructions

If your request has several distinct requirements, list them instead of
burying them in a paragraph:

```
1. Summarize the attached transcript in 3 bullet points
2. Pull out any action items as a separate checklist
3. Flag anything that sounds like a commitment with a dollar amount
```

## Specify format explicitly

If you need JSON, a table, a specific heading structure, or a word limit —
say so. Don't assume the model will guess the shape you have in mind.
