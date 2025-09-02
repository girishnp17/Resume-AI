#!/usr/bin/env python3
"""
AI Resume Generator - Clean and focused implementation
"""

import gradio as gr
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from ai.resume_generator import AIResumeGenerator

class ResumeApp:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        
    def generate_resume(self, full_name, email, phone, location, linkedin, portfolio, 
                       summary, experience, education, projects, skills, certifications, job_description):
        try:
            if not self.api_key:
                return None, "❌ Gemini API key not found in .env file"
            
            generator = AIResumeGenerator(api_key=self.api_key, template_type="tech")
            
            raw_data = {
                "full_name": full_name, "email": email, "phone": phone, "location": location,
                "linkedin": linkedin, "portfolio": portfolio, "summary": summary,
                "experience": experience, "education": education, "projects": projects,
                "skills": skills, "certifications": certifications
            }
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_path = generator.generate_resume(raw_data, job_description, f"resume_{timestamp}")
            
            if pdf_path and os.path.exists(pdf_path):
                return pdf_path, "✅ Resume generated successfully!"
            else:
                return None, "❌ Resume generation failed"
                
        except Exception as e:
            return None, f"❌ Error: {str(e)}"

    def load_sample(self, sample_type):
        samples = {
            "software_engineer": (
                "Alex Johnson", "alex.johnson@email.com", "+1-555-0123", "San Francisco, CA",
                "linkedin.com/in/alexjohnson", "alexjohnson.dev",
                "Experienced software engineer with 5+ years developing scalable web applications",
                "Senior Software Engineer at TechCorp Inc.\n2022 - Present\nLed development of microservices architecture serving 1M+ users",
                "Bachelor of Science in Computer Science\nStanford University\n2019\nGPA: 3.8/4.0",
                "E-commerce Platform\nFull-stack web application with React and Node.js\nDeployed to production with 500+ users",
                "Python, JavaScript, React, Node.js, AWS, Docker, Kubernetes",
                "AWS Certified Solutions Architect\nAmazon Web Services\n2023"
            )
        }
        return samples.get(sample_type, ("",) * 12)

def create_interface():
    app = ResumeApp()
    
    with gr.Blocks(title="AI Resume Generator") as interface:
        gr.Markdown("# 🤖 AI Resume Generator")
        gr.Markdown("Create professional resumes with AI enhancement")
        
        with gr.Row():
            with gr.Column():
                full_name = gr.Textbox(label="Full Name", placeholder="John Doe")
                email = gr.Textbox(label="Email", placeholder="john.doe@email.com")
                phone = gr.Textbox(label="Phone", placeholder="+1-555-0123")
                location = gr.Textbox(label="Location", placeholder="San Francisco, CA")
                linkedin = gr.Textbox(label="LinkedIn", placeholder="linkedin.com/in/johndoe")
                portfolio = gr.Textbox(label="Portfolio", placeholder="johndoe.dev")
                summary = gr.Textbox(label="Summary", lines=3, placeholder="Professional summary...")
                
                experience = gr.Textbox(label="Experience", lines=6, 
                    placeholder="Senior Software Engineer at Company\n2022 - Present\nKey achievements...")
                education = gr.Textbox(label="Education", lines=4,
                    placeholder="Bachelor of Science\nUniversity Name\n2019")
                projects = gr.Textbox(label="Projects", lines=6,
                    placeholder="Project Name\nDescription and technologies used...")
                skills = gr.Textbox(label="Skills", lines=2,
                    placeholder="Python, JavaScript, React, AWS...")
                certifications = gr.Textbox(label="Certifications", lines=4,
                    placeholder="AWS Certified Solutions Architect\nAmazon Web Services\n2023")
                
                job_description = gr.Textbox(label="Target Job Description (Optional)", lines=8,
                    placeholder="Paste job description for AI optimization...")
            
            with gr.Column():
                sample_dropdown = gr.Dropdown(
                    choices=["", "software_engineer"], 
                    label="Load Sample Data"
                )
                load_btn = gr.Button("Load Sample")
                generate_btn = gr.Button("Generate Resume", variant="primary")
                
                status = gr.Markdown("Ready to generate resume")
                pdf_output = gr.File(label="Generated Resume", file_types=[".pdf"])
        
        # Event handlers
        load_btn.click(
            app.load_sample,
            inputs=[sample_dropdown],
            outputs=[full_name, email, phone, location, linkedin, portfolio, 
                    summary, experience, education, projects, skills, certifications]
        )
        
        generate_btn.click(
            app.generate_resume,
            inputs=[full_name, email, phone, location, linkedin, portfolio,
                   summary, experience, education, projects, skills, certifications, job_description],
            outputs=[pdf_output, status]
        )
    
    return interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(server_name="0.0.0.0", server_port=None)