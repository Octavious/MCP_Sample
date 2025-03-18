from typing import Any
from mcp.server.fastmcp import FastMCP
import sqlite3
import os

# Initialize FastMCP server
mcp = FastMCP("SearchWords")

@mcp.tool()
async def search_words(search_term: str) -> str:
    """Search for words in the Quran database.

    Args:
        search_term: Word or phrase to search for in the Quran
    """
    # Connect to the SQLite database
    db_path = os.path.join(os.path.dirname(__file__), 'quran.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Search for verses containing the term
    query = """
    SELECT sura, sura_num, verse_num, text 
    FROM verses 
    WHERE text LIKE ?
    ORDER BY sura_num, verse_num
    """
    cursor.execute(query, (f'%{search_term}%',))
    results = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    if not results:
        return f"No verses found containing '{search_term}'."
    
    # Format the results
    formatted_results = []
    for sura, sura_num, verse_num, text in results:
        formatted_results.append(f"Surah {sura} ({sura_num}:{verse_num})\n{text}")
    
    return "\n---\n".join(formatted_results)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')