"""
Hero Section Component
Eye-catching introduction section with professional presentation
"""

from nicegui import ui
from app.config import portfolio_config
import asyncio

async def create_hero_section():
    """Create the hero section with animated introduction"""
    
    with ui.element('section').props('id=hero').classes('hero-gradient min-h-screen flex items-center justify-center relative'):
        with ui.container().classes('max-w-6xl mx-auto px-4 py-20 text-center relative z-10'):
            
            # Profile image placeholder
            with ui.row().classes('justify-center mb-8'):
                ui.image('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop&crop=face').classes(
                    'w-32 h-32 rounded-full border-4 border-indigo-400 shadow-2xl floating-animation'
                )
            
            # Main heading with typing animation
            ui.html(f'''
            <h1 class="text-5xl md:text-7xl font-bold mb-6 fade-in">
                <span class="bg-gradient-to-r from-indigo-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
                    {portfolio_config.name}
                </span>
            </h1>
            ''')
            
            # Professional title
            ui.html(f'''
            <h2 class="text-xl md:text-2xl text-slate-300 mb-8 fade-in" style="animation-delay: 0.2s;">
                {portfolio_config.title}
            </h2>
            ''')
            
            # Professional summary
            ui.html(f'''
            <p class="text-lg text-slate-400 max-w-3xl mx-auto mb-12 leading-relaxed fade-in" style="animation-delay: 0.4s;">
                {portfolio_config.summary}
            </p>
            ''')
            
            # Call-to-action buttons
            with ui.row().classes('gap-4 justify-center fade-in').style('animation-delay: 0.6s;'):
                ui.button('View My Work', on_click=lambda: ui.navigate.to('#projects')).classes(
                    'btn-primary text-lg px-8 py-3'
                ).props('icon=work')
                
                ui.button('Contact Me', on_click=lambda: ui.navigate.to('#contact')).classes(
                    'bg-transparent border-2 border-indigo-400 text-indigo-400 hover:bg-indigo-400 hover:text-white transition-all duration-300 text-lg px-8 py-3 rounded-lg'
                ).props('icon=contact_mail')
            
            # Social links
            with ui.row().classes('gap-6 justify-center mt-12 fade-in').style('animation-delay: 0.8s;'):
                ui.link(target=portfolio_config.github_url).classes('text-slate-400 hover:text-white transition-colors text-2xl'):
                    ui.html('<i class="fab fa-github"></i>')
                
                ui.link(target=portfolio_config.linkedin_url).classes('text-slate-400 hover:text-blue-400 transition-colors text-2xl'):
                    ui.html('<i class="fab fa-linkedin"></i>')
                
                ui.link(target=portfolio_config.twitter_url).classes('text-slate-400 hover:text-cyan-400 transition-colors text-2xl'):
                    ui.html('<i class="fab fa-twitter"></i>')
        
        # Animated background elements
        ui.html('''
        <div class="absolute inset-0 overflow-hidden pointer-events-none">
            <div class="absolute -top-40 -right-40 w-80 h-80 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse"></div>
            <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-cyan-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse" style="animation-delay: 2s;"></div>
            <div class="absolute top-40 left-1/2 w-80 h-80 bg-indigo-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse" style="animation-delay: 4s;"></div>
        </div>
        ''')
        
        # Scroll indicator
        ui.html('''
        <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 text-slate-400 animate-bounce">
            <i class="fas fa-chevron-down text-2xl"></i>
        </div>
        ''')