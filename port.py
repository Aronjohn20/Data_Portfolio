import streamlit as st
 
st.set_page_config(
    page_title="Alex Mercer | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
# ─────────────────────────────────────────────
#  ✏️  EDIT YOUR INFO HERE
# ─────────────────────────────────────────────
NAME     = "Alex Mercer"
TAGLINE  = "Data Analyst · Turning raw data into real decisions"
EMAIL    = "alex.mercer@email.com"
LINKEDIN = "https://linkedin.com/in/alexmercer"
GITHUB   = "https://github.com/alexmercer"
RESUME   = ""   # paste your Google Drive / Dropbox PDF link here
 
ABOUT = """
Hi! I'm Alex, a data analyst who loves digging into messy datasets and surfacing
clean, actionable insights. I work across the full analytics stack — from wrangling
data with PySpark and SQL to building interactive dashboards in Power BI and Tableau.
<br><br>
When I'm not querying databases, I'm probably tinkering with Python scripts or
exploring the latest in ML tooling.
"""
 
# ✏️ Add / remove skills freely
SKILLS = [
    {"name": "SQL",              "level": 92, "color": "#00B4D8"},
    {"name": "Python",           "level": 90, "color": "#3DDC97"},
    {"name": "Excel",            "level": 88, "color": "#48CAE4"},
    {"name": "Power BI/Tableau", "level": 85, "color": "#E76F51"},
    {"name": "PySpark",          "level": 75, "color": "#F4A261"},
    {"name": "Machine Learning", "level": 65, "color": "#9B89FF"},
]
 
# ✏️ Add / remove projects freely — just copy-paste a block
PROJECTS = [
    {
        "title":  "Customer Churn Prediction",
        "emoji":  "📉",
        "color":  "#FF6B6B",
        "tags":   ["Python", "Scikit-learn", "SQL", "Tableau"],
        "desc":   "Built an end-to-end churn prediction pipeline for a telecom dataset (50k+ customers). Reduced churn by 18% after deploying actionable segment-level insights to the marketing team.",
        "link":   "https://github.com/alexmercer/churn-prediction",
    },
    {
        "title":  "Sales Dashboard — Power BI",
        "emoji":  "📊",
        "color":  "#FFD166",
        "tags":   ["Power BI", "SQL", "Excel"],
        "desc":   "Interactive regional sales dashboard with drill-down capability, KPI cards, and automated weekly email reports. Used by 3 regional managers daily.",
        "link":   "",
    },
    {
        "title":  "E-Commerce Data Pipeline",
        "emoji":  "⚡",
        "color":  "#06D6A0",
        "tags":   ["PySpark", "Python", "SQL"],
        "desc":   "Designed and deployed a PySpark ETL pipeline processing 2M+ daily transactions on Databricks. Reduced data latency from 6 hours to under 30 minutes.",
        "link":   "https://github.com/alexmercer/ecom-pipeline",
    },
    {
        "title":  "HR Analytics Report",
        "emoji":  "👥",
        "color":  "#74B9FF",
        "tags":   ["Python", "Tableau", "Excel"],
        "desc":   "Analysed attrition patterns across departments. Identified key drivers with logistic regression (AUC 0.84). Presented findings to HR leadership.",
        "link":   "",
    },
]
 
# ─────────────────────────────────────────────
#  STYLES + FULL PAGE LAYOUT
# ─────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
 
html, body, [class*="css"] {{
    font-family: 'Space Grotesk', sans-serif;
    background-color: #070d1a;
    color: #c8daf0;
    overflow-x: hidden;
}}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
section[data-testid="stMain"] > div {{ padding: 0 !important; }}
 
/* ── TOP NAV ── */
.topnav {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    background: rgba(7,13,26,.92); backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255,255,255,.06);
    display: flex; justify-content: space-between; align-items: center;
    padding: .7rem 3rem;
}}
.topnav-logo {{
    font-family: 'JetBrains Mono', monospace;
    color: #3DDC97; font-size: .9rem; font-weight: 600;
}}
.topnav-links {{ display: flex; gap: 4px; }}
.topnav-links a {{
    color: #7a9abf; font-size: .8rem; font-weight: 500;
    text-decoration: none; padding: .3rem .85rem; border-radius: 6px;
    transition: all .2s;
}}
.topnav-links a:hover {{
    color: #3DDC97; background: rgba(61,220,151,.1);
}}
 
/* ── FULL SCREEN SECTIONS ── */
.section {{
    min-height: 100vh;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    padding: 6rem 2rem 3rem;
    position: relative; overflow: hidden;
}}
.section:nth-child(odd) {{ background: #070d1a; }}
.section:nth-child(even) {{ background: #0a1120; }}
 
/* subtle grid bg */
.section::before {{
    content: '';
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(61,220,151,.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(61,220,151,.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
}}
 
/* glow blobs */
.blob {{
    position: absolute; border-radius: 50%;
    filter: blur(80px); pointer-events: none; z-index: 0;
}}
 
/* ── SECTION HEADINGS ── */
.sec-heading {{
    font-size: 1.9rem; font-weight: 700; color: #e0ecff;
    text-align: center; margin-bottom: 2.5rem;
    position: relative; z-index: 1;
}}
.sec-heading span {{
    background: linear-gradient(90deg,#3DDC97,#00B4D8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
 
/* ── HERO ── */
.hero-wrap {{ text-align: center; position: relative; z-index: 1; max-width: 700px; }}
.hero-name {{
    font-size: 3.6rem; font-weight: 700; line-height: 1.1;
    background: linear-gradient(90deg,#3DDC97,#00B4D8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: .5rem;
}}
.hero-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: .95rem; color: #5a8ab0; margin-bottom: 1.8rem;
}}
.hero-badges {{ display: flex; flex-wrap: wrap; gap: .5rem; justify-content: center; margin-bottom: 2rem; }}
.hbadge {{
    font-family: 'JetBrains Mono', monospace; font-size: .72rem;
    padding: .28rem .8rem; border-radius: 20px;
    border: 1px solid rgba(61,220,151,.3);
    background: rgba(61,220,151,.07); color: #3DDC97;
}}
.hero-cta {{ display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }}
.btn-solid {{
    padding: .55rem 1.5rem; border-radius: 8px; font-size: .88rem;
    font-weight: 700; background: #3DDC97; color: #070d1a;
    text-decoration: none; transition: all .2s; display: inline-block;
}}
.btn-solid:hover {{ background: #2fc484; transform: translateY(-2px); }}
.btn-out {{
    padding: .55rem 1.5rem; border-radius: 8px; font-size: .88rem;
    font-weight: 700; background: transparent;
    border: 1.5px solid #3DDC97; color: #3DDC97;
    text-decoration: none; transition: all .2s; display: inline-block;
}}
.btn-out:hover {{ background: rgba(61,220,151,.1); transform: translateY(-2px); }}
 
/* scroll hint */
.scroll-hint {{
    position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%);
    z-index: 1; display: flex; flex-direction: column; align-items: center;
    gap: .4rem; color: #2e4a6a; font-size: .72rem;
    font-family: 'JetBrains Mono', monospace;
    animation: bounce 2s ease-in-out infinite;
}}
@keyframes bounce {{
    0%,100% {{ transform: translateX(-50%) translateY(0); }}
    50% {{ transform: translateX(-50%) translateY(6px); }}
}}
 
/* ── ABOUT ── */
.about-card {{
    background: #0d1b2a; border: 1px solid #1a3050;
    border-radius: 16px; padding: 2.2rem 2.5rem;
    max-width: 680px; line-height: 1.9; font-size: .97rem;
    color: #9ab8d4; position: relative; z-index: 1;
}}
.about-card::before {{
    content: '';
    position: absolute; top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(#3DDC97, #00B4D8);
    border-radius: 4px 0 0 4px;
}}
.about-stat-row {{
    display: flex; gap: 1rem; margin-top: 1.5rem; flex-wrap: wrap;
}}
.about-stat {{
    flex: 1; min-width: 100px;
    background: rgba(61,220,151,.06);
    border: 1px solid rgba(61,220,151,.15);
    border-radius: 10px; padding: .8rem 1rem; text-align: center;
}}
.about-stat-num {{
    font-size: 1.5rem; font-weight: 700; color: #3DDC97;
    font-family: 'JetBrains Mono', monospace;
}}
.about-stat-label {{ font-size: .72rem; color: #5a8ab0; margin-top: .2rem; }}
 
/* ── PROJECTS ── */
.proj-grid {{
    display: grid; grid-template-columns: repeat(2, 1fr);
    gap: 1.2rem; width: 100%; max-width: 820px; position: relative; z-index: 1;
}}
.proj-card {{
    background: #0d1b2a; border-radius: 14px;
    border: 1px solid #1a3050;
    padding: 1.6rem; cursor: pointer;
    transition: transform .3s, box-shadow .3s, border-color .3s;
    position: relative; overflow: hidden;
}}
.proj-card:hover {{
    transform: translateY(-7px) scale(1.02);
    border-color: var(--accent);
    box-shadow: 0 0 30px rgba(var(--accent-rgb), .25), 0 16px 40px rgba(0,0,0,.4);
}}
.proj-topbar {{
    height: 3px; border-radius: 3px;
    margin: -1.6rem -1.6rem 1.2rem;
    background: var(--accent);
}}
.proj-emoji {{ font-size: 1.7rem; margin-bottom: .5rem; }}
.proj-title {{ font-size: 1rem; font-weight: 700; color: #ddeeff; margin-bottom: .5rem; }}
.proj-desc {{ font-size: .82rem; color: #6a8aaa; line-height: 1.75; margin-bottom: .9rem; }}
.proj-tags {{ display: flex; flex-wrap: wrap; gap: .35rem; margin-bottom: .8rem; }}
.ptag {{
    font-family: 'JetBrains Mono', monospace; font-size: .67rem;
    padding: .18rem .55rem; border-radius: 5px;
    background: rgba(255,255,255,.06); color: #7a9abf;
}}
.proj-link a {{
    font-size: .78rem; color: #3DDC97;
    text-decoration: none; font-weight: 600;
}}
.proj-link a:hover {{ text-decoration: underline; }}
 
/* ── SKILLS ── */
.skills-grid {{
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 1rem 3rem; width: 100%; max-width: 680px;
    position: relative; z-index: 1;
}}
.skill-item {{ }}
.skill-label {{
    display: flex; justify-content: space-between;
    font-size: .85rem; color: #aac4df; margin-bottom: .4rem;
}}
.skill-track {{
    background: #111e30; border-radius: 20px;
    height: 8px; overflow: hidden;
}}
.skill-fill {{
    height: 100%; border-radius: 20px;
    background: var(--sc);
    position: relative;
}}
.skill-fill::after {{
    content: ''; position: absolute; inset: 0;
    border-radius: 20px;
    background: linear-gradient(90deg, transparent 60%, rgba(255,255,255,.15));
}}
 
/* ── CONTACT ── */
.contact-wrap {{ position: relative; z-index: 1; width: 100%; max-width: 500px; }}
.contact-card {{
    background: #0d1b2a; border: 1px solid #1a3050;
    border-radius: 16px; padding: 2.5rem; text-align: center;
}}
.contact-card p {{ color: #7a9abf; font-size: .93rem; line-height: 1.8; margin-bottom: 1.8rem; }}
.clinks {{ display: flex; flex-direction: column; gap: .7rem; }}
.clink {{
    display: flex; align-items: center; gap: .8rem;
    padding: .75rem 1.1rem; border-radius: 10px;
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.08);
    color: #aac4df; font-size: .88rem; text-decoration: none;
    transition: all .25s;
}}
.clink:hover {{
    background: rgba(61,220,151,.08);
    border-color: rgba(61,220,151,.3); color: #3DDC97;
    transform: translateX(4px);
}}
.clink-icon {{ font-size: 1rem; width: 22px; text-align: center; }}
 
/* ── FOOTER ── */
.footer {{
    text-align: center; padding: 1.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem; color: #1e3450;
    background: #060b16;
    border-top: 1px solid rgba(255,255,255,.04);
}}
</style>
 
<!-- ═══════════════ TOP NAV ═══════════════ -->
<div class="topnav">
  <span class="topnav-logo">$ {NAME.lower().replace(' ','.')}</span>
  <div class="topnav-links">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#contact">Contact</a>
  </div>
</div>
 
<!-- ═══════════════ HERO ═══════════════ -->
<div class="section" id="home">
  <div class="blob" style="width:400px;height:400px;background:rgba(61,220,151,.07);top:-100px;right:-100px;"></div>
  <div class="blob" style="width:300px;height:300px;background:rgba(0,180,216,.06);bottom:-80px;left:-80px;"></div>
  <div class="hero-wrap">
    <div class="hero-name">{NAME}</div>
    <div class="hero-tag">$ {TAGLINE}</div>
    <div class="hero-badges">
      {''.join(f'<span class="hbadge">{s["name"]}</span>' for s in SKILLS)}
    </div>
    <div class="hero-cta">
      <a href="#contact" class="btn-solid">✉ Get in Touch</a>
      <a href="#projects" class="btn-out">🚀 View Projects</a>
      {f'<a href="{RESUME}" target="_blank" class="btn-out">📄 Resume</a>' if RESUME else ''}
      <a href="{LINKEDIN}" target="_blank" class="btn-out">🔗 LinkedIn</a>
    </div>
  </div>
  <div class="scroll-hint">↓ scroll</div>
</div>
 
<!-- ═══════════════ ABOUT ═══════════════ -->
<div class="section" id="about">
  <div class="blob" style="width:350px;height:350px;background:rgba(0,180,216,.06);top:50px;left:-80px;"></div>
  <div class="sec-heading">About <span>Me</span></div>
  <div class="about-card">
    {ABOUT}
    <div class="about-stat-row">
      <div class="about-stat"><div class="about-stat-num">4+</div><div class="about-stat-label">Years Experience</div></div>
      <div class="about-stat"><div class="about-stat-num">20+</div><div class="about-stat-label">Projects Done</div></div>
      <div class="about-stat"><div class="about-stat-num">6</div><div class="about-stat-label">Tools Mastered</div></div>
      <div class="about-stat"><div class="about-stat-num">∞</div><div class="about-stat-label">Coffee Consumed</div></div>
    </div>
  </div>
</div>
 
<!-- ═══════════════ PROJECTS ═══════════════ -->
<div class="section" id="projects">
  <div class="blob" style="width:300px;height:300px;background:rgba(61,220,151,.06);bottom:50px;right:-60px;"></div>
  <div class="sec-heading">My <span>Projects</span></div>
  <div class="proj-grid">
""", unsafe_allow_html=True)
 
# Render project cards
for proj in PROJECTS:
    # extract rgb from hex for box-shadow
    h = proj["color"].lstrip("#")
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    tags_html = "".join(f'<span class="ptag">{t}</span>' for t in proj["tags"])
    link_html = f'<div class="proj-link"><a href="{proj["link"]}" target="_blank">→ View Project</a></div>' if proj.get("link") else ""
    st.markdown(f"""
    <div class="proj-card" style="--accent:{proj['color']};--accent-rgb:{r},{g},{b}">
      <div class="proj-topbar"></div>
      <div class="proj-emoji">{proj['emoji']}</div>
      <div class="proj-title">{proj['title']}</div>
      <div class="proj-desc">{proj['desc']}</div>
      <div class="proj-tags">{tags_html}</div>
      {link_html}
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""
  </div>
</div>
 
<!-- ═══════════════ SKILLS ═══════════════ -->
<div class="section" id="skills">
  <div class="blob" style="width:350px;height:350px;background:rgba(0,180,216,.05);top:0;right:-60px;"></div>
  <div class="sec-heading">Skills & <span>Tools</span></div>
  <div class="skills-grid">
""", unsafe_allow_html=True)
 
for skill in SKILLS:
    st.markdown(f"""
    <div class="skill-item">
      <div class="skill-label"><span>{skill['name']}</span><span>{skill['level']}%</span></div>
      <div class="skill-track">
        <div class="skill-fill" style="width:{skill['level']}%;--sc:{skill['color']}"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
 
# Contact section
contact_links = f"""
<a href="mailto:{st.session_state.get('email', 'alex.mercer@email.com')}" class="clink">
  <span class="clink-icon">✉</span> alex.mercer@email.com
</a>
"""
 
import urllib.parse
linkedin_url = "https://linkedin.com/in/alexmercer"
github_url   = "https://github.com/alexmercer"
 
st.markdown(f"""
  </div>
</div>
 
<!-- ═══════════════ CONTACT ═══════════════ -->
<div class="section" id="contact">
  <div class="blob" style="width:400px;height:400px;background:rgba(61,220,151,.07);bottom:-100px;left:-100px;"></div>
  <div class="sec-heading">Get In <span>Touch</span></div>
  <div class="contact-wrap">
    <div class="contact-card">
      <p>I'm open to freelance, full-time, and collaboration opportunities.<br>Drop a message — I'd love to connect!</p>
      <div class="clinks">
        <a href="mailto:{EMAIL}" class="clink"><span class="clink-icon">✉</span>{EMAIL}</a>
        <a href="{LINKEDIN}" target="_blank" class="clink"><span class="clink-icon">🔗</span>LinkedIn Profile</a>
        <a href="{GITHUB}" target="_blank" class="clink"><span class="clink-icon">🐙</span>GitHub Profile</a>
        {f'<a href="{RESUME}" target="_blank" class="clink"><span class="clink-icon">📄</span>Download Resume</a>' if RESUME else ''}
      </div>
    </div>
  </div>
</div>
 
<!-- ═══════════════ FOOTER ═══════════════ -->
<div class="footer">
  Built with Streamlit &amp; ❤️ · {NAME} © 2025
</div>
""", unsafe_allow_html=True)
