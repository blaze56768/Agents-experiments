import gradio as gr
from smolagents import GradioUI
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI

# Import your custom tools
from tools import WeatherInfoTool, HubStatsTool  # optionally: DuckDuckGoSearchTool
from retriever import load_guest_dataset  # assumes this returns a tool-compatible object


# Initialize the Hugging Face model
model = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")

# Initialize the web search tool
#search_tool = DuckDuckGoSearchTool()

# Initialize the weather tool
weather_info_tool = WeatherInfoTool()

# Initialize the Hub stats tool
hub_stats_tool = HubStatsTool()

# Load the guest dataset and initialize the guest info tool
guest_info_tool = load_guest_dataset()

# Create Alfred with all the tools
alfred = AgentWorkflow.from_tools_or_functions(
    [ weather_info_tool, hub_stats_tool],
    llm=model
)

if __name__ == "__main__":
    GradioUI(alfred).launch()