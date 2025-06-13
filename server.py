import asyncio
from mcp.server.fastmcp import FastMCP
from optimized_research import optimized_research

# Create FastMCP instance
mcp = FastMCP("crew_research")

@mcp.tool()
async def crew_research(query: str) -> str:
    """Run optimized research system for given user query. Fast and detailed.

    Args:
        query (str): The research query or question.

    Returns:
        str: The research response from the optimized research pipeline.
    """
    return optimized_research(query)


# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")


# add this inside ./.cursor/mcp.json
# {
#   "mcpServers": {
#     "crew_research": {
#       "command": "uv",
#       "args": [
#         "--directory",
#         "d:\\mcp",
#         "run",
#         "server.py"
#       ],
#       "env": {
#         "LINKUP_API_KEY": "your_linkup_api_key_here"
#       }
#     }
#   }
# }
