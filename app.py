"""
GRADIEN INTERACTIVE VISUALIZER - Streamlit Version
Media Pembelajaran Matematika SMP
Materi: Menentukan Gradien Garis Lurus

Author: Yustika Berlian Cindy Aprillia
Untuk: SMP Negeri 2 Lawang, Kelas VIII-H
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import random
from fractions import Fraction

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Gradien Visualizer — Media Pembelajaran Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

/* Hide default Streamlit header/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Page background */
.stApp {
    background-color: #F4F7FF;
}

/* App header */
.app-header {
    background: linear-gradient(135deg, #3A0CA3, #4361EE);
    padding: 28px 40px 22px 40px;
    border-radius: 0 0 0 0;
    margin-bottom: 0;
}
.app-header h1 {
    color: white;
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.5px;
}
.app-header p {
    color: #A5B4FC;
    margin: 4px 0 0 0;
    font-size: 1rem;
}
.accent-stripe {
    height: 5px;
    background: linear-gradient(90deg, #F72585, #4361EE, #06D6A0);
    margin-bottom: 20px;
}

/* Nav tabs */
.stRadio > div {
    flex-direction: row;
    gap: 12px;
}
.stRadio label {
    background: #4361EE;
    color: white !important;
    padding: 10px 24px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.95rem;
    cursor: pointer;
}

/* Cards */
.card {
    background: white;
    border-radius: 14px;
    padding: 28px;
    box-shadow: 0 2px 12px rgba(67,97,238,0.08);
    margin-bottom: 18px;
}
.card-green  { background: #E8F5E9; border-left: 5px solid #16A34A; border-radius: 10px; padding: 22px 26px; margin-bottom: 20px; }
.card-orange { background: #FFF3E0; border-left: 5px solid #EA580C; border-radius: 10px; padding: 22px 26px; margin-bottom: 20px; }
.card-purple { background: #F3E5F5; border-left: 5px solid #9333EA; border-radius: 10px; padding: 22px 26px; margin-bottom: 20px; }

/* Result box */
.result-box {
    background: #EEF2FF;
    border-radius: 12px;
    padding: 22px;
    text-align: center;
}
.result-value {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 6px 0;
}
.result-desc {
    color: #64748B;
    font-size: 0.95rem;
}

/* Steps */
.step-card {
    background: white;
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 12px;
    box-shadow: 0 1px 6px rgba(0,0,0,0.07);
}
.step-badge {
    display: inline-block;
    padding: 3px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    color: white;
    margin-bottom: 8px;
}
.formula-box {
    background: #EEF2FF;
    border-radius: 8px;
    padding: 12px 20px;
    font-family: 'Courier New', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #3A0CA3;
    margin: 10px 0;
}
.conclusion-box {
    background: #ECFDF5;
    border: 1.5px solid #06D6A0;
    border-radius: 12px;
    padding: 20px 26px;
    margin-top: 16px;
}

/* Score box */
.score-box {
    background: #4361EE;
    color: white;
    border-radius: 10px;
    padding: 18px;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 800;
    margin-bottom: 16px;
}

/* Review sections */
.review-header {
    background: #FFB703;
    border-radius: 12px;
    padding: 20px 30px;
    margin-bottom: 24px;
}
.review-header h2 {
    color: white;
    font-size: 1.6rem;
    font-weight: 800;
    margin: 0;
}
.section-title {
    font-size: 1.2rem;
    font-weight: 800;
    margin: 0 0 14px 0;
}
.review-content p { margin: 6px 0; line-height: 1.7; }

/* Feedback messages */
.feedback-correct {
    background: #ECFDF5;
    border: 2px solid #06D6A0;
    border-radius: 10px;
    padding: 16px 20px;
    text-align: center;
    color: #065F46;
    font-weight: 700;
    font-size: 1.1rem;
}
.feedback-wrong {
    background: #FEF2F2;
    border: 2px solid #EF233C;
    border-radius: 10px;
    padding: 16px 20px;
    text-align: center;
    color: #991B1B;
    font-weight: 700;
    font-size: 1.1rem;
}
.feedback-hint {
    background: #FFFBEB;
    border: 2px solid #FFB703;
    border-radius: 10px;
    padding: 16px 20px;
    color: #92400E;
    font-weight: 600;
}
.info-tip {
    background: #4361EE;
    color: white;
    border-radius: 10px;
    padding: 18px 24px;
    font-weight: 600;
    margin-top: 12px;
}

/* Divider */
.review-divider {
    border: none;
    border-top: 2px solid #CBD5E1;
    margin: 18px 0;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────
def fraction_str(numerator, denominator):
    if denominator == 0:
        return "tak terdefinisi"
    f = Fraction(int(round(numerator)), int(round(denominator)))
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"

def format_num(v):
    if v == int(v):
        return str(int(v))
    return f"{v:.1f}"

def build_steps(x1, y1, x2, y2):
    x1s, y1s = format_num(x1), format_num(y1)
    x2s, y2s = format_num(x2), format_num(y2)
    dx = x2 - x1
    dy = y2 - y1
    dxs, dys = format_num(dx), format_num(dy)
    steps = []

    # Langkah 1
    if x1 == 0 and y1 == 0:
        step1_lines = [
            {"type": "bullet", "text": f"Titik pertama : O(0, 0)  ← Titik pusat / origin"},
            {"type": "bullet", "text": f"Titik kedua   : ({x2s}, {y2s})"},
        ]
    else:
        step1_lines = [
            {"type": "bullet", "text": f"Titik pertama : ({x1s}, {y1s})  →  x₁ = {x1s},  y₁ = {y1s}"},
            {"type": "bullet", "text": f"Titik kedua   : ({x2s}, {y2s})  →  x₂ = {x2s},  y₂ = {y2s}"},
        ]
    steps.append({"title": "Identifikasi Koordinat Titik", "lines": step1_lines})

    # Langkah 2
    if x1 == 0 and y1 == 0:
        step2_lines = [
            {"type": "text", "text": "Karena garis melewati titik pusat O(0, 0), digunakan rumus khusus yang lebih sederhana:"},
            {"type": "formula", "text": "m  =  y / x"},
            {"type": "keterangan", "text": "di mana x dan y adalah koordinat titik kedua (selain O)"},
        ]
    else:
        step2_lines = [
            {"type": "text", "text": "Gunakan rumus gradien dua titik:"},
            {"type": "formula", "text": "m  =  (y₂ − y₁) / (x₂ − x₁)"},
            {"type": "keterangan", "text": "Rumus ini berlaku untuk semua pasang titik selama x₂ ≠ x₁"},
        ]
    steps.append({"title": "Rumus yang Digunakan", "lines": step2_lines})

    # Langkah 3
    if dx == 0:
        step3_lines = [
            {"type": "text", "text": "Masukkan nilai koordinat ke dalam rumus:"},
            {"type": "formula", "text": f"m  =  ({y2s} − {y1s}) / ({x2s} − {x1s})"},
            {"type": "formula", "text": f"m  =  {dys} / {dxs}"},
        ]
        steps.append({"title": "Substitusi Nilai", "lines": step3_lines})
        steps.append({
            "title": "Cek Penyebut (x₂ − x₁)",
            "lines": [
                {"type": "text", "text": f"Diperoleh x₂ − x₁ = {dxs}"},
                {"type": "text", "text": "⚠️ Karena penyebut = 0, gradien TIDAK TERDEFINISI. Ini adalah garis vertikal."},
            ]
        })
        return steps

    if x1 == 0 and y1 == 0:
        step3_lines = [
            {"type": "text", "text": "Masukkan koordinat titik kedua ke dalam rumus:"},
            {"type": "formula", "text": f"m  =  {y2s} / {x2s}"},
        ]
    else:
        step3_lines = [
            {"type": "text", "text": "Masukkan nilai koordinat ke dalam rumus:"},
            {"type": "formula", "text": f"m  =  ({y2s} − {y1s}) / ({x2s} − {x1s})"},
            {"type": "formula", "text": f"m  =  {dys} / {dxs}"},
        ]
    steps.append({"title": "Substitusi Nilai", "lines": step3_lines})

    # Langkah 4
    frac = Fraction(int(round(dy)), int(round(dx)))
    m_str = fraction_str(dy, dx)
    if frac.denominator == 1:
        simplify_lines = [
            {"type": "text", "text": "Bagi pembilang dan penyebut:"},
            {"type": "formula", "text": f"m  =  {dys} ÷ {dxs}  =  {m_str}"},
            {"type": "keterangan", "text": "Hasil sudah berupa bilangan bulat, tidak perlu disederhanakan lagi."},
        ]
    else:
        simplify_lines = [
            {"type": "text", "text": "Sederhanakan pecahan dengan membagi pembilang dan penyebut dengan FPB-nya:"},
            {"type": "formula", "text": f"m  =  {dys}/{dxs}  =  {m_str}"},
            {"type": "keterangan", "text": f"Pecahan {dys}/{dxs} disederhanakan menjadi {m_str} (bentuk paling sederhana)."},
        ]
    steps.append({"title": "Sederhanakan / Hitung Hasil", "lines": simplify_lines})
    return steps

def build_conclusion(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        return {
            "summary": "Gradien tidak terdefinisi  (garis vertikal)",
            "desc": "Garis vertikal tidak memiliki nilai gradien karena penyebutnya = 0.",
            "color": "#64748B"
        }
    m = Fraction(int(round(dy)), int(round(dx)))
    m_str = fraction_str(dy, dx)
    m_val = float(m)
    if m_val > 0:
        desc = "📈  Garis NAIK dari kiri ke kanan  →  gradien bernilai POSITIF"
        color = "#06D6A0"
    elif m_val < 0:
        desc = "📉  Garis TURUN dari kiri ke kanan  →  gradien bernilai NEGATIF"
        color = "#EF233C"
    else:
        desc = "➡️  Garis HORIZONTAL  →  gradien bernilai NOL"
        color = "#4361EE"
    return {"summary": f"Gradien garis  =  m  =  {m_str}", "desc": desc, "color": color}

def draw_graph(x1, y1, x2, y2, color, title="Visualisasi Garis Lurus"):
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("#FAFBFF")
    ax.set_facecolor("#F0F4FF")

    xr = max(abs(x1), abs(x2), 5) + 3
    yr = max(abs(y1), abs(y2), 5) + 3
    ax.set_xlim(-xr, xr)
    ax.set_ylim(-yr, yr)

    ax.axhline(0, color="#94A3B8", linewidth=1.2)
    ax.axvline(0, color="#94A3B8", linewidth=1.2)
    ax.grid(True, linestyle="--", linewidth=0.6, color="#CBD5E1", alpha=0.8)

    ax.plot([x1, x2], [y1, y2], color=color, linewidth=3.5,
            marker="o", markersize=11, markeredgecolor="white",
            markeredgewidth=2, zorder=4)

    bbox_props = dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor=color, linewidth=1.5, alpha=0.9)
    off = max(xr, yr) * 0.07
    ax.annotate(f"({format_num(x1)}, {format_num(y1)})",
                xy=(x1, y1), xytext=(x1 + off, y1 + off),
                fontsize=11, fontweight="bold", bbox=bbox_props, color=color)
    ax.annotate(f"({format_num(x2)}, {format_num(y2)})",
                xy=(x2, y2), xytext=(x2 + off, y2 + off),
                fontsize=11, fontweight="bold", bbox=bbox_props, color=color)

    ax.set_xlabel("x", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_ylabel("y", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_title(title, fontsize=15, fontweight="bold", color="#3A0CA3", pad=14)
    fig.tight_layout()
    return fig

def draw_empty_graph():
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("#FAFBFF")
    ax.set_facecolor("#F0F4FF")
    ax.axhline(0, color="#94A3B8", linewidth=1.2)
    ax.axvline(0, color="#94A3B8", linewidth=1.2)
    ax.grid(True, linestyle="--", linewidth=0.6, color="#CBD5E1", alpha=0.8)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel("x", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_ylabel("y", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_title("Sistem Koordinat Kartesius", fontsize=15, fontweight="bold",
                 color="#3A0CA3", pad=14)
    fig.tight_layout()
    return fig

# ─────────────────────────────────────────────
#  SESSION STATE INIT
# ─────────────────────────────────────────────
if "mode" not in st.session_state:
    st.session_state.mode = "visualizer"
if "calc_result" not in st.session_state:
    st.session_state.calc_result = None
if "show_steps" not in st.session_state:
    st.session_state.show_steps = False
if "drill_score" not in st.session_state:
    st.session_state.drill_score = 0
if "drill_total" not in st.session_state:
    st.session_state.drill_total = 0
if "drill_coords" not in st.session_state:
    st.session_state.drill_coords = None
if "drill_feedback" not in st.session_state:
    st.session_state.drill_feedback = None
if "drill_answered" not in st.session_state:
    st.session_state.drill_answered = False

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1>📐 Gradien Visualizer</h1>
    <p>Media Pembelajaran Interaktif &nbsp;·&nbsp; SMP Kelas VIII</p>
</div>
<div class="accent-stripe"></div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  NAVIGATION
# ─────────────────────────────────────────────
col_nav1, col_nav2, col_nav3, col_nav_rest = st.columns([1.4, 1.6, 1.3, 4])
with col_nav1:
    if st.button("📊  Mode Visualizer", use_container_width=True,
                 type="primary" if st.session_state.mode == "visualizer" else "secondary"):
        st.session_state.mode = "visualizer"
        st.session_state.show_steps = False
        st.rerun()
with col_nav2:
    if st.button("🎯  Mode Drill Practice", use_container_width=True,
                 type="primary" if st.session_state.mode == "drill" else "secondary"):
        st.session_state.mode = "drill"
        st.rerun()
with col_nav3:
    if st.button("📚  Review Materi", use_container_width=True,
                 type="primary" if st.session_state.mode == "review" else "secondary"):
        st.session_state.mode = "review"
        st.rerun()

st.markdown("<hr style='margin: 6px 0 20px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════
#  MODE: VISUALIZER
# ═══════════════════════════════════════════════
if st.session_state.mode == "visualizer":
    left, right = st.columns([1.1, 1.6])

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🗂️ Input Koordinat")
        st.caption("Masukkan koordinat dua titik untuk menentukan gradien.")
        st.markdown("---")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**🔴 Titik 1**")
            x1_in = st.number_input("x₁", value=0.0, step=1.0, key="x1", label_visibility="visible")
            y1_in = st.number_input("y₁", value=0.0, step=1.0, key="y1")
        with c2:
            st.markdown("**🔵 Titik 2**")
            x2_in = st.number_input("x₂", value=4.0, step=1.0, key="x2")
            y2_in = st.number_input("y₂", value=8.0, step=1.0, key="y2")

        st.markdown("---")

        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            hitung = st.button("✅ Hitung Gradien", use_container_width=True, type="primary")
        with btn_col2:
            reset = st.button("🔄 Reset", use_container_width=True)

        langkah = st.button("📋 Tampilkan Langkah-Langkah", use_container_width=True)

        if reset:
            st.session_state.calc_result = None
            st.session_state.show_steps = False
            st.rerun()

        if hitung or langkah:
            x1, y1, x2, y2 = x1_in, y1_in, x2_in, y2_in
            dx = x2 - x1
            dy = y2 - y1
            if dx == 0:
                m_str = "tak terdefinisi"
                desc = "Garis vertikal  (x₁ = x₂)"
                color = "#94A3B8"
            else:
                m_str = fraction_str(dy, dx)
                m_val = dy / dx
                if m_val > 0:
                    color = "#06D6A0"
                    desc = "📈 Garis naik · gradien positif"
                elif m_val < 0:
                    color = "#EF233C"
                    desc = "📉 Garis turun · gradien negatif"
                else:
                    color = "#4361EE"
                    desc = "➡️ Garis horizontal · gradien nol"
            st.session_state.calc_result = {
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "m_str": m_str, "desc": desc, "color": color
            }
            if langkah:
                st.session_state.show_steps = True
            st.rerun()

        # Result box
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
        if st.session_state.calc_result:
            r = st.session_state.calc_result
            st.markdown(f"""
            <div class="result-box">
                <div style="color:#64748B; font-size:0.85rem; font-weight:700; letter-spacing:1px;">HASIL GRADIEN</div>
                <div class="result-value" style="color:{r['color']}">m &nbsp;=&nbsp; {r['m_str']}</div>
                <div class="result-desc">{r['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-box">
                <div style="color:#64748B; font-size:0.85rem; font-weight:700; letter-spacing:1px;">HASIL</div>
                <div style="color:#94A3B8; font-size:1.1rem; margin:10px 0;">Masukkan koordinat<br>lalu klik Hitung Gradien</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        if st.session_state.calc_result:
            r = st.session_state.calc_result
            fig = draw_graph(r["x1"], r["y1"], r["x2"], r["y2"], r["color"])
        else:
            fig = draw_empty_graph()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    # Steps section (below)
    if st.session_state.show_steps and st.session_state.calc_result:
        r = st.session_state.calc_result
        st.markdown("---")
        st.markdown("## 📋 Langkah-Langkah Perhitungan")

        x1, y1, x2, y2 = r["x1"], r["y1"], r["x2"], r["y2"]
        x1s, y1s = format_num(x1), format_num(y1)
        x2s, y2s = format_num(x2), format_num(y2)

        # Soal card
        if x1 == 0 and y1 == 0:
            soal_text = f"Tentukan gradien garis yang melalui titik O(0, 0) dan ({x2s}, {y2s})"
        else:
            soal_text = f"Tentukan gradien garis yang melalui titik ({x1s}, {y1s}) dan ({x2s}, {y2s})"

        st.info(f"📌 **SOAL**\n\n{soal_text}")

        step_colors = ["#0284C7", "#16A34A", "#EA580C", "#9333EA", "#E91E63"]
        steps_data = build_steps(x1, y1, x2, y2)

        for i, step in enumerate(steps_data):
            color = step_colors[i % len(step_colors)]
            with st.container():
                st.markdown(f"""
                <div class="step-card" style="border-left: 5px solid {color};">
                    <span class="step-badge" style="background:{color};">Langkah {i+1}</span>
                    <strong style="font-size:1.05rem; margin-left:10px;">{step['title']}</strong>
                """, unsafe_allow_html=True)

                for line in step["lines"]:
                    ltype = line.get("type", "text")
                    if ltype == "text":
                        st.markdown(f"<p style='margin:8px 0; color:#1E293B;'>{line['text']}</p>", unsafe_allow_html=True)
                    elif ltype == "bullet":
                        st.markdown(f"<p style='margin:6px 0;'>• {line['text']}</p>", unsafe_allow_html=True)
                    elif ltype == "formula":
                        st.markdown(f"<div class='formula-box'>{line['text']}</div>", unsafe_allow_html=True)
                    elif ltype == "keterangan":
                        st.markdown(f"<p style='color:#64748B; font-style:italic; font-size:0.9rem; margin:4px 0;'>{line['text']}</p>", unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        # Conclusion
        conc = build_conclusion(x1, y1, x2, y2)
        st.markdown(f"""
        <div class="conclusion-box">
            <div style="color:#16A34A; font-weight:800; font-size:0.9rem; letter-spacing:1px;">✅  KESIMPULAN</div>
            <div style="font-size:1.3rem; font-weight:800; color:#1E293B; margin:10px 0 6px 0;">{conc['summary']}</div>
            <div style="color:#64748B;">{conc['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("❌ Tutup Langkah-Langkah"):
            st.session_state.show_steps = False
            st.rerun()

# ═══════════════════════════════════════════════
#  MODE: DRILL PRACTICE
# ═══════════════════════════════════════════════
elif st.session_state.mode == "drill":
    left, right = st.columns([1.6, 1.1])

    with right:
        # Score
        st.markdown(f"""
        <div class="score-box">
            🏆 Skor &nbsp; {st.session_state.drill_score} / {st.session_state.drill_total}
        </div>
        """, unsafe_allow_html=True)

        # Question text
        if st.session_state.drill_coords:
            x1, y1, x2, y2 = st.session_state.drill_coords
            q_num = st.session_state.drill_total + (0 if st.session_state.drill_answered else 1)
            st.markdown(f"""
            <div class="card">
                <p style="color:#4361EE; font-weight:700; font-size:0.9rem;">SOAL #{q_num}</p>
                <p style="color:#1E293B; font-size:1rem; margin-top:6px;">
                    Perhatikan grafik di sebelah kiri.<br>
                    <strong>Berapa nilai gradien garis tersebut?</strong><br>
                    <span style="color:#64748B; font-size:0.9rem;">(Tulis sebagai desimal atau pecahan, mis: -1/2)</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card" style="text-align:center; color:#64748B;">
                <p style="font-size:1.1rem;">Klik <strong>Soal Baru</strong> untuk memulai latihan! 🎯</p>
            </div>
            """, unsafe_allow_html=True)

        # Answer input
        ans_input = st.text_input("Gradien ( m ) =", placeholder="contoh: 2 atau -1/2",
                                   key="drill_ans", disabled=st.session_state.drill_answered)

        btn_r1, btn_r2 = st.columns(2)
        with btn_r1:
            new_q = st.button("🎲 Soal Baru", use_container_width=True, type="primary")
        with btn_r2:
            cek = st.button("✔ Cek Jawaban", use_container_width=True,
                            disabled=st.session_state.drill_answered or not st.session_state.drill_coords)

        hint_btn = st.button("💡 Tampilkan Koordinat", use_container_width=True)

        # Handle new question
        if new_q:
            if random.random() < 0.3:
                x1, y1 = 0, 0
                x2 = random.choice([i for i in range(-8, 9) if i != 0])
                y2 = random.randint(-8, 8)
            else:
                x1 = random.randint(-7, 7)
                y1 = random.randint(-7, 7)
                x2 = random.choice([i for i in range(-7, 8) if i != x1])
                y2 = random.randint(-7, 7)
            st.session_state.drill_coords = (x1, y1, x2, y2)
            st.session_state.drill_feedback = None
            st.session_state.drill_answered = False
            st.rerun()

        # Handle check answer
        if cek and st.session_state.drill_coords and not st.session_state.drill_answered:
            raw = ans_input.strip()
            valid = True
            user_m = None
            try:
                if "/" in raw:
                    n, d = raw.split("/")
                    user_m = float(n) / float(d)
                elif raw:
                    user_m = float(raw)
                else:
                    valid = False
            except (ValueError, ZeroDivisionError):
                valid = False

            if not valid or user_m is None:
                st.session_state.drill_feedback = {"type": "error", "text": "⚠️ Masukkan angka atau pecahan seperti -1/2"}
            else:
                x1, y1, x2, y2 = st.session_state.drill_coords
                correct = Fraction(int(round(y2 - y1)), int(round(x2 - x1)))
                correct_str = fraction_str(y2 - y1, x2 - x1)
                st.session_state.drill_total += 1
                if abs(user_m - float(correct)) < 0.0001:
                    st.session_state.drill_score += 1
                    st.session_state.drill_feedback = {"type": "correct", "text": f"✅ Benar!\n\nm = {correct_str}"}
                else:
                    st.session_state.drill_feedback = {"type": "wrong", "text": f"❌ Belum tepat.\n\nJawaban yang benar:\nm = {correct_str}"}
                st.session_state.drill_answered = True
            st.rerun()

        # Handle hint
        if hint_btn:
            if st.session_state.drill_coords:
                x1, y1, x2, y2 = st.session_state.drill_coords
                st.session_state.drill_feedback = {
                    "type": "hint",
                    "text": f"💡 Petunjuk:\n\nTitik 1 : ({format_num(x1)}, {format_num(y1)})\nTitik 2 : ({format_num(x2)}, {format_num(y2)})"
                }
                st.rerun()

        # Show feedback
        if st.session_state.drill_feedback:
            fb = st.session_state.drill_feedback
            if fb["type"] == "correct":
                st.markdown(f'<div class="feedback-correct">{fb["text"].replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
            elif fb["type"] == "wrong":
                st.markdown(f'<div class="feedback-wrong">{fb["text"].replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
            elif fb["type"] == "hint":
                st.markdown(f'<div class="feedback-hint">{fb["text"].replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
            elif fb["type"] == "error":
                st.warning(fb["text"])

    with left:
        if st.session_state.drill_coords:
            x1, y1, x2, y2 = st.session_state.drill_coords
            m_val = (y2 - y1) / (x2 - x1)
            color = "#06D6A0" if m_val > 0 else ("#EF233C" if m_val < 0 else "#4361EE")
            fig = draw_graph(x1, y1, x2, y2, color, title="Tentukan Gradien Garis Ini!")
        else:
            fig, ax = plt.subplots(figsize=(7, 6))
            fig.patch.set_facecolor("#FAFBFF")
            ax.set_facecolor("#F0F4FF")
            ax.axhline(0, color="#94A3B8", linewidth=1.2)
            ax.axvline(0, color="#94A3B8", linewidth=1.2)
            ax.grid(True, linestyle="--", linewidth=0.6, color="#CBD5E1", alpha=0.8)
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_title("Klik 'Soal Baru' untuk mulai!", fontsize=14,
                         fontweight="bold", color="#64748B", pad=12)
            fig.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

# ═══════════════════════════════════════════════
#  MODE: REVIEW MATERI
# ═══════════════════════════════════════════════
elif st.session_state.mode == "review":
    st.markdown("""
    <div class="review-header">
        <h2>📚 REVIEW MATERI - GRADIEN GARIS LURUS</h2>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 1 ──────────────────────────────
    st.markdown("""
    <div class="card-green">
        <p class="section-title" style="color:#16A34A;">1️⃣ &nbsp; GRADIEN MELALUI TITIK PUSAT</p>
        <p style="font-weight:700; color:#1E293B;">GRADIEN GARIS MELALUI TITIK PUSAT (0,0) DAN TITIK (x,y)</p>

        <p><strong>📐 Rumus:</strong></p>
        <div class="formula-box" style="background:#D1FAE5; color:#065F46;">m = y/x &nbsp;&nbsp;&nbsp; (dengan syarat x ≠ 0)</div>

        <p><strong>⚠️ Catatan Penting:</strong></p>
        <p>• Jika x = 0 (garis vertikal) → gradien <strong>TIDAK TERDEFINISI</strong><br>
           • Jika y = 0 (garis horizontal) → gradien m = 0</p>

        <hr class="review-divider">

        <p><strong>📝 CONTOH 1: Gradien Positif</strong></p>
        <p>Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (4, 8)!</p>
        <p><em>Penyelesaian:</em><br>
        Persamaan garis lurus melalui titik (0,0) dan (4,8), sehingga gradiennya adalah:</p>
        <div class="formula-box" style="background:#D1FAE5; color:#065F46;">m = y/x = 8/4 = 2</div>
        <p>✅ <strong>Kesimpulan:</strong><br>
        Didapatkan gradien positif (m = 2), artinya garis <strong>NAIK</strong> dari kiri ke kanan.</p>

        <hr class="review-divider">

        <p><strong>📝 CONTOH 2: Gradien Negatif</strong></p>
        <p>Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (6, −3)!</p>
        <p><em>Penyelesaian:</em><br>
        Persamaan garis lurus melalui titik (0,0) dan (6,−3), sehingga gradiennya adalah:</p>
        <div class="formula-box" style="background:#D1FAE5; color:#065F46;">m = y/x = -3/6 = -1/2</div>
        <p>✅ <strong>Kesimpulan:</strong><br>
        Didapatkan gradien negatif (m = −1/2), artinya garis <strong>TURUN</strong> dari kiri ke kanan, seperti jalan menurun.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 2 ──────────────────────────────
    st.markdown("""
    <div class="card-orange">
        <p class="section-title" style="color:#EA580C;">2️⃣ &nbsp; GRADIEN MELALUI DUA TITIK</p>
        <p style="font-weight:700; color:#1E293B;">GRADIEN GARIS MELALUI DUA TITIK (x₁,y₁) DAN (x₂,y₂)</p>

        <p><strong>📐 Rumus:</strong></p>
        <div class="formula-box" style="background:#FED7AA; color:#7C2D12;">m = (y₂ - y₁) / (x₂ - x₁) &nbsp;&nbsp;&nbsp; (dengan syarat x₁ ≠ x₂)</div>

        <p><strong>⚠️ Catatan Penting:</strong></p>
        <p>• Jika x₁ = x₂ (garis vertikal) → gradien <strong>TIDAK TERDEFINISI</strong></p>

        <hr class="review-divider">

        <p><strong>📝 CONTOH 1: Gradien Tidak Terdefinisi</strong></p>
        <p>Tentukan gradien garis yang melalui P(3,1) dan Q(3,5)!</p>
        <p><em>Penyelesaian:</em><br>
        Titik P(3,1) → x₁ = 3 dan y₁ = 1<br>
        Titik Q(3,5) → x₂ = 3 dan y₂ = 5<br><br>
        Gradien garis PQ sebagai berikut:</p>
        <div class="formula-box" style="background:#FED7AA; color:#7C2D12;">m = (y₂ - y₁)/(x₂ - x₁) = (5 - 1)/(3 - 3) = 4/0</div>
        <p>✅ <strong>Kesimpulan:</strong><br>
        Diperoleh x₁ dan x₂ = 0. Karena penyebut = 0, maka gradien <strong>TIDAK TERDEFINISI</strong> dan berupa <strong>GARIS VERTIKAL</strong>.</p>

        <hr class="review-divider">

        <p><strong>📝 CONTOH 2: Gradien Negatif</strong></p>
        <p>Tentukan gradien garis yang melalui P(1,4) dan Q(5,2)!</p>
        <p><em>Penyelesaian:</em><br>
        Titik P(1,4) → x₁ = 1 dan y₁ = 4<br>
        Titik Q(5,2) → x₂ = 5 dan y₂ = 2<br><br>
        Gradien garis PQ sebagai berikut:</p>
        <div class="formula-box" style="background:#FED7AA; color:#7C2D12;">m = (y₂ - y₁)/(x₂ - x₁) = (2 - 4)/(5 - 1) = -2/4 = -1/2</div>
        <p>✅ <strong>Kesimpulan:</strong><br>
        Jadi, gradien garis PQ adalah −1/2. Didapatkan gradien negatif, artinya garis <strong>TURUN</strong> dari kiri ke kanan.</p>

        <hr class="review-divider">

        <p><strong>📝 CONTOH 3: Gradien Nol</strong></p>
        <p>Tentukan gradien garis yang melalui P(2,3) dan Q(7,3)!</p>
        <p><em>Penyelesaian:</em><br>
        Titik P(2,3) → x₁ = 2 dan y₁ = 3<br>
        Titik Q(7,3) → x₂ = 7 dan y₂ = 3<br><br>
        Gradien garis PQ sebagai berikut:</p>
        <div class="formula-box" style="background:#FED7AA; color:#7C2D12;">m = (y₂ - y₁)/(x₂ - x₁) = (3 - 3)/(7 - 2) = 0/5 = 0</div>
        <p>✅ <strong>Kesimpulan:</strong><br>
        Jadi, gradien garis PQ adalah 0. Didapatkan gradien 0 dan berupa <strong>GARIS HORIZONTAL</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 3 ──────────────────────────────
    st.markdown("""
    <div class="card-purple">
        <p class="section-title" style="color:#9333EA;">3️⃣ &nbsp; INTERPRETASI &amp; TIPS</p>
        <p style="font-weight:700; color:#1E293B;">INTERPRETASI NILAI GRADIEN</p>

        <p><strong>📊 Berdasarkan Nilai m:</strong></p>
        <p>
        • <strong>m &gt; 0</strong> &nbsp;→&nbsp; Garis <strong>NAIK</strong> dari kiri ke kanan (gradien POSITIF)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<em>Contoh: m = 2, m = 1/2, m = 5</em><br><br>
        • <strong>m &lt; 0</strong> &nbsp;→&nbsp; Garis <strong>TURUN</strong> dari kiri ke kanan (gradien NEGATIF)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<em>Contoh: m = -2, m = -1/2, m = -5</em><br><br>
        • <strong>m = 0</strong> &nbsp;→&nbsp; Garis <strong>HORIZONTAL</strong> (sejajar sumbu x)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<em>Contoh: garis y = 3, y = -2</em><br><br>
        • <strong>m tidak terdefinisi</strong> &nbsp;→&nbsp; Garis <strong>VERTIKAL</strong> (sejajar sumbu y)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<em>Contoh: garis x = 2, x = -5</em>
        </p>

        <hr class="review-divider">

        <p><strong>💡 TIPS PENTING:</strong></p>
        <p>
        1. Semakin besar nilai |m|, semakin <strong>CURAM</strong> garisnya<br>
        2. Dua garis sejajar memiliki gradien yang <strong>SAMA</strong><br>
        3. Dua garis tegak lurus: m₁ × m₂ = −1<br>
        4. Untuk garis horizontal: gradien selalu 0<br>
        5. Untuk garis vertikal: gradien tidak terdefinisi
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Bottom tip ──────────────────────────────
    st.markdown("""
    <div class="info-tip">
        💡 Gunakan <strong>Mode Visualizer</strong> untuk melihat grafik dan perhitungan langkah demi langkah!<br>
        🎯 Gunakan <strong>Mode Drill Practice</strong> untuk berlatih mengerjakan soal!
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:40px; padding:20px; color:#94A3B8; font-size:0.85rem;">
    📐 Gradien Visualizer &nbsp;·&nbsp; Media Pembelajaran Matematika SMP Kelas VIII<br>
    Dibuat oleh <strong>Yustika Berlian Cindy Aprillia</strong> &nbsp;·&nbsp; SMP Negeri 2 Lawang
</div>
""", unsafe_allow_html=True)
