# Design Tokens — Manual Web Output

## CSS Variables (Phase 5 default dark theme)

```css
:root {
  --bg:        #0d0f14;   /* page background */
  --surface:   #151820;   /* sidebar, card backgrounds */
  --surface2:  #1c2030;   /* hover states, table headers */
  --border:    #252a38;   /* all borders */
  --accent:    #e8a020;   /* primary highlight (amber-gold) */
  --accent2:   #3b82f6;   /* secondary highlight (blue) */
  --danger:    #ef4444;   /* danger callouts */
  --warning:   #f59e0b;   /* warning callouts */
  --caution:   #f97316;   /* caution callouts */
  --note:      #3b82f6;   /* note callouts */
  --success:   #22c55e;   /* checklist pass, wizard complete */
  --text:      #e8eaf0;   /* primary text */
  --text-dim:  #7a8099;   /* secondary text */
  --text-muted:#4a5068;   /* tertiary text, labels */
  --nav-w:     280px;     /* sidebar width */
  --radius:    10px;      /* border radius */
}
```

## Light Theme Override

To switch to a light theme, replace `:root` with:

```css
:root {
  --bg:        #f8f9fa;
  --surface:   #ffffff;
  --surface2:  #f1f3f5;
  --border:    #dee2e6;
  --accent:    #c47a00;
  --accent2:   #1d4ed8;
  --danger:    #dc2626;
  --warning:   #d97706;
  --caution:   #ea580c;
  --note:      #1d4ed8;
  --success:   #16a34a;
  --text:      #111827;
  --text-dim:  #4b5563;
  --text-muted:#9ca3af;
}
```

## Typography

```css
--font-head: 'Syne', sans-serif;        /* headings, nav labels */
--font-mono: 'JetBrains Mono', monospace; /* badges, labels, code */
--font-body: 'Inter', sans-serif;        /* body text */
```

Google Fonts CDN links (include in `<head>`):
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
```

## Component Colour Map

| Component | Key colour variable |
|---|---|
| `safety_banner` danger | `--danger` + rgba(--danger, .08) bg |
| `safety_banner` warning | `--warning` + rgba(--warning, .08) bg |
| `safety_banner` note | `--note` + rgba(--note, .08) bg |
| `procedure_wizard` progress | `--accent` |
| `interactive_checklist` progress | `--success` |
| `interactive_checklist` critical badge | `--danger` |
| `maintenance_schedule` priority high | `--danger` |
| `maintenance_schedule` priority medium | `--warning` |
| `maintenance_schedule` priority low | `--success` |
| `fault_finder` cause label | `--warning` |
| `fault_finder` fix label | `--success` |
| Nav active border | `--accent` |

## Sidebar Width

Default `--nav-w: 280px`. For dense manuals with long section titles, increase
to 320px. For mobile-first, collapse to 0 and use a hamburger toggle.

## Responsive Breakpoint

At `max-width: 768px`:
- Sidebar stacks above content (`flex-direction: column`)
- Chapter blocks reduce padding (`24px 20px` → `32px 20px`)
- Cover reduces padding (`48px 20px 40px`)
- Fault finder cause grid drops to single column
