import streamlit as st
import time
from datetime import datetime
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Dhruv Puri - Elite Data Strategist",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'trainer'

# Function to load and encode image (you'll need to add your image file)
@st.cache_data
def get_base64_image(image_path):
    """Convert image to base64 string for embedding in HTML"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Custom CSS with modern design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

/* Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.main > div {
    padding-top: 0rem;
}

body {
    font-family: 'Inter', sans-serif;
    background: #0a0a0a;
    color: white;
    overflow-x: hidden;
}

/* Hide Streamlit elements */
.stDeployButton {display: none;}
footer {visibility: hidden;}
.stApp > header {visibility: hidden;}
.stMainBlockContainer {padding: 0 !important;}

/* Navigation */
.navigation {
    position: fixed;
    top: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    background: rgba(15, 15, 15, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 60px;
    padding: 8px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.nav-buttons {
    display: flex;
    gap: 8px;
}

/* Hero section */
.hero-section {
    min-height: 100vh;
    background: 
        radial-gradient(circle at 20% 50%, rgba(120, 40, 200, 0.3) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 100, 150, 0.2) 0%, transparent 50%),
        linear-gradient(135deg, #0a0a0a 0%, #1a0a1a 50%, #0a0a0a 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.hero-content {
    text-align: center;
    max-width: 900px;
    padding: 2rem;
    z-index: 2;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(3rem, 8vw, 7rem);
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #ff6b9d 50%, #c44569 100%);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
    letter-spacing: -0.02em;
    animation: gradient-animation 4s ease-in-out infinite;
}

.hero-subtitle {
    font-size: clamp(1.2rem, 3vw, 1.8rem);
    font-weight: 400;
    opacity: 0.8;
    margin-bottom: 3rem;
    line-height: 1.6;
}

@keyframes gradient-animation {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* Content sections */
.content-section {
    min-height: 100vh;
    padding: 6rem 2rem 4rem;
    background: linear-gradient(180deg, #0a0a0a 0%, #0f0f0f 100%);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.5rem, 6vw, 4rem);
    font-weight: 700;
    text-align: center;
    margin-bottom: 4rem;
    background: linear-gradient(135deg, #ffffff 0%, #ff6b9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Glass cards */
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.glass-card:hover {
    transform: translateY(-8px);
    border-color: rgba(255, 107, 157, 0.2);
    box-shadow: 0 35px 70px rgba(255, 107, 157, 0.1);
}

.glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 107, 157, 0.5), transparent);
}

/* Profile section */
.profile-grid {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 4rem;
    align-items: center;
}

@media (max-width: 768px) {
    .profile-grid {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 2rem;
    }
}

.profile-image-container {
    position: relative;
    width: 280px;
    height: 280px;
    margin: 0 auto;
}

.profile-image {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    padding: 4px;
    position: relative;
    animation: profile-glow 3s ease-in-out infinite;
}

.profile-image-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: #0a0a0a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    position: relative;
    overflow: hidden;
}

/* Replace with actual image when available */
.profile-placeholder {
    font-size: 5rem;
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

@keyframes profile-glow {
    0%, 100% { box-shadow: 0 0 30px rgba(255, 107, 157, 0.4); }
    50% { box-shadow: 0 0 50px rgba(196, 69, 105, 0.6); }
}

.profile-content h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.profile-content p {
    font-size: 1.1rem;
    line-height: 1.8;
    opacity: 0.9;
    margin-bottom: 1.5rem;
}

.highlight {
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
}

/* Stats grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.stat-card {
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.1), rgba(196, 69, 105, 0.05));
    border: 1px solid rgba(255, 107, 157, 0.2);
    border-radius: 20px;
    padding: 2.5rem 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.stat-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255, 107, 157, 0.4);
}

.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    line-height: 1;
}

.stat-label {
    font-size: 1rem;
    opacity: 0.8;
    font-weight: 500;
}

/* Skills section */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin: 2rem 0;
}

.skill-tag {
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.15), rgba(196, 69, 105, 0.1));
    border: 1px solid rgba(255, 107, 157, 0.3);
    color: white;
    padding: 1rem 2rem;
    border-radius: 50px;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.skill-tag:hover {
    transform: translateY(-3px);
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.25), rgba(196, 69, 105, 0.15));
    box-shadow: 0 15px 30px rgba(255, 107, 157, 0.2);
}

/* Program card */
.program-card {
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.05), rgba(196, 69, 105, 0.02));
    border: 1px solid rgba(255, 107, 157, 0.15);
    border-radius: 28px;
    padding: 4rem;
    margin: 3rem 0;
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
    background: linear-gradient(90deg, #ff6b9d, #c44569, #ff6b9d);
}

.program-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.program-subtitle {
    font-size: 1.2rem;
    text-align: center;
    opacity: 0.8;
    margin-bottom: 3rem;
}

.program-description {
    font-size: 1.2rem;
    line-height: 1.8;
    text-align: center;
    margin-bottom: 3rem;
    opacity: 0.9;
}

/* Features grid */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 3rem 0;
}

.feature-item {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 2rem;
    transition: all 0.3s ease;
}

.feature-item:hover {
    background: rgba(255, 107, 157, 0.05);
    border-color: rgba(255, 107, 157, 0.2);
    transform: translateY(-3px);
}

.feature-icon {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.feature-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #ff6b9d;
}

.feature-description {
    opacity: 0.8;
    line-height: 1.6;
}

/* Module cards */
.modules-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.module-card {
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.08), rgba(196, 69, 105, 0.04));
    border: 1px solid rgba(255, 107, 157, 0.2);
    border-radius: 20px;
    padding: 2.5rem;
    transition: all 0.3s ease;
}

.module-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255, 107, 157, 0.4);
}

.module-title {
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #ff6b9d;
}

.module-description {
    opacity: 0.8;
    line-height: 1.6;
}

/* CTA Button */
.cta-container {
    text-align: center;
    margin: 4rem 0;
}

.cta-button {
    display: inline-block;
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    color: white;
    text-decoration: none;
    padding: 1.2rem 3rem;
    border-radius: 60px;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(255, 107, 157, 0.3);
    position: relative;
    overflow: hidden;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 20px 40px rgba(255, 107, 157, 0.4);
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.6s;
}

.cta-button:hover::before {
    left: 100%;
}

/* Company section */
.company-info {
    text-align: center;
    padding: 3rem;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 20px;
    margin: 2rem 0;
}

.company-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.company-details {
    font-size: 1.1rem;
    opacity: 0.8;
    margin-bottom: 2rem;
    line-height: 1.6;
}

.contact-info {
    font-size: 1rem;
    opacity: 0.7;
    margin-bottom: 1rem;
}

/* Responsive design */
@media (max-width: 768px) {
    .hero-title {
        font-size: 3rem;
    }
    
    .section-title {
        font-size: 2.5rem;
    }
    
    .glass-card {
        padding: 2rem;
    }
    
    .program-card {
        padding: 2rem;
    }
    
    .features-grid {
        grid-template-columns: 1fr;
    }
    
    .modules-grid {
        grid-template-columns: 1fr;
    }
}

/* Animation classes */
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 0.8s ease-out forwards;
}

@keyframes fadeInUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.stButton > button {
    background: linear-gradient(135deg, #ff6b9d, #c44569) !important;
    color: white !important;
    border: none !important;
    border-radius: 60px !important;
    padding: 0.8rem 2rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 5px 15px rgba(255, 107, 157, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 25px rgba(255, 107, 157, 0.4) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="navigation">
    <div class="nav-buttons">
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🧠 Meet Your Trainer", key="nav_trainer", use_container_width=True):
        st.session_state.page = 'trainer'
        
with col2:
    if st.button("🚀 See Projects", key="nav_projects", use_container_width=True):
        st.session_state.page = 'projects'

st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section (always visible)
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <h1 class="hero-title">DHRUV PURI</h1>
        <p class="hero-subtitle">Elite Data Strategist • Financial Innovator • Mentor to 1000+ Professionals</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Content based on selected page
if st.session_state.page == 'trainer':
    st.markdown('<div class="content-section"><div class="container">', unsafe_allow_html=True)
    
    # Profile Section
    st.markdown(f"""
    <div class="glass-card fade-in">
        <div class="profile-grid">
            <div class="profile-image-container">
                <div class="profile-image">
                    <div class="profile-image-inner">
                        <!-- Replace this placeholder with your actual image -->
                        <div class="profile-placeholder">👨‍💼</div>
                        <!-- Uncomment and use this when you have your image -->
                        <!-- <img src="data:image/jpeg;base64,{get_base64_image('your_image_path.jpg')}" 
                             style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;"> -->
                    </div>
                </div>
            </div>
            <div class="profile-content">
                <h2>The <span class="highlight">Data Whisperer</span></h2>
                <p>
                    I've transformed <strong>1000+ professionals</strong> - from first-year students to senior managers 
                    at companies like <strong>Swiggy</strong>. My data analysis initiative achieved remarkable success, 
                    securing the <strong>4th global rank in WURI Awards</strong> worldwide.
                </p>
                <p>
                    My expertise spans <strong>Python, Excel, SQL, Power BI, and Financial Analysis</strong>. 
                    I've mastered the art of turning raw data into strategic insights that drive real business outcomes.
                </p>
                <p>
                    The genesis of this journey began during my college years when I constantly wondered: 
                    "How can I connect with working professionals from my alumni network and learn directly from them 
                    instead of taking random courses?" I always wished such a platform existed, and I wanted to solve 
                    this very problem. So here I am, with everything I've learned, ready to help you transform your career.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 2rem;">Impact Metrics</h3>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">1000+</div>
                <div class="stat-label">Students Transformed</div>
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
    
    # Skills Section
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 2rem;">Expertise Arsenal</h3>
        <div class="skills-grid">
            <div class="skill-tag">🐍 Python Mastery</div>
            <div class="skill-tag">📊 Excel Wizardry</div>
            <div class="skill-tag">🗃️ SQL Excellence</div>
            <div class="skill-tag">📈 Power BI Expertise</div>
            <div class="skill-tag">💰 Financial Analysis</div>
            <div class="skill-tag">📉 Risk Modeling</div>
            <div class="skill-tag">🤖 Data Strategy</div>
            <div class="skill-tag">📊 Quantitative Methods</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Mission Section
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 2rem;">The Mission</h3>
        <div style="text-align: center; padding: 2rem;">
            <p style="font-size: 1.4rem; line-height: 1.8; font-style: italic; opacity: 0.9; max-width: 800px; margin: 0 auto;">
                "Every corporate giant started where you are now. The difference? They had mentors who showed them the 
                shortcuts to success. I'm here to be that catalyst for you - transforming your potential into 
                unstoppable momentum in the world of data and finance."
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Company Section
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 2rem;">Company</h3>
        <div class="company-info">
            <h4 class="company-name">[Your Company Name]</h4>
            <div class="contact-info">
                <p>📍 [Your Location] | 🌐 [Your Website] | 📧 [Your Email] | 📱 [Your Phone]</p>
            </div>
            <div class="company-details">
                <p>
                    [Add your company's story here - how you're revolutionizing data education, 
                    your vision for transforming careers, and what makes your approach unique in the market. 
                    Describe your company's values, mission, and the impact you're making in the industry.]
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

elif st.session_state.page == 'projects':
    st.markdown('<div class="content-section"><div class="container">', unsafe_allow_html=True)
    
    st.markdown("""
    <h1 class="section-title">Elite Training Program</h1>
    """, unsafe_allow_html=True)
    
    # Main Program Card
    st.markdown("""
    <div class="program-card fade-in">
        <h2 class="program-title">Quantitative Strategy Development</h2>
        <p class="program-subtitle">Training for Investments in Equity Markets</p>
        <p class="program-description">
            Transform from a data enthusiast to a quantitative strategist. This comprehensive program 
            is designed for students passionate about finance, trading, and data-driven decision-making. 
            Join an exclusive cohort and master the art of systematic trading strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # What You'll Get Section
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 3rem;">🔹 What You'll Get</h3>
        <div class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">🎯</div>
                <h4 class="feature-title">Live Weekend Sessions</h4>
                <p class="feature-description">Interactive sessions led by working professionals every weekend</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">📊</div>
                <h4 class="feature-title">Premium Financial Datasets</h4>
                <p class="feature-description">Access to exclusive financial datasets worth thousands of dollars</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🎓</div>
                <h4 class="feature-title">Dual Certification</h4>
                <p class="feature-description">Two certificates - one for training completion, one for live project</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🤝</div>
                <h4 class="feature-title">Exclusive Cohort Access</h4>
                <p class="feature-description">Network with like-minded professionals and build lasting connections</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🏆</div>
                <h4 class="feature-title">Real-World Experience</h4>
                <p class="feature-description">Hands-on assignments and practical project implementation</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">👨‍🏫</div>
                <h4 class="feature-title">Personal Mentorship</h4>
                <p class="feature-description">One-on-one guidance throughout your learning journey</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Syllabus and Tools
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 3rem;">Syllabus & Tools</h3>
        <div class="skills-grid" style="margin-bottom: 3rem;">
            <div class="skill-tag">🐍 Python</div>
            <div class="skill-tag">📊 Google Sheets</div>
            <div class="skill-tag">📈 Excel</div>
            <div class="skill-tag">🤖 Macros</div>
            <div class="skill-tag">📉 Backtesting</div>
            <div class="skill-tag">💹 Strategy Development</div>
        </div>
        
        <div class="modules-grid">
            <div class="module-card">
                <h4 class="module-title">⚡ Module 1: Momentum Strategy</h4>
                <p class="module-description">
                    Development of one momentum-based strategy with comprehensive backtesting. 
                    Learn to identify market trends, optimize entry/exit points, and validate 
                    strategy performance using historical data.
                </p>
            </div>
            <div class="module-card">
                <h4 class="module-title">🎯 Module 2: Multi-Factor Strategy</h4>
                <p class="module-description">
                    Development of one multi-factor strategy incorporating various market indicators. 
                    Master advanced portfolio construction, risk management, and strategy optimization 
                    through rigorous backtesting methodologies.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Program Structure
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2.5rem; margin-bottom: 3rem;">Program Structure</h3>
        <div style="text-align: center; max-width: 800px; margin: 0 auto;">
            <div style="background: rgba(255, 107, 157, 0.1); border: 1px solid rgba(255, 107, 157, 0.2); 
                        border-radius: 20px; padding: 3rem; margin-bottom: 2rem;">
                <h4 style="color: #ff6b9d; font-size: 1.6rem; margin-bottom: 1.5rem; font-weight: 600;">
                    ⏱️ Flexible Duration
                </h4>
                <p style="font-size: 1.2rem; line-height: 1.7; opacity: 0.9; margin-bottom: 1rem;">
                    <strong>No rigid deadlines.</strong> We complete the project when it's perfect - estimated 6 months.
                </p>
                <p style="font-size: 1.1rem; opacity: 0.8; line-height: 1.6;">
                    🗓️ Live lectures every weekend<br>
                    📝 Practice worksheets for weekdays<br>
                    🎯 Complete backtesting and strategy development<br>
                    🧠 Brainstorming and validation sessions<br>
                    🏆 Final project implementation
                </p>
            </div>
            
            <div style="background: rgba(196, 69, 105, 0.1); border: 1px solid rgba(196, 69, 105, 0.2); 
                        border-radius: 20px; padding: 2rem;">
                <h4 style="color: #c44569; font-size: 1.4rem; margin-bottom: 1rem; font-weight: 600;">
                    📌 Limited Seats Available
                </h4>
                <p style="opacity: 0.8; line-height: 1.6;">
                    Open to all students passionate about finance, trading, or data-driven decision-making.
                    Join an exclusive cohort of motivated learners.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Registration CTA
    st.markdown("""
    <div class="glass-card fade-in">
        <div class="cta-container">
            <h3 style="font-size: 2rem; margin-bottom: 1.5rem; color: #ff6b9d; font-weight: 700;">
                🚀 Ready to Transform Your Future?
            </h3>
            <p style="font-size: 1.2rem; margin-bottom: 3rem; opacity: 0.9; max-width: 600px; margin-left: auto; margin-right: auto;">
                Fill out the form below if you're interested in joining this exclusive program. 
                Take the first step towards becoming a quantitative strategy expert.
            </p>
            
            <!-- Replace this URL with your actual Google Form link -->
            <a href="https://forms.google.com/your-registration-form-link" 
               target="_blank" class="cta-button">
                📝 REGISTER YOUR INTEREST
            </a>
            
            <p style="font-size: 0.9rem; opacity: 0.6; margin-top: 2rem;">
                * Please replace the Google Form URL above with your actual registration form link
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional Information
    st.markdown("""
    <div class="glass-card fade-in">
        <h3 class="section-title" style="font-size: 2rem; margin-bottom: 2rem;">Program Highlights</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎓</div>
                <h4 style="color: #ff6b9d; margin-bottom: 1rem; font-size: 1.3rem;">Comprehensive Learning</h4>
                <p style="opacity: 0.8; line-height: 1.6;">
                    From basic concepts to advanced strategy implementation, 
                    covering every aspect of quantitative finance.
                </p>
            </div>
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💼</div>
                <h4 style="color: #ff6b9d; margin-bottom: 1rem; font-size: 1.3rem;">Industry-Ready Skills</h4>
                <p style="opacity: 0.8; line-height: 1.6;">
                    Gain practical skills that are immediately applicable 
                    in real-world financial environments.
                </p>
            </div>
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🌟</div>
                <h4 style="color: #ff6b9d; margin-bottom: 1rem; font-size: 1.3rem;">Career Transformation</h4>
                <p style="opacity: 0.8; line-height: 1.6;">
                    Position yourself as a quantitative expert ready for 
                    high-impact roles in finance and data science.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

# Add smooth scrolling and animations
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all fade-in elements
    document.querySelectorAll('.fade-in').forEach(el => {
        el.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
        observer.observe(el);
    });
    
    // Add parallax effect to hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            heroSection.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });
});
</script>
""", unsafe_allow_html=True)
