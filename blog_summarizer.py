"""
Main Blog Summarizer Module
Orchestrates the entire podcast generation pipeline
"""

import os
from crewai import Crew, Process, LLM
from crewai_tools import FirecrawlScrapeWebsiteTool

# Import modular components
from tasks import create_scrape_task, create_summarize_task, create_transition_task

def initialize_llm():
    """
    Initialize the language model with Ollama configuration
    
    Returns:
        LLM: Configured language model instance
    """
    return LLM(
        model="ollama/deepseek-r1:1.5b",
        base_url="http://172.17.0.1:11434",
        api_key="not-needed"
    )

def initialize_tools():
    """
    Initialize all tools needed for the pipeline
    
    Returns:
        list: List of initialized tools
    """
    firecrawl_api_key = os.environ.get("FIRECRAWL_API_KEY")
    
    if not firecrawl_api_key:
        raise ValueError("FIRECRAWL_API_KEY environment variable is not set")
    
    return [
        FirecrawlScrapeWebsiteTool(api_key=firecrawl_api_key)
    ]

def create_blog_summarization_process(url):
    """
    Create the complete blog summarization process pipeline
    
    Args:
        url: The blog URL to process
    
    Returns:
        Crew: Configured crew with all tasks
    """
    # Initialize components
    llm = initialize_llm()
    tools = initialize_tools()
    
    # Create all tasks using modular functions
    print(f"🔍 Starting blog summarization process for: {url}")
    
    # Step 1: Scrape the blog content
    print("📄 Creating scraping task...")
    scrape_task = create_scrape_task(url, llm, tools)
    
    # Step 2: Summarize the content
    print("📝 Creating summarization task...")
    summarize_task = create_summarize_task(scrape_task, llm)
    
    # Step 3: Add podcast transitions
    print("🎙️ Creating transition task...")
    transition_task = create_transition_task(summarize_task, llm)
    
    # Create the crew with all tasks
    print("🚀 Assembling crew with all tasks...")
    crew = Crew(
        tasks=[scrape_task, summarize_task, transition_task],
        process=Process.sequential,
        verbose=True,
    )
    
    print("✅ Blog summarization process created successfully")
    return crew

def summarize_blog(url):
    """
    Main function to summarize a blog into a podcast script
    
    Args:
        url: The blog URL to process
    
    Returns:
        str: Podcast script with transition phrases
    """
    try:
        # Validate URL
        if not url or not isinstance(url, str) or not url.startswith(('http://', 'https://')):
            raise ValueError(f"Invalid URL provided: {url}")
        
        print(f"🎯 Starting podcast generation for: {url}")
        
        # Create and execute the crew
        crew = create_blog_summarization_process(url)
        result = crew.kickoff()
        
        # Get the final output
        podcast_script = str(result.raw)
        
        # Validate output
        if not podcast_script or len(podcast_script.strip()) < 50:
            raise ValueError("Generated podcast script is too short or empty")
        
        print(f"✅ Successfully generated podcast script ({len(podcast_script)} characters)")
        return podcast_script
        
    except Exception as e:
        error_message = f"❌ Error in summarize_blog: {str(e)}"
        print(error_message)
        raise Exception(error_message)