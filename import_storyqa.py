import asyncio
from datasets import load_dataset
from parlant_qna.app import create_persistent_app

async def run():
    ds = load_dataset("yale-nlp/MSRS", "story-qa", split="train")
    async with create_persistent_app() as app:
        for i, row in enumerate(ds):
            variants = [row['query'].strip()]
            answer = "\n\n".join(row['answer']) if isinstance(row['answer'], list) else str(row['answer'])
            q = await app.create_question(variants, answer)
            print(i, ")", q.id)
    print("done")

if __name__ == "__main__":
    asyncio.run(run())
