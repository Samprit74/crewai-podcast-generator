"""
Podcast Transition Module
Specialized agent for adding natural podcast transition phrases
"""

from crewai import Agent, Task

def create_podcast_transition_agent(llm):
    """
    Create a specialized agent for adding podcast transition phrases
    
    Args:
        llm: The language model to use
    
    Returns:
        Agent: Podcast transition agent
    """
    return Agent(
        name="PodcastTransitionAgent",
        role="Podcast Script Enhancer",
        goal="Add natural podcast transition phrases to make content engaging for audio",
        backstory="""You are a professional podcast producer with 10+ years of experience.
        You specialize in transforming written content into natural-sounding podcast scripts.
        You know exactly when to add phrases like 'As for the heading...', 
        'Now coming to the main part...', and 'In conclusion...' 
        to create perfect audio flow that keeps listeners engaged.""",
        llm=llm,
        verbose=True
    )

def create_transition_task(summarize_task, llm):
    """
    Create task to add podcast transition phrases
    
    Args:
        summarize_task: The previous summarization task
        llm: The language model to use
    
    Returns:
        Task: Transition enhancement task
    """
    # Create the transition agent
    transition_agent = create_podcast_transition_agent(llm)
    
    # Detailed transition instructions
    transition_instructions = """
    TRANSITION PHRASES TO USE:
    
    1. FOR HEADINGS/MAIN TOPICS:
       • "As for the heading..."
       • "Now, regarding the main topic..."
       • "Let's start with..."
       • "The heading suggests that..."
    
    2. BETWEEN MAIN SECTIONS:
       • "Now, coming to the main part..."
       • "Moving on to the next section..."
       • "As we transition to..."
       • "Let's dive deeper into..."
       • "Shifting our focus to..."
    
    3. FOR KEY POINTS WITHIN SECTIONS:
       • "An important point here is..."
       • "What's interesting about this..."
       • "Here's something crucial..."
       • "Now, regarding this specific aspect..."
       • "This brings us to..."
    
    4. FOR LISTS OR MULTIPLE POINTS:
       • "First up..."
       • "Next..."
       • "Additionally..."
       • "Another key factor..."
       • "Furthermore..."
       • "On top of that..."
    
    5. FOR CONCLUSIONS:
       • "So, to summarize..."
       • "In conclusion..."
       • "Before we wrap up..."
       • "To bring it all together..."
       • "As a final takeaway..."
       • "Ultimately..."
    
    6. GENERAL TRANSITIONS:
       • "Now, moving forward..."
       • "With that said..."
       • "Shifting gears slightly..."
       • "Building on that idea..."
       • "Let's transition to..."
       • "At this point..."
    """
    
    # Script structure template
    structure_template = """
    REQUIRED SCRIPT STRUCTURE:
    
    1. BEGINNING (Always start with this):
       "As for the heading, [brief introduction about the topic]"
    
    2. MIDDLE SECTIONS (Use these patterns):
       "Now, coming to the [section name]... [explain the section]"
       "An important point here is... [elaborate on key point]"
       "Moving on to the next aspect... [continue explanation]"
    
    3. CONCLUSION (Always end with this):
       "In conclusion... [summarize main takeaways]"
       "As a final takeaway... [ending thought]"
    """
    
    # Rules for the agent
    rules = """
    STRICT RULES TO FOLLOW:
    
    1. Use AT LEAST 5 different transition phrases from the list above
    2. Always start with "As for the heading..."
    3. Always end with "In conclusion..."
    4. Keep the script between 200-240 words
    5. Write in flowing paragraphs only - NO bullet points or lists
    6. Make it sound conversational and engaging
    7. Do NOT include URLs, citations, or technical jargon
    8. Do NOT use markdown formatting
    9. Ensure smooth flow between sentences
    10. Make it sound like a real podcast host speaking naturally
    """
    
    # Combine all instructions
    full_description = f"""
    TRANSFORM THE SUMMARIZED CONTENT INTO A PROFESSIONAL PODCAST SCRIPT
    
    Your task is to take the summarized blog content and enhance it with natural 
    podcast transition phrases to make it perfect for audio delivery.
    
    {transition_instructions}
    
    {structure_template}
    
    {rules}
    
    REMEMBER: Your output should be a polished podcast script that sounds like 
    it's being spoken by a professional podcast host. Listeners should feel 
    engaged and guided smoothly through the content.
    """
    
    return Task(
        description=full_description,
        expected_output="A polished 200-240 word podcast script with natural transition phrases, ready for audio recording.",
        agent=transition_agent,
        context=[summarize_task]
    )