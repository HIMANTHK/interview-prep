#!/usr/bin/env python3
"""
generate_html.py
================
Run this whenever you update Interview_Prep_200_QA.md to rebuild the viewer:

    python generate_html.py

Output: Interview_Prep_200_QA.html — open in any browser.
Features: sidebar nav, expand/collapse Q&A, search, progress tracking (saved
in browser localStorage), print-to-PDF friendly.
"""
import re
import html as _html
from pathlib import Path

SRC = Path(__file__).with_name("Interview_Prep_200_QA.md")
OUT = Path(__file__).with_name("Interview_Prep_200_QA.html")


# ─── Markdown → HTML helpers ────────────────────────────────────────────────

def esc(t: str) -> str:
    return _html.escape(str(t))

def inline_md(t: str) -> str:
    """Convert inline markdown (bold, code) to HTML."""
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t

def block_md(text: str) -> str:
    """Convert a markdown block to HTML paragraphs / lists / blockquotes."""
    lines = text.split('\n')
    out = []
    in_ul = False
    para: list[str] = []

    def flush():
        nonlocal in_ul
        if para:
            out.append('<p>' + ' '.join(para) + '</p>')
            para.clear()
        if in_ul:
            out.append('</ul>')
            in_ul = False

    for line in lines:
        s = line.strip()
        if not s:
            flush()
        elif s.startswith('> '):
            flush()
            out.append(f'<blockquote>{inline_md(s[2:])}</blockquote>')
        elif re.match(r'^- ', s):
            if para:
                out.append('<p>' + ' '.join(para) + '</p>')
                para.clear()
            if not in_ul:
                out.append('<ul>')
                in_ul = True
            out.append('<li>' + inline_md(s[2:]) + '</li>')
        else:
            if in_ul:
                out.append('</ul>')
                in_ul = False
            para.append(inline_md(s))

    flush()
    return '\n'.join(out)


# ─── Parse markdown ─────────────────────────────────────────────────────────

def parse(content: str):
    lines = content.split('\n')

    # Strip YAML frontmatter (--- ... ---)
    if lines and lines[0].strip() == '---':
        try:
            end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == '---')
            lines = lines[end + 1:]
        except StopIteration:
            pass

    intro: list[str] = []
    sections: list[dict] = []
    cur_sec: dict | None = None
    cur_qs: list[dict] = []
    in_intro = False
    i = 0

    while i < len(lines):
        s = lines[i].strip()

        # "How to use" intro section
        if re.match(r'^# How to use this guide', s):
            in_intro = True
            i += 1
            continue

        # Section header: # Section A — Title (Q1–Q22)
        sec_m = re.match(r'^# (Section ([A-Z]) — .+)', s)
        if sec_m:
            if cur_sec is not None:
                sections.append({
                    'id': f'sec-{cur_sec["letter"]}',
                    'letter': cur_sec['letter'],
                    'title': cur_sec['title'],
                    'questions': cur_qs,
                })
            cur_sec = {'letter': sec_m.group(2), 'title': sec_m.group(1)}
            cur_qs = []
            in_intro = False
            i += 1
            continue

        # Horizontal rule — just marks end of section, skip
        if s == '---':
            in_intro = False
            i += 1
            continue

        # Collect intro text
        if in_intro and s and not s.startswith('#'):
            intro.append(lines[i])
            i += 1
            continue

        # Question: **N. Question text?**
        q_m = re.match(r'^\*\*(\d+)\.\s+(.+?)\*\*\s*$', s)
        if q_m and cur_sec is not None:
            q_num = int(q_m.group(1))
            q_text = q_m.group(2)
            ans_lines: list[str] = []
            i += 1
            while i < len(lines):
                nxt = lines[i].strip()
                if re.match(r'^\*\*\d+\.', nxt) or re.match(r'^# ', nxt):
                    break
                if nxt == '---':
                    i += 1
                    break
                ans_lines.append(lines[i])
                i += 1
            cur_qs.append({
                'num': q_num,
                'q': q_text,
                'a': '\n'.join(ans_lines).strip(),
            })
            continue

        i += 1

    if cur_sec is not None:
        sections.append({
            'id': f'sec-{cur_sec["letter"]}',
            'letter': cur_sec['letter'],
            'title': cur_sec['title'],
            'questions': cur_qs,
        })

    return '\n'.join(intro).strip(), sections


# ─── HTML builder ────────────────────────────────────────────────────────────

def build_html(intro_raw: str, sections: list) -> str:
    total = sum(len(s['questions']) for s in sections)

    # ── Sidebar navigation ──
    nav_parts = []
    for sec in sections:
        short_m = re.match(r'Section [A-Z] — (.+?)(?:\s+\(Q|\s*$)', sec['title'])
        short = short_m.group(1) if short_m else sec['title']
        range_m = re.search(r'\(Q(\d+)[–—-]Q?(\d+)\)', sec['title'])
        range_str = f"Q{range_m.group(1)}–{range_m.group(2)}" if range_m else ''
        n = len(sec['questions'])
        nav_parts.append(
            f'<a href="#{sec["id"]}" class="nav-item" data-sec="{sec["id"]}">'
            f'<span class="nav-letter">{esc(sec["letter"])}</span>'
            f'<div class="nav-body">'
            f'<span class="nav-title">{esc(short)}</span>'
            f'<span class="nav-sub">{esc(range_str)} &middot; '
            f'<span id="cnt-{sec["id"]}">{n}</span> Q</span>'
            f'</div>'
            f'</a>'
        )
    nav_html = '\n'.join(nav_parts)

    # ── Section blocks ──
    sec_parts = []
    for sec in sections:
        n = len(sec['questions'])
        cards = []
        for q in sec['questions']:
            ans_html = block_md(q['a'])
            cards.append(
                f'<div class="qa-card" id="q{q["num"]}" data-sec="{sec["id"]}">'
                f'<div class="qa-q" onclick="toggleCard(this)">'
                f'<span class="qnum">Q{q["num"]}</span>'
                f'<span class="qtext">{esc(q["q"])}</span>'
                f'<button class="check-btn" onclick="markDone(event,{q["num"]})" title="Mark as reviewed">&#9711;</button>'
                f'<span class="arrow">&#9656;</span>'
                f'</div>'
                f'<div class="qa-a"><div class="ans-inner">{ans_html}</div></div>'
                f'</div>'
            )
        cards_html = '\n'.join(cards)
        sid = sec['id']
        sec_parts.append(
            f'<section id="{sid}" class="sec-block">'
            f'<div class="sec-hdr">'
            f'<h2>{esc(sec["title"])}</h2>'
            f'<div class="sec-acts">'
            f'<span class="sec-stat" id="stat-{sid}">0/{n} reviewed</span>'
            f'<button class="tiny-btn" onclick="secExpand(\'{sid}\')">Expand</button>'
            f'<button class="tiny-btn" onclick="secCollapse(\'{sid}\')">Collapse</button>'
            f'</div>'
            f'</div>'
            f'<div class="cards-list">{cards_html}</div>'
            f'</section>'
        )
    sections_html = '\n'.join(sec_parts)

    intro_html = block_md(intro_raw) if intro_raw else ''

    # ── Assemble final HTML ──
    html = HTML_TEMPLATE
    html = html.replace('%%NAV%%', nav_html)
    html = html.replace('%%INTRO%%', intro_html)
    html = html.replace('%%SECTIONS%%', sections_html)
    html = html.replace('%%TOTAL%%', str(total))
    return html


# ─── HTML Template ───────────────────────────────────────────────────────────

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interview Prep — 200 Q&amp;A | Himanshu Kumar</title>
<style>
/* ── Reset & root ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --sb-w: 272px;
  --sb-bg: #111827;
  --sb-border: #1f2937;
  --sb-text: #9ca3af;
  --sb-hover: #1f2937;
  --sb-active-bg: #1e3a5f;
  --sb-active-text: #60a5fa;
  --sb-letter-bg: #1f2937;
  --sb-letter-active: #3b82f6;
  --bg: #f3f4f6;
  --card: #ffffff;
  --text: #111827;
  --muted: #6b7280;
  --border: #e5e7eb;
  --accent: #2563eb;
  --accent-light: #eff6ff;
  --green: #059669;
  --green-light: #ecfdf5;
  --ans-bg: #f9fafb;
  --code-bg: #f3f4f6;
  --code-fg: #be185d;
  --note-bg: #fffbeb;
  --note-border: #fcd34d;
  --topbar: 56px;
}
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }

/* ── Layout ── */
.layout { display: flex; min-height: 100vh; }

/* ── Sidebar ── */
.sidebar {
  width: var(--sb-w);
  background: var(--sb-bg);
  position: fixed;
  top: 0; left: 0; bottom: 0;
  display: flex; flex-direction: column;
  overflow: hidden;
  border-right: 1px solid var(--sb-border);
  z-index: 200;
}
.sb-header {
  padding: 20px 16px 14px;
  border-bottom: 1px solid var(--sb-border);
  flex-shrink: 0;
}
.sb-header .brand { font-size: 13px; font-weight: 700; color: #f9fafb; letter-spacing: .04em; text-transform: uppercase; }
.sb-header .sub { font-size: 11px; color: var(--sb-text); margin-top: 3px; }
.sb-progress { padding: 12px 16px; border-bottom: 1px solid var(--sb-border); flex-shrink: 0; }
.sb-prog-label { font-size: 11px; color: var(--sb-text); display: flex; justify-content: space-between; margin-bottom: 7px; }
.sb-prog-label #prog-txt { color: #d1d5db; }
.prog-track { height: 5px; background: #1f2937; border-radius: 3px; overflow: hidden; }
.prog-fill { height: 100%; background: linear-gradient(90deg, #2563eb, #10b981); border-radius: 3px; width: 0; transition: width .4s ease; }
.sb-nav { flex: 1; overflow-y: auto; padding: 6px 0; }
.sb-nav::-webkit-scrollbar { width: 4px; }
.sb-nav::-webkit-scrollbar-thumb { background: #374151; border-radius: 2px; }
.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 9px 14px;
  text-decoration: none;
  color: var(--sb-text);
  font-size: 13px;
  border-left: 3px solid transparent;
  transition: background .12s, color .12s;
}
.nav-item:hover { background: var(--sb-hover); color: #e5e7eb; }
.nav-item.active { background: var(--sb-active-bg); color: var(--sb-active-text); border-left-color: var(--sb-letter-active); }
.nav-letter {
  width: 24px; height: 24px; border-radius: 5px;
  background: var(--sb-letter-bg);
  color: #60a5fa;
  font-size: 12px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.nav-item.active .nav-letter { background: var(--sb-letter-active); color: #fff; }
.nav-body { flex: 1; min-width: 0; }
.nav-title { display: block; font-size: 12.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.nav-sub { font-size: 10.5px; color: #4b5563; display: block; margin-top: 1px; }
.nav-item.active .nav-sub { color: #93c5fd; }

/* ── Main ── */
.main { margin-left: var(--sb-w); flex: 1; display: flex; flex-direction: column; }

/* ── Top bar ── */
.topbar {
  position: sticky; top: 0;
  background: white;
  border-bottom: 1px solid var(--border);
  padding: 10px 28px;
  display: flex; align-items: center; gap: 12px;
  z-index: 100;
  height: var(--topbar);
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
}
.search-wrap { position: relative; flex: 1; max-width: 440px; }
.search-icon { position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: #9ca3af; font-size: 15px; pointer-events: none; }
.search-input {
  width: 100%;
  padding: 8px 12px 8px 34px;
  border: 1.5px solid var(--border);
  border-radius: 8px;
  font-size: 14px; color: var(--text);
  background: var(--bg);
  outline: none; transition: border .15s, background .15s;
}
.search-input:focus { border-color: var(--accent); background: #fff; }
.tb-actions { display: flex; gap: 8px; margin-left: auto; }
.btn {
  padding: 7px 14px; font-size: 13px;
  border: 1.5px solid var(--border); border-radius: 7px;
  cursor: pointer; background: white; color: var(--muted);
  transition: background .15s, border .15s;
}
.btn:hover { background: var(--bg); border-color: #d1d5db; }
.btn.primary { background: var(--accent); color: white; border-color: var(--accent); }
.btn.primary:hover { background: #1d4ed8; }

/* ── Content area ── */
.content { padding: 28px 32px; max-width: 940px; }

/* ── Intro card ── */
.intro-card {
  background: linear-gradient(135deg, #1e3a5f 0%, #1e40af 100%);
  color: white; border-radius: 12px;
  padding: 22px 26px; margin-bottom: 30px;
}
.intro-card h2 { font-size: 16px; font-weight: 700; letter-spacing: .02em; margin-bottom: 12px; opacity: .95; }
.intro-card p { font-size: 13.5px; line-height: 1.75; opacity: .88; margin-bottom: 8px; }
.intro-card p:last-child { margin-bottom: 0; }
.intro-card strong { color: #93c5fd; font-weight: 600; }
.intro-card ul { list-style: none; padding: 0; }
.intro-card li { font-size: 13.5px; line-height: 1.75; opacity: .88; padding-left: 16px; position: relative; margin-bottom: 4px; }
.intro-card li::before { content: '›'; position: absolute; left: 0; opacity: .7; }
.intro-card code { background: rgba(255,255,255,.15); padding: 1px 5px; border-radius: 3px; font-size: 12.5px; }

/* ── Section block ── */
.sec-block { margin-bottom: 36px; }
.sec-block.hidden { display: none; }
.sec-hdr {
  display: flex; align-items: flex-start; gap: 12px;
  padding-bottom: 10px;
  border-bottom: 2px solid #dbeafe;
  margin-bottom: 12px;
}
.sec-hdr h2 { font-size: 17px; font-weight: 700; color: #1e40af; flex: 1; line-height: 1.4; }
.sec-acts { display: flex; align-items: center; gap: 8px; flex-shrink: 0; padding-top: 2px; }
.sec-stat { font-size: 11.5px; color: var(--muted); white-space: nowrap; }
.tiny-btn {
  font-size: 11px; padding: 3px 9px;
  border: 1px solid var(--border); border-radius: 5px;
  cursor: pointer; background: white; color: var(--muted);
  transition: background .12s;
}
.tiny-btn:hover { background: var(--bg); }

/* ── Q&A card ── */
.qa-card {
  border: 1.5px solid var(--border); border-radius: 8px;
  margin-bottom: 7px; background: var(--card);
  transition: border-color .15s;
  overflow: hidden;
}
.qa-card:hover { border-color: #bfdbfe; }
.qa-card.open { border-color: var(--accent); }
.qa-card.done { border-color: #6ee7b7; background: var(--green-light); }
.qa-card.hidden { display: none; }

.qa-q {
  display: flex; align-items: flex-start; gap: 10px;
  padding: 11px 14px; cursor: pointer; user-select: none;
}
.qa-q:hover { background: #fafafa; }
.qa-card.open .qa-q { background: var(--accent-light); }
.qa-card.done .qa-q { background: var(--green-light); }
.qnum {
  font-size: 11px; font-weight: 700;
  color: white; background: var(--accent);
  padding: 2px 7px; border-radius: 4px;
  flex-shrink: 0; margin-top: 1px;
}
.qa-card.done .qnum { background: var(--green); }
.qtext { flex: 1; font-size: 14px; font-weight: 600; color: var(--text); line-height: 1.45; }
.check-btn {
  flex-shrink: 0; background: none; border: none;
  font-size: 18px; cursor: pointer; color: #9ca3af;
  padding: 0 2px; line-height: 1; margin-top: -1px;
  transition: color .15s, transform .15s;
}
.check-btn:hover { color: var(--green); transform: scale(1.15); }
.qa-card.done .check-btn { color: var(--green); }
.arrow {
  flex-shrink: 0; font-size: 13px; color: #9ca3af;
  transition: transform .2s; margin-top: 2px;
}
.qa-card.open .arrow { transform: rotate(90deg); }

/* Answer */
.qa-a { display: none; }
.qa-a.open { display: block; }
.ans-inner {
  padding: 14px 14px 16px 14px;
  border-top: 1px solid var(--border);
  background: var(--ans-bg);
}
.ans-inner p { font-size: 14px; line-height: 1.78; color: #1f2937; margin-bottom: 10px; }
.ans-inner p:last-child { margin-bottom: 0; }
.ans-inner ul { padding-left: 20px; margin-bottom: 10px; }
.ans-inner li { font-size: 14px; line-height: 1.75; margin-bottom: 5px; color: #1f2937; }
.ans-inner strong { color: #1d4ed8; font-weight: 600; }
.ans-inner code {
  background: var(--code-bg); color: var(--code-fg);
  padding: 1px 5px; border-radius: 3px;
  font-family: 'SF Mono', 'Cascadia Code', Consolas, monospace;
  font-size: 12.5px; border: 1px solid #e5e7eb;
}
.ans-inner blockquote {
  border-left: 3px solid #fbbf24;
  background: var(--note-bg);
  padding: 10px 14px;
  margin-bottom: 10px;
  border-radius: 0 6px 6px 0;
  font-size: 13.5px; color: #78350f; font-style: italic;
}

/* ── No results ── */
.no-results { display: none; text-align: center; padding: 80px 0; color: var(--muted); }
.no-results.visible { display: block; }
.no-results .icon { font-size: 40px; margin-bottom: 12px; display: block; }
.no-results p { font-size: 15px; }

/* ── Back-to-top ── */
.back-top {
  position: fixed; bottom: 22px; right: 22px;
  width: 40px; height: 40px;
  background: var(--accent); color: white;
  border: none; border-radius: 50%;
  font-size: 18px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 14px rgba(37,99,235,.35);
  opacity: 0; pointer-events: none; transition: opacity .2s;
}
.back-top.show { opacity: 1; pointer-events: all; }

/* ── Print ── */
@media print {
  .sidebar, .topbar, .back-top, .sec-acts, .check-btn { display: none !important; }
  .main { margin-left: 0; }
  .qa-a { display: block !important; }
  .ans-inner { border-top: 1px solid #e5e7eb; }
  .qa-card { break-inside: avoid; border: 1px solid #e5e7eb; margin-bottom: 10px; }
  .arrow { display: none; }
  .content { padding: 0; max-width: 100%; }
  .qa-card.open .qa-q, .qa-card.done .qa-q { background: none; }
  .intro-card { background: #f3f4f6 !important; color: #111 !important; -webkit-print-color-adjust: exact; }
}

/* ── Responsive ── */
@media (max-width: 700px) {
  :root { --sb-w: 0px; }
  .sidebar { transform: translateX(-100%); transition: transform .25s; }
  .sidebar.open { transform: none; width: 270px; }
  .main { margin-left: 0; }
  .content { padding: 16px; }
  .topbar { padding: 10px 14px; }
}
</style>
</head>
<body>

<div class="layout">

  <!-- ── Sidebar ── -->
  <nav class="sidebar" id="sidebar">
    <div class="sb-header">
      <div class="brand">Interview Prep</div>
      <div class="sub">Himanshu Kumar &mdash; Oracle SCM</div>
    </div>
    <div class="sb-progress">
      <div class="sb-prog-label">
        <span>Progress</span>
        <span><span id="prog-txt">0 / %%TOTAL%%</span> reviewed</span>
      </div>
      <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
    </div>
    <div class="sb-nav" id="sb-nav">
%%NAV%%
    </div>
  </nav>

  <!-- ── Main ── -->
  <div class="main">

    <!-- Top bar -->
    <div class="topbar">
      <div class="search-wrap">
        <span class="search-icon">&#128269;</span>
        <input class="search-input" id="search" type="text"
               placeholder="Search questions &amp; answers&hellip;"
               oninput="doSearch(this.value)" autocomplete="off">
      </div>
      <div class="tb-actions">
        <button class="btn" onclick="expandAll()">Expand All</button>
        <button class="btn" onclick="collapseAll()">Collapse All</button>
        <button class="btn primary" onclick="window.print()">&#128424; Print / PDF</button>
      </div>
    </div>

    <!-- Content -->
    <div class="content" id="content">

      <div class="intro-card">
        <h2>&#128216; How to Use This Guide</h2>
%%INTRO%%
      </div>

%%SECTIONS%%

      <div class="no-results" id="no-results">
        <span class="icon">&#128270;</span>
        <p>No questions match your search.</p>
      </div>
    </div>
  </div>
</div>

<button class="back-top" id="back-top" onclick="window.scrollTo({top:0,behavior:'smooth'})" title="Back to top">&#8679;</button>

<script>
(function () {
  const TOTAL = %%TOTAL%%;
  let doneSet = new Set(JSON.parse(localStorage.getItem('iq_done') || '[]'));

  /* ─ Progress ─ */
  function updateProgress() {
    const n = doneSet.size;
    document.getElementById('prog-txt').textContent = n + ' / ' + TOTAL;
    document.getElementById('prog-fill').style.width = (n / TOTAL * 100).toFixed(1) + '%';
    // Update per-section stats
    document.querySelectorAll('.sec-block').forEach(function(sec) {
      const id = sec.id;
      const cards = sec.querySelectorAll('.qa-card');
      const done = [...cards].filter(function(c){ return c.classList.contains('done'); }).length;
      const el = document.getElementById('cnt-' + id);
      if (el) el.textContent = cards.length;
      const st = document.getElementById('stat-' + id);
      if (st) st.textContent = done + '/' + cards.length + ' reviewed';
    });
  }

  /* ─ Mark done ─ */
  window.markDone = function(e, num) {
    e.stopPropagation();
    const card = document.getElementById('q' + num);
    if (!card) return;
    const btn = card.querySelector('.check-btn');
    if (doneSet.has(num)) {
      doneSet.delete(num);
      card.classList.remove('done');
      btn.innerHTML = '&#9711;';
    } else {
      doneSet.add(num);
      card.classList.add('done');
      btn.innerHTML = '&#9646;';
    }
    localStorage.setItem('iq_done', JSON.stringify([...doneSet]));
    updateProgress();
  };

  /* ─ Toggle card ─ */
  window.toggleCard = function(el) {
    const card = el.closest('.qa-card');
    const ans = card.querySelector('.qa-a');
    const open = card.classList.contains('open');
    card.classList.toggle('open', !open);
    ans.classList.toggle('open', !open);
  };

  /* ─ Section expand / collapse ─ */
  window.secExpand = function(id) {
    document.querySelectorAll('#' + id + ' .qa-card:not(.hidden)').forEach(function(c) {
      c.classList.add('open');
      c.querySelector('.qa-a').classList.add('open');
    });
  };
  window.secCollapse = function(id) {
    document.querySelectorAll('#' + id + ' .qa-card').forEach(function(c) {
      c.classList.remove('open');
      c.querySelector('.qa-a').classList.remove('open');
    });
  };
  window.expandAll = function() {
    document.querySelectorAll('.qa-card:not(.hidden)').forEach(function(c) {
      c.classList.add('open');
      c.querySelector('.qa-a').classList.add('open');
    });
  };
  window.collapseAll = function() {
    document.querySelectorAll('.qa-card').forEach(function(c) {
      c.classList.remove('open');
      c.querySelector('.qa-a').classList.remove('open');
    });
  };

  /* ─ Search ─ */
  window.doSearch = function(query) {
    const q = query.toLowerCase().trim();
    let any = false;
    document.querySelectorAll('.qa-card').forEach(function(card) {
      const qt = card.querySelector('.qtext').textContent.toLowerCase();
      const at = card.querySelector('.ans-inner').textContent.toLowerCase();
      const show = !q || qt.includes(q) || at.includes(q);
      card.classList.toggle('hidden', !show);
      if (show) any = true;
    });
    document.querySelectorAll('.sec-block').forEach(function(sec) {
      const vis = sec.querySelectorAll('.qa-card:not(.hidden)').length > 0;
      sec.classList.toggle('hidden', !vis);
    });
    const nr = document.getElementById('no-results');
    if (any || !q) nr.classList.remove('visible'); else nr.classList.add('visible');
  };

  /* ─ Active nav on scroll ─ */
  function updateNav() {
    const scrollY = window.scrollY + 80;
    let active = null;
    document.querySelectorAll('.sec-block').forEach(function(sec) {
      if (sec.offsetTop <= scrollY) active = sec.id;
    });
    document.querySelectorAll('.nav-item').forEach(function(a) {
      a.classList.toggle('active', a.dataset.sec === active);
    });
    const bt = document.getElementById('back-top');
    bt.classList.toggle('show', window.scrollY > 350);
  }
  window.addEventListener('scroll', updateNav, { passive: true });

  /* ─ Init ─ */
  doneSet.forEach(function(num) {
    const card = document.getElementById('q' + num);
    if (card) {
      card.classList.add('done');
      const btn = card.querySelector('.check-btn');
      if (btn) btn.innerHTML = '&#9646;';
    }
  });
  updateProgress();
  updateNav();
})();
</script>
</body>
</html>
"""


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    if not SRC.exists():
        print(f"Error: source file not found: {SRC}")
        return 1
    print(f"Reading {SRC.name} ...")
    content = SRC.read_text(encoding='utf-8')
    intro, sections = parse(content)
    total_q = sum(len(s['questions']) for s in sections)
    print(f"Parsed {len(sections)} sections, {total_q} questions.")
    html_out = build_html(intro, sections)
    OUT.write_text(html_out, encoding='utf-8')
    print(f"Written → {OUT.name}  ({OUT.stat().st_size // 1024} KB)")
    print("Open Interview_Prep_200_QA.html in your browser.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
