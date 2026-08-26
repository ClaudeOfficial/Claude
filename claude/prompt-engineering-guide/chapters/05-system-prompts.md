# Chapter 5: System prompts and role assignment

A system prompt sets the persistent context for a whole conversation:
who the model should act as, what it knows about the situation, and what
constraints apply throughout — separate from any single turn's request.

## What belongs in a system prompt vs. a user message

**System prompt (stable, applies to every turn):**
- The model's role ("You are a technical support agent for a home
  networking company")
- Constraints that should never be violated ("Never recommend a
  competitor's product by name")
- Background the model needs but the end user shouldn't have to repeat
  ("Our current firmware version is 4.2.1")

**User message (specific to this turn):**
- The actual question or task at hand

## Example

```
System: You are a customer support agent for Meridian Cameras. You have
access to our product catalog and return policy (30 days, unopened box).
Keep responses under 100 words. If a question is outside camera support
(e.g. general photography advice unrelated to our products), politely
redirect the user to our community forum.

User: Can I return a camera I opened but didn't like?
```

## Common mistakes

- **Putting everything in the system prompt**, including things that
  change every turn — this bloats the prompt and can bury the actually
  important constraints
- **Vague roles** ("You are a helpful assistant") that don't actually
  constrain behavior in any useful way
- **Contradicting the role later in the conversation** without updating
  the system prompt, which leaves the model juggling two conflicting sets
  of instructions
