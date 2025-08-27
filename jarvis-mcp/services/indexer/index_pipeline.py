import os
from .db.models import get_db, File, Chunk, Symbol
from .ast.parse import parse_file
from .embeddings.embed import embed_text

PROJECT_PATH = '/workspace/project'

def reindex(payload):
    # Walk project, parse files, update DB
    db = get_db()
    for root, dirs, files in os.walk(PROJECT_PATH):
        for fname in files:
            path = os.path.join(root, fname)
            try:
                ast = parse_file(path)
                embedding = embed_text(open(path).read())
                # Store in DB
                db.add(File(path=path))
                db.add(Chunk(path=path, embedding=embedding))
                db.add(Symbol(path=path, symbols=ast['symbols']))
            except Exception as e:
                continue
    db.commit()
    return {"status": "reindexed"}

def search_index(payload):
    # Simple keyword search
    db = get_db()
    keyword = payload.get('keyword', '')
    results = db.query(Chunk).filter(Chunk.text.contains(keyword)).all()
    return {"results": [c.path for c in results]}

def pull_context(payload):
    # Return ranked snippets
    db = get_db()
    symbol = payload.get('symbol', '')
    results = db.query(Symbol).filter(Symbol.symbols.contains(symbol)).all()
    return {"snippets": [r.path for r in results]}

def get_stats():
    db = get_db()
    return {
        "files": db.query(File).count(),
        "chunks": db.query(Chunk).count(),
        "symbols": db.query(Symbol).count()
    }
