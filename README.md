

AI-Powered Resume Screening System

An intelligent, full-stack application that automatically screens resumes against job descriptions using Natural Language Processing (NLP) and *Machine Learning. The system evaluates resumes, calculates a match score, and highlights matched and missing skills to aid recruiters in quick and transparent candidate selection.



🚀 Features

Resume Parsing: Extracts text from PDF and DOCX resumes.
Job Description Matching: Uses semantic similarity via sentence-transformers (BERT-based model).
Skill Highlighting: Displays matched and missing keywords for transparency.
Real-Time Scoring: Generates match percentage instantly after upload.
Modern UI: Responsive React interface with interactive score display.
Cloud Ready: Backend API deployable to AWS/Render for scalability.

---

🛠 Tech Stack

Frontend: React.js, Tailwind CSS
Backend: Flask (Python)
NLP Model: Sentence-BERT (all-MiniLM-L6-v2)
Libraries: PyPDF2, python-docx, scikit-learn, sentence-transformers
Deployment: AWS EC2 / Render



📂 Project Structure


AI_Resume_Screener/
│── backend/               # Flask API and NLP logic  
│── frontend/              # React.js UI  
│── sample_resumes/        # Example resumes for testing  
│── requirements.txt       # Python dependencies  
│── package.json           # React dependencies  
│── README.md              # Project documentation  




 ⚙ Installation & Setup

 Backend Setup

bash
cd backend
pip install -r requirements.txt
python app.py


 Frontend Setup

bash
cd frontend
npm install
npm start

📊 Output Example

Input:

Resume: resume.pdf
Job Description: Software Engineer (React, Python, AWS)

Output:
Match Score: 89%
Matched Skills: React, Python, AWS, REST API
 Missing Skills: GraphQL, Docker



💡 Future Enhancements

Multi-language resume parsing
Integration with LinkedIn & job boards
AI-powered candidate ranking system





