import streamlit as st

st.set_page_config(
    page_title="Alex Mercer | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════
#  ✏️  EDIT YOUR INFO HERE — NEVER TOUCH BELOW
# ══════════════════════════════════════════════
NAME        = "Alex Mercer"
ROLE        = "Data Analyst"
TAGLINE     = "I turn raw chaos into clean insight."
EMAIL       = "alex.mercer@email.com"
LINKEDIN    = "https://linkedin.com/in/alexmercer"
GITHUB      = "https://github.com/alexmercer"
RESUME_URL  = ""           # ← paste Google Drive / Dropbox PDF link
PHOTO_URL   = ""           # ← paste a direct image URL or leave empty

ABOUT_TEXT = """
Hi! I'm Alex — a data analyst obsessed with finding the story inside messy datasets.
I work end-to-end: SQL wrangling, PySpark pipelines, Power BI dashboards, and Python models.
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
    {"name": "Python",           "icon": "🐍", "color": "#3DDC97", "level": 90},
    {"name": "SQL",              "icon": "🗄️", "color": "#00D4FF", "level": 92},
    {"name": "PySpark",          "icon": "⚡", "color": "#FF6B35", "level": 75},
    {"name": "Power BI",         "icon": "📊", "color": "#F7C59F", "level": 85},
    {"name": "Tableau",          "icon": "📈", "color": "#FF4DFF", "level": 82},
    {"name": "Excel",            "icon": "📗", "color": "#00FF88", "level": 88},
    {"name": "Machine Learning", "icon": "🤖", "color": "#BD00FF", "level": 65},
    {"name": "DAX",              "icon": "🔢", "color": "#FF007A", "level": 78},
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
    {
        "role":    "Senior Data Analyst",
        "company": "TechCorp Solutions",
        "period":  "2022 – Present",
        "color":   "#3DDC97",
        "points":  ["Led analytics for 3 product lines", "Built enterprise Power BI ecosystem", "Mentored 2 junior analysts"],
    },
    {
        "role":    "Data Analyst",
        "company": "RetailX Analytics",
        "period":  "2020 – 2022",
        "color":   "#00D4FF",
        "points":  ["Designed ETL pipelines in PySpark", "Reduced reporting time by 60%", "Customer segmentation models"],
    },
    {
        "role":    "Junior Data Analyst",
        "company": "StartupBase",
        "period":  "2019 – 2020",
        "color":   "#FF4DFF",
        "points":  ["SQL reporting & dashboards", "A/B test analysis", "Python automation scripts"],
    },
]

# ✏️ Certifications
CERTS = [
    {"name": "Google Data Analytics",       "issuer": "Google / Coursera",   "year": "2023", "color": "#3DDC97"},
    {"name": "Microsoft Power BI Analyst",  "issuer": "Microsoft",           "year": "2022", "color": "#00D4FF"},
    {"name": "Databricks Spark Developer",  "issuer": "Databricks",          "year": "2023", "color": "#FF6B35"},
    {"name": "Tableau Desktop Specialist",  "issuer": "Tableau",             "year": "2021", "color": "#FF4DFF"},
    {"name": "SQL for Data Science",        "issuer": "UC Davis / Coursera", "year": "2020", "color": "#FFD166"},
]

# ✏️ GitHub stats (update manually)
GITHUB_USERNAME = "alexmercer"
GH_STATS = {
    "repos":   42,
    "stars":   180,
    "commits": "1.2k",
    "streak":  "47 days",
}

# ══════════════════════════════════════════════
#  PAGE ROUTING
# ══════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "home"

PAGE = st.session_state.page
params = st.query_params
if "page" in params and params["page"] != PAGE:
    st.session_state.page = params["page"]
    PAGE = params["page"]

# ══════════════════════════════════════════════
#  GLOBAL STYLES
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');

html,body,[class*="css"]{
  font-family:'Outfit',sans-serif;
  background:#030712;
  color:#e2e8f0;
  overflow-x:hidden;
}
#MainMenu,footer,header{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
section[data-testid="stMain"]>div{padding:0!important}

body::after{
  content:'';position:fixed;inset:0;
  background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.025) 2px,rgba(0,0,0,.025) 4px);
  pointer-events:none;z-index:9999;
}

.nav{
  position:fixed;top:0;left:0;right:0;z-index:1000;
  background:rgba(3,7,18,.9);backdrop-filter:blur(16px);
  border-bottom:1px solid rgba(255,255,255,.07);
  display:flex;justify-content:space-between;align-items:center;
  padding:.75rem 3rem;
}
.nav-logo{
  font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;
  background:linear-gradient(90deg,#3DDC97,#00D4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.nav-links{display:flex;gap:.3rem}
.nav-links a{
  font-size:.78rem;font-weight:500;color:#64748b;
  text-decoration:none;padding:.35rem .9rem;border-radius:6px;
  border:1px solid transparent;transition:all .2s;
}
.nav-links a:hover,.nav-links a.active{
  color:#fff;border-color:rgba(255,255,255,.12);
  background:rgba(255,255,255,.06);
}

.page{padding-top:56px;min-height:100vh}

.section{padding:5rem 4rem 4rem;max-width:1200px;margin:0 auto}

.sec-eyebrow{
  font-family:'DM Mono',monospace;font-size:.72rem;
  letter-spacing:3px;text-transform:uppercase;
  color:#3DDC97;margin-bottom:.6rem;
}
.sec-title{
  font-family:'Syne',sans-serif;font-size:2.6rem;font-weight:800;
  color:#fff;line-height:1.1;margin-bottom:.5rem;
}
.sec-title span{
  background:linear-gradient(90deg,#3DDC97,#00D4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.sec-sub{font-size:.95rem;color:#64748b;margin-bottom:3rem;max-width:500px}

/* HERO */
.hero{
  min-height:calc(100vh - 56px);
  display:grid;grid-template-columns:1fr 1fr;
  align-items:center;gap:4rem;
  padding:4rem;max-width:1200px;margin:0 auto;
}
.hero-eyebrow{
  font-family:'DM Mono',monospace;font-size:.75rem;
  letter-spacing:3px;color:#3DDC97;margin-bottom:1rem;
  display:flex;align-items:center;gap:.5rem;
}
.hero-eyebrow::before{content:'';width:30px;height:1px;background:#3DDC97}
.hero-name{
  font-family:'Syne',sans-serif;font-size:4rem;font-weight:800;
  line-height:1.05;color:#fff;margin-bottom:.5rem;
}
.neon-g{
  background:linear-gradient(90deg,#3DDC97,#00D4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.hero-role{
  font-family:'Syne',sans-serif;font-size:1.5rem;
  font-weight:600;color:#94a3b8;margin-bottom:1rem;
}
.hero-tagline{
  font-size:1.05rem;color:#64748b;line-height:1.7;
  margin-bottom:2rem;max-width:440px;
  font-style:italic;border-left:2px solid #3DDC97;padding-left:1rem;
}
.hero-btns{display:flex;gap:.8rem;flex-wrap:wrap;margin-bottom:2.5rem}
.btn-neon{
  padding:.6rem 1.5rem;border-radius:8px;font-size:.85rem;
  font-weight:600;text-decoration:none;transition:all .25s;
  display:inline-flex;align-items:center;gap:.4rem;
  font-family:'Outfit',sans-serif;
}
.btn-neon-g{
  background:linear-gradient(135deg,#3DDC97,#00D4FF);
  color:#030712;box-shadow:0 0 20px rgba(61,220,151,.4);
}
.btn-neon-g:hover{box-shadow:0 0 35px rgba(61,220,151,.7);transform:translateY(-2px)}
.btn-neon-o{
  background:transparent;color:#fff;
  border:1px solid rgba(255,255,255,.2);
}
.btn-neon-o:hover{border-color:#3DDC97;color:#3DDC97;background:rgba(61,220,151,.07)}

.stat-row{display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center}
.stat-item{text-align:center}
.stat-num{
  font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:800;
  background:linear-gradient(135deg,#3DDC97,#00D4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.stat-label{font-size:.7rem;color:#475569;font-family:'DM Mono',monospace;letter-spacing:1px}
.stat-div{width:1px;height:36px;background:rgba(255,255,255,.08)}

.hero-right{display:flex;justify-content:center;align-items:center;position:relative}
.photo-container{position:relative;width:320px;height:320px;display:flex;align-items:center;justify-content:center}
.photo-ring{position:absolute;border-radius:50%;border:1px solid transparent;animation:spin linear infinite}
.photo-ring-1{width:320px;height:320px;border-color:rgba(61,220,151,.3);border-top-color:#3DDC97;animation-duration:8s}
.photo-ring-2{width:280px;height:280px;border-color:rgba(0,212,255,.2);border-right-color:#00D4FF;animation-duration:12s;animation-direction:reverse}
.photo-ring-3{width:355px;height:355px;border-color:rgba(189,0,255,.1);border-bottom-color:rgba(189,0,255,.4);animation-duration:20s}
@keyframes spin{to{transform:rotate(360deg)}}
.photo-inner{
  width:230px;height:230px;border-radius:50%;
  background:linear-gradient(135deg,#0d1f2d,#1a0533);
  border:2px solid rgba(61,220,151,.3);
  display:flex;align-items:center;justify-content:center;
  font-size:5rem;overflow:hidden;
  box-shadow:0 0 40px rgba(61,220,151,.15),inset 0 0 40px rgba(0,0,0,.5);
}
.photo-inner img{width:100%;height:100%;object-fit:cover;border-radius:50%}
.photo-placeholder{font-size:4.5rem;filter:drop-shadow(0 0 12px #3DDC97)}

/* ABOUT */
.about-text{
  font-size:.97rem;color:#94a3b8;line-height:1.9;
  background:rgba(255,255,255,.02);
  border:1px solid rgba(255,255,255,.06);
  border-radius:14px;padding:2rem;position:relative;
}
.about-text::before{
  content:'';position:absolute;top:0;left:0;
  width:3px;height:100%;
  background:linear-gradient(#3DDC97,#BD00FF);
  border-radius:3px 0 0 3px;
}

/* SKILLS */
.skills-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.skill-badge{
  background:rgba(255,255,255,.03);
  border:1px solid rgba(255,255,255,.07);
  border-radius:14px;padding:1.2rem 1rem;text-align:center;
  transition:all .3s;cursor:default;position:relative;overflow:hidden;
}
.skill-badge::before{
  content:'';position:absolute;inset:0;border-radius:14px;
  background:radial-gradient(circle at 50% 0%,var(--sc) 0%,transparent 70%);
  opacity:0;transition:opacity .3s;
}
.skill-badge:hover::before{opacity:.15}
.skill-badge:hover{
  border-color:var(--sc);
  box-shadow:0 0 25px color-mix(in srgb,var(--sc) 40%,transparent),0 0 8px color-mix(in srgb,var(--sc) 20%,transparent);
  transform:translateY(-5px);
}
.skill-icon{
  font-size:2rem;margin-bottom:.6rem;display:block;
  filter:drop-shadow(0 0 6px var(--sc));
  animation:pulse-glow 2.5s ease-in-out infinite alternate;
}
@keyframes pulse-glow{
  0%{filter:drop-shadow(0 0 4px var(--sc)) brightness(1)}
  100%{filter:drop-shadow(0 0 14px var(--sc)) drop-shadow(0 0 28px var(--sc)) brightness(1.2)}
}
.skill-name{font-size:.8rem;font-weight:600;color:#e2e8f0;margin-bottom:.5rem}
.skill-bar-track{background:rgba(255,255,255,.07);border-radius:20px;height:4px;overflow:hidden}
.skill-bar-fill{
  height:100%;border-radius:20px;
  background:linear-gradient(90deg,var(--sc),color-mix(in srgb,var(--sc) 50%,#fff));
  box-shadow:0 0 8px var(--sc);
}
.skill-pct{font-size:.65rem;color:#475569;font-family:'DM Mono',monospace;margin-top:.3rem}

/* BG GRID */
.bg-grid{
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(61,220,151,.03) 1px,transparent 1px),
    linear-gradient(90deg,rgba(61,220,151,.03) 1px,transparent 1px);
  background-size:60px 60px;
}

/* PROJECTS */
.proj-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}
.proj-card{
  background:rgba(255,255,255,.03);
  border:1px solid rgba(255,255,255,.07);
  border-radius:16px;padding:1.6rem;
  transition:all .35s;position:relative;overflow:hidden;
}
.proj-card::after{
  content:'';position:absolute;inset:0;border-radius:16px;
  background:radial-gradient(circle at 30% 0%,var(--pc) 0%,transparent 65%);
  opacity:0;transition:opacity .35s;
}
.proj-card:hover{
  border-color:var(--pc);
  transform:translateY(-8px) scale(1.02);
  box-shadow:0 0 0 1px var(--pc),0 0 40px color-mix(in srgb,var(--pc) 25%,transparent),0 20px 60px rgba(0,0,0,.5);
}
.proj-card:hover::after{opacity:.08}
.proj-topbar{height:2px;margin:-1.6rem -1.6rem 1.4rem;background:var(--pc);box-shadow:0 0 12px var(--pc)}
.proj-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.8rem}
.proj-emoji{font-size:1.8rem;filter:drop-shadow(0 0 8px var(--pc))}
.proj-impact{
  font-family:'DM Mono',monospace;font-size:.65rem;
  padding:.2rem .6rem;border-radius:20px;
  background:color-mix(in srgb,var(--pc) 15%,transparent);
  border:1px solid color-mix(in srgb,var(--pc) 40%,transparent);
  color:var(--pc);
}
.proj-title{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:#f1f5f9;margin-bottom:.6rem}
.proj-desc{font-size:.8rem;color:#64748b;line-height:1.7;margin-bottom:1rem}
.proj-tags{display:flex;flex-wrap:wrap;gap:.3rem;margin-bottom:.9rem}
.ptag{
  font-size:.62rem;font-family:'DM Mono',monospace;
  padding:.18rem .55rem;border-radius:5px;
  background:rgba(255,255,255,.05);color:#94a3b8;
  border:1px solid rgba(255,255,255,.07);
}
.proj-link a{font-size:.75rem;color:var(--pc);text-decoration:none;font-weight:600;font-family:'DM Mono',monospace}
.proj-link a:hover{text-shadow:0 0 10px var(--pc)}

/* TIMELINE */
.timeline{position:relative;padding-left:2rem}
.timeline::before{
  content:'';position:absolute;left:0;top:0;bottom:0;
  width:1px;background:linear-gradient(#3DDC97,#BD00FF,transparent);
}
.tl-item{position:relative;margin-bottom:2.5rem;padding-left:1.5rem}
.tl-dot{
  position:absolute;left:-2.45rem;top:.35rem;
  width:12px;height:12px;border-radius:50%;
  background:var(--tc);box-shadow:0 0 12px var(--tc),0 0 24px var(--tc);
  border:2px solid rgba(255,255,255,.15);
}
.tl-period{font-family:'DM Mono',monospace;font-size:.67rem;color:#475569;margin-bottom:.3rem;letter-spacing:1px}
.tl-role{font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;color:#f1f5f9;margin-bottom:.15rem}
.tl-company{font-size:.82rem;color:var(--tc);margin-bottom:.6rem;font-weight:600}
.tl-points{list-style:none;padding:0}
.tl-points li{font-size:.82rem;color:#64748b;margin-bottom:.3rem;padding-left:.9rem;position:relative}
.tl-points li::before{content:'▸';position:absolute;left:0;color:var(--tc);font-size:.65rem}

/* CERTS */
.certs-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.cert-card{
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
  border-radius:12px;padding:1.2rem 1.3rem;transition:all .3s;position:relative;overflow:hidden;
}
.cert-card:hover{
  border-color:var(--cc);
  box-shadow:0 0 20px color-mix(in srgb,var(--cc) 30%,transparent);
  transform:translateY(-3px);
}
.cert-card::before{content:'🏆';position:absolute;right:1rem;top:1rem;font-size:1.2rem;opacity:.2}
.cert-name{font-size:.87rem;font-weight:700;color:#f1f5f9;margin-bottom:.3rem}
.cert-issuer{font-size:.75rem;color:var(--cc);margin-bottom:.2rem;font-weight:600}
.cert-year{font-family:'DM Mono',monospace;font-size:.67rem;color:#475569}

/* GH STATS */
.gh-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.gh-stat{
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
  border-radius:12px;padding:1.5rem;text-align:center;transition:all .3s;
}
.gh-stat:hover{border-color:#3DDC97;box-shadow:0 0 20px rgba(61,220,151,.2)}
.gh-stat-num{
  font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;
  background:linear-gradient(135deg,#3DDC97,#00D4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.gh-stat-label{font-size:.72rem;color:#475569;font-family:'DM Mono',monospace;margin-top:.3rem}

/* RESUME */
.resume-box{
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
  border-radius:16px;padding:3rem;text-align:center;max-width:500px;margin:0 auto;
}
.resume-box p{color:#64748b;line-height:1.8;margin-bottom:1.5rem;font-size:.92rem}
.resume-icon{font-size:3.5rem;margin-bottom:1rem;filter:drop-shadow(0 0 16px #3DDC97)}

/* FOOTER */
.footer{
  background:rgba(3,7,18,.95);border-top:1px solid rgba(255,255,255,.06);
  padding:3rem 4rem;
}
.footer-inner{
  max-width:1200px;margin:0 auto;
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1.5rem;
}
.footer-logo{
  font-family:'Syne',sans-serif;font-weight:800;font-size:1.1rem;
  background:linear-gradient(90deg,#3DDC97,#00D4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.footer-sub{font-size:.75rem;color:#334155;margin-top:.2rem;font-family:'DM Mono',monospace}
.footer-links{display:flex;gap:.8rem;flex-wrap:wrap}
.footer-link{
  display:flex;align-items:center;gap:.4rem;
  padding:.45rem 1rem;border-radius:8px;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
  color:#94a3b8;font-size:.78rem;text-decoration:none;transition:all .25s;font-weight:500;
}
.footer-link:hover{border-color:#3DDC97;color:#3DDC97;background:rgba(61,220,151,.07)}
.footer-copy{
  font-size:.7rem;color:#1e293b;font-family:'DM Mono',monospace;
  margin-top:1.5rem;text-align:center;max-width:1200px;
  margin-left:auto;margin-right:auto;
}
.neon-divider{
  height:1px;max-width:1200px;margin:0 auto;
  background:linear-gradient(90deg,transparent,#3DDC97,#00D4FF,#BD00FF,transparent);
  opacity:.25;
}
</style>
""", unsafe_allow_html=True)

# Background grid
st.markdown('<div class="bg-grid"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  NAV BAR
# ══════════════════════════════════════════════
p1 = "active" if PAGE == "home"     else ""
p2 = "active" if PAGE == "projects" else ""
p3 = "active" if PAGE == "about3"   else ""

st.markdown(f"""
<div class="nav">
  <span class="nav-logo">{NAME.lower().replace(' ','.')}</span>
  <div class="nav-links">
    <a href="?page=home"     class="{p1}">01 · About</a>
    <a href="?page=projects" class="{p2}">02 · Projects</a>
    <a href="?page=about3"   class="{p3}">03 · Experience</a>
  </div>
</div>
""", unsafe_allow_html=True)


def footer():
    rl = f'<a href="{RESUME_URL}" target="_blank" class="footer-link">📄 Resume</a>' if RESUME_URL else ''
    st.markdown(f"""
    <div class="neon-divider"></div>
    <div class="footer">
      <div class="footer-inner">
        <div>
          <div class="footer-logo">{NAME}</div>
          <div class="footer-sub">Data Analyst · {EMAIL}</div>
        </div>
        <div class="footer-links">
          <a href="mailto:{EMAIL}" class="footer-link">✉ Email</a>
          <a href="{LINKEDIN}" target="_blank" class="footer-link">🔗 LinkedIn</a>
          <a href="{GITHUB}" target="_blank" class="footer-link">🐙 GitHub</a>
          {rl}
        </div>
      </div>
      <div class="footer-copy">Built with Streamlit · {NAME} © 2025</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  PAGE 1 — ABOUT + SKILLS
# ══════════════════════════════════════════════
if PAGE == "home":
    st.markdown('<div class="page">', unsafe_allow_html=True)

    photo_html = (
        f'<img src="{PHOTO_URL}" alt="{NAME}"/>'
        if PHOTO_URL else
        '<div class="photo-placeholder">🧑‍💻</div>'
    )

    stats_html = ""
    for i, s in enumerate(STATS):
        stats_html += f'<div class="stat-item"><div class="stat-num">{s["num"]}</div><div class="stat-label">{s["label"]}</div></div>'
        if i < len(STATS) - 1:
            stats_html += '<div class="stat-div"></div>'

    rl = f'<a href="{RESUME_URL}" target="_blank" class="btn-neon btn-neon-o">📄 Resume</a>' if RESUME_URL else ''

    st.markdown(f"""
    <div class="hero">
      <div style="position:relative;z-index:1">
        <div class="hero-eyebrow">Available for opportunities</div>
        <div class="hero-name">Hi, I'm<br><span class="neon-g">{NAME}</span></div>
        <div class="hero-role">{ROLE}</div>
        <div class="hero-tagline">"{TAGLINE}"</div>
        <div class="hero-btns">
          <a href="?page=projects" class="btn-neon btn-neon-g">🚀 View Projects</a>
          <a href="{LINKEDIN}" target="_blank" class="btn-neon btn-neon-o">🔗 LinkedIn</a>
          {rl}
        </div>
        <div class="stat-row">{stats_html}</div>
      </div>
      <div class="hero-right">
        <div style="position:absolute;width:250px;height:250px;border-radius:50%;background:radial-gradient(circle,rgba(61,220,151,.1),transparent 70%);pointer-events:none"></div>
        <div style="position:absolute;width:350px;height:350px;border-radius:50%;background:radial-gradient(circle,rgba(0,212,255,.06),transparent 70%);pointer-events:none"></div>
        <div class="photo-container">
          <div class="photo-ring photo-ring-3"></div>
          <div class="photo-ring photo-ring-1"></div>
          <div class="photo-ring photo-ring-2"></div>
          <div class="photo-inner">{photo_html}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # ABOUT
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// who am i</div>
      <div class="sec-title">About <span>Me</span></div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="about-text">{ABOUT_TEXT}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # SKILLS
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// what i use</div>
      <div class="sec-title">Skills & <span>Tools</span></div>
      <div class="sec-sub">Hover any badge to see it glow ✨</div>
      <div class="skills-grid">
    """, unsafe_allow_html=True)

    for sk in SKILLS:
        st.markdown(f"""
        <div class="skill-badge" style="--sc:{sk['color']}">
          <span class="skill-icon">{sk['icon']}</span>
          <div class="skill-name">{sk['name']}</div>
          <div class="skill-bar-track">
            <div class="skill-bar-fill" style="width:{sk['level']}%"></div>
          </div>
          <div class="skill-pct">{sk['level']}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
    footer()
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
      <div class="sec-sub">Hover any card for the full neon glow 🔥</div>
      <div class="proj-grid">
    """, unsafe_allow_html=True)

    for proj in PROJECTS:
        tags_html = "".join(f'<span class="ptag">{t}</span>' for t in proj["tech"])
        link_html = (
            f'<div class="proj-link"><a href="{proj["link"]}" target="_blank">→ View on GitHub</a></div>'
            if proj.get("link") else ""
        )
        st.markdown(f"""
        <div class="proj-card" style="--pc:{proj['color']}">
          <div class="proj-topbar"></div>
          <div class="proj-header">
            <span class="proj-emoji">{proj['emoji']}</span>
            <span class="proj-impact">{proj['impact']}</span>
          </div>
          <div class="proj-title">{proj['title']}</div>
          <div class="proj-desc">{proj['desc']}</div>
          <div class="proj-tags">{tags_html}</div>
          {link_html}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
    footer()
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
        st.markdown(f"""
        <div class="tl-item" style="--tc:{exp['color']}">
          <div class="tl-dot"></div>
          <div class="tl-period">{exp['period']}</div>
          <div class="tl-role">{exp['role']}</div>
          <div class="tl-company">{exp['company']}</div>
          <ul class="tl-points">{pts}</ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # CERTS
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// what i've earned</div>
      <div class="sec-title"><span>Certifications</span> & Achievements</div>
      <div class="sec-sub">Official credentials and completed courses</div>
      <div class="certs-grid">
    """, unsafe_allow_html=True)

    for cert in CERTS:
        st.markdown(f"""
        <div class="cert-card" style="--cc:{cert['color']}">
          <div class="cert-name">{cert['name']}</div>
          <div class="cert-issuer">{cert['issuer']}</div>
          <div class="cert-year">{cert['year']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # GITHUB STATS
    st.markdown(f"""
    <div class="section">
      <div class="sec-eyebrow">// my github</div>
      <div class="sec-title">GitHub <span>Activity</span></div>
      <div class="sec-sub">Open source contributions and stats</div>
      <div class="gh-grid">
        <div class="gh-stat"><div class="gh-stat-num">{GH_STATS['repos']}</div><div class="gh-stat-label">Repositories</div></div>
        <div class="gh-stat"><div class="gh-stat-num">{GH_STATS['stars']}</div><div class="gh-stat-label">Stars Earned</div></div>
        <div class="gh-stat"><div class="gh-stat-num">{GH_STATS['commits']}</div><div class="gh-stat-label">Total Commits</div></div>
        <div class="gh-stat"><div class="gh-stat-num">{GH_STATS['streak']}</div><div class="gh-stat-label">Longest Streak</div></div>
      </div>
      <div style="margin-top:1.5rem;text-align:center">
        <a href="https://github.com/{GITHUB_USERNAME}" target="_blank" class="btn-neon btn-neon-o" style="display:inline-flex">🐙 Visit GitHub Profile</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # RESUME
    st.markdown("""
    <div class="section">
      <div class="sec-eyebrow">// download</div>
      <div class="sec-title">My <span>Resume</span></div>
    """, unsafe_allow_html=True)

    if RESUME_URL:
        st.markdown(f"""
        <div class="resume-box">
          <div class="resume-icon">📄</div>
          <p>My full resume with detailed work history, education, skills and achievements.</p>
          <a href="{RESUME_URL}" target="_blank" class="btn-neon btn-neon-g">⬇ Download Resume PDF</a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="resume-box">
          <div class="resume-icon">📄</div>
          <p>Resume coming soon!<br>Set the <code>RESUME_URL</code> variable at the top of <code>port.py</code> to add your CV link.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    footer()
    st.markdown('</div>', unsafe_allow_html=True)
