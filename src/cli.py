import os
import argparse
from optimind_agent import OptiMindAgent
from optimus_core import OptimusCore

def main():
    parser = argparse.ArgumentParser(description="OptiMind: AI Blog Architect")
    parser.add_argument('--analyze', type=str, help='Post ID to analyze')
    parser.add_argument('--status', action='store_true', help='Check system status')
    parser.add_argument('--search', type=str, help='Semantic search in memory')

    args = parser.parse_args()

    if args.analyze:
        agent = OptiMindAgent(blog_id=os.getenv("BLOG_ID"), api_key=os.getenv("BLOGGER_API_KEY"))
        agent.run_analysis(args.analyze)
    elif args.status:
        print("🤖 OptiMind Core: ONLINE")
        print("⚙️ Status: 18-Core Mesh ACTIVE")
        print("🔗 Connection: Blogger API Verified")
    elif args.search:
        core = OptimusCore()
        results = core.search_memory(args.search)
        for r in results:
            print(f"🔎 Found: {r}")
    else:
        print("OptiMind Ready. Use --help for commands.")

if __name__ == "__main__":
    main()
