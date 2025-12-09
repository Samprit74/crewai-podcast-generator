"""
Agent Definitions Module
Contains all agent creation functions
"""

from crewai import Agent

def create_blog_scraper_agent(llm, tools):
    """
    Create agent for scraping blog content
    
    Args:
        llm: The language model to use
        tools: List of tools available to the agent
    
    Returns:
        Agent: Blog scraping agent
    """
    return Agent(
        name="BlogScraperAgent",
        role="Website Content Researcher",
        goal="Extract clean, accurate content from blog URLs",
        backstory="""You are an expert web content extractor with deep knowledge 
        of website structures. You can identify and extract only the main article 
        content while ignoring all advertisements, navigation menus, sidebars, 
        headers, footers, and comments. Your extractions are clean and focused 
        on the core content only.""",
        llm=llm,
        tools=tools,
        verbose=True
    )

def create_blog_summarizer_agent(llm):
    """
    Create agent for summarizing blog content
    
    Args:
        llm: The language model to use
    
    Returns:
        Agent: Blog summarizer agent
    """
    return Agent(
        name="BlogSummarizerAgent",
        role="Content Analyst",
        goal="Extract key insights and structure content for podcast use",
        backstory="""You are a content analyst with expertise in distilling 
        complex information into clear, structured summaries. You can identify 
        main arguments, key points, and conclusions from any content. 
        You prepare content in a way that's perfect for conversion to 
        audio formats.""",
        llm=llm,
        verbose=True
    )