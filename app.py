import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="My Portfolio", layout="centered")

# Load images (you can replace these with your own images)
profile_pic = Image.open("Myself.jpeg")  # Replace with your own image

# Custom CSS for colorful styling
st.markdown("""
    <style>
        body {
            background-color: #007acc;
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        .header {
            text-align: center;
            padding: 20px;
        }
        .profile-pic {
            border-radius: 400%;
            width: 400px;
            margin: 0 auto;
            display: block;
        }
        .page-title {
            color: #007acc;
            text-align: center;
            padding: 20px;
        }
        .section-title {
            color: #007acc;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        a {
            color: #007acc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section-content {
            padding: 0 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
page = st.sidebar.selectbox("Navigation", ["Introduction", "Skills", "Projects", "Experience", "Publications & Certifications", "Vlogs", "Contact"])

# Introduction Page

if page == "Introduction":
    # Ensure 'profile_pic' is a correct path to your local image file
    profile_pic_path = "D:\PORTFOLIO\Myself.jpeg"  # Update this path

    # Use Markdown with HTML to control layout
    st.markdown(f"""
        <style>
            .main {{
                background-color: #E0F7FA; 
                padding: 20px;
                text-align: center;
            }}
            .header {{
                margin-bottom: 20px;
            }}
            .profile-pic {{
                margin: 20px auto;  /* Center the image */
                width: 300px;
            }}
            .profile-pic img {{
                width: 100%;  /* Ensure the image fits the container */
                
            }}
            .content {{
                font-size: 18px; 
                color: #555555;
            }}
            .intro {{
                font-size: 22px;
            }}
        </style>
        <div class='main'>
            <div class='header'><h1>My Portfolio</h1></div>
            <div class='profile-pic'>
                <img src='{profile_pic_path}' alt='Profile Picture' />
            </div>
            <h3 style='color: #4CAF50; font-weight: bold;'>Hello, I'm <span style='color: #FF5722;'>TRISHITA MUKHERJEE</span>!</h3>
            <p class='content'>
                I am a Computer Science Engineering graduate with a passion for technology, software development, and problem-solving skills. 
                I am a positive hardworker, self-learner, self-motivated person. Besides this, I am also a quick learner. I have a strong team-building capability, leadership skills.
            </p>
            <p class='intro'>
                Welcome to my portfolio where you can learn more about my skills, experience, projects, and much more.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Vlogs Page
elif page == "Vlogs":
    st.markdown("<h2 class='page-title'>Vlogs</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Check out my latest vlogs!
        - [Vlog 1: Title](https://www.youtube.com/watch?v=video1)  
          Brief description of the vlog content.
        - [Vlog 2: Title](https://www.youtube.com/watch?v=video2)  
          Brief description of the vlog content.
        - [Vlog 3: Title](https://www.youtube.com/watch?v=video3)  
          Brief description of the vlog content.
    """)

# Experience Page
elif page == "Experience":
    st.markdown("<h2 class='page-title'>Experience</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Work Experience
        **Software Developer Intern**  
        *XYZ Tech Solutions* - June 2023 to August 2023  
        - Developed and maintained web applications using Django and React.js.
        - [View Project](https://github.com/yourusername/project1)  

        **Research Assistant**  
        *ABC University* - September 2022 to May 2023  
        - Assisted in research on machine learning algorithms for data analysis.
        - [View Publication](https://www.journal.com/publication1)
    """)

# Publications Page
elif page == "Publications & Certifications":
    st.markdown("<h2 class='page-title'>Publications & Certifications</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Published Papers
        - [Paper 1: Title](https://www.journal.com/publication1)  
          Brief description of the paper.

        ### Certifications
        - [Certification 1: Title](https://www.certificate.com/cert1)  
          Issued by [Institution Name].
        - [Certification 2: Title](https://www.certificate.com/cert2)  
          Issued by [Institution Name].
    """)

# Skills Page
elif page == "Skills":
    st.markdown("<h2 class='page-title'>Skills</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Programming Languages
        - Python
        - JavaScript
        - C++
        - Java

        ### Web Development
        - HTML, CSS, JavaScript
        - React.js
        - Django, Flask

        ### Tools & Technologies
        - Git & GitHub
        - Docker
        - AWS, Azure
        - Data Structures & Algorithms
    """)

# Projects Page
elif page == "Projects":
    st.markdown("<h2 class='page-title'>Projects</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Notable Projects
        - **Project 1: Portfolio Website**  
          - Developed a personal portfolio website using HTML, CSS, and JavaScript.
          - Integrated backend services using Django.
          - [View on GitHub](https://github.com/yourusername/portfolio-website)

        - **Project 2: E-commerce Platform**  
          - Built a full-stack e-commerce platform with React.js and Flask.
          - Implemented features like user authentication, product management, and payment processing.
          - [View on GitHub](https://github.com/yourusername/ecommerce-platform)

        - **Project 3: Machine Learning Model**  
          - Created a machine learning model to predict customer churn.
          - Used Python libraries such as Pandas, NumPy, and Scikit-learn for data analysis and model building.
          - [View on GitHub](https://github.com/yourusername/ml-model)
    """)

# Contact Page
elif page == "Contact":
    st.markdown("<h2 class='page-title'>Contact</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Get in Touch
        Feel free to reach out to me via the following methods:

        - **Email:** your.email@example.com
        - **LinkedIn:** [Your LinkedIn](https://www.linkedin.com)
        - **GitHub:** [Your GitHub](https://github.com/yourusername)
    """)

# Run the app
if __name__ == "__main__":
    pass  # Optional: additional logic if needed
