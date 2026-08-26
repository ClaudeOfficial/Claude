# Chapter 4: XML tags for structure

When a prompt has multiple distinct pieces — instructions, reference
material, examples, formatting rules — wrapping each piece in a
descriptively-named XML tag makes the structure unambiguous, both to the
model and to anyone else reading the prompt later.

## Why it helps

Plain paragraphs blur boundaries. It's not always clear where "the
document to summarize" ends and "the instructions about how to summarize
it" begin. Tags remove that ambiguity:

```
<document>
{the full text to summarize}
</document>

<instructions>
Summarize the document above in 3 bullet points. Do not include any
information that isn't explicitly stated in the document.
</instructions>
```

## Nesting for multi-part inputs

```
<emails>
  <email id="1">{email text}</email>
  <email id="2">{email text}</email>
</emails>

<task>
For each email above, output its id and a one-word sentiment label
(positive, negative, or neutral).
</task>
```

## Tag naming conventions

There's no fixed tag vocabulary — pick names that describe the content:
`<context>`, `<question>`, `<examples>`, `<formatting_instructions>`. The
main rule is consistency: once you pick a tag name for a section, use the
same name every time you reference it later in the prompt.
