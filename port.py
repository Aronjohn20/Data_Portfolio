import streamlit as st

st.set_page_config(
    page_title="Aron Varghese John | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════
#  ✏️  EDIT YOUR INFO HERE — NEVER TOUCH BELOW
# ══════════════════════════════════════════════
NAME        = "Aron Varghese John"
ROLE        = "Data Analyst"
# TAGLINE     = "I turn raw chaos into clean insight."
EMAIL       = "aronjohn12112004@gmail.com"
LINKEDIN    = "www.linkedin.com/in/aron-john27"
GITHUB      = "https://github.com/Aronjohn20/Aronjohn20"
RESUME_URL  = "https://drive.google.com/drive/folders/15_RRig9nWpqGERHO2WGEbcDbIGdb0tQZ?usp=drive_link"           # ← paste Google Drive / Dropbox PDF link
PHOTO_URL   = "WhatsApp Image 2026-01-29 at 19.53.31.jpeg"           # ← paste a direct image URL or leave empty

ABOUT_TEXT = """
Hi! I'm Aron — a aspiring data analyst obsessed with finding the story and solutions inside messy datasets.
I work end-to-end: SQL wrangling, Excel Handling, CLeaning, Transforming, Visualizing and Deriving Insights
making people understand what problem they are facing and how to handle it.
I care about making data <em>understandable</em>, not just accurate.
"""

STATS = [
    {"num": "4+",  "label": "Years Exp."},
    {"num": "20+", "label": "Projects"},
    {"num": "6",   "label": "Tools"},
    {"num": "∞",   "label": "Coffees"},
]

# Icon = emoji, color = neon hex
SKILLS = [
    {"name": "Python",           "icon": "🐍", "color": "#3DDC97", "level": 70},
    {"name": "SQL",              "icon": "🗄️", "color": "#00D4FF", "level": 70},
    {"name": "PySpark",          "icon": "⚡", "color": "#FF6B35", "level": 60},
    {"name": "Power BI",         "icon": "📊", "color": "#F7C59F", "level": 80},
    {"name": "Tableau",          "icon": "📈", "color": "#FF4DFF", "level": 50},
    {"name": "Excel",            "icon": "📗", "color": "#00FF88", "level": 75},
    # {"name": "Machine Learning", "icon": "🤖", "color": "#BD00FF", "level": 65},
    {"name": "DAX",              "icon": "🔢", "color": "#FF007A", "level": 60},
]

# ✏️ Copy-paste a block {} to add a new project
PROJECTS = [
    {
        "title":  "Customer Churn Prediction",
        "emoji":  "📉",
        "color":  "#FF4D6D",
        "tech":   ["Python", "Scikit-learn", "SQL", "Tableau"],
        "desc":   "End-to-end ML pipeline on 50k+ telecom customers. Deployed actionable insights that reduced churn by 18%. Featured logistic regression + gradient boosting ensemble.",
        "impact": "↓18% Churn",
        "link":   "https://github.com/alexmercer/churn-prediction",
    },
    {
        "title":  "E-Commerce Data Pipeline",
        "emoji":  "⚡",
        "color":  "#00FFB2",
        "tech":   ["PySpark", "Python", "Databricks", "SQL"],
        "desc":   "Designed a PySpark ETL pipeline processing 2M+ daily transactions on Databricks. Slashed data latency from 6 hours to under 30 minutes. Zero downtime deployment.",
        "impact": "6hr → 30min",
        "link":   "https://github.com/alexmercer/ecom-pipeline",
    },
    {
        "title":  "Sales Dashboard — Power BI",
        "emoji":  "📊",
        "color":  "#FFD166",
        "tech":   ["Power BI", "DAX", "SQL", "Excel"],
        "desc":   "Interactive regional sales dashboard with drill-through capability, KPI scorecards, and automated weekly email snapshots. Used by 3 regional managers daily.",
        "impact": "3 Teams Daily",
        "link":   "",
    },
    {
        "title":  "HR Attrition Analytics",
        "emoji":  "👥",
        "color":  "#BD00FF",
        "tech":   ["Python", "Tableau", "Excel", "SQL"],
        "desc":   "Analysed attrition across departments using Python + Tableau. Logistic regression model hit AUC 0.84. Findings presented to C-suite, leading to new retention policy.",
        "impact": "AUC 0.84",
        "link":   "",
    },
    {
        "title":  "Market Basket Analysis",
        "emoji":  "🛒",
        "color":  "#00D4FF",
        "tech":   ["Python", "Apriori", "SQL", "Power BI"],
        "desc":   "Association rule mining on 500k+ transactions to surface cross-sell opportunities. Recommendations adopted by marketing team — 12% lift in basket size.",
        "impact": "+12% Basket",
        "link":   "",
    },
    {
        "title":  "Real-Time Sales Tracker",
        "emoji":  "🔴",
        "color":  "#FF6B35",
        "tech":   ["Python", "Streamlit", "SQL", "Plotly"],
        "desc":   "Live sales monitoring dashboard with Streamlit + Plotly. Auto-refreshes every 60s, sends Slack alerts on anomalies. Deployed on internal server for sales team.",
        "impact": "Real-time",
        "link":   "",
    },
]

# ✏️ Work experience
EXPERIENCE = [
    # {
    #     "role":    "Senior Data Analyst",
    #     "company": "TechCorp Solutions",
    #     "period":  "2022 – Present",
    #     "color":   "#3DDC97",
    #     "points":  ["Led analytics for 3 product lines", "Built enterprise Power BI ecosystem", "Mentored 2 junior analysts"],
    # },
    # {
    #     "role":    "Data Analyst",
    #     "company": "RetailX Analytics",
    #     "period":  "2020 – 2022",
    #     "color":   "#00D4FF",
    #     "points":  ["Designed ETL pipelines in PySpark", "Reduced reporting time by 60%", "Customer segmentation models"],
    # },
    # {
    #     "role":    "Junior Data Analyst",
    #     "company": "StartupBase",
    #     "period":  "2019 – 2020",
    #     "color":   "#FF4DFF",
    #     "points":  ["SQL reporting & dashboards", "A/B test analysis", "Python automation scripts"],
    # },
]

# ✏️ Certifications
CERTS = [
    {"name": "Fundamentals of Analytics on AWS - Part 1",  "issuer": "AWS",   "year": "2025", "color": "#3DDC97"},
    {"name": "Fundamentals of Analytics on AWS - Part 2",  "issuer": "AWS",           "year": "2025", "color": "#00D4FF"},
    {"name": "Python - Hackerrank",  "issuer": "Hackerrank",          "year": "2025", "color": "#FF6B35"},
    {"name": "SQL - Hackerrank",  "issuer": "Hackerrank",             "year": "2025", "color": "#FF4DFF" }
]

# # ✏️ GitHub stats (update manually)
# GITHUB_USERNAME = "alexmercer"
# GH_STATS = {
#     "repos":   42,
#     "stars":   180,
#     "commits": "1.2k",
#     "streak":  "47 days",
# }

# ══════════════════════════════════════════════════════════
#  PAGE STATE — using session_state (no URL, no new tabs!)
# ══════════════════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "home"
 
def go(p):
    st.session_state.page = p
    st.rerun()
 
PAGE = st.session_state.page
 
# ══════════════════════════════════════════════════════════
#  GLOBAL CSS
# ══════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');
 
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
    background: #030712 !important;
    color: #e2e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stMain"] > div { padding: 0 !important; }
 
/* hide default streamlit button styles, we restyle them as nav */
div[data-testid="stHorizontalBlock"] > div { padding: 0 !important; gap: 0 !important; }
 
/* scanlines */
body::after {
    content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 9999;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,.02) 2px, rgba(0,0,0,.02) 4px);
}
 
/* bg grid */
.bg-grid {
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background-image:
        linear-gradient(rgba(61,220,151,.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(61,220,151,.03) 1px, transparent 1px);
    background-size: 60px 60px;
}
 
/* ── NAV (top bar rendered via HTML, buttons rendered via st.button) ── */
.nav-bar {
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    background: rgba(3,7,18,.92); backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(255,255,255,.07);
    padding: .65rem 2.5rem;
    display: flex; align-items: center; justify-content: space-between;
}
.nav-logo {
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: .95rem;
    background: linear-gradient(90deg, #3DDC97, #00D4FF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
 
/* Streamlit buttons styled as nav pills */
.stButton > button {
    background: transparent !important;
    border: 1px solid transparent !important;
    color: #64748b !important;
    font-size: .78rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 500 !important;
    padding: .3rem .85rem !important;
    border-radius: 6px !important;
    transition: all .2s !important;
    white-space: nowrap !important;
}
.stButton > button:hover {
    color: #fff !important;
    border-color: rgba(255,255,255,.12) !important;
    background: rgba(255,255,255,.06) !important;
}
.nav-active > div > button {
    color: #3DDC97 !important;
    border-color: rgba(61,220,151,.3) !important;
    background: rgba(61,220,151,.08) !important;
}
 
/* ── PAGE WRAPPER ── */
.page { padding-top: 58px; }
 
/* ── SECTION ── */
.section { padding: 4rem 4rem 3rem; max-width: 1200px; margin: 0 auto; }
 
.sec-eyebrow {
    font-family: 'DM Mono', monospace; font-size: .7rem;
    letter-spacing: 3px; text-transform: uppercase;
    color: #3DDC97; margin-bottom: .5rem;
}
.sec-title {
    font-family: 'Syne', sans-serif; font-size: 2.4rem; font-weight: 800;
    color: #fff; line-height: 1.1; margin-bottom: .4rem;
}
.sec-title span {
    background: linear-gradient(90deg, #3DDC97, #00D4FF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.sec-sub { font-size: .9rem; color: #64748b; margin-bottom: 2.5rem; }
 
/* ── HERO ── */
.hero-wrap {
    display: grid; grid-template-columns: 1fr 420px;
    align-items: center; gap: 3rem;
    padding: 3rem 4rem 2rem; max-width: 1200px; margin: 0 auto;
}
.hero-eyebrow {
    font-family: 'DM Mono', monospace; font-size: .72rem;
    letter-spacing: 3px; color: #3DDC97; margin-bottom: .9rem;
    display: flex; align-items: center; gap: .5rem;
}
.hero-eyebrow::before { content: ''; width: 28px; height: 1px; background: #3DDC97; }
.hero-name {
    font-family: 'Syne', sans-serif; font-size: 3.6rem; font-weight: 800;
    line-height: 1.05; color: #fff; margin-bottom: .4rem;
}
.neon-g {
    background: linear-gradient(90deg, #3DDC97, #00D4FF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-role {
    font-family: 'Syne', sans-serif; font-size: 1.4rem;
    font-weight: 600; color: #94a3b8; margin-bottom: .8rem;
}
.hero-tagline {
    font-size: 1rem; color: #64748b; line-height: 1.7;
    margin-bottom: 1.8rem; font-style: italic;
    border-left: 2px solid #3DDC97; padding-left: 1rem;
    max-width: 420px;
}
.hero-btns { display: flex; gap: .8rem; flex-wrap: wrap; margin-bottom: 2rem; }
.btn-g {
    padding: .55rem 1.4rem; border-radius: 8px; font-size: .84rem;
    font-weight: 700; text-decoration: none; transition: all .25s;
    display: inline-flex; align-items: center; gap: .4rem;
    background: linear-gradient(135deg, #3DDC97, #00D4FF);
    color: #030712; box-shadow: 0 0 20px rgba(61,220,151,.4);
}
.btn-g:hover { box-shadow: 0 0 35px rgba(61,220,151,.7); transform: translateY(-2px); }
.btn-o {
    padding: .55rem 1.4rem; border-radius: 8px; font-size: .84rem;
    font-weight: 700; text-decoration: none; transition: all .25s;
    display: inline-flex; align-items: center; gap: .4rem;
    background: transparent; color: #fff;
    border: 1px solid rgba(255,255,255,.2);
}
.btn-o:hover { border-color: #3DDC97; color: #3DDC97; background: rgba(61,220,151,.07); }
 
.stat-row { display: flex; gap: 1.2rem; align-items: center; flex-wrap: wrap; }
.stat-item { text-align: center; }
.stat-num {
    font-family: 'Syne', sans-serif; font-size: 1.7rem; font-weight: 800;
    background: linear-gradient(135deg, #3DDC97, #00D4FF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.stat-label { font-size: .67rem; color: #475569; font-family: 'DM Mono', monospace; letter-spacing: 1px; }
.stat-div { width: 1px; height: 32px; background: rgba(255,255,255,.08); }
 
/* PHOTO */
.photo-wrap { display: flex; justify-content: center; align-items: center; position: relative; }
.photo-glow {
    position: absolute; width: 300px; height: 300px; border-radius: 50%;
    background: radial-gradient(circle, rgba(61,220,151,.12), transparent 70%);
    pointer-events: none;
}
.photo-glow2 {
    position: absolute; width: 380px; height: 380px; border-radius: 50%;
    background: radial-gradient(circle, rgba(0,212,255,.07), transparent 70%);
    pointer-events: none;
}
.photo-container { position: relative; width: 300px; height: 300px; display: flex; align-items: center; justify-content: center; }
.ring { position: absolute; border-radius: 50%; border: 1px solid transparent; animation: spin linear infinite; }
.r1 { width: 300px; height: 300px; border-color: rgba(61,220,151,.3); border-top-color: #3DDC97; animation-duration: 8s; }
.r2 { width: 262px; height: 262px; border-color: rgba(0,212,255,.2); border-right-color: #00D4FF; animation-duration: 12s; animation-direction: reverse; }
.r3 { width: 334px; height: 334px; border-color: rgba(189,0,255,.1); border-bottom-color: rgba(189,0,255,.4); animation-duration: 20s; }
@keyframes spin { to { transform: rotate(360deg); } }
.photo-inner {
    width: 218px; height: 218px; border-radius: 50%;
    background: linear-gradient(135deg, #0d1f2d, #1a0533);
    border: 2px solid rgba(61,220,151,.3);
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
    box-shadow: 0 0 40px rgba(61,220,151,.15), inset 0 0 40px rgba(0,0,0,.5);
}
.photo-inner img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
.photo-placeholder { font-size: 4rem; filter: drop-shadow(0 0 12px #3DDC97); }
 
/* ABOUT */
.about-text {
    font-size: .95rem; color: #94a3b8; line-height: 1.9;
    background: rgba(255,255,255,.02); border: 1px solid rgba(255,255,255,.06);
    border-radius: 14px; padding: 1.8rem; position: relative;
}
.about-text::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(#3DDC97, #BD00FF);
    border-radius: 3px 0 0 3px;
}
 
/* SKILLS */
.skills-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: .9rem; }
.skill-badge {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 13px; padding: 1.1rem .9rem; text-align: center;
    transition: all .3s; position: relative; overflow: hidden;
}
.skill-badge::before {
    content: ''; position: absolute; inset: 0; border-radius: 13px;
    background: radial-gradient(circle at 50% 0%, var(--sc) 0%, transparent 70%);
    opacity: 0; transition: opacity .3s;
}
.skill-badge:hover::before { opacity: .15; }
.skill-badge:hover {
    border-color: var(--sc);
    box-shadow: 0 0 24px color-mix(in srgb, var(--sc) 40%, transparent);
    transform: translateY(-5px);
}
.skill-icon {
    font-size: 1.9rem; margin-bottom: .5rem; display: block;
    animation: pglow 2.5s ease-in-out infinite alternate;
}
@keyframes pglow {
    0%   { filter: drop-shadow(0 0 4px var(--sc)) brightness(1); }
    100% { filter: drop-shadow(0 0 14px var(--sc)) drop-shadow(0 0 28px var(--sc)) brightness(1.2); }
}
.skill-name { font-size: .78rem; font-weight: 600; color: #e2e8f0; margin-bottom: .45rem; }
.skill-track { background: rgba(255,255,255,.07); border-radius: 20px; height: 4px; overflow: hidden; }
.skill-fill {
    height: 100%; border-radius: 20px;
    background: linear-gradient(90deg, var(--sc), color-mix(in srgb, var(--sc) 50%, #fff));
    box-shadow: 0 0 8px var(--sc);
}
.skill-pct { font-size: .62rem; color: #475569; font-family: 'DM Mono', monospace; margin-top: .28rem; }
 
/* DIVIDER */
.ndiv {
    height: 1px; max-width: 1200px; margin: 0 auto;
    background: linear-gradient(90deg, transparent, #3DDC97, #00D4FF, #BD00FF, transparent);
    opacity: .2;
}
 
/* PROJECTS */
.proj-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; }
.proj-card {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 15px; padding: 1.5rem; transition: all .35s;
    position: relative; overflow: hidden;
}
.proj-card::after {
    content: ''; position: absolute; inset: 0; border-radius: 15px;
    background: radial-gradient(circle at 30% 0%, var(--pc) 0%, transparent 65%);
    opacity: 0; transition: opacity .35s;
}
.proj-card:hover {
    border-color: var(--pc); transform: translateY(-8px) scale(1.02);
    box-shadow: 0 0 0 1px var(--pc), 0 0 40px color-mix(in srgb, var(--pc) 25%, transparent), 0 20px 60px rgba(0,0,0,.5);
}
.proj-card:hover::after { opacity: .08; }
.proj-topbar { height: 2px; margin: -1.5rem -1.5rem 1.3rem; background: var(--pc); box-shadow: 0 0 12px var(--pc); }
.proj-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: .7rem; }
.proj-emoji { font-size: 1.7rem; filter: drop-shadow(0 0 8px var(--pc)); }
.proj-impact {
    font-family: 'DM Mono', monospace; font-size: .62rem;
    padding: .18rem .55rem; border-radius: 20px;
    background: color-mix(in srgb, var(--pc) 15%, transparent);
    border: 1px solid color-mix(in srgb, var(--pc) 40%, transparent);
    color: var(--pc);
}
.proj-title { font-family: 'Syne', sans-serif; font-size: .97rem; font-weight: 700; color: #f1f5f9; margin-bottom: .5rem; }
.proj-desc { font-size: .78rem; color: #64748b; line-height: 1.7; margin-bottom: .9rem; }
.proj-tags { display: flex; flex-wrap: wrap; gap: .28rem; margin-bottom: .8rem; }
.ptag {
    font-size: .6rem; font-family: 'DM Mono', monospace;
    padding: .15rem .5rem; border-radius: 5px;
    background: rgba(255,255,255,.05); color: #94a3b8;
    border: 1px solid rgba(255,255,255,.07);
}
.proj-link a { font-size: .73rem; color: var(--pc); text-decoration: none; font-weight: 600; font-family: 'DM Mono', monospace; }
.proj-link a:hover { text-shadow: 0 0 10px var(--pc); }
 
/* TIMELINE */
.timeline { position: relative; padding-left: 2rem; }
.timeline::before {
    content: ''; position: absolute; left: 0; top: 0; bottom: 0;
    width: 1px; background: linear-gradient(#3DDC97, #BD00FF, transparent);
}
.tl-item { position: relative; margin-bottom: 2.2rem; padding-left: 1.4rem; }
.tl-dot {
    position: absolute; left: -2.42rem; top: .3rem;
    width: 11px; height: 11px; border-radius: 50%;
    background: var(--tc); box-shadow: 0 0 10px var(--tc), 0 0 20px var(--tc);
    border: 2px solid rgba(255,255,255,.15);
}
.tl-period { font-family: 'DM Mono', monospace; font-size: .65rem; color: #475569; margin-bottom: .25rem; letter-spacing: 1px; }
.tl-role { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #f1f5f9; margin-bottom: .12rem; }
.tl-company { font-size: .8rem; color: var(--tc); margin-bottom: .5rem; font-weight: 600; }
.tl-points { list-style: none; padding: 0; }
.tl-points li { font-size: .8rem; color: #64748b; margin-bottom: .25rem; padding-left: .85rem; position: relative; }
.tl-points li::before { content: '▸'; position: absolute; left: 0; color: var(--tc); font-size: .62rem; }
 
/* CERTS */
.certs-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; }
.cert-card {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 12px; padding: 1.1rem 1.2rem; transition: all .3s; position: relative; overflow: hidden;
}
.cert-card:hover {
    border-color: var(--cc);
    box-shadow: 0 0 20px color-mix(in srgb, var(--cc) 30%, transparent);
    transform: translateY(-3px);
}
.cert-card::before { content: '🏆'; position: absolute; right: .9rem; top: .9rem; font-size: 1.1rem; opacity: .18; }
.cert-name { font-size: .84rem; font-weight: 700; color: #f1f5f9; margin-bottom: .28rem; }
.cert-issuer { font-size: .73rem; color: var(--cc); margin-bottom: .18rem; font-weight: 600; }
.cert-year { font-family: 'DM Mono', monospace; font-size: .65rem; color: #475569; }
 
/* GH STATS */
.gh-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: .9rem; }
.gh-stat {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 12px; padding: 1.4rem; text-align: center; transition: all .3s;
}
.gh-stat:hover { border-color: #3DDC97; box-shadow: 0 0 20px rgba(61,220,151,.2); }
.gh-num {
    font-family: 'Syne', sans-serif; font-size: 1.9rem; font-weight: 800;
    background: linear-gradient(135deg, #3DDC97, #00D4FF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.gh-label { font-size: .7rem; color: #475569; font-family: 'DM Mono', monospace; margin-top: .28rem; }
 
/* RESUME */
.resume-box {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 16px; padding: 3rem; text-align: center; max-width: 480px; margin: 0 auto;
}
.resume-box p { color: #64748b; line-height: 1.8; margin-bottom: 1.4rem; font-size: .9rem; }
.resume-icon { font-size: 3.2rem; margin-bottom: .9rem; filter: drop-shadow(0 0 16px #3DDC97); }
 
/* FOOTER */
.footer {
    background: rgba(3,7,18,.97); border-top: 1px solid rgba(255,255,255,.06);
    padding: 2.5rem 4rem;
}
.footer-inner {
    max-width: 1200px; margin: 0 auto;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.2rem;
}
.footer-logo {
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.05rem;
    background: linear-gradient(90deg, #3DDC97, #00D4FF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.footer-sub { font-size: .72rem; color: #334155; margin-top: .18rem; font-family: 'DM Mono', monospace; }
.footer-links { display: flex; gap: .7rem; flex-wrap: wrap; }
.footer-link {
    display: flex; align-items: center; gap: .35rem;
    padding: .4rem .9rem; border-radius: 7px;
    background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.07);
    color: #94a3b8; font-size: .76rem; text-decoration: none; transition: all .22s; font-weight: 500;
}
.footer-link:hover { border-color: #3DDC97; color: #3DDC97; background: rgba(61,220,151,.07); }
.footer-copy { font-size: .68rem; color: #1e293b; font-family: 'DM Mono', monospace; margin-top: 1.2rem; text-align: center; max-width: 1200px; margin-left: auto; margin-right: auto; }
</style>
""", unsafe_allow_html=True)
 
# ── BG GRID ──
st.markdown('<div class="bg-grid"></div>', unsafe_allow_html=True)
 
# ══════════════════════════════════════════════
#  NAV — using st.button so NO new tabs ever
# ══════════════════════════════════════════════
st.markdown(f"""
<div class="nav-bar">
  <span class="nav-logo">{NAME.lower().replace(' ','.')}</span>
</div>
""", unsafe_allow_html=True)
 
# Nav buttons rendered in a tight row just below the logo bar
nav_cols = st.columns([6, 1, 1, 1])
with nav_cols[1]:
    cls = "nav-active" if PAGE == "home" else ""
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
    if st.button("01 · About", key="nav_home"):
        go("home")
    st.markdown('</div>', unsafe_allow_html=True)
 
with nav_cols[2]:
    cls = "nav-active" if PAGE == "projects" else ""
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
    if st.button("02 · Projects", key="nav_proj"):
        go("projects")
    st.markdown('</div>', unsafe_allow_html=True)
 
with nav_cols[3]:
    cls = "nav-active" if PAGE == "about3" else ""
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
    if st.button("03 · Experience", key="nav_exp"):
        go("about3")
    st.markdown('</div>', unsafe_allow_html=True)
 
 
# ── FOOTER HELPER ──
def render_footer():
    rl = f'<a href="{RESUME_URL}" target="_blank" class="footer-link">📄 Resume</a>' if RESUME_URL else ''
    st.markdown(f"""
    <div class="ndiv"></div>
    <div class="footer">
      <div class="footer-inner">
        <div>
          <div class="footer-logo">{NAME}</div>
          <div class="footer-sub">Data Analyst &middot; {EMAIL}</div>
        </div>
        <div class="footer-links">
          <a href="mailto:{EMAIL}" class="footer-link">&#9993; Email</a>
          <a href="{LINKEDIN}" target="_blank" class="footer-link">&#128279; LinkedIn</a>
          <a href="{GITHUB}" target="_blank" class="footer-link">&#128025; GitHub</a>
          {rl}
        </div>
      </div>
      <div class="footer-copy">Built with Streamlit &middot; {NAME} &copy; 2025</div>
    </div>
    """, unsafe_allow_html=True)
 
 
# ══════════════════════════════════════════════
#  PAGE 1 — ABOUT + SKILLS
# ══════════════════════════════════════════════
if PAGE == "home":
    st.markdown('<div class="page">', unsafe_allow_html=True)
 
    # Photo HTML
    photo_html = (
        f'<img src="{PHOTO_URL}" alt="{NAME}"/>'
        if PHOTO_URL
        else '<div class="photo-placeholder">&#129489;&#8205;&#128187;</div>'
    )
 
    # Build stats HTML safely
    stats_parts = []
    for i, s in enumerate(STATS):
        stats_parts.append(
            f'<div class="stat-item">'
            f'<div class="stat-num">{s["num"]}</div>'
            f'<div class="stat-label">{s["label"]}</div>'
            f'</div>'
        )
        if i < len(STATS) - 1:
            stats_parts.append('<div class="stat-div"></div>')
    stats_html = "".join(stats_parts)
 
    rl = (f'<a href="{RESUME_URL}" target="_blank" class="btn-o">&#128196; Resume</a>'
          if RESUME_URL else "")
 
    st.markdown(f"""
    <div class="hero-wrap">
      <div>
        <div class="hero-eyebrow">Available for opportunities</div>
        <div class="hero-name">Hi, I'm<br><span class="neon-g">{NAME}</span></div>
        <div class="hero-role">{ROLE}</div>
        <div class="hero-tagline">"{TAGLINE}"</div>
        <div class="hero-btns">
          <a href="#projects" class="btn-g">&#128640; View Projects</a>
          <a href="{LINKEDIN}" target="_blank" class="btn-o">&#128279; LinkedIn</a>
          {rl}
        </div>
        <div class="stat-row">{stats_html}</div>
      </div>
      <div class="photo-wrap">
        <div class="photo-glow"></div>
        <div class="photo-glow2"></div>
        <div class="photo-container">
          <div class="ring r3"></div>
          <div class="ring r1"></div>
          <div class="ring r2"></div>
          <div class="photo-inner">{photo_html}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)
 
    # ABOUT
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// who am i</div>
      <div class="sec-title">About <span>Me</span></div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="about-text">{ABOUT_TEXT}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
 
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)
 
    # SKILLS
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// what i use</div>
      <div class="sec-title">Skills &amp; <span>Tools</span></div>
      <div class="sec-sub">Hover any badge to see it glow &#10024;</div>
      <div class="skills-grid">
    """, unsafe_allow_html=True)
 
    for sk in SKILLS:
        st.markdown(
            f'<div class="skill-badge" style="--sc:{sk["color"]}">'
            f'<span class="skill-icon">{sk["icon"]}</span>'
            f'<div class="skill-name">{sk["name"]}</div>'
            f'<div class="skill-track"><div class="skill-fill" style="width:{sk["level"]}%"></div></div>'
            f'<div class="skill-pct">{sk["level"]}%</div>'
            f'</div>',
            unsafe_allow_html=True
        )
 
    st.markdown('</div></div>', unsafe_allow_html=True)
    render_footer()
    st.markdown('</div>', unsafe_allow_html=True)
 
 
# ══════════════════════════════════════════════
#  PAGE 2 — PROJECTS
# ══════════════════════════════════════════════
elif PAGE == "projects":
    st.markdown('<div class="page">', unsafe_allow_html=True)
 
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// what i've built</div>
      <div class="sec-title">My <span>Projects</span></div>
      <div class="sec-sub">Hover any card for the full neon glow &#128293;</div>
      <div class="proj-grid">
    """, unsafe_allow_html=True)
 
    for proj in PROJECTS:
        tags_html = "".join(f'<span class="ptag">{t}</span>' for t in proj["tech"])
        link_html = (
            f'<div class="proj-link"><a href="{proj["link"]}" target="_blank">&#8594; View on GitHub</a></div>'
            if proj.get("link") else ""
        )
        st.markdown(
            f'<div class="proj-card" style="--pc:{proj["color"]}">'
            f'<div class="proj-topbar"></div>'
            f'<div class="proj-header">'
            f'<span class="proj-emoji">{proj["emoji"]}</span>'
            f'<span class="proj-impact">{proj["impact"]}</span>'
            f'</div>'
            f'<div class="proj-title">{proj["title"]}</div>'
            f'<div class="proj-desc">{proj["desc"]}</div>'
            f'<div class="proj-tags">{tags_html}</div>'
            f'{link_html}'
            f'</div>',
            unsafe_allow_html=True
        )
 
    st.markdown('</div></div>', unsafe_allow_html=True)
    render_footer()
    st.markdown('</div>', unsafe_allow_html=True)
 
 
# ══════════════════════════════════════════════
#  PAGE 3 — EXPERIENCE + CERTS + GITHUB + RESUME
# ══════════════════════════════════════════════
elif PAGE == "about3":
    st.markdown('<div class="page">', unsafe_allow_html=True)
 
    # EXPERIENCE
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// where i've worked</div>
      <div class="sec-title">Work <span>Experience</span></div>
      <div class="sec-sub">My professional journey so far</div>
      <div class="timeline">
    """, unsafe_allow_html=True)
 
    for exp in EXPERIENCE:
        pts = "".join(f"<li>{p}</li>" for p in exp["points"])
        st.markdown(
            f'<div class="tl-item" style="--tc:{exp["color"]}">'
            f'<div class="tl-dot"></div>'
            f'<div class="tl-period">{exp["period"]}</div>'
            f'<div class="tl-role">{exp["role"]}</div>'
            f'<div class="tl-company">{exp["company"]}</div>'
            f'<ul class="tl-points">{pts}</ul>'
            f'</div>',
            unsafe_allow_html=True
        )
 
    st.markdown('</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)
 
    # CERTS
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// what i've earned</div>
      <div class="sec-title"><span>Certifications</span> &amp; Achievements</div>
      <div class="sec-sub">Official credentials and completed courses</div>
      <div class="certs-grid">
    """, unsafe_allow_html=True)
 
    for cert in CERTS:
        st.markdown(
            f'<div class="cert-card" style="--cc:{cert["color"]}">'
            f'<div class="cert-name">{cert["name"]}</div>'
            f'<div class="cert-issuer">{cert["issuer"]}</div>'
            f'<div class="cert-year">{cert["year"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
 
    st.markdown('</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)
 
    # GITHUB STATS
    st.markdown(f"""
    <div class="section">
      <div class="sec-eyebrow">// my github</div>
      <div class="sec-title">GitHub <span>Activity</span></div>
      <div class="sec-sub">Open source contributions and stats</div>
      <div class="gh-grid">
        <div class="gh-stat"><div class="gh-num">{GH_STATS['repos']}</div><div class="gh-label">Repositories</div></div>
        <div class="gh-stat"><div class="gh-num">{GH_STATS['stars']}</div><div class="gh-label">Stars Earned</div></div>
        <div class="gh-stat"><div class="gh-num">{GH_STATS['commits']}</div><div class="gh-label">Total Commits</div></div>
        <div class="gh-stat"><div class="gh-num">{GH_STATS['streak']}</div><div class="gh-label">Longest Streak</div></div>
      </div>
      <div style="margin-top:1.4rem;text-align:center">
        <a href="https://github.com/{GITHUB_USERNAME}" target="_blank" class="btn-o" style="display:inline-flex">&#128025; Visit GitHub Profile</a>
      </div>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)
 
    # RESUME
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// download</div>
      <div class="sec-title">My <span>Resume</span></div>
    """, unsafe_allow_html=True)
 
    if RESUME_URL:
        st.markdown(f"""
        <div class="resume-box">
          <div class="resume-icon">&#128196;</div>
          <p>My full resume with detailed work history, education, skills and achievements.</p>
          <a href="{RESUME_URL}" target="_blank" class="btn-g">&#11015; Download Resume PDF</a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="resume-box">
          <div class="resume-icon">&#128196;</div>
          <p>Resume coming soon!<br>Set the <code>RESUME_URL</code> at the top of <code>port.py</code> to add your CV link.</p>
        </div>
        """, unsafe_allow_html=True)
 
    st.markdown('</div>', unsafe_allow_html=True)
    render_footer()
    st.markdown('</div>', unsafe_allow_html=True)
