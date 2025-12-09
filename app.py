import gradio as gr
import os
from elevenlabs import ElevenLabs
from blog_summarizer import summarize_blog

def process_url(url):
    """Process URL and generate podcast"""
    try:
        # 1. Generate summary
        summary = summarize_blog(url)
        
        # 2. Initialize ElevenLabs
        client = ElevenLabs(
            api_key=os.environ.get("ELEVENLABS_API_KEY")
        )
        
        # 3. Convert to speech
        response = client.text_to_speech.convert(
            text=summary[:1000],
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_flash_v2_5",
            output_format="mp3_44100_128",
        )
        
        # 4. Save audio
        audio_file_path = "/app/podcast_audio.mp3"
        with open(audio_file_path, "wb") as audio_file:
            for chunk in response:
                audio_file.write(chunk)
        
        status = "✅ Podcast generated successfully!"
        return status, summary, audio_file_path
        
    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        return error_msg, "", None

# Create Gradio interface
with gr.Blocks() as demo:
    # Simple header
    gr.Markdown("# 🎙️ AI Podcast Generator")
    gr.Markdown("Transform any blog article into a professional podcast with lifelike AI voice")
    
    # URL Input
    url_input = gr.Textbox(
        label="Blog URL",
        placeholder="Paste your blog URL here...\nExample: https://medium.com/technology/article",
        lines=3
    )
    
    # Generate Button
    generate_btn = gr.Button("🚀 Generate Podcast")
    
    # Status Output
    status_output = gr.Textbox(
        label="Status",
        interactive=False
    )
    
    # Summary Output
    summary_output = gr.Textbox(
        label="Podcast Script",
        lines=10,
        interactive=False
    )
    
    # Audio Output
    audio_output = gr.Audio(
        label="Podcast Audio",
        type="filepath",
        interactive=False
    )
    
    # Event handler
    def generate_podcast(url):
        if not url or not url.strip():
            return (
                "⚠️ Please enter a valid URL",
                "",
                None
            )
        
        try:
            # Process the URL
            status_msg, summary_text, audio_path = process_url(url)
            return status_msg, summary_text, audio_path
        except Exception as e:
            return f"❌ Error: {str(e)}", "", None
    
    # Connect button to function
    generate_btn.click(
        fn=generate_podcast,
        inputs=[url_input],
        outputs=[status_output, summary_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch(
        server_port=7777,
        server_name="0.0.0.0",
        share=False
    )