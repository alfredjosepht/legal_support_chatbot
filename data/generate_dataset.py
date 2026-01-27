import random
import csv

domains = {
    "physical_violence": [
        "senior punched me",
        "i was beaten by classmates",
        "someone attacked me in hostel",
        "i was slapped by a senior",
        "assaulted by students"
    ],
    "sexual_offence": [
        "someone touched me without consent",
        "received sexual messages",
        "teacher made sexual comments",
        "forced into inappropriate contact",
        "senior tried to molest me"
    ],
    "threat_intimidation": [
        "senior is threatening me",
        "received death threats",
        "warned not to complain",
        "threatened by classmates",
        "intimidated by seniors"
    ],
    "ragging": [
        "forced humiliating acts",
        "ragged daily in hostel",
        "forced to clean rooms",
        "verbal and physical ragging",
        "harassed by seniors"
    ],
    "cyber_crime": [
        "fake instagram account created",
        "online harassment",
        "threats on whatsapp",
        "photos shared without consent",
        "cyber bullying"
    ],
    "discrimination_hate": [
        "abused for my caste",
        "religious discrimination",
        "racist remarks in class",
        "excluded due to caste",
        "harassed for religion"
    ],
    "institutional_misconduct": [
        "college holding certificates",
        "tc not given",
        "forced to sign bond",
        "documents withheld",
        "administration harassment"
    ],
    "stalking": [
        "someone following me",
        "constant messages from person",
        "being stalked online",
        "followed after class",
        "stalker in hostel"
    ],
    "kidnapping_confinement": [
        "locked in room",
        "prevented from leaving",
        "held against will",
        "confined by students",
        "forced to stay inside"
    ],
    "financial_exploitation": [
        "forced to give money",
        "money extorted",
        "forced to pay seniors",
        "financial harassment",
        "money demanded under threat"
    ],
    "defamation": [
        "false rumors spread",
        "reputation damaged",
        "false allegations online",
        "character assassination",
        "fake complaints filed"
    ],
    "substance_abuse": [
        "forced to drink alcohol",
        "forced to consume drugs",
        "pressured to smoke",
        "drug use forced",
        "illegal substances pushed"
    ],
    "mental_harassment": [
        "constant mental harassment",
        "psychological abuse",
        "verbal abuse daily",
        "emotionally tortured",
        "mental pressure from teachers"
    ],
    "mixed_or_unclear": [
        "i feel unsafe",
        "college environment is bad",
        "many problems in college",
        "dont know what to do",
        "something wrong happening"
    ]
}

TARGET_PER_DOMAIN = 80   # 80 × ~13 domains ≈ 1000+

rows = []

for domain, phrases in domains.items():
    for _ in range(TARGET_PER_DOMAIN):
        sentence = random.choice(phrases)
        rows.append([sentence, domain])

random.shuffle(rows)

with open("data/training/domain_dataset_generated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "domain"])
    writer.writerows(rows)

print("✅ Generated dataset:", len(rows), "samples")
