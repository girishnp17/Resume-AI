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
- **Single AI Call**: Efficient workflow with one enhancement step
- **Dual Optimization**: ATS and HR optimized in one pass
- **Professional Output**: High-quality LaTeX-generated PDFs
- **Customizable**: Multiple templates and targeting options

## 📁 Project Structure

```
Resume-ai/
├── app.py                     # Main script
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── resume_env/                # Python virtual environment
└── src/
    ├── __init__.py
    ├── ai/
    │   ├── __init__.py
    │   └── resume_generator.py    # Core AI resume generator
    ├── prompts/
    │   ├── __init__.py
    │   └── enhancement_prompts.py # AI enhancement prompts
    └── templates/
        ├── __init__.py
        └── latex_templates.py     # Professional LaTeX templates
```

## 🛠️ Setup

1. **Activate Environment**:
   ```bash
   source resume_env/bin/activate
   ```

2. **Set API Key**:
   Create a `.env` file in the root of the project and add your Gemini API key.
   You can use the `.env.example` file as a template.
   ```bash
   GEMINI_API_KEY="your_gemini_api_key_here"
   ```

3. **Run App**:
   ```bash
   python app.py
   ```

## 📋 Available Templates

1. **Modern Professional** - Best for Tech/Business roles
2. **Minimal Tech** - Best for Software Engineering roles  
3. **Clean Academic** - Best for Academic/Research roles
4. **Executive** - Best for Senior/Executive roles

## 🔧 Dependencies

- `google-generativeai` - Gemini AI integration
- LaTeX distribution (texlive-full) - PDF compilation
- Python 3.8+ - Core runtime

## 🚀 Quick Start

```bash
# 1. Activate environment
source resume_env/bin/activate

# 2. Create .env file and add your API key
cp .env.example .env
# then edit .env with your key

# 3. Run app
python app.py

# 4. Select template and profile
# 5. Get professional PDF resume!
```

## 🎨 Usage

The application will prompt you to select a resume template and a sample profile to generate the resume.

1. **Select a Template**: Choose one of the available LaTeX templates.
2. **Select a Profile**: Choose one of the sample profiles.
3. **Generate Resume**: The script will generate a PDF resume based on your selections.

The generated resume will be saved in the root directory of the project.

## 📝 Adding New Templates

To add a new LaTeX template, you need to:

1. **Add the Template**: Add the new LaTeX template to the `src/templates/latex_templates.py` file.
2. **Update the `AIResumeGenerator`**: Add the new template to the `TEMPLATES` dictionary in the `AIResumeGenerator` class in `src/ai/resume_generator.py`.

## 📝 Adding New Profiles

To add a new sample profile, you need to:

1. **Add the Profile**: Add the new profile to the `samples` dictionary in the `load_sample` method in the `app.py` file.

## 📝 Adding New Prompts

To add a new prompt, you need to:

1. **Add the Prompt**: Add the new prompt to the `src/prompts/enhancement_prompts.py` file.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.



---

**Built with ❤️ using Google Gemini AI and LaTeX**