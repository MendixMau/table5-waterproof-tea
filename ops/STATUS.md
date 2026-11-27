# Agent status (the lead updates this)

| Agent | Pod | Plan | Output | Status |
|---|---|---|---|---|
| truth-customers | Truth | ops/agents/truth-customers.md | truth/customers-market.md | running |
| truth-history | Truth | ops/agents/truth-history.md | truth/history-cultures.md | running |
| business | Business | ops/agents/business.md | truth/business-case.md | running |
| business-validator | Business | ops/agents/business-validator.md | judge/business-validation.md | waits for business |
| strategist | Story | ops/agents/strategist.md | brand/strategy.md | ✅ done, 5 questions open |
| storyteller | Story | ops/agents/storyteller.md | deck/story.md | 🟡 draft 2 (420 words), waits for business + history |
| identity | Design | ops/agents/identity.md | brand/identity/ | running |
| product | Make | ops/agents/product.md | product/index.html | running |

**Restart any agent:** "Read ops/agents/_common.md and ops/agents/<name>.md, then do the task (resume from the output if it exists)."
