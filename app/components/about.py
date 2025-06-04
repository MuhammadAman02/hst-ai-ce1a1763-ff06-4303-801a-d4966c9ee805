"""
About Section Component
Professional background and personal introduction
"""

from nicegui import ui
from app.config import portfolio_config

async def create_about_section():
    """Create the about section with professional background"""
    
    with ui.element('section').props('id=about').classes('py-20 bg-slate-900/50'):
        with ui.container().classes('max-w-6xl mx-auto px-4'):
            
            # Section title
            ui.html('<h2 class="section-title text-center mb-16">About Me</h2>')
            
            with ui.row().classes('gap-12 items-center'):
                
                # Professional image
                with ui.column().classes('w-full md:w-1/3'):
                    ui.image('https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&h=800&fit=crop').classes(
                        'w-full rounded-2xl shadow-2xl glass-card'
                    )
                
                # About content
                with ui.column().classes('w-full md:w-2/3 space-y-6'):
                    
                    ui.html(f'''
                    <div class="glass-card p-8 rounded-2xl">
                        <h3 class="text-2xl font-bold text-white mb-4">Professional Journey</h3>
                        <p class="text-slate-300 text-lg leading-relaxed mb-6">
                            {portfolio_config.summary}
                        </p>
                        
                        <p class="text-slate-300 text-lg leading-relaxed mb-6">
                            My passion for artificial intelligence began during my undergraduate studies at UC Berkeley, 
                            where I first encountered the transformative potential of machine learning. Since then, I've 
                            dedicated my career to pushing the boundaries of what's possible with AI technology.
                        </p>
                        
                        <p class="text-slate-300 text-lg leading-relaxed">
                            I believe in building AI solutions that are not just technically sophisticated, but also 
                            ethical, scalable, and genuinely useful. My approach combines rigorous scientific methodology 
                            with practical engineering skills to deliver systems that create real business value.
                        </p>
                    </div>
                    ''')
                    
                    # Key highlights
                    with ui.card().classes('glass-card p-6'):
                        ui.label('Key Highlights').classes('text-xl font-bold text-white mb-4')
                        
                        highlights = [
                            "🎓 M.S. Computer Science from Stanford University",
                            "🏆 5+ years of hands-on AI/ML experience",
                            "🚀 Led teams building production ML systems",
                            "📊 Deployed models serving 50M+ predictions daily",
                            "📝 Published research in top-tier AI conferences",
                            "☁️ Expert in cloud-native MLOps architectures"
                        ]
                        
                        for highlight in highlights:
                            ui.html(f'<div class="flex items-center mb-2 text-slate-300"><span class="mr-3">{highlight}</span></div>')
            
            # Education and Certifications
            with ui.row().classes('gap-8 mt-16'):
                
                # Education
                with ui.column().classes('w-full md:w-1/2'):
                    with ui.card().classes('glass-card p-6 h-full'):
                        ui.label('Education').classes('text-xl font-bold text-white mb-4')
                        
                        for edu in portfolio_config.education:
                            ui.html(f'''
                            <div class="mb-4 pb-4 border-b border-slate-600 last:border-b-0">
                                <h4 class="font-semibold text-indigo-400">{edu["degree"]}</h4>
                                <p class="text-slate-300">{edu["school"]}</p>
                                <p class="text-slate-400 text-sm">{edu["year"]} • GPA: {edu["gpa"]}</p>
                                <p class="text-slate-400 text-sm">Specialization: {edu["specialization"]}</p>
                            </div>
                            ''')
                
                # Certifications
                with ui.column().classes('w-full md:w-1/2'):
                    with ui.card().classes('glass-card p-6 h-full'):
                        ui.label('Certifications').classes('text-xl font-bold text-white mb-4')
                        
                        for cert in portfolio_config.certifications:
                            ui.html(f'''
                            <div class="mb-4 pb-4 border-b border-slate-600 last:border-b-0">
                                <h4 class="font-semibold text-cyan-400">{cert["name"]}</h4>
                                <p class="text-slate-300">{cert["issuer"]}</p>
                                <p class="text-slate-400 text-sm">{cert["year"]}</p>
                            </div>
                            ''')