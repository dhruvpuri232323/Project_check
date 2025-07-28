import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Dhruv Puri - Data Analysis Trainer & Finance Expert",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    .nav-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .nav-button {
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 25px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .nav-button.active {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .profile-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border: 1px solid #e0e6ed;
        margin: 1rem 0;
    }
    
    .profile-image {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        border: 5px solid #667eea;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: #333;
        margin: 0.5rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #d63384;
    }
    
    .skill-tag {
        background: linear-gradient(45deg, #a8edea 0%, #fed6e3 100%);
        color: #333;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        display: inline-block;
        font-weight: 500;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .project-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .project-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .feature-list {
        background: rgba(255,255,255,0.1);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .module-card {
        background: rgba(255,255,255,0.15);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        backdrop-filter: blur(5px);
    }
    
    .company-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .highlight-text {
        background: linear-gradient(45deg, #f093fb, #f5576c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        width: 100%;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        border-top: 1px solid #eee;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'meet_trainer'

# Header
st.markdown("""
<div class="main-header">
    <h1>Dhruv Puri</h1>
    <p>Data Analysis Trainer | Finance Expert | Strategy Developer</p>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("👨‍🏫 Meet Your Trainer", key="trainer_btn", use_container_width=True):
            st.session_state.current_page = 'meet_trainer'
    with col_b:
        if st.button("🚀 See Projects", key="projects_btn", use_container_width=True):
            st.session_state.current_page = 'see_projects'

# Meet Your Trainer Page
if st.session_state.current_page == 'meet_trainer':
    st.markdown("## 👨‍🏫 Meet Your Trainer")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder for profile image
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        border-radius: 50%; margin: 0 auto; display: flex; align-items: center; justify-content: center;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                <span style="font-size: 4rem; color: white;">👨‍💼</span>
            </div>
            <h3 style="color: #667eea; margin-top: 1rem;">Upload your photo here</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats cards
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">1000+</div>
            <div>Students Taught</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">4th</div>
            <div>Global Rank - WURI Awards</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="profile-card">
            <h2 style="color: #667eea; margin-bottom: 1rem;">🎯 About Dhruv Puri</h2>
            
            <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
                I have had the privilege of teaching <strong>1000+ students</strong>, ranging from first-year students 
                to senior managers from prestigious companies like <strong>Swiggy</strong>. My journey began with 
                an initiative for teaching data analysis, which eventually achieved the 
                <strong class="highlight-text">4th Global Rank in WURI Awards</strong>.
            </p>
            
            <h3 style="color: #667eea; margin: 1.5rem 0 1rem 0;">🛠️ My Skills</h3>
            <div style="margin-bottom: 1.5rem;">
                <span class="skill-tag">🐍 Python</span>
                <span class="skill-tag">📊 Excel</span>
                <span class="skill-tag">🗃️ SQL</span>
                <span class="skill-tag">📈 Power BI</span>
                <span class="skill-tag">💰 Financial Analysis</span>
            </div>
            
            <h3 style="color: #667eea; margin: 1.5rem 0 1rem 0;">💡 My Mission</h3>
            <p style="font-size: 1.1rem; line-height: 1.6; font-style: italic; 
               background: linear-gradient(135deg, #f8f9ff 0%, #e8f2ff 100%); 
               padding: 1.5rem; border-radius: 10px; border-left: 4px solid #667eea;">
                When I was in college, I always wondered how I could connect with working professionals 
                from my alumni base and learn directly from them instead of taking random courses. 
                I always wished such a platform existed, and I wanted to solve this very problem. 
                So here I am, with everything I have learned, helping you bridge that gap and learn 
                from real industry experience.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Company Section
    st.markdown("""
    <div class="company-section">
        <h2 style="text-align: center; margin-bottom: 2rem;">🏢 Company Information</h2>
        <div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); 
                    border-radius: 15px; backdrop-filter: blur(10px);">
            <h3>Company Name: [Your Company Name Here]</h3>
            <p style="font-size: 1.1rem; margin: 1rem 0;">
                📍 Location: [Your Company Location]<br>
                🌐 Website: [Your Website URL]<br>
                📧 Email: [Your Contact Email]<br>
                📱 Phone: [Your Contact Number]
            </p>
            <p style="font-size: 1rem; line-height: 1.6;">
                [Add your company description, mission, vision, and key services here. 
                This section will showcase your company's expertise and professional background.]
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# See Projects Page
elif st.session_state.current_page == 'see_projects':
    st.markdown("## 🚀 Projects & Training Programs")
    
    st.markdown("""
    <div class="project-card">
        <div class="project-title">📈 Quantitative Strategy Development Training for Investments in Equity Markets</div>
        
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            A comprehensive program designed to teach you real-world quantitative investment strategies 
            with hands-on experience in strategy development and backtesting.
        </p>
        
        <div class="feature-list">
            <h3 style="margin-bottom: 1rem;">🔹 What You'll Get:</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
                <div>✅ Live weekend sessions by working professionals</div>
                <div>✅ Access to premium financial datasets</div>
                <div>✅ Hands-on assignments & exclusive cohort access</div>
                <div>✅ 2 certificates – one for training, one for the live project</div>
                <div>✅ Real-world project experience with mentorship</div>
                <div>✅ Practice worksheets for weekdays</div>
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
            <h3>⏱️ Program Duration & Structure</h3>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                <strong>Duration:</strong> Not bound by strict timelines - we complete the project when it's done! 
                <strong>Estimated time: 6 months</strong><br><br>
                
                <strong>Schedule:</strong><br>
                🗓️ Live lectures every weekend<br>
                📝 Practice worksheets for weekdays<br>
                🎯 Project-based learning approach<br>
                🏆 Certificate of completion upon finishing
            </p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
            <div class="module-card">
                <h4>📊 Module 1: Momentum Strategy</h4>
                <p>Development of momentum-based strategy and comprehensive backtesting</p>
            </div>
            <div class="module-card">
                <h4>📈 Module 2: Multi-Factor Strategy</h4>
                <p>Development of multi-factor strategy with advanced backtesting techniques</p>
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
            <h3>🛠️ Tools & Technologies</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
                <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;">🐍 Python</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;">📊 Google Sheets</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;">📈 Excel</span>
                <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;">🤖 Macros</span>
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
            <h3>🎯 What You'll Experience</h3>
            <ul style="font-size: 1.1rem; line-height: 1.8;">
                <li>Complete backtesting and strategy development</li>
                <li>Interactive brainstorming sessions</li>
                <li>Strategy validation techniques</li>
                <li>Real-world project implementation</li>
                <li>Professional mentorship throughout the journey</li>
                <li>Industry-standard practices and methodologies</li>
            </ul>
        </div>
        
        <div style="background: linear-gradient(45deg, #ff6b6b, #feca57); padding: 1.5rem; border-radius: 15px; 
                    text-align: center; margin: 1.5rem 0; color: white; font-weight: 600;">
            📌 Limited seats available. Open to all students passionate about finance, trading, or data-driven decision-making.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Registration Form
    st.markdown("""
    <div class="form-container">
        <h2 style="text-align: center; color: #667eea; margin-bottom: 1.5rem;">
            📝 Registration Form
        </h2>
        <p style="text-align: center; margin-bottom: 2rem; font-size: 1.1rem;">
            Fill out the form below if you are interested in joining our program!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name *", placeholder="Enter your full name")
            email = st.text_input("Email Address *", placeholder="your.email@example.com")
            phone = st.text_input("Phone Number *", placeholder="+91 XXXXX XXXXX")
            
        with col2:
            education = st.selectbox("Education Level *", 
                                   ["Select", "Undergraduate Student", "Graduate Student", 
                                    "Working Professional", "Other"])
            experience = st.selectbox("Experience with Finance/Trading", 
                                    ["Beginner", "Intermediate", "Advanced"])  
            current_role = st.text_input("Current Role/Position", 
                                       placeholder="Student/Analyst/Manager etc.")
        
        motivation = st.text_area("Why are you interested in this program? *", 
                                placeholder="Tell us about your goals and expectations...")
        
        background = st.text_area("Previous experience with Python/Excel/Data Analysis", 
                                placeholder="Briefly describe your technical background...")
        
        availability = st.selectbox("Weekend Availability", 
                                  ["Available both days", "Only Saturdays", "Only Sundays", "Limited availability"])
        
        newsletter = st.checkbox("I want to receive updates about future programs and workshops")
        terms = st.checkbox("I agree to the terms and conditions *")
        
        submitted = st.form_submit_button("🚀 Submit Application", use_container_width=True)
        
        if submitted:
            if name and email and phone and education != "Select" and motivation and terms:
                st.success("🎉 Thank you for your application! We'll get back to you within 48 hours.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

# Footer
st.markdown("""
<div class="footer">
    <p>© 2024 Dhruv Puri. All rights reserved.</p>
    <p>Built with ❤️ using Streamlit | Connect with me: 
    <a href="mailto:your.email@example.com" style="color: #667eea;">📧 Email</a> | 
    <a href="https://linkedin.com/in/yourprofile" style="color: #667eea;">💼 LinkedIn</a> | 
    <a href="https://github.com/yourprofile" style="color: #667eea;">🐱 GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)