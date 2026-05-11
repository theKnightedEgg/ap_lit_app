import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

CHARACTERS = [
    {
        "id": "effia",
        "name": "Effia",
        "line": "gh",
        "subtitle": "Marries British officer",
        "generation": 1,
        "analysis": "Effia's chapter is about her marrying a British soldier. As she lives in luxury above the Cape Coast Castle, she does not know that below her, her sister is being kept and sold into slavery. She keeps the black stone, and her family's association with the slave trade shapes the rest of the Ghanian side of the story.",
        "quote": "She did not know about the dungeon. How could she?"
    },
    {
        "id": "esi",
        "name": "Esi",
        "line": "us",
        "subtitle": "Enslaved, taken to America",
        "generation": 1,
"analysis": "On the other hand, Esi is kept in the dungeon, where she is kept in horrific conditions. In contrast to Effia, she loses the black stone, symbolizing her severance with Africa and shaping the American line of the story.",
        "quote": "The first night Esi slept in the dungeon, she dreamed of the fish."
    },
    {
        "id": "quey",
        "name": "Quey",
        "line": "gh",
        "subtitle": "Mixed-race, complicit in trade",
        "generation": 2,
        "analysis": "Quey is directly affected by Effia's marriage into British society. He is surrounded by the British slave trade, and decides to actively take part in it as a slaver. This active decision to propagate slavery passes down a curse through the rest of the Ghana line.",
        "quote": "He had to choose between two worlds — and chose the one that would destroy him."
    },
    {
        "id": "ness",
        "name": "Ness",
        "line": "us",
        "subtitle": "Enslaved on Alabama plantation",
        "generation": 2,
        "analysis": "Ness is enslaved on an Alabama plantation, and her story is focused on how slavery has stripped away African heritage by showing her forcibly disconnected from her son. She is shown basically losing everything when she tries to escape from \"Hell\". She has to give up Kojo so he can escape, and Sam is taken from her.",
        "quote": "Her love for Sam was the one thing they had not taken. So they took Sam."
    },
    {
        "id": "james",
        "name": "James",
        "line": "gh",
        "subtitle": "Caught in colonial change",
        "generation": 3,
        "analysis": "James' chapter shows how he inherits the identity of a slaver, showing how the legacy of slavery exists long after it has been legally banned by the British. He is shunned by people for being associated with slavers, but also inherits lots of wealth. In the end, he decides to escape an arranged marriage to marry for love, but his privilege prevents saves his life, showing that he can never truly escape his family's legacy of slavery.",
        "quote": "James stood between two worlds, belonging fully to neither."
    },
    {
        "id": "kojo",
        "name": "Kojo",
        "line": "us",
        "subtitle": "Free Black man, always hunted",
        "generation": 3,
        "analysis": "H's chapter shows how even after slavery is abolished, the same structure is still in place to make sure that African-Americans never truly get freedom. Very shortly after he is freed from slavery, he is accused of a crime he did not commit and sent to work in the coal mines. However, this chapter also marks the beginning of a new African-American identity. He manages to settle down and finally break the cycle of the American line being constantly disconnected from their",
        "quote": "He was free, but free in the way that a fish in a net is free."
    },
    {
        "id": "abena",
        "name": "Abena",
        "line": "gh",
        "subtitle": "Famine, Christianity's arrival",
        "generation": 4,
        "analysis": "Abena's chapter shows Gyasi shifting the Ghana line's inherited wound toward a new form of subjugation. The cocoa trade and missionary Christianity arrive together, and Abena must navigate economic survival alongside cultural transformation. Gyasi structures this chapter to show how empire operates across generations through slow replacement rather than a single rupture, with each generation absorbing a little more of what the previous one was told to let go.",
        "quote": "The missionaries came with a Bible. The British came with maps. Together they took everything."
    },
    {
        "id": "h",
        "name": "H",
        "line": "us",
        "subtitle": "Convict leased into coal mines",
        "generation": 4,
        "analysis": "H's chapter shows how even after slavery is abolished, the same structure is still in place to make sure that African-Americans never truly get freedom. Very shortly after he is freed from slavery, he is accused of a crime he did not commit and sent to work in the coal mines. However, this chapter also marks the beginning of a new African-American identity. He manages to settle down and finally break the cycle of the American line being constantly disconnected from their parents.",
        "quote": "His name was H. He had been given it the day he arrived at the mine."
    },
    {
        "id": "akua",
        "name": "Akua",
        "line": "gh",
        "subtitle": "Haunted by fire, trauma passed on",
        "generation": 5,
        "analysis": "Akua has no direct memory of the slave trade yet carries a recurring dream of a woman made of fire, an image that descends from violence she never witnessed. Gyasi uses this to show that trauma travels through bodies and dreams and silences rather than through conscious memory.",
        "quote": "She had the fire dream again. The woman made of fire, walking."
    },
    {
        "id": "willie",
        "name": "Willie",
        "line": "us",
        "subtitle": "Great Migration north to Harlem",
        "generation": 5,
        "analysis": "Willie's chapter is structured around the promise of geographic change. She moves north during the Great Migration seeking a different life, and she finds Harlem full of possibility and also full of people carrying the same wounds she hoped to leave behind. The American chapters follow a pattern: each generation reaches toward a new form of freedom while also tracing how deeply the inherited damage runs beneath it.",
        "quote": "She had moved north to leave everything behind. But she had brought herself with her."
    },
    {
        "id": "yaw",
        "name": "Yaw",
        "line": "gh",
        "subtitle": "Scarred by mother's fire",
        "generation": 6,
        "analysis": "As a history teacher, Yaw pushes his students to ask not just what happened but why, and who shaped the telling. His facial scars are Akua's trauma from their family's involvement in slavery made visible on his body, the clearest image in the novel of how one generation's crisis defines the next. Gyasi places this chapter near the end to frame everything the reader has witnessed as precisely the kind of history Yaw is asking us to examine.",
        "quote": "We cannot know what we do not ask. History is not the things that happened. It is the story we tell about them."
    },
    {
        "id": "sonny",
        "name": "Sonny",
        "line": "us",
        "subtitle": "Heroin, jazz, 1960s activism",
        "generation": 6,
        "analysis": "Sonny's story starts with him as a civil rights activist. However, he gets increasingly and increasingly frustrated when he realizes that he is powerless. Eventually, he turns to heroin to try to forget that sense of powerlessness, but is eventually rescued from the addiction by his mother Willie. His chapter shows both the importance of heritage and the dangers of being African-American. The book states that if not for his mother, he would have just been another crackhead, but his African-American heritage is what made the government target him with heroin in the first place.",
        "quote": "The movement was everywhere, but Sonny could not always find himself inside it."
    },
    {
        "id": "marjorie",
        "name": "Marjorie",
        "line": "gh",
        "subtitle": "Between two worlds",
        "generation": 7,
        "analysis": "Marjorie's chapter starts with her growing up moving between Ghana and America, inheriting the Ghana line's layered identity and carrying it into new territory. However, she is conflicted between these two identities. Her chapter also exists to bring her into the same space as Marcus, and builds towards contact and recognition rather than resolution.",
        "quote": "She was always between two worlds, and she had stopped trying to choose."
    },
    {
        "id": "marcus",
        "name": "Marcus",
        "line": "us",
        "subtitle": "Returns to Ghana, finds the origin",
        "generation": 7,
        "analysis": "Marcus's chapter closes the novel by having him physically return to the place Esi was taken from. Gyasi gives him the work of tracing the prison-to-poverty pipeline as his academic research, meaning he is studying the same system that consumed H, now from the outside as a scholar. When he swims in the ocean at Cape Coast, Gyasi completes the structural circle.",
        "quote": "He dove into the water and felt everything."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/characters")
def characters():
    return jsonify(CHARACTERS)


@app.route("/api/character/<char_id>")
def character(char_id):
    char = next((c for c in CHARACTERS if c["id"] == char_id), None)
    if char:
        return jsonify(char)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))
