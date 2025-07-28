import streamlit as st
import time
import json
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Advanced page configuration
st.set_page_config(
    page_title="Dhruv Puri - Elite Data Strategist",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state with advanced features
if 'page' not in st.session_state:
    st.session_state.page = 'trainer'
if 'animation_complete' not in st.session_state:
    st.session_state.animation_complete = False
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

# Advanced CSS with modern animations and glassmorphism
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.main > div {
    padding-top: 0rem;
}

body {
    background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #0c0c0c 100%);
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
}

/* Advanced hero section with particle effect */
.hero-container {
    position: relative;
    height: 100vh;
    background: radial-gradient(circle at 20% 50%, #120078 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, #ff0080 0%, transparent 50%),
                radial-gradient(circle at 40% 80%, #7928ca 0%, transparent 50%),
                linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    overflow: hidden;
}

.hero-content {
    text-align: center;
    z-index: 10;
    max-width: 800px;
    padding: 2rem;
}

.hero-title {
    font-size: clamp(3rem, 8vw, 8rem);
    font-weight: 900;
    background: linear-gradient(45deg, #ff0080, #7928ca, #00d4ff);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient-shift 3s ease-in-out infinite;
    margin-bottom: 1rem;
    text-shadow: 0 0 50px rgba(255, 0, 128, 0.3);
}

.hero-subtitle {
    font-size: clamp(1.2rem, 3vw, 2rem);
    font-weight: 300;
    opacity: 0.9;
    margin-bottom: 2rem;
    animation: fadeInUp 1s ease-out 0.5s both;
}

.floating-particles {
    position: absolute;
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.particle {
    position: absolute;
    background: linear-gradient(45deg, #ff0080, #7928ca);
    border-radius: 50%;
    animation: float 6s ease-in-out infinite;
}

@keyframes gradient-shift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.7; }
    50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Advanced navigation */
.nav-container {
    position: fixed;
    top: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 50px;
    padding: 0.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.nav-pills {
    display: flex;
    gap: 0.5rem;
}

.nav-pill {
    padding: 0.8rem 2rem;
    border-radius: 50px;
    background: transparent;
    color: white;
    border: none;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-weight: 500;
    font-size: 0.9rem;
}

.nav-pill.active {
    background: linear-gradient(45deg, #ff0080, #7928ca);
    box-shadow: 0 4px 20px rgba(255, 0, 128, 0.4);
}

.nav-pill:hover:not(.active) {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
}

/* Content sections with glassmorphism */
.content-section {
    min-height: 100vh;
    padding: 6rem 2rem 2rem;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
}

.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
    color: white;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
    border-color: rgba(255, 255, 255, 0.2);
}

.profile-section {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 3rem;
    align-items: center;
}

@media (max-width: 768px) {
    .profile-section {
        grid-template-columns: 1fr;
        text-align: center;
    }
}

.profile-image-container {
    position: relative;
    width: 250px;
    height: 250px;
    margin: 0 auto;
}

.profile-image {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(45deg, #ff0080, #7928ca, #00d4ff);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    animation: pulse-glow 2s ease-in-out infinite;
    position: relative;
    overflow: hidden;
}

.profile-image::before {
    content: '';
    position: absolute;
    inset: 3px;
    border-radius: 50%;
    background: #0a0a0a;
    z-index: 1;
}

.profile-emoji {
    position: relative;
    z-index: 2;
}

@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(255, 0, 128, 0.5); }
    50% { box-shadow: 0 0 40px rgba(121, 40, 202, 0.8); }
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.stat-card {
    background: linear-gradient(135deg, rgba(255, 0, 128, 0.1), rgba(121, 40, 202, 0.1));
    border: 1px solid rgba(255, 0, 128, 0.2);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #ff0080, transparent);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

.stat-number {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(45deg, #ff0080, #7928ca);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.9rem;
    opacity: 0.8;
    font-weight: 500;
}

.skills-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 2rem 0;
}

.skill-tag {
    background: linear-gradient(45deg, rgba(255, 0, 128, 0.2), rgba(121, 40, 202, 0.2));
    border: 1px solid rgba(255, 0, 128, 0.3);
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 50px;
    font-weight: 500;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.skill-tag:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(255, 0, 128, 0.3);
}

.cta-button {
    background: linear-gradient(45deg, #ff0080, #7928ca);
    color: white;
    border: none;
    padding: 1rem 3rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    text-decoration: none;
    display: inline-block;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(255, 0, 128, 0.4);
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s;
}

.cta-button:hover::before {
    left: 100%;
}

.program-card {
    background: linear-gradient(135deg, rgba(255, 0, 128, 0.05), rgba(121, 40, 202, 0.05));
    border: 1px solid rgba(255, 0, 128, 0.1);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    position: relative;
    overflow: hidden;
}

.program-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #ff0080, #7928ca, #00d4ff);
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.feature-item {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}

.feature-item:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 0, 128, 0.2);
}

.section-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(45deg, #ff0080, #7928ca, #00d4ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 2rem;
    text-align: center;
}

.text-gradient {
    background: linear-gradient(45deg, #ff0080, #7928ca);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
}

/* Hide Streamlit elements */
.stDeployButton {display:none;}
footer {visibility: hidden;}
.stApp > header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Create floating particles
particles_html = """
<div class="floating-particles">
""" + "".join([f'<div class="particle" style="left:{np.random.randint(0,100)}%; top:{np.random.randint(0,100)}%; width:{np.random.randint(2,8)}px; height:{np.random.randint(2,8)}px; animation-delay:{np.random.randint(0,5)}s;"></div>' for _ in range(50)]) + """
</div>
"""

# Hero Section
st.markdown(f"""
<div class="hero-container">
    {particles_html}
    <div class="hero-content">
        <h1 class="hero-title">DHRUV PURI</h1>
        <p class="hero-subtitle">Elite Data Strategist • Financial Innovator • Mentor to 1000+ Professionals</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Advanced Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("🧠 Meet Your Strategist", key="nav_trainer", use_container_width=True):
            st.session_state.page = 'trainer'
    with nav_col2:
        if st.button("🚀 Elite Programs", key="nav_projects", use_container_width=True):
            st.session_state.page = 'projects'

# Trainer Page
if st.session_state.page == 'trainer':
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Profile Section
    st.markdown("""
    <div class="glass-card">
        <div class="profile-section">
            <div class="profile-image-container">
                <div class="profile-image">
                    <span class="profile-emoji">🧠</span>
                </div>
            </div>
            <div>
                <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; color: white;">
                    The <span class="text-gradient">Data Whisperer</span>
                </h2>
                <p style="font-size: 1.2rem; line-height: 1.8; opacity: 0.9; margin-bottom: 2rem;">
                    I've cracked the code for <strong>1000+ professionals</strong> – from fresh graduates to C-suite executives at companies like <strong>Swiggy</strong>. My data analysis initiative didn't just succeed; it dominated globally, claiming the <strong>4th position in WURI Awards</strong> worldwide.
                </p>
                <p style="font-size: 1.1rem; line-height: 1.7; opacity: 0.8;">
                    Born from a simple frustration in college – "Why can't I learn directly from industry giants instead of generic courses?" – I built the bridge I wished existed. Now, I'm here with battle-tested strategies, ready to transform your data game.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section with real-time animation
    st.markdown("""
    <div class="glass-card">
        <h3 class="section-title" style="font-size: 2rem;">Impact Metrics</h3>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">1000+</div>
                <div class="stat-label">Professionals Transformed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">4th</div>
                <div class="stat-label">Global WURI Ranking</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">50+</div>
                <div class="stat-label">Fortune 500 Alumni</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">95%</div>
                <div class="stat-label">Success Rate</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills Arsenal
    st.markdown("""
    <div class="glass-card">
        <h3 class="section-title" style="font-size: 2rem;">Arsenal of Expertise</h3>
        <div class="skills-container">
            <div class="skill-tag">🐍 Python Mastery</div>
            <div class="skill-tag">📊 Excel Wizardry</div>
            <div class="skill-tag">🗃️ SQL Supremacy</div>
            <div class="skill-tag">📈 Power BI Excellence</div>
            <div class="skill-tag">💰 Financial Analysis</div>
            <div class="skill-tag">📉 Risk Modeling</div>
            <div class="skill-tag">🤖 Machine Learning</div>
            <div class="skill-tag">📊 Data Visualization</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Mission Section
    st.markdown("""
    <div class="glass-card">
        <h3 class="section-title" style="font-size: 2rem;">The Mission</h3>
        <div style="text-align: center; padding: 2rem;">
            <p style="font-size: 1.3rem; line-height: 1.8; font-style: italic; opacity: 0.9;">
                "Every corporate giant was once where you are now. The difference? 
                They had mentors who showed them the shortcuts. I'm here to be that catalyst for you – 
                turning your potential into unstoppable momentum."
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Company Section
    st.markdown("""
    <div class="glass-card">
        <h3 class="section-title" style="font-size: 2rem;">Enterprise</h3>
        <div style="text-align: center; padding: 2rem;">
            <h4 style="font-size: 1.8rem; margin-bottom: 1rem; color: white;">
                [Your Company Name]
            </h4>
            <p style="font-size: 1.1rem; opacity: 0.8; margin-bottom: 2rem;">
                📍 [Location] | 🌐 [Website] | 📧 [Email] | 📱 [Phone]
            </p>
            <p style="font-size: 1rem; line-height: 1.6; opacity: 0.7;">
                [Add your company's revolutionary story, vision, and how you're disrupting the traditional education space]
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Page
elif st.session_state.page == 'projects':
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    st.markdown("""
    <h1 class="section-title">Elite Training Programs</h1>
    """, unsafe_allow_html=True)
    
    # Main Program Card
    st.markdown("""
    <div class="program-card">
        <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1.5rem; text-align: center;">
            <span class="text-gradient">Quantitative Strategy Development</span><br>
            <span style="font-size: 1.2rem; opacity: 0.8;">Elite Training for Equity Markets</span>
        </h2>
        
        <p style="font-size: 1.2rem; line-height: 1.8; text-align: center; margin-bottom: 3rem; opacity: 0.9;">
            Transform from a data enthusiast to a quantitative strategist. This isn't just a course – 
            it's your gateway to the exclusive world of algorithmic trading and data-driven investment decisions.
        </p>
        
        <div class="feature-grid">
            <div class="feature-item">
                <h4 style="color: #ff0080; margin-bottom: 1rem;">🎯 Live Expert Sessions</h4>
                <p>Weekend sessions led by industry veterans from top-tier firms</p>
            </div>
            <div class="feature-item">
                <h4 style="color: #7928ca; margin-bottom: 1rem;">📊 Premium Data Access</h4>
                <p>Exclusive financial datasets worth $10,000+ annually</p>
            </div>
            <div class="feature-item">
                <h4 style="color: #00d4ff; margin-bottom: 1rem;">🏆 Dual Certification</h4>
                <p>Training completion + Live project implementation certificates</p>
            </div>
            <div class="feature-item">
                <h4 style="color: #ff0080; margin-bottom: 1rem;">🤝 Elite Network</h4>
                <p>Exclusive cohort access with like-minded professionals</p>
            </div>
            <div class="feature-item">
                <h4 style="color: #7928ca; margin-bottom: 1rem;">🎓 Personal Mentorship</h4>
                <p>One-on-one guidance throughout your journey</p>
            </div>
            <div class="feature-item">
                <h4 style="color: #00d4ff; margin-bottom: 1rem;">📈 Real Portfolio</h4>
                <p>Build and deploy actual strategies with real market data</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Program Structure
    st.markdown("""
    <div class="glass-card">
        <h3 class="section-title" style="font-size: 2rem;">Program Architecture</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div style="background: linear-gradient(135deg, rgba(255, 0, 128, 0.1), rgba(121, 40, 202, 0.1)); 
                        border: 1px solid rgba(255, 0, 128, 0.2); border-radius: 16px; padding: 2rem;">
                <h4 style="color: #ff0080; font-size: 1.5rem; margin-bottom: 1rem;">⚡ Module 1: Momentum Mastery</h4>
                <p style="opacity: 0.8;">Build momentum-based strategies that capture market trends with precision timing and risk management</p>
            </div>
            <div style="background: linear-gradient(135deg, rgba(121, 40, 202, 0.1), rgba(0, 212, 255, 0.1)); 
                        border: 1px solid rgba(121, 40, 202, 0.2); border-radius: 16px; padding: 2rem;">
                <h4 style="color: #7928ca; font-size: 1.5rem; margin-bottom: 1rem;">🎯 Module 2: Multi-Factor Excellence</h4>
                <p style="opacity: 0.8;">Advanced multi-factor models combining fundamental, technical, and sentiment analysis</p>
            </div>
        </div>
        
        <div style="margin-top: 3rem; text-align: center; background: rgba(255, 255, 255, 0.02); 
                    border-radius: 16px; padding: 2rem;">
            <h4 style="color: #00d4ff; font-size: 1.5rem; margin-bottom: 1rem;">⏱️ Flexible Timeline</h4>
            <p style="font-size: 1.1rem; opacity: 0.9;">
                <strong>No rigid deadlines.</strong> We complete the project when it's perfect – estimated 6 months.<br>
                🗓️ Live sessions every weekend | 📝 Practice assignments for weekdays | 🎯 Project-based learning
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tech Stack
    st.markdown("""
    <div class="glass-card">
        <h3 class="section-title" style="font-size: 2rem;">Technology Arsenal</h3>
        <div class="skills-container" style="justify-content: center;">
            <div class="skill-tag" style="font-size: 1.1rem;">🐍 Python Ecosystem</div>
            <div class="skill-tag" style="font-size: 1.1rem;">📊 Google Sheets API</div>
            <div class="skill-tag" style="font-size: 1.1rem;">📈 Advanced Excel</div>
            <div class="skill-tag" style="font-size: 1.1rem;">🤖 VBA Macros</div>
            <div class="skill-tag" style="font-size: 1.1rem;">📉 Backtesting Frameworks</div>
            <div class="skill-tag" style="font-size: 1.1rem;">🔥 Real-time Data APIs</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
    <div class="glass-card" style="text-align: center; background: linear-gradient(135deg, rgba(255, 0, 128, 0.1), rgba(121, 40, 202, 0.1));">
        <h3 style="font-size: 2rem; margin-bottom: 1rem; color: #ff0080;">⚡ Limited Elite Seats Available</h3>
        <p style="font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9;">
            Join the exclusive cohort of data-driven decision makers and quantitative strategists
        </p>
    """, unsafe_allow_html=True)
    
    # Registration link
    st.markdown("""
        <div style="margin: 2rem 0;">
            <a href="https://forms.google.com/your-form-link" target="_blank" class="cta-button">
                🚀 SECURE YOUR SPOT NOW
            </a>
        </div>
        <p style="font-size: 0.9rem; opacity: 0.7; margin-top: 1rem;">
            * Replace the Google Form link above with your actual registration form
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Advanced JavaScript for interactions
st.markdown("""
<script>
// Smooth scrolling and advanced interactions
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // Intersection Observer for animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    
    // Observe all cards
    document.querySelectorAll('.glass-card, .program-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });
});
</script>
""", unsafe_allow_html=True)
