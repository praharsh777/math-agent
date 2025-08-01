from langchain.tools import Tool
from langchain.utilities import WikipediaAPIWrapper

# Initialize Wikipedia search tool
wiki = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia Search",
    func=wiki.run,
    description="Useful for answering general knowledge or non-math questions."
)

# You can add more tools to this list later
tools = [
    wikipedia_tool
]
