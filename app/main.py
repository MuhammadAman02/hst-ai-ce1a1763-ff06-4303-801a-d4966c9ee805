"""
AI Engineer Portfolio - Main Application
Professional portfolio with interactive components and modern design
"""

from nicegui import ui
from app.config import PortfolioConfig
from app.components.hero import create_hero_section
from app.components.about import create_about_section
from app.components.skills import create_skills_section
from app.components.projects import create_projects_section
from app.components.experience import create_experience_section
from app.components.contact import create_contact_section
from app.components.footer import create_footer
import asyncio

# Global configuration
config = PortfolioConfig()

def create_portfolio_app():
    """Create the main portfolio application"""
    
    # Add custom CSS for modern styling
    ui.add_head_html("""
    <style>
        :root {
            --primary-color: #6366f1;
            --secondary-color: #8b5cf6;
            --accent-color: #06b6d4;
            --dark-bg: #0f172a;
            --card-bg: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --gradient: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        }
        
        body {
            background: var(--dark-bg);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
        }
        
        .hero-gradient {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            position: relative;
            overflow: hidden;
        }
        
        .hero-gradient::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 20%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }
        
        .glass-card {
            background: rgba(30, 41, 59, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .skill-bar {
            background: rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            overflow: hidden;
            height: 8px;
        }
        
        .skill-progress {
            background: var(--gradient);
            height: 100%;
            border-radius: 8px;
            transition: width 1s ease-in-out;
        }
        
        .project-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
        }
        
        .project-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }
        
        .btn-primary {
            background: var(--gradient);
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            color: white;
            font-weight: 600;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }
        
        .floating-animation {
            animation: float 6s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .section-title {
                font-size: 2rem;
            }
        }
        
        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: var(--dark-bg);
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--primary-color);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: var(--secondary-color);
        }
    </style>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    """)

    @ui.page('/')
    async def index():
        """Main portfolio page"""
        
        # Navigation
        with ui.header().classes('bg-slate-900/95 backdrop-blur-sm border-b border-slate-700 fixed top-0 z-50'):
            with ui.row().classes('w-full max-w-6xl mx-auto px-4 py-3 items-center justify-between'):
                ui.label('AI Engineer').classes('text-xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent')
                
                with ui.row().classes('gap-6 hidden md:flex'):
                    ui.link('About', '#about').classes('text-slate-300 hover:text-white transition-colors')
                    ui.link('Skills', '#skills').classes('text-slate-300 hover:text-white transition-colors')
                    ui.link('Projects', '#projects').classes('text-slate-300 hover:text-white transition-colors')
                    ui.link('Experience', '#experience').classes('text-slate-300 hover:text-white transition-colors')
                    ui.link('Contact', '#contact').classes('text-slate-300 hover:text-white transition-colors')
        
        # Add top padding to account for fixed header
        ui.html('<div class="h-16"></div>')
        
        # Portfolio sections
        await create_hero_section()
        await create_about_section()
        await create_skills_section()
        await create_projects_section()
        await create_experience_section()
        await create_contact_section()
        create_footer()
        
        # Add smooth scroll behavior
        ui.add_head_html("""
        <script>
            // Smooth scroll for anchor links
            document.addEventListener('DOMContentLoaded', function() {
                const links = document.querySelectorAll('a[href^="#"]');
                links.forEach(link => {
                    link.addEventListener('click', function(e) {
                        e.preventDefault();
                        const target = document.querySelector(this.getAttribute('href'));
                        if (target) {
                            target.scrollIntoView({
                                behavior: 'smooth',
                                block: 'start'
                            });
                        }
                    });
                });
                
                // Animate skill bars when they come into view
                const observerOptions = {
                    threshold: 0.5,
                    rootMargin: '0px 0px -100px 0px'
                };
                
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const skillBars = entry.target.querySelectorAll('.skill-progress');
                            skillBars.forEach(bar => {
                                const width = bar.getAttribute('data-width');
                                bar.style.width = width + '%';
                            });
                        }
                    });
                }, observerOptions);
                
                const skillsSection = document.querySelector('#skills');
                if (skillsSection) {
                    observer.observe(skillsSection);
                }
            });
        </script>
        """)

    return True