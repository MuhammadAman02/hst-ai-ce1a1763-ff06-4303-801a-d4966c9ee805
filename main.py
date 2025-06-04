"""
AI Engineer Portfolio - Entry Point
Professional portfolio showcasing AI engineering expertise
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the main application
from app.main import create_portfolio_app

if __name__ in {"__main__", "__mp_main__"}:
    # Create and run the portfolio application
    create_portfolio_app()
    
    # Start the NiceGUI application
    from nicegui import ui
    ui.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        title="AI Engineer Portfolio",
        favicon="🤖",
        dark=True,
        show=False,
        reload=False
    )