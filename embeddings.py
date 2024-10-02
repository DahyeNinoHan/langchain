from langchain_upstage import UpstageEmbeddings
 
embeddings = UpstageEmbeddings(
  api_key="UPSTAGE_API_KEY",
  model="solar-embedding-1-large"
)
 
doc_result = embeddings.embed_documents(
    ["SOLAR 10.7B: Scaling Large Language Models with Simple yet Effective Depth Up-Scaling.", "DUS is simple yet effective in scaling up high performance LLMs from small ones."]
)
 
query_result = embeddings.embed_query("What makes Solar LLM small yet effective?")
print(query_result)