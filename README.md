# 🤖 AI Resume Generator

**Refined Workflow: Raw JSON → Gemini Enhancement → LaTeX → PDF**

A streamlined AI-powered resume generator that creates professional, ATS-optimized resumes using Google's Gemini AI and LaTeX templates.

## 🚀 Features

- **AI-Powered Enhancement**: Single Gemini prompt optimizes for both ATS and HR
- **Professional LaTeX Templates**: 4 high-quality templates (Modern, Tech, Academic, Executive)
- **ATS Optimization**: Keyword-rich, structured content that passes applicant tracking systems
- **HR Optimization**: Compelling, results-focused content that impresses recruiters
- **Job Targeting**: Tailors resumes to specific job descriptions
- **Clean Architecture**: Separated prompts, templates, and core logic

## 📁 Project Structure

```
Resume-ai/
├── demo.py                    # Main demo script
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── resume_env/               # Python virtual environment
└── src/
    ├── ai/
    │   ├── resume_generator.py    # Core AI resume generator
    │   └── sample_data.py         # Sample data for testing
    ├── prompts/
    │   └── enhancement_prompts.py # AI enhancement prompts
    └── templates/
        └── latex_templates.py     # Professional LaTeX templates
```

## 🛠️ Setup

1. **Activate Environment**:
   ```bash
   source resume_env/bin/activate
   ```

2. **Set API Key**:
   ```bash
   export GEMINI_API_KEY="your_gemini_api_key_here"
   ```

3. **Run Demo**:
   ```bash
   python demo.py
   ```

## 🎯 Refined Workflow

### Step 1: Collect User Data
Raw resume data in JSON format with basic information.

### Step 2: Gemini Enhancement (ATS + HR Combined)
Single powerful AI prompt that:
- Optimizes keywords for ATS systems
- Enhances content for human recruiters
- Quantifies achievements with metrics
- Uses strong action verbs
- Maintains JSON structure

### Step 3: Map JSON → LaTeX Template
Enhanced data is mapped to professional LaTeX templates with:
- Clean, ATS-friendly formatting
- Visual appeal for HR review
- Consistent professional styling

### Step 4: Generate PDF Resume
LaTeX compilation produces final PDF that is:
- ATS-passable (structured text, keywords)
- HR-attractive (well-formatted, impactful)

## 📋 Available Templates

1. **Modern Professional** - Best for Tech/Business roles
2. **Minimal Tech** - Best for Software Engineering roles  
3. **Clean Academic** - Best for Academic/Research roles
4. **Executive** - Best for Senior/Executive roles

## 📊 Sample Profiles

- **Software Engineer** - Full-stack developer with 5+ years experience
- **Data Scientist** - ML expert with statistical analysis background
- **Marketing Manager** - Digital marketing professional with growth track record

## 🧪 Testing

The demo script offers two modes:
1. **Full Demo** - Complete workflow with sample data
2. **Component Testing** - Test individual AI components

## 🎨 Usage Example

```python
from src.ai.resume_generator import AIResumeGenerator

# Initialize generator
generator = AIResumeGenerator(
    api_key="your_api_key",
    template_type="modern"
)

# Raw resume data
raw_data = {
    "full_name": "John Doe",
    "email": "john@example.com",
    # ... more fields
}

# Generate enhanced resume
pdf_path = generator.generate_resume(
    raw_data=raw_data,
    job_description="Optional job description for targeting",
    output_name="john_doe_resume"
)
```

## 🔧 Dependencies

- `google-generativeai` - Gemini AI integration
- LaTeX distribution (texlive-full) - PDF compilation
- Python 3.8+ - Core runtime

## 💡 Key Benefits

- **Single AI Call** - Efficient workflow with one enhancement step
- **Dual Optimization** - ATS and HR optimized in one pass
- **Professional Output** - High-quality LaTeX-generated PDFs
- **Customizable** - Multiple templates and targeting options
- **Clean Architecture** - Separated concerns for maintainability

## 🚀 Quick Start

```bash
# 1. Activate environment
source resume_env/bin/activate

# 2. Set API key
export GEMINI_API_KEY="your_key"

# 3. Run demo
./demo.py

# 4. Select template and profile
# 5. Get professional PDF resume!
```

---

**Built with ❤️ using Google Gemini AI and LaTeX**