"""
Task Definitions Module
Contains all task creation functions
"""

from crewai import Task
from agents import create_blog_scraper_agent, create_blog_summarizer_agent
from podcast_transitions import create_podcast_transition_agent

def create_scrape_task(url, llm, tools):
    """
    Create task for scraping blog content
    
    Args:
        url: The blog URL to scrape
        llm: The language model to use
        tools: List of tools available
    
    Returns:
        Task: Blog scraping task
    """
    # Create the scraping agent
    scraper_agent = create_blog_scraper_agent(llm, tools)
    
    # Task description
    description = f"""
    EXTRACT CLEAN BLOG CONTENT FROM: {url}
    
    Your task is to extract ONLY the main article content from the provided URL.
    
    CRITICAL INSTRUCTIONS:
    1. IGNORE all navigation menus, headers, footers, sidebars
    2. IGNORE all advertisements, pop-ups, and promotional content
    3. IGNORE all comments sections and user-generated content
    4. IGNORE all social media widgets and sharing buttons
    5. IGNORE all related articles or recommended content sections
    6. IGNORE all author bios and publication information (unless part of main article)
    
    FOCUS ONLY ON:
    1. The main article title/heading
    2. The main article body/content
    3. Subheadings within the article
    4. Paragraphs and text content
    5. Lists (both bulleted and numbered) within the article
    
    OUTPUT REQUIREMENTS:
    1. Return ONLY the pure article text
    2. Preserve the structure with headings, paragraphs, and lists
    3. Format in clean markdown
    4. Do NOT include any URLs or external links
    5. Do NOT include any images or media references
    6. Do NOT include any citation formats or references
    
    Your output should be ready for the next agent to analyze and summarize.
    """
    
    return Task(
        description=description,
        expected_output="Full blog content in clean markdown format without any website elements",
        agent=scraper_agent
    )

def create_summarize_task(scrape_task, llm):
    """
    Create task for summarizing scraped content
    
    Args:
        scrape_task: The previous scraping task
        llm: The language model to use
    
    Returns:
        Task: Blog summarization task
    """
    # Create the summarizer agent
    summarizer_agent = create_blog_summarizer_agent(llm)
    
    # Task description
    description = """
    ANALYZE AND STRUCTURE BLOG CONTENT FOR PODCAST CONVERSION
    
    Your task is to analyze the scraped blog content and create a structured 
    outline that captures all key information for podcast conversion.
    
    ANALYSIS STEPS:
    1. Identify the main topic and core message
    2. Break down the content into logical sections
    3. Extract key arguments and supporting points for each section
    4. Identify important data, statistics, or examples
    5. Determine the conclusion and main takeaways
    
    STRUCTURE REQUIREMENTS:
    1. Main Topic: What is the article about?
    2. Key Sections: What are the main parts/arguments?
    3. Points per Section: What are the important details in each section?
    4. Conclusion: What are the final takeaways?
    
    OUTPUT GUIDELINES:
    1. Focus on extracting the most valuable insights
    2. Organize information logically
    3. Keep it concise but comprehensive
    4. Prepare it for easy conversion to spoken format
    5. Highlight what would be most engaging for listeners
    
    Remember: Your output will be used to create a podcast script, 
    so focus on what would work well in audio format.
    """
    
    return Task(
        description=description,
        expected_output="A structured outline of key points from the blog, ready for podcast conversion",
        agent=summarizer_agent,
        context=[scrape_task]
    )

def create_transition_task(summarize_task, llm):
    """
    Create task for adding podcast transitions
    
    Args:
        summarize_task: The previous summarization task
        llm: The language model to use
    
    Returns:
        Task: Transition enhancement task
    """
    # Import the function from podcast_transitions module
    from podcast_transitions import create_transition_task as create_transition_task_func
    return create_transition_task_func(summarize_task, llm)