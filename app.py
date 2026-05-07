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
        "analysis": "Gyasi opens Effia's chapter by placing her literally above the dungeon where Esi is held, same building, different floors, different fates. This physical arrangement is the novel's central architectural metaphor. Privilege and suffering exist in the same space, separated by a floor they cannot see through. By keeping Effia unaware of what lies beneath her, Gyasi shows how complicity travels forward through ignorance rather than intention, and how that ignorance becomes the first thing Effia's descendants carry with them.",
        "quote": "She did not know about the dungeon. How could she?"
    },
    {
        "id": "esi",
        "name": "Esi",
        "line": "us",
        "subtitle": "Enslaved, taken to America",
        "generation": 1,
"analysis": "Gyasi gives Esi far less page time than Effia, a structural choice that mirrors how the historical record treats enslaved people. Where Effia's chapter moves slowly and domestically, Esi's is compressed and immediate. The stone necklace Maame gives only to Effia becomes the novel's symbol of what the American line will spend generations searching for, a traceable inheritance. Every subsequent American chapter is shaped by this original separation.",
        "quote": "The first night Esi slept in the dungeon, she dreamed of the fish."
    },
    {
        "id": "quey",
        "name": "Quey",
        "line": "gh",
        "subtitle": "Mixed-race, complicit in trade",
        "generation": 2,
        "analysis": "Gyasi structures Quey's chapter as an inheritance problem. He receives Effia's position of proximity to British power and must decide what to do with it. Where Effia's complicity was passive, Quey's is deliberate. This escalation across generations is one of Gyasi's key structural moves: each Ghana chapter raises the moral stakes rather than resetting them, showing how the choices of one generation become the starting conditions for the next.",
        "quote": "He had to choose between two worlds — and chose the one that would destroy him."
    },
    {
        "id": "ness",
        "name": "Ness",
        "line": "us",
        "subtitle": "Enslaved on Alabama plantation",
        "generation": 2,
        "analysis": "Ness's chapter is structured around what she is prevented from passing on. Gyasi shows her love for her son Sam turned into leverage against her, and then removes Sam from the narrative entirely, as he is removed from her life. This is how Gyasi builds inherited trauma in the American line: as an absence rather than a presence. Each generation begins already missing something they have no words for.",
        "quote": "Her love for Sam was the one thing they had not taken. So they took Sam."
    },
    {
        "id": "james",
        "name": "James",
        "line": "gh",
        "subtitle": "Caught in colonial change",
        "generation": 3,
        "analysis": "James inherits Quey's wealth but arrives in a changed world. Gyasi uses his chapter to show how colonialism reshapes the terms of inheritance itself, with the slave trade now illegal and British Christianity rewriting what it means to be Ghanaian. Each Ghana chapter hands the next generation a transformed landscape and asks them to reconstruct identity from whatever the colonial system has left available to them.",
        "quote": "James stood between two worlds, belonging fully to neither."
    },
    {
        "id": "kojo",
        "name": "Kojo",
        "line": "us",
        "subtitle": "Free Black man, always hunted",
        "generation": 3,
        "analysis": "Kojo's chapter arrives after legal emancipation and demonstrates how the underlying structure of control persists. Gyasi builds the American chapters so that each generation inherits the previous one's wound in a new legal form. Esi was enslaved by law, Ness by ownership, and Kojo lives under the Fugitive Slave Act, which keeps his freedom conditional. The wound is continuous; the legal vocabulary around it simply updates with each generation.",
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
        "analysis": "Gyasi places H's chapter deliberately after the Civil War to make a structural argument about legal change and lived reality. H inherits Kojo's conditional freedom and watches it collapse through the convict leasing system, where criminal justice becomes the new mechanism for forced labor. His name, reduced to a single letter, echoes how Esi was reduced to property. The American line carries the same wound forward, rebranded by each era into its acceptable legal form.",
        "quote": "His name was H. He had been given it the day he arrived at the mine."
    },
    {
        "id": "akua",
        "name": "Akua",
        "line": "gh",
        "subtitle": "Haunted by fire, trauma passed on",
        "generation": 5,
        "analysis": "Akua's chapter is where Gyasi makes the generational transmission of trauma most visible. Akua has no direct memory of the slave trade yet carries a recurring dream of a woman made of fire, an image that descends from violence she never witnessed. Gyasi uses this to show that trauma travels through bodies and dreams and silences rather than through conscious memory. What one generation experienced becomes the next generation's haunting.",
        "quote": "She had the fire dream again. The woman made of fire, walking."
    },
    {
        "id": "willie",
        "name": "Willie",
        "line": "us",
        "subtitle": "Great Migration north to Harlem",
        "generation": 5,
        "analysis": "Willie's chapter is structured around the promise of geographic change. She moves north during the Great Migration seeking a different life, and Gyasi shows her finding Harlem full of possibility and also full of people carrying the same wounds she hoped to leave behind. The American chapters follow a pattern: each generation reaches toward a new form of freedom, and Gyasi honors that reach while also tracing how deeply the inherited damage runs beneath it.",
        "quote": "She had moved north to leave everything behind. But she had brought herself with her."
    },
    {
        "id": "yaw",
        "name": "Yaw",
        "line": "gh",
        "subtitle": "Scarred by mother's fire",
        "generation": 6,
        "analysis": "Yaw's chapter is Gyasi's most direct statement about the novel's own project. As a history teacher, he pushes his students to ask not just what happened but why, and who shaped the telling. His facial scars are Akua's trauma made visible on his body, the clearest image in the novel of how one generation's crisis becomes the next generation's defining mark. Gyasi places this chapter near the end to frame everything the reader has witnessed as precisely the kind of history Yaw is asking us to examine.",
        "quote": "We cannot know what we do not ask. History is not the things that happened. It is the story we tell about them."
    },
    {
        "id": "sonny",
        "name": "Sonny",
        "line": "us",
        "subtitle": "Heroin, jazz, 1960s activism",
        "generation": 6,
        "analysis": "Sonny's chapter places him inside the Civil Rights Movement and shows him reaching toward it with genuine desire. Gyasi structures this chapter to show that political liberation and personal healing operate on separate timelines. The movement reshapes the law; it does not reach the interior damage that four generations of inherited silence have built up inside one family. Sonny wants to be present for the history happening around him, and Gyasi shows how much it costs him that he cannot always get there.",
        "quote": "The movement was everywhere, but Sonny could not always find himself inside it."
    },
    {
        "id": "marjorie",
        "name": "Marjorie",
        "line": "gh",
        "subtitle": "Between two worlds",
        "generation": 7,
        "analysis": "Marjorie's chapter is noticeably shorter than those before it, a structural signal that Gyasi is compressing time as the two lines draw together. She grows up moving between Ghana and America, inheriting the Ghana line's layered identity and carrying it into new territory. Her chapter exists to bring her into the same space as Marcus, and Gyasi is intentional about this: the final generation's work is contact and recognition rather than resolution.",
        "quote": "She was always between two worlds, and she had stopped trying to choose."
    },
    {
        "id": "marcus",
        "name": "Marcus",
        "line": "us",
        "subtitle": "Returns to Ghana, finds the origin",
        "generation": 7,
        "analysis": "Marcus's chapter closes the novel by having him physically return to the place Esi was taken from. Gyasi gives him the work of tracing the prison-to-poverty pipeline as his academic research, meaning he is studying the same system that consumed H, now from the outside as a scholar. When he swims in the ocean at Cape Coast, Gyasi completes the structural circle. The American line returns to the moment of original rupture. The circle closes, and Gyasi lets it rest there, with Marcus holding a stone and not yet knowing about the necklace.",
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
