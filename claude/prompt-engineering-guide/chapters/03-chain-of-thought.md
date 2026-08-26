# Chapter 3: Chain of thought

For tasks that involve multiple steps of reasoning — math, multi-step
logic, weighing tradeoffs — asking the model to think step by step before
giving a final answer measurably improves accuracy, because it gives the
model room to work through intermediate steps instead of jumping straight
to a conclusion.

## The basic pattern

```
A store had 120 items. They sold 35% on Monday and 20 more on Tuesday.
How many items are left?

Think through this step by step before giving your final answer.
```

## Structuring the thinking explicitly

For tasks where you want to separate the reasoning from the final answer
(e.g., so you can show only the answer to an end user), ask for the
reasoning in a clearly delimited section:

```
First, work through your reasoning inside <reasoning> tags.
Then give your final answer inside <answer> tags, with no other text.
```

This makes it trivial to parse out just the `<answer>` block
programmatically while still getting the accuracy benefit of the model
reasoning first.

## When chain of thought doesn't help

For simple factual lookups or short creative tasks, forcing a reasoning
step mostly just adds latency and token cost without improving quality.
Reserve it for tasks where there's real intermediate work to do.
