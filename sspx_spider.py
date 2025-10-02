import praw
import json

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="redditspider:v1.0 (by u/marte_)"
)

sub = reddit.subreddit("sspx")
result = []
seen_posts = set()       # para garantir posts únicos
seen_comments = set()    # para garantir comentários únicos

# pega até ~1000 posts (limite da API oficial)
for post in sub.new(limit=None):
    if post.id in seen_posts:
        continue
    seen_posts.add(post.id)

    data = {
        "id": post.id,
        "title": post.title,
        "author": str(post.author),
        "score": post.score,
        "created_utc": post.created_utc,
        "url": post.url,
        "num_comments": post.num_comments,
        "selftext": post.selftext
    }

    # pega TODOS os comentários
    post.comments.replace_more(limit=None)
    comments_data = []
    for c in post.comments.list():
        if c.id in seen_comments:
            continue
        seen_comments.add(c.id)
        comments_data.append({
            "id": c.id,
            "author": str(c.author),
            "score": c.score,
            "body": c.body
        })

    data["comments"] = comments_data
    result.append(data)

# salva no JSON completo
with open("sspx_dump_full.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"✅ Coleta finalizada! Total de posts salvos: {len(result)}")
print(f"📌 Posts únicos: {len(seen_posts)} | Comentários únicos: {len(seen_comments)}")
