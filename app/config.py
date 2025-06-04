"""
Portfolio Configuration
Centralized configuration for the AI Engineer portfolio
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List, Dict, Any
import os

class PortfolioConfig(BaseSettings):
    """Portfolio configuration settings"""
    
    # Personal Information
    name: str = Field(default="Alex Chen", description="Full name")
    title: str = Field(default="AI Engineer & Machine Learning Specialist", description="Professional title")
    email: str = Field(default="alex.chen@example.com", description="Contact email")
    phone: str = Field(default="+1 (555) 123-4567", description="Contact phone")
    location: str = Field(default="San Francisco, CA", description="Location")
    
    # Social Links
    github_url: str = Field(default="https://github.com/alexchen", description="GitHub profile")
    linkedin_url: str = Field(default="https://linkedin.com/in/alexchen", description="LinkedIn profile")
    twitter_url: str = Field(default="https://twitter.com/alexchen", description="Twitter profile")
    
    # Professional Summary
    summary: str = Field(
        default="Passionate AI Engineer with 5+ years of experience in machine learning, deep learning, and MLOps. Specialized in building scalable AI solutions that drive business value. Expert in Python, TensorFlow, PyTorch, and cloud platforms.",
        description="Professional summary"
    )
    
    # Skills Configuration
    technical_skills: Dict[str, int] = Field(
        default={
            "Python": 95,
            "Machine Learning": 90,
            "Deep Learning": 88,
            "TensorFlow/PyTorch": 85,
            "MLOps": 82,
            "Cloud Platforms (AWS/GCP)": 80,
            "Docker/Kubernetes": 78,
            "Data Engineering": 85,
            "Computer Vision": 83,
            "Natural Language Processing": 80
        },
        description="Technical skills with proficiency levels (0-100)"
    )
    
    # Projects Configuration
    featured_projects: List[Dict[str, Any]] = Field(
        default=[
            {
                "title": "AI-Powered Customer Insights Platform",
                "description": "Built an end-to-end ML pipeline that analyzes customer behavior patterns using deep learning. Increased customer retention by 25% and reduced churn prediction error by 40%.",
                "technologies": ["Python", "TensorFlow", "Apache Kafka", "PostgreSQL", "Docker"],
                "github_url": "https://github.com/alexchen/customer-insights",
                "demo_url": "https://customer-insights-demo.com",
                "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=400&fit=crop",
                "status": "Production"
            },
            {
                "title": "Real-time Fraud Detection System",
                "description": "Developed a real-time fraud detection system using ensemble methods and streaming data processing. Achieved 99.2% accuracy with sub-100ms latency.",
                "technologies": ["Python", "Scikit-learn", "Apache Spark", "Redis", "Kubernetes"],
                "github_url": "https://github.com/alexchen/fraud-detection",
                "demo_url": "https://fraud-detection-demo.com",
                "image_url": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&h=400&fit=crop",
                "status": "Production"
            },
            {
                "title": "Computer Vision Quality Control",
                "description": "Implemented automated quality control system for manufacturing using computer vision. Reduced manual inspection time by 80% and improved defect detection accuracy to 96%.",
                "technologies": ["Python", "OpenCV", "PyTorch", "FastAPI", "AWS"],
                "github_url": "https://github.com/alexchen/cv-quality-control",
                "demo_url": "https://cv-qc-demo.com",
                "image_url": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&h=400&fit=crop",
                "status": "Production"
            },
            {
                "title": "NLP Document Classification API",
                "description": "Created a scalable document classification service using transformer models. Processes 10,000+ documents per hour with 94% accuracy across 50+ categories.",
                "technologies": ["Python", "Transformers", "FastAPI", "PostgreSQL", "Docker"],
                "github_url": "https://github.com/alexchen/nlp-classification",
                "demo_url": "https://nlp-classification-demo.com",
                "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=400&fit=crop",
                "status": "Production"
            }
        ],
        description="Featured projects showcase"
    )
    
    # Experience Configuration
    work_experience: List[Dict[str, Any]] = Field(
        default=[
            {
                "company": "TechCorp AI",
                "position": "Senior AI Engineer",
                "duration": "2022 - Present",
                "location": "San Francisco, CA",
                "description": "Lead AI initiatives for enterprise clients, developing custom ML solutions that drive business value. Manage a team of 4 ML engineers and collaborate with product teams to integrate AI capabilities.",
                "achievements": [
                    "Architected ML platform serving 50M+ predictions daily",
                    "Reduced model training time by 60% through optimization",
                    "Led migration to cloud-native MLOps infrastructure"
                ]
            },
            {
                "company": "DataFlow Solutions",
                "position": "Machine Learning Engineer",
                "duration": "2020 - 2022",
                "location": "Seattle, WA",
                "description": "Developed and deployed machine learning models for fintech applications. Specialized in fraud detection, risk assessment, and customer analytics.",
                "achievements": [
                    "Built fraud detection system with 99.1% accuracy",
                    "Implemented real-time ML inference pipeline",
                    "Reduced false positive rate by 45%"
                ]
            },
            {
                "company": "AI Innovations Lab",
                "position": "AI Research Engineer",
                "duration": "2019 - 2020",
                "location": "Boston, MA",
                "description": "Conducted research in computer vision and natural language processing. Published papers and developed proof-of-concept AI applications.",
                "achievements": [
                    "Published 3 papers in top-tier AI conferences",
                    "Developed novel CNN architecture for medical imaging",
                    "Won 'Best Innovation' award at company hackathon"
                ]
            }
        ],
        description="Work experience history"
    )
    
    # Education Configuration
    education: List[Dict[str, Any]] = Field(
        default=[
            {
                "degree": "M.S. in Computer Science",
                "school": "Stanford University",
                "year": "2019",
                "specialization": "Artificial Intelligence",
                "gpa": "3.9/4.0"
            },
            {
                "degree": "B.S. in Computer Engineering",
                "school": "UC Berkeley",
                "year": "2017",
                "specialization": "Machine Learning",
                "gpa": "3.8/4.0"
            }
        ],
        description="Educational background"
    )
    
    # Certifications
    certifications: List[Dict[str, str]] = Field(
        default=[
            {"name": "AWS Certified Machine Learning - Specialty", "issuer": "Amazon Web Services", "year": "2023"},
            {"name": "Google Cloud Professional ML Engineer", "issuer": "Google Cloud", "year": "2022"},
            {"name": "TensorFlow Developer Certificate", "issuer": "TensorFlow", "year": "2021"},
            {"name": "Kubernetes Certified Application Developer", "issuer": "CNCF", "year": "2022"}
        ],
        description="Professional certifications"
    )
    
    # Application Settings
    app_title: str = Field(default="AI Engineer Portfolio", description="Application title")
    app_description: str = Field(default="Professional portfolio showcasing AI engineering expertise", description="Application description")
    
    # Contact Form Settings
    contact_email_recipient: str = Field(default="alex.chen@example.com", description="Email recipient for contact form")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Global configuration instance
portfolio_config = PortfolioConfig()