import streamlit as st
 
# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Alex Mercer | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
# ─────────────────────────────────────────────
#  ✏️  EDIT YOUR INFO HERE
# ─────────────────────────────────────────────
NAME        = "Alex Mercer"
TAGLINE     = "Data Analyst · Turning raw data into real decisions"
EMAIL       = "alex.mercer@email.com"
LINKEDIN    = "https://linkedin.com/in/alexmercer"   # ← paste your LinkedIn URL
GITHUB      = "https://github.com/alexmercer"        # ← paste your GitHub URL
RESUME_URL  = ""                                     # ← paste Google Drive / Dropbox link to PDF
 
ABOUT = """
Hi! I'm Alex, a data analyst who loves digging into messy datasets and surfacing clean, 
actionable insights. I work across the full analytics stack — from wrangling data with 
PySpark and SQL to building interactive dashboards in Power BI and Tableau.
 
When I'm not querying databases, I'm probably tinkering with Python scripts or 
exploring the latest in ML tooling.
"""
 
SKILLS = [
    {"name": "Python",           "level": 90, "color": "#3DDC97"},
    {"name": "SQL",              "level": 92, "color": "#00B4D8"},
    {"name": "PySpark",          "level": 75, "color": "#F4A261"},
    {"name": "Power BI/Tableau", "level": 85, "color": "#E76F51"},
    {"name": "Excel",            "level": 88, "color": "#48CAE4"},
    {"name": "Machine Learning", "level": 65, "color": "#9B89FF"},
]
 
# ─────────────────────────────────────────────
#  ✏️  ADD / EDIT YOUR PROJECTS HERE
#  Copy-paste a new block {} to add a project
# ─────────────────────────────────────────────
PROJECTS = [
    {
        "title":       "Customer Churn Prediction",
        "emoji":       "📉",
        "color":       "#FF6B6B",       # card accent color — change freely
        "tags":        ["Python", "Scikit-learn", "SQL", "Tableau"],
        "description": "Built an end-to-end churn prediction pipeline for a telecom dataset "
                       "(50k+ customers). Reduced churn by 18% after deploying actionable "
                       "segment-level insights to the marketing team.",
        "link":        "https://github.com/alexmercer/churn-prediction",
    },
    {
        "title":       "Sales Dashboard — Power BI",
        "emoji":       "📊",
        "color":       "#FFD166",
        "tags":        ["Power BI", "SQL", "Excel"],
        "description": "Interactive regional sales dashboard with drill-down capability, "
                       "KPI cards, and automated weekly email reports. Used by 3 regional "
                       "managers daily.",
        "link":        "",              # leave empty if no link
    },
    {
        "title":       "E-Commerce Data Pipeline",
        "emoji":       "⚡",
        "color":       "#06D6A0",
        "tags":        ["PySpark", "Python", "SQL"],
        "description": "Designed and deployed a PySpark ETL pipeline processing 2M+ daily "
                       "transactions on Databricks. Reduced data latency from 6 hours to "
                       "under 30 minutes.",
        "link":        "https://github.com/alexmercer/ecom-pipeline",
    },
    {
        "title":       "HR Analytics Report",
        "emoji":       "👥",
        "color":       "#74B9FF",
        "tags":        ["Python", "Excel", "Tableau"],
        "description": "Analysed attrition patterns across departments using Python + "
                       "Tableau. Identified key drivers of attrition with a logistic "
                       "regression model (AUC 0.84).",
        "link":        "",
    },
]
 
# ─────────────────────────────────────────────
#  STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
 
/* Base */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: #0a0f1e;
    color: #cdd9f0;
}
 
/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; }
 
/* ── HERO ── */
.hero-wrap {
    background: linear-gradient(135deg, #0d1b2a 0%, #112240 50%, #0a2e1f 100%);
    border: 1px solid #1e3a5f;
    border-radius: 20px;
    padding: 3.5rem 3rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero-wrap::before {
    content: "";
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 70% 50%, rgba(0,200,120,0.08) 0%, transparent 60%),
                radial-gradient(ellipse at 20% 80%, rgba(0,140,255,0.08) 0%, transparent 55%);
    pointer-events: none;
}
.hero-name {
    font-size: 3.4rem; font-weight: 700; line-height: 1.1;
    background: linear-gradient(90deg, #3DDC97, #00B4D8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: .4rem;
}
.hero-tagline {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem; color: #7fbfdf; margin-bottom: 1.8rem;
}
.badge-row { display: flex; flex-wrap: wrap; gap: .6rem; margin-bottom: 1.8rem; }
.badge {
    font-family: 'JetBrains Mono', monospace; font-size: .75rem;
    padding: .3rem .85rem; border-radius: 20px;
    border: 1px solid #1e4d3a; background: rgba(61,220,151,.08);
    color: #3DDC97;
}
.hero-links a {
    display: inline-block; margin-right: .8rem;
    padding: .5rem 1.4rem; border-radius: 8px; font-weight: 600;
    font-size: .9rem; text-decoration: none; transition: all .2s;
}
.btn-primary { background: #3DDC97; color: #0a0f1e !important; }
.btn-primary:hover { background: #2fc484; }
.btn-outline { border: 1px solid #3DDC97; color: #3DDC97 !important; background: transparent; }
.btn-outline:hover { background: rgba(61,220,151,.12); }
 
/* ── SECTION HEADERS ── */
.section-header {
    font-size: 1.55rem; font-weight: 700; color: #e2eaf8;
    border-left: 4px solid #3DDC97;
    padding-left: .85rem; margin: 2.5rem 0 1.5rem;
}
 
/* ── ABOUT CARD ── */
.about-card {
    background: #0d1b2a; border: 1px solid #1e3a5f;
    border-radius: 14px; padding: 1.8rem 2rem; line-height: 1.85;
    font-size: 1rem; color: #b0c8e8;
}
 
/* ── PROJECT CARD ── */
.proj-card {
    background: #0d1b2a; border-radius: 14px;
    border: 1px solid #1a2f4a;
    padding: 1.6rem 1.6rem 1.4rem;
    height: 100%;
    transition: transform .2s, box-shadow .2s;
    position: relative; overflow: hidden;
}
.proj-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,.5); }
.proj-top-bar {
    height: 4px; border-radius: 4px;
    margin: -1.6rem -1.6rem 1.2rem;
}
.proj-emoji { font-size: 1.8rem; margin-bottom: .5rem; }
.proj-title { font-size: 1.1rem; font-weight: 700; color: #e2eaf8; margin-bottom: .6rem; }
.proj-desc { font-size: .88rem; color: #8faabf; line-height: 1.7; margin-bottom: 1rem; }
.tag-row { display: flex; flex-wrap: wrap; gap: .4rem; }
.tag {
    font-family: 'JetBrains Mono', monospace; font-size: .7rem;
    padding: .2rem .6rem; border-radius: 6px;
    background: rgba(255,255,255,.06); color: #90b4ce;
}
.proj-link a {
    font-size: .82rem; color: #3DDC97; text-decoration: none;
    font-weight: 600;
}
.proj-link a:hover { text-decoration: underline; }
 
/* ── SKILL BAR ── */
.skill-row { margin-bottom: 1rem; }
.skill-label {
    display: flex; justify-content: space-between;
    font-size: .9rem; margin-bottom: .35rem; color: #cdd9f0;
}
.skill-track {
    background: #162033; border-radius: 30px;
    height: 8px; overflow: hidden;
}
.skill-fill {
    height: 100%; border-radius: 30px;
    transition: width 1s ease;
}
 
/* ── CONTACT CARD ── */
.contact-card {
    background: linear-gradient(135deg, #0d1b2a, #0a2e1f);
    border: 1px solid #1e3a5f; border-radius: 14px;
    padding: 2rem; text-align: center;
}
.contact-card a {
    display: inline-block; margin: .4rem .5rem;
    color: #3DDC97; font-weight: 600; text-decoration: none;
    font-size: .95rem;
}
.contact-card a:hover { text-decoration: underline; }
 
/* ── FOOTER ── */
.footer {
    text-align: center; margin-top: 3rem;
    font-size: .78rem; color: #2e4a6a;
    font-family: 'JetBrains Mono', monospace;
}
</style>
""", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  NAV
# ─────────────────────────────────────────────
nav_cols = st.columns([1, 1, 1, 1, 1, 3])
nav_labels = ["About", "Projects", "Skills", "Resume", "Contact"]
nav_anchors = ["about", "projects", "skills", "resume", "contact"]
for i, (col, label, anchor) in enumerate(zip(nav_cols[:5], nav_labels, nav_anchors)):
    col.markdown(f"<a href='#{anchor}' style='color:#3DDC97;font-weight:600;text-decoration:none;font-size:.9rem;'>{label}</a>", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────
skill_badges = " ".join([f'<span class="badge">{s["name"]}</span>' for s in SKILLS])
resume_btn = f'<a href="{RESUME_URL}" class="btn-outline" target="_blank">📄 Resume</a>' if RESUME_URL else ""
 
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-name">{NAME}</div>
  <div class="hero-tagline">$ {TAGLINE}</div>
  <div class="badge-row">{skill_badges}</div>
  <div class="hero-links">
    <a href="mailto:{EMAIL}" class="btn-primary">✉ Get in Touch</a>
    <a href="{LINKEDIN}" target="_blank" class="btn-outline">🔗 LinkedIn</a>
    {resume_btn}
  </div>
</div>
""", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  ABOUT
# ─────────────────────────────────────────────
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">👤 About Me</div>', unsafe_allow_html=True)
st.markdown(f'<div class="about-card">{ABOUT}</div>', unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  PROJECTS
# ─────────────────────────────────────────────
st.markdown('<a name="projects"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">🚀 Projects</div>', unsafe_allow_html=True)
 
cols_per_row = 2
for i in range(0, len(PROJECTS), cols_per_row):
    row_projects = PROJECTS[i : i + cols_per_row]
    cols = st.columns(cols_per_row)
    for col, proj in zip(cols, row_projects):
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in proj["tags"]])
        link_html = f'<div class="proj-link" style="margin-top:.8rem"><a href="{proj["link"]}" target="_blank">→ View Project</a></div>' if proj.get("link") else ""
        col.markdown(f"""
        <div class="proj-card">
          <div class="proj-top-bar" style="background:{proj['color']};"></div>
          <div class="proj-emoji">{proj['emoji']}</div>
          <div class="proj-title">{proj['title']}</div>
          <div class="proj-desc">{proj['description']}</div>
          <div class="tag-row">{tags_html}</div>
          {link_html}
        </div>
        """, unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  SKILLS
# ─────────────────────────────────────────────
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">🛠 Skills & Tools</div>', unsafe_allow_html=True)
 
scol1, scol2 = st.columns(2)
half = len(SKILLS) // 2 + len(SKILLS) % 2
for col, skill_slice in zip([scol1, scol2], [SKILLS[:half], SKILLS[half:]]):
    for skill in skill_slice:
        col.markdown(f"""
        <div class="skill-row">
          <div class="skill-label"><span>{skill['name']}</span><span>{skill['level']}%</span></div>
          <div class="skill-track">
            <div class="skill-fill" style="width:{skill['level']}%;background:{skill['color']};"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  RESUME
# ─────────────────────────────────────────────
st.markdown('<a name="resume"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">📄 Resume / CV</div>', unsafe_allow_html=True)
 
if RESUME_URL:
    st.markdown(f"""
    <div class="contact-card">
      <p style="color:#b0c8e8;margin-bottom:1rem;">Download or view my full resume below.</p>
      <a href="{RESUME_URL}" target="_blank" class="btn-primary" style="padding:.6rem 1.6rem;border-radius:8px;background:#3DDC97;color:#0a0f1e;font-weight:700;text-decoration:none;">
        ⬇ Download Resume
      </a>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="contact-card">
      <p style="color:#7fbfdf;">📌 Resume coming soon — set the <code>RESUME_URL</code> variable at the top of the file to add your CV link.</p>
    </div>
    """, unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  CONTACT
# ─────────────────────────────────────────────
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">📬 Contact</div>', unsafe_allow_html=True)
 
st.markdown(f"""
<div class="contact-card">
  <p style="color:#b0c8e8;font-size:1rem;margin-bottom:1rem;">
    I'm open to freelance, full-time, and collaboration opportunities.<br>
    Feel free to reach out!
  </p>
  <a href="mailto:{EMAIL}">✉ {EMAIL}</a>
  <a href="{LINKEDIN}" target="_blank">🔗 LinkedIn</a>
  <a href="{GITHUB}" target="_blank">🐙 GitHub</a>
</div>
""", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown(f'<div class="footer">Built with Streamlit · {NAME} © 2025</div>', unsafe_allow_html=True)
