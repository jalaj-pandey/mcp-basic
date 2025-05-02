from mcp.server.fastmcp import FastMCP
mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name:str) -> str:
    """Say hello to a person.
    Args:
        name (str): The name of the person to greet.
        """
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport='stdio')
