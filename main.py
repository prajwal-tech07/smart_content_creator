from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.python import PythonTools
import os
from dotenv import load_dotenv

load_dotenv()

# Content Research Agent - Finds trending topics
research_agent = Agent(
    name="Content Research Agent",
    role="Research trending topics and hashtags for content creation",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Find trending topics in the specified niche",
        "Research popular hashtags with high engagement",
        "Always include sources and data"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Content Generation Agent
content_agent = Agent(
    name="Content Creator Agent",
    role="Generate engaging social media content and captions",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[PythonTools()],
    instructions=[
        "Create engaging captions and posts",
        "Include call-to-actions and engagement hooks",
        "Use tables to display content variations"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Platform Optimization Agent
optimization_agent = Agent(
    name="Platform Optimizer Agent",
    role="Optimize content for different social media platforms",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[PythonTools()],
    instructions=[
        "Adapt content for Instagram, Twitter, LinkedIn formats",
        "Optimize hashtag usage per platform",
        "Use tables to show platform-specific versions"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Multi-Agent System (like your multi_ai_agent)
content_creator_system = Agent(
    team=[research_agent, content_agent, optimization_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always include sources",
        "Use tables to display content",
        "Coordinate all agents for comprehensive content creation"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Example usage (similar to your NVDA query)
if __name__ == "__main__":
    content_creator_system.print_response(
        "Create social media content for a fitness influencer focusing on home workouts. "
        "Include trending hashtags and optimize for Instagram and Twitter.",
        stream=True
    )
