---
name: manual-to-web
description: >
  Converts user/service manual documents (PDF, DOCX, etc.) into fully interactive
  web-based HTML manuals with step wizards, tappable checklists, fault finders,
  maintenance schedules, and sidebar navigation. Use this skill whenever the user
  mentions converting a manual, document, or PDF into a web version, interactive
  HTML, or online documentation. Also trigger for phrases like "turn my manual into
  a website", "make my PDF interactive", "convert service doc to web", "document
  to HTML", "interactive manual", or any request to transform structured technical
  documents into browsable web experiences. The skill runs a 6-phase AI agent
  pipeline that is heavily token-optimised — most phases use zero tokens and AI
  is called only for content that genuinely benefits from enrichment.
---

# Manual → Interactive Web Conversion Pipeline

## Overview

Transforms a source document into a fully self-contained interactive HTML manual
through 6 sequential agent phases. Each phase produces a JSON/HTML artifact that
feeds the next.

```
PDF / DOCX
    ↓
Phase 1 → content_map.json      (parse, 0 tokens)
Phase 2 → content_tree.json     (structure, 0 tokens)
Phase 3 → enriched_tree.json    (AI enrichment, minimal tokens)
Phase 4 → component_map.json    (UI mapping, 0 tokens)
Phase 5 → manual.html           (web build, 0 tokens)
Phase 6 → qa_report.html        (QA + auto-fix, 0 tokens)
```

**Token strategy**: Phases 1, 2, 4, 5, 6 use zero AI tokens. Phase 3 uses AI
only on blocks flagged `ai_needed=True` (typically 30–40% of body text). All
results are cached — re-runs on unchanged sections cost 0 tokens.

---

## Quick Start

```python
# Run phases in order, passing each output as the next phase's input
python phase1_parser_agent.py       # PDF → content_map.json
python phase2_structure_agent.py    # → content_tree.json
python phase3_enrichment_agent.py   # → enriched_tree.json  (needs ANTHROPIC_API_KEY)
python phase4_interactivity_agent.py # → component_map.json
python phase5_web_builder.py        # → manual.html
python phase6_qa_agent.py           # → qa_report.html + auto-fix
```

Change `INPUT_PDF` / `INPUT_JSON` at the top of each script to point to your file.

---

## Phase 1 — Document Parser

**Script**: `scripts/phase1_parser_agent.py`  
**Input**: PDF file path  
**Output**: `content_map.json`  
**Tokens**: 0

Extracts all content using `pdfplumber`. Classifies every text block by type:

| Block type | Detection rule |
|---|---|
| `chapter_heading` | Starts with "Chapter N" or ALL CAPS ≤6 words |
| `section_heading` | Matches `N.N` pattern or title-case ≤10 words |
| `step` | Starts with "Step N" or `N. ` |
| `warning` / `danger` / `caution` / `note` | Leading keyword match |
| `body` | Everything else |

Also extracts tables (typed by headers) and builds a chapter/section hierarchy.

**Output structure**:
```json
{
  "metadata": { "title", "pages", "source_file" },
  "stats": { "total_blocks", "total_tables", "block_type_counts" },
  "pages": [{ "page_number", "blocks": [...], "tables": [...] }],
  "structure": { "chapters": [...], "all_blocks": [...] }
}
```

---

## Phase 2 — Structure Analyzer

**Script**: `scripts/phase2_structure_agent.py`  
**Input**: `content_map.json`  
**Output**: `content_tree.json`  
**Tokens**: 0

Builds a semantic content tree. Key jobs:

- Groups consecutive steps into `procedure` nodes
- Tags each block with `ai_needed: true/false`
- Classifies tables by semantic type: `spec_table`, `troubleshoot_table`,
  `checklist_table`, `maintenance_table`, `parts_table`, `generic_table`
- Classifies sections by type: `safety_section`, `spec_section`,
  `install_section`, `operation_section`, `maintenance_section`,
  `troubleshoot_section`
- Caches results by content hash — unchanged sections cost 0 on re-run

**`ai_needed` rules** (blocks skipping AI = 0 tokens):
- Steps, warnings, danger, caution, note → always `false`
- Body text < 8 words → `false`
- Figure captions, part numbers, "See also" references → `false`
- Substantive body text ≥ 8 words → `true`

---

## Phase 3 — Content Enrichment Agent

**Script**: `scripts/phase3_enrichment_agent.py`  
**Input**: `content_tree.json`  
**Output**: `enriched_tree.json`  
**Tokens**: minimal (only flagged blocks)

The only phase that calls the Claude API. Uses all 4 token strategies:

1. **Skip** — only processes `ai_needed=True` blocks
2. **Cache** — MD5 hash per block; cached results cost 0 tokens on re-run
3. **Batch** — all body blocks in a section sent in one API call
4. **Route** — cheap model for rewrites, powerful model for reasoning tasks

**Model routing**:
| Task | Model |
|---|---|
| Body text rewrite | `claude-haiku-4-5-20251001` |
| Spec table summary | `claude-haiku-4-5-20251001` |
| Maintenance row enrichment (priority, est_minutes) | `claude-haiku-4-5-20251001` |
| Checklist enrichment (critical flag) | `claude-haiku-4-5-20251001` |
| Troubleshoot → decision tree | `claude-sonnet-4-6` |

**Enrichment per table type**:
- `spec_table` → adds `summary_sentence`
- `troubleshoot_table` → adds `decision_tree: [{symptom, causes:[{cause, fix}]}]`
- `maintenance_table` → adds `priority` (high/medium/low) + `est_minutes` per row
- `checklist_table` → adds `critical: bool` per item

**Requires**: `ANTHROPIC_API_KEY` environment variable

---

## Phase 4 — Interactivity Builder

**Script**: `scripts/phase4_interactivity_agent.py`  
**Input**: `enriched_tree.json`  
**Output**: `component_map.json`  
**Tokens**: 0

Pure rule-based mapping — no AI. Assigns a UI component to every content node:

| Content node | → Component |
|---|---|
| Cover page | `cover_hero` |
| TOC | `toc_nav` (auto-generated) |
| warning / danger / caution / note | `safety_banner` |
| spec_table | `spec_table` |
| troubleshoot_table | `fault_finder` |
| checklist_table | `interactive_checklist` |
| maintenance_table | `maintenance_schedule` |
| procedure (≥3 steps) | `procedure_wizard` |
| body text | `body_section` |

Also builds the full sidebar navigation tree with chapter icons and ⚡ badges
on sections that contain interactive components.

---

## Phase 5 — Web Builder

**Script**: `scripts/phase5_web_builder.py`  
**Input**: `component_map.json`  
**Output**: `manual.html` (fully self-contained, no external dependencies)  
**Tokens**: 0

Generates a single-file HTML manual. All CSS and JS are inlined.

**Interactive components rendered**:
- `procedure_wizard` — Next/Back stepper, progress bar, step dots
- `interactive_checklist` — tap to check, CRITICAL badges, progress bar, reset
- `maintenance_schedule` — filter by interval, sortable by priority/time
- `fault_finder` — live search over symptoms, expandable cause→fix tree
- `safety_banner` — colour-coded (red=danger, amber=warning, blue=note)
- `spec_table` — responsive with plain-English summary header

**Design**:
- Dark-themed, professional industrial aesthetic
- Sticky sidebar navigation
- Fully responsive (mobile-friendly — manuals are often used in the field)
- No external fonts or scripts needed at runtime

For the reference design tokens and styling approach, see:
`references/design-tokens.md`

---

## Phase 6 — QA Validator

**Script**: `scripts/phase6_qa_agent.py`  
**Input**: all pipeline artifacts + `manual.html`  
**Output**: `qa_report.json` + `qa_report.html`  
**Tokens**: 0

Runs 6 check categories (43+ individual checks):

| Category | What it checks |
|---|---|
| Pipeline | All 5 artifact files exist and are valid JSON/HTML |
| Coverage | Every chapter, callout type, step, and table present in HTML |
| Links | Every `href="#anchor"` resolves to a real `id` in the DOM |
| Data | Every interactive component has its JS data payload |
| Accessibility | H1 count, alt text, lang attr, viewport meta, skip-nav, color usage |
| Structure | Source block counts vs output component counts |

**Auto-fix**: After identifying failures, the agent patches the HTML directly
(adds missing anchor `<div>` targets, renames mismatched ids, injects skip-nav)
and re-runs validation to confirm fixes.

**Overall status**: `PASS` (0 failures) or `NEEDS REVIEW` (≥1 failure).

---

## Token Budget Reference

For a 500-page industrial manual:

| Approach | Est. tokens | Est. cost (Sonnet) |
|---|---|---|
| Naive (send everything) | ~2,000,000 | ~$6.00 |
| Optimised (this pipeline) | ~150,000 | ~$0.45 |
| Cached re-run | ~10,000 | ~$0.03 |

---

## Dependencies

```bash
pip install pdfplumber reportlab pypdf --break-system-packages
```

For DOCX input: `pip install python-docx --break-system-packages`  
Python 3.8+ required. All scripts are single-file with no framework dependencies.

---

## Adapting to New Document Types

**DOCX**: Replace the `pdfplumber` extraction in Phase 1 with `python-docx`.
The output `content_map.json` schema is identical — downstream phases are
unchanged.

**Scanned PDFs**: Add a Tesseract OCR pre-pass before Phase 1. Output plain
text per page, then feed into the same block classifier.

**Multi-volume manuals**: Run Phase 1 per volume, merge `content_map.json`
files (append `pages` and `structure.all_blocks`), then continue from Phase 2.

For detailed guidance on each adaptation, see `references/adapting-inputs.md`.

---

## Output Customisation

To change the web output style, modify `phase5_web_builder.py`:

- **Light theme**: swap CSS variable values in `:root` (see `references/design-tokens.md`)
- **Different framework**: replace the inline HTML/JS generation with a
  Jinja2 template or a React/Next.js component generator — `component_map.json`
  is framework-agnostic
- **Add a chapter**: add a new `render_chN()` function and register it in the
  `secHtml` dispatch dict
- **Hosting**: the output `.html` is fully self-contained — deploy to S3,
  GitHub Pages, Vercel, or any static host as-is
