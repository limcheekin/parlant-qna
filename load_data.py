from pathlib import Path  
import os  
from parlant_qna.app import parse_md_file, create_persistent_app  
  
async def load_example_questions():  
    async with create_persistent_app() as app:  
        dir = Path("example_qna")  
          
        for file in os.listdir(dir):
            print(file)  
            question = await parse_md_file(dir / file)  
            await app.create_question(question.variants, question.answer)


if __name__ == "__main__":
    import asyncio
    asyncio.run(load_example_questions())            