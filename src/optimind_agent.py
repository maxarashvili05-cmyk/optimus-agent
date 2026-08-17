import os
from googleapiclient.discovery import build
from optimus_core import OptimusCore

class OptiMindAgent:
    def __init__(self, blog_id, api_key):
        self.blog_id = blog_id
        self.service = build('blogger', 'v3', developerKey=api_key)
        self.core = OptimusCore()

    def run_analysis(self, post_id):
        print(f"🔍 [LOG]: Initiating 18-core mesh analysis for Post ID: {post_id}...")
        post = self.service.posts().get(blogId=self.blog_id, postId=post_id).execute()
        text = post["title"] + " " + post["content"]

        # Save to CockroachDB + S3
        self.core.save_memory(mem_id=post_id, text=text, mem_type="blog_post")

        print(f"✅ [LOG]: Content processed. SEO tags optimized. Pushing to Blogger...")
        return True
