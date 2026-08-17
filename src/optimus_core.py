import os
import json
import subprocess
from sqlalchemy import create_engine, Table, Column, String, MetaData
import openai
import boto3

DB_URL = "postgresql://TechMind:BC5PhN1DmQDfoWZiSBFxPg@bamboo-hoatzin-19289.jxf.gcp-europe-west2.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
engine = create_engine(DB_URL)

metadata = MetaData()
agent_memory = Table(
    "agent_memory", metadata,
    Column("id", String, primary_key=True),
    Column("type", String),
    Column("content", String),
    Column("embedding", String),
)
metadata.create_all(engine)

class OptimusCore:
    def __init__(self):
        self.db = engine
        self.s3 = boto3.client("s3")
        print("🤖 OptimusCore connected to CockroachDB cluster!")

    def save_memory(self, mem_id, text, mem_type="conversation"):
        embedding = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )["data"][0]["embedding"]

        with self.db.connect() as conn:
            conn.execute(agent_memory.insert().values(
                id=mem_id,
                type=mem_type,
                content=text,
                embedding=json.dumps(embedding)
            ))

        self.s3.put_object(
            Bucket=os.getenv("AWS_S3_BUCKET"),
            Key=f"memory/{mem_id}.json",
            Body=json.dumps({"text": text})
        )
        print("💾 Memory saved to CockroachDB + S3")

    def search_memory(self, query_text, top_k=3):
        embedding = openai.Embedding.create(
            input=query_text,
            model="text-embedding-ada-002"
        )["data"][0]["embedding"]

        sql = f"""
        SELECT id, type, content
        FROM agent_memory
        ORDER BY embedding <-> '{json.dumps(embedding)}'
        LIMIT {top_k};
        """
        with self.db.connect() as conn:
            results = conn.execute(sql).fetchall()
        return results

    def ccloud_status(self):
        result = subprocess.run(["ccloud", "clusters", "list", "--json"], capture_output=True)
        return json.loads(result.stdout)

    def trigger_lambda(self, function_name, payload):
        lambda_client = boto3.client("lambda")
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload)
        )
        return json.loads(response["Payload"].read())
