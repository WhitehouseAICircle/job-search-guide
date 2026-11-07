"""Rebuild the static guide: python build_site.py (requires Python Markdown)."""
from pathlib import Path
import html
import re
import markdown

ROOT = Path(__file__).resolve().parent
PAGES = {
    'walkthrough.html': ('docs/job-search-workflow.md', 'The walkthrough', '01', 'Try a job search, one step at a time.'),
    'instructions.html': ('docs/project-instructions.md', 'Project instructions', '02', 'Give your assistant a useful starting point.'),
    'prompts.html': ('docs/example-chats.md', 'Prompts to try', '03', 'A little help with the next task.'),
    'privacy.html': ('docs/privacy-notes.md', 'Privacy first', '04', 'Share less. Keep yourself in control.'),
    'journey.html': ('docs/whole-job-search.md', 'Your whole job-search journey', '08', 'From the first recruiter call to the decision that suits you.'),
    'linkedin.html': ('docs/linkedin-profile.md', 'Refresh your LinkedIn profile', '07', 'Bring your experience up to date, one section at a time.'),
    'job-sweep.html': ('docs/job-sweep.md', 'Job Sweep', '06', 'Let a regular search bring potential roles to you.'),
    'screenshots.html': ('images/README.md', 'Inside the demo', '05', 'See what the fictional practice run looked like.'),
}
LINKS = {'whole-job-search.md':'journey.html', 'linkedin-profile.md':'linkedin.html', 'job-sweep.md':'job-sweep.html', 'job-search-workflow.md':'walkthrough.html', 'project-instructions.md':'instructions.html', 'example-chats.md':'prompts.html', 'privacy-notes.md':'privacy.html'}

def chrome(title, body, current=''):
    links = [('walkthrough.html','Walkthrough'), ('prompts.html','Prompts'), ('privacy.html','Privacy')]
    nav = ''.join('<a href="{}" {}>{}</a>'.format(href, 'aria-current="page"' if current == href else '', label) for href,label in links)
    return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Whitehouse AI Circle</title><meta name="description" content="A friendly, practical guide to organising a job search with ChatGPT Projects. Fictional examples, copyable prompts and privacy advice from Whitehouse AI Circle.">
<meta name="theme-color" content="#194c43"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header class="header"><div class="header-inner"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">✳</span><span>Whitehouse<br><b>AI Circle</b></span></a><nav aria-label="Main navigation">{nav}<a class="nav-start" href="instructions.html">Get set up <span aria-hidden="true">↗</span></a></nav></div></header>
{body}<footer><div class="footer-inner"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">✳</span><span>Useful AI.<br><b>Shared locally.</b></span></a><p>Made for the Whitehouse AI Circle.<br>Practical learning, at your own pace.</p><div><a href="https://github.com/WhitehouseAICircle/job-search-guide">View the guides on GitHub ↗</a><p class="small">Fictional demo · Updated 7 November 2026</p></div></div></footer><div id="copy-status" class="sr-only" role="status" aria-live="polite"></div></body></html>'''

def rewrite_link(match):
    before, url, after = match.groups()
    if not url.startswith(('http:', 'https:', '#')):
        name = url.split('/')[-1]
        if 'screenshots/' in url:
            url = 'images/screenshots/' + name
        elif name == 'README.md':
            url = 'screenshots.html' if 'images' in url else 'index.html'
        elif name in LINKS:
            url = LINKS[name]
    return before + url + after

for output, (source, title, number, subtitle) in PAGES.items():
    text = (ROOT/source).read_text(encoding='utf-8')
    text = re.sub(r'^# .+\n', '', text, count=1)
    text = re.sub(r'^\[Back to the guide\].*\n', '', text, flags=re.M)
    text = text.replace('Use the fictional profile in the walkthrough first.', 'Use the fictional profile in the walkthrough first.')
    content = markdown.markdown(text, extensions=['fenced_code','tables','toc','sane_lists'])
    content = re.sub(r'((?:href|src)=")([^"]+)(")', rewrite_link, content)
    content = re.sub(r'<img ', '<img loading="lazy" decoding="async" ', content)
    headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', content)
    toc = ''.join(f'<a href="#{anchor}">{re.sub("<[^>]*>", "", label)}</a>' for anchor,label in headings)
    body = f'''<main id="main"><div class="article-intro wrap"><a class="back" href="index.html">← All guides</a><p class="eyebrow">THE JOB-SEARCH GUIDE / {number}</p><h1>{title}</h1><p class="intro">{subtitle}</p></div><div class="article-layout wrap"><aside class="contents"><p class="eyebrow">ON THIS PAGE</p><nav aria-label="On this page">{toc}</nav><a class="source-link" href="https://github.com/WhitehouseAICircle/job-search-guide/blob/main/{source}">Read the source ↗</a></aside><article class="prose">{content}<div class="article-end"><span>Keep going, at your own pace.</span><a href="index.html#guides">Explore the other guides →</a></div></article></div></main>'''
    (ROOT/output).write_text(chrome(title,body,output),encoding='utf-8')

home = '''<main id="main"><section class="hero wrap"><div class="hero-copy"><p class="eyebrow"><span class="tiny-dot"></span> A PRACTICAL COMMUNITY GUIDE</p><h1>A little AI help.<br>A more organised<br><em>job search.</em></h1><p class="hero-description">From the first recruiter call to comparing offers. Keep your job search together in one ChatGPT Project, with help at each step.</p><div class="hero-actions"><a class="button" href="walkthrough.html">Try the walkthrough <span aria-hidden="true">→</span></a><a class="text-link" href="privacy.html">Read the privacy notes</a></div><div class="quick-links" aria-label="Optional job-search guides"><p class="eyebrow">TWO MORE WAYS TO HELP YOUR SEARCH</p><a href="job-sweep.html">Daily Job Sweep <span aria-hidden="true">&#8599;</span></a><a href="linkedin.html">LinkedIn profile refresh <span aria-hidden="true">&#8599;</span></a></div><div class="hero-meta"><span>20–30 minutes</span><span>Beginner friendly</span><span>No coding needed</span></div></div><div class="demo-board"><div class="board-top"><span class="paper-label">LET’S TRY AN EXAMPLE</span><span aria-hidden="true">↗</span></div><div class="board-title"><span class="folder-icon" aria-hidden="true">▱</span><div><h2>My job search</h2><p>One Project. A few focused chats.</p></div></div><div class="board-rows"><div><span class="row-symbol">01</span><span>Understand the advert</span><span aria-hidden="true">↗</span></div><div><span class="row-symbol">02</span><span>Find the right words for my CV</span><span aria-hidden="true">↗</span></div><div><span class="row-symbol">03</span><span>Practise an interview</span><span aria-hidden="true">↗</span></div></div><div class="example-note"><span class="note-label">A SMALL CHANGE, GROUNDED IN FACT</span><p>“Updated a stock spreadsheet”</p><span class="note-arrow" aria-hidden="true">↓</span><p class="improved">“Kept stock information up to date using an existing spreadsheet template.”</p><small>Clearer wording. The same real experience.</small></div><span class="board-caption">Illustrative layout · Fictional practice example</span></div></section>
<section class="journey-section wrap" aria-labelledby="journey-heading"><p class="eyebrow">ONE PROJECT. THE WHOLE JOURNEY.</p><h2 id="journey-heading">From first contact to your final decision.</h2><p class="journey-intro">Find roles or prepare for a recruiter call. Tailor applications for different jobs, rehearse interviews aloud and compare offers against what matters to you.</p><ol class="journey-stages"><li><b>Find & prepare</b><span>Job searches, recruiter calls and questions to ask.</span></li><li><b>Tailor & apply</b><span>Checked CVs and applications for each role, ready for you to send.</span></li><li><b>Practise aloud</b><span>Phone, online or in-person interviews, with simulated panel roles and feedback.</span></li><li><b>Reflect & improve</b><span>Add your debrief and recruiter or employer feedback after each conversation.</span></li><li><b>Compare & decide</b><span>Weigh up offers, clarify missing terms and choose what suits you.</span></li></ol><div class="journey-habit"><strong>The key habit: keep it up to date.</strong><p>After each call or interview, speak or type a short update. Check the summary and keep a current overview for the next step. Confirm which details ChatGPT is using; it may miss earlier information.</p></div><p class="small">Voice availability varies. Panel practice is a simulation, and you stay in charge of applications and decisions.</p><a class="text-link" href="journey.html">See the full journey and copy the prompts &#8594;</a></section>
<section class="principle-strip"><div class="wrap"><span class="strip-symbol" aria-hidden="true">✳</span><p><strong>You bring the experience.</strong> AI helps you organise and explain it. You check the facts and decide what to send.</p></div></section>
<section class="guides-section wrap" id="guides"><div class="section-heading"><div><p class="eyebrow">A PLACE TO BEGIN</p><h2>Take the next useful step.</h2></div><p>Follow the walkthrough from start to finish,<br>or dip into what you need today.</p></div><div class="guide-list">
<a class="guide-row" href="walkthrough.html"><span class="guide-number">01</span><div><h3>Try the full walkthrough</h3><p>Meet Candidate A, compare a fictional role and work through a practice application.</p></div><span class="guide-type">START HERE</span><span class="guide-arrow" aria-hidden="true">↗</span></a>
<a class="guide-row" href="instructions.html"><span class="guide-number">02</span><div><h3>Set up your Project</h3><p>Copy instructions that ask for plain English, honest claims and manageable steps.</p></div><span class="guide-type">COPY & PASTE</span><span class="guide-arrow" aria-hidden="true">↗</span></a>
<a class="guide-row" href="prompts.html"><span class="guide-number">03</span><div><h3>Find a prompt for the task</h3><p>CV edits, supporting statements, recruiter replies and interview practice.</p></div><span class="guide-type">11 IDEAS TO TRY</span><span class="guide-arrow" aria-hidden="true">↗</span></a>
<a class="guide-row" href="privacy.html"><span class="guide-number">04</span><div><h3>Keep personal details private</h3><p>What to leave out of uploads, shared chats and public screenshots.</p></div><span class="guide-type">READ FIRST</span><span class="guide-arrow" aria-hidden="true">↗</span></a>
<a class="guide-row" href="job-sweep.html"><span class="guide-number">06</span><div><h3>Set up a daily Job Sweep</h3><p>Choose your filters, try a search and schedule a shortlist to review.</p></div><span class="guide-type">OPTIONAL NEXT STEP</span><span class="guide-arrow" aria-hidden="true">↗</span></a>
<a class="guide-row" href="linkedin.html"><span class="guide-number">07</span><div><h3>Refresh your LinkedIn profile</h3><p>Review your headline, About section and skills, starting with sharing controls.</p></div><span class="guide-type">OPTIONAL NEXT STEP</span><span class="guide-arrow" aria-hidden="true">&#8599;</span></a>
</div></section>
<section class="inside-section wrap"><div class="inside-image"><img src="images/screenshots/01-project-overview.jpg" alt="A fictional practice Project with separate profile and interview chats" width="690" height="400" loading="lazy"><span>THE PRACTICE PROJECT · 7 NOVEMBER 2026</span></div><div class="inside-copy"><p class="eyebrow">TRIED WITH A FICTIONAL CANDIDATE</p><h2>See what it<br>looks like.</h2><p>We worked through the exercises in ChatGPT and captured the results. The useful bits — and the suggestions that needed a closer look — are part of the guide.</p><a class="text-link" href="screenshots.html">Take a look inside the demo →</a></div></section>
<section class="before-section wrap"><div class="before-label"><span aria-hidden="true">↳</span><h2>Before you try it</h2></div><div><p>Start with the fictional example. Don’t upload your real CV just to see how it works.</p><p class="small">AI can make convincing mistakes. Check every skill, qualification, date and employer detail. This guide is a learning resource, not a recruitment service or a promise of employment.</p><a href="privacy.html">A quick privacy check →</a></div></section>
<section class="about-section wrap"><p class="eyebrow">WHITEHOUSE AI CIRCLE</p><h2>Useful knowledge.<br>Shared between neighbours.</h2><p>We’re a local community exploring positive, practical uses of AI in everyday life, work and learning. You don’t need to be technical to take part — just curious.</p><p class="small">Project background: <a href="https://learn.chatgpt.com/docs/projects">official OpenAI Projects guide ↗</a><br>Checked 7 November 2026. Menus and features may change.</p></section></main>'''
(ROOT/'index.html').write_text(chrome('A more organised job search',home),encoding='utf-8')
print('Built nine static HTML pages.')
