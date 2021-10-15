from app.models import db, Character

def seed_characters():

    zooey = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/zooey-url.png',
        name='Zooey (Grand)',
        max_hp=1180,
        max_atk=9200,
        element_id=6,
        race_id=5,
        specialty_id=1,
        archetype_id=1,
        charge_attack_id=1,
    )
    predator = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Predator/predator-url.png',
        name='Predator',
        max_hp=1100,
        max_atk=10500,
        element_id=6,
        race_id=1,
        specialty_id=7,
        archetype_id=1,
        charge_attack_id=2,
    )
    rei = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Rei/rei-url.png',
        name='Rei (Grand)',
        max_hp=1000,
        max_atk=10000,
        element_id=6,
        race_id=4,
        specialty_id=5,
        archetype_id=7,
        charge_attack_id=3,
    )
    helel = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Helel/helel-url.png',
        name='Helel ben Shalem (Grand)',
        max_hp=1270,
        max_atk=8880,
        element_id=6,
        race_id=6,
        specialty_id=3,
        archetype_id=3,
        charge_attack_id=4,
    )
    olivia = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Olivia/olivia-url.png',
        name='Olivia (Grand)',
        max_hp=1480,
        max_atk=7800,
        element_id=6,
        race_id=5,
        specialty_id=1,
        archetype_id=8,
        charge_attack_id=5,
    )
    orchid = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Orchid/orchid-url.png',
        name='Orchid (Grand)',
        max_hp=1950,
        max_atk=8850,
        element_id=6,
        race_id=6,
        specialty_id=7,
        archetype_id=2,
        charge_attack_id=6,
    )
    black_knight = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-BlackKnight/blackknight-url.png',
        name='Black Knight (Grand)',
        max_hp=1780,
        max_atk=11850,
        element_id=6,
        race_id=1,
        specialty_id=1,
        archetype_id=1,
        charge_attack_id=7,
    )
    clarisse = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Clarisse/clarisse-url.png',
        name='Clarisse (Valentine)',
        max_hp=1214,
        max_atk=9130,
        element_id=6,
        race_id=1,
        specialty_id=5,
        archetype_id=3,
        charge_attack_id=8,
    )
    kolulu = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Kolulu/kolulu-url.png',
        name='Kolulu',
        max_hp=1190,
        max_atk=11100,
        element_id=6,
        race_id=1,
        specialty_id=3,
        archetype_id=1,
        charge_attack_id=9,
    )
    meg = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Meg/meg-url.png',
        name='Meg (Summer)',
        max_hp=1080,
        max_atk=10600,
        element_id=6,
        race_id=1,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=10,
    )
    narmaya = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Narmaya/narmiya-url.png',
        name='Narmaya',
        max_hp=1330,
        max_atk=12200,
        element_id=6,
        race_id=2,
        specialty_id=10,
        archetype_id=6,
        charge_attack_id=11,
    )
    vikala = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vikala/vikala-url.png',
        name='Vikala',
        max_hp=1750,
        max_atk=9000,
        element_id=6,
        race_id=1,
        specialty_id=7,
        archetype_id=4,
        charge_attack_id=13,
    )
    amira = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Amira/amira-url.png',
        name='Amira (Summer)',
        max_hp=1960,
        max_atk=6750,
        element_id=6,
        race_id=6,
        specialty_id=7,
        archetype_id=3,
        charge_attack_id=14,
    )
    anthuria = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Anthuria/anthuria-url.png',
        name='Anthuria (Yukata)',
        max_hp=1480,
        max_atk=7000,
        element_id=6,
        race_id=3,
        specialty_id=7,
        archetype_id=3,
        charge_attack_id=15,
    )
    tabina = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Tabina/tabina-url.png',
        name='Tabina (Summer)',
        max_hp=1245,
        max_atk=9775,
        element_id=6,
        race_id=1,
        specialty_id=8,
        archetype_id=5,
        charge_attack_id=16,
    )
    vaseraga = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vaseraga/vaseraga-url.png',
        name='Vaseraga',
        max_hp=1890,
        max_atk=13170,
        element_id=6,
        race_id=2,
        specialty_id=4,
        archetype_id=1,
        charge_attack_id=17,
    )
    wulf_and_renie = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Wulfandrenie/wulfandrenie-url.png',
        name='Wulf and Renie',
        max_hp=1480,
        max_atk=8600,
        element_id=6,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=18,
    )
    mimlemel = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Milemel/F-Mimlemel.png',
        name='Mimlemel (Summer)',
        max_hp=1150,
        max_atk=9240,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=19,
    )
    nemone= Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Nemone/F-Nemone.png',
        name='Nemone (Holiday)',
        max_hp=1460,
        max_atk=7100,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=20,
    )
    athena = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Athena/F-Athena.png',
        name='Athena',
        max_hp=2330,
        max_atk=8300,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=21,
    )
    kumbhira = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Kumbhira/F-Kumbhira.png',
        name='Kumbhira (Summer)',
        max_hp=1300,
        max_atk=11000,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=22,
    )
    anila = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Anila/F-Anila.png',
        name='Anila',
        max_hp=2015,
        max_atk=10415,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=23,
    )
    izmir = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Izmir/F-Izmir.png',
        name='Izmir (Yukata)',
        max_hp=1320,
        max_atk=10200,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=24,
    )
    shiva = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Shiva/F-Shiva.png',
        name='Shiva (Grand)',
        max_hp=1240,
        max_atk=11400,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=25,
    )
    siegfried = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Siefried/F-Siefried.png',
        name='Siegfried',
        max_hp=1200,
        max_atk=9200,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=26,
    )
    f_anthuria = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Anthuria/F-Anthuria.png',
        name='Anthuria',
        max_hp=1150,
        max_atk=7970,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=27,
    )
    yuisis = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Fire/F-Yuisis/F-Yuisis.png',
        name='Yuisis',
        max_hp=952,
        max_atk=9640,
        element_id=2,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=28,
    )
    poseidon = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Poseidon/W-Poseidon.png',
        name='Poseidon (Grand)',
        max_hp=1260,
        max_atk=9700,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=29,
    )
    cagliostro = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Cagliostro/W-Cagliostro.png',
        name='Cagliostro (Summer)',
        max_hp=1760,
        max_atk=6400,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=30,
    )
    w_helel = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Helel/W-Helel.png',
        name='Helel ben Shalem (Summer)',
        max_hp=1300,
        max_atk=8770,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=31,
    )
    vajra = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Vajra/W-Vajra.png',
        name='Vajra',
        max_hp=1340,
        max_atk=10420,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=32,
    )
    w_zeta = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Zeta/W-Zeta.png',
        name='Zeta',
        max_hp=1120,
        max_atk=10400,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=33,
    )
    lily = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Lily/W-Lily.png',
        name='Lily',
        max_hp=1876,
        max_atk=7720,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=34,
    )
    w_lucio = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Lucio/W-Lucio.png',
        name='Lucio (Summer)',
        max_hp=1700,
        max_atk=7800,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=35,
    )
    w_kolulu = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Kolulu/W-Kolulu.png',
        name='Kolulu (Summer)',
        max_hp=1160,
        max_atk=10050,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=36,
    )
    vane = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Vane/W-Vane.png',
        name='Vane',
        max_hp=2600,
        max_atk=8190,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=37,
    )
    europa = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Water/W-Europa/W-Europa.png',
        name='Europa (Grand)',
        max_hp=2000,
        max_atk=6800,
        element_id=1,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=38,
    )
    mahira = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Mahira/E_Mahira.png',
        name='Mahira',
        max_hp=1770,
        max_atk=10160,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=39,
    )
    e_narmaya = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Narmaya/E_Narmaya.png',
        name='Narmaya (Holiday)',
        max_hp=1185,
        max_atk=10885,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=40,
    )
    e_sandalphon = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Sandalphon/E_Sandalphon.png',
        name='Sandalphon (Grand)',
        max_hp=1080,
        max_atk=9800,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=41,
    )
    e_illnot = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Illnot/E_Illnot.png',
        name='Illnot (Summer)',
        max_hp=1330,
        max_atk=8550,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=42,
    )
    e_zeta_and_vaseraga = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Zeta_and_Vaseraga/E_Zeta_and_Vaseraga.png',
        name='Zeta and Vaseraga (Halloween)',
        max_hp=1520,
        max_atk=5200,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=43,
    )
    e_alexiel_summer = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Alexiel_Summer/E_Alexiel_Summer.png',
        name='Alexiel (Summer)',
        max_hp=1240,
        max_atk=9000,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=44,
    )
    golden_knight = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Golden_Knight/E_Golden_Knight.png',
        name='Golden Knight (Grand)',
        max_hp=1200,
        max_atk=10000,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=45,
    )
    pengy = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Pengy/E_Pengy.png',
        name='Pengy',
        max_hp=1280,
        max_atk=8800,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=46,
    )
    alexiel = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Alexiel/E_Alexiel.png',
        name='Alexiel (Grand)',
        max_hp=1960,
        max_atk=7000,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=47,
    )
    lamretta = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Earth/E_Lamretta/E_Lamretta.png',
        name='Lamretta',
        max_hp=1350,
        max_atk=9300,
        element_id=4,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=48,
    )
    andira = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi-Andira/Wi-Andira.png',
        name='Andira',
        max_hp=1660,
        max_atk=8940,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=49,
    )
    wi_narmaya = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi-Narmaya/Wi-Narmaya.png',
        name='Narmaya (Grand)',
        max_hp=1000,
        max_atk=11830,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=50,
    )
    grimnir = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi-Grimnir/Wi-Grimnir.png',
        name='Grimnir (Grand)',
        max_hp=1640,
        max_atk=7800,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=51,
    )
    valentine_grimnir = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi-Valentine-Grimnir/Wi-Valentine-Grimnir.png',
        name='Valentine Grimnir',
        max_hp=1214,
        max_atk=9900,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=52,
    )
    korwa = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi_Korwa/Wi_Korwa.png',
        name='Korwa',
        max_hp=1550,
        max_atk=6850,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=53,
    )
    lecia = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi_Lecia/Wi_Lecia.png',
        name='Lecia (Grand)',
        max_hp=1900,
        max_atk=8500,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=54,
    )
    summer_anila = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi_Summer_Anila/Wi_Summer_Anila.png',
        name='Summer Anila',
        max_hp=1400,
        max_atk=8990,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=55,
    )
    tiamat = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi_Tiamat/Wi_Tiamat.png',
        name='Tiamat',
        max_hp=1940,
        max_atk=8800,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=56,
    )
    yurius = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi_Yurius/Wi_Yurius.png',
        name='Yurius',
        max_hp=1930,
        max_atk=11550,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=57,
    )
    catura = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Wind/Wi_Catura/Wi_Catura.png',
        name='Catura',
        max_hp=1147,
        max_atk=11043,
        element_id=3,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=58,
    )
    nehan = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L-Nehan/L_Nehan.png',
        name='Nehan (Grand)',
        max_hp=1146,
        max_atk=7896,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=59,
    )
    jeanne_d_arc = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Jeanne_d\'Arc/L_Jeanne_d\'Arc.png',
        name='Jeanne d\'Arc (Grand)',
        max_hp=1580,
        max_atk=8400,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=60,
    )
    aglovale = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Aglovale/L_Aglovale.png',
        name='Aglovale',
        max_hp=1220,
        max_atk=9900,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=61,
    )
    l_cagliostro = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Cagliostro/L_Cagliostro.png',
        name='Cagliostro (Grand)',
        max_hp=1280,
        max_atk=8880,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=62,
    )
    hallessena = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Hallessena/L_Hallessena.png',
        name='Hallessena (Halloween)',
        max_hp=1090,
        max_atk=10800,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=63,
    )
    halluel_and_malluel = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Halluel_and_Malluel/L_Halluel_and_Malluel.png',
        name='Halluel and Malluel (Halloween)',
        max_hp=1600,
        max_atk=4000,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=64,
    )
    io = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Io/L_Io.png',
        name='Io (Grand)',
        max_hp=2100,
        max_atk=9140,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=65,
    )
    noa = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Noa/L_Noa.png',
        name='Noa (Grand)',
        max_hp=1100,
        max_atk=9700,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=66,
    )
    zahlhamelina_yukata = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Zahlhamelina/L_Zahlhamelina.png',
        name='Zahlhamelina (Yukata)',
        max_hp=1192,
        max_atk=9040,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=67,
    )
    lucio = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Lucio/L_Lucio.png',
        name='Lucio (Grand)',
        max_hp=1660,
        max_atk=7700,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=68,
    )
    l_nicholas = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Light/L_Nicholas/L_Nicholas.png',
        name='Nicholas',
        max_hp=1000,
        max_atk=11000,
        element_id=5,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=68,
    )


    db.session.add(zooey)
    db.session.add(predator)
    db.session.add(rei)
    db.session.add(helel)
    db.session.add(olivia)
    db.session.add(orchid)
    db.session.add(black_knight)
    db.session.add(clarisse)
    db.session.add(kolulu)
    db.session.add(meg)
    db.session.add(narmaya)
    db.session.add(vikala)
    db.session.add(amira)
    db.session.add(anthuria)
    db.session.add(tabina)
    db.session.add(vaseraga)
    db.session.add(wulf_and_renie)
    db.session.add(mimlemel)
    db.session.add(nemone)
    db.session.add(athena)
    db.session.add(kumbhira)
    db.session.add(anila)
    db.session.add(izmir)
    db.session.add(shiva)
    db.session.add(siegfried)
    db.session.add(f_anthuria)
    db.session.add(yuisis)
    db.session.add(poseidon)
    db.session.add(cagliostro)
    db.session.add(w_helel)
    db.session.add(vajra)
    db.session.add(w_zeta)
    db.session.add(lily)
    db.session.add(w_lucio)
    db.session.add(w_kolulu)
    db.session.add(vane)
    db.session.add(europa)
    db.session.add(mahira)
    db.session.add(e_narmaya)
    db.session.add(e_sandalphon)
    db.session.add(e_illnot)
    db.session.add(e_zeta_and_vaseraga)
    db.session.add(e_alexiel_summer)
    db.session.add(golden_knight)
    db.session.add(pengy)
    db.session.add(alexiel)
    db.session.add(lamretta)
    db.session.add(andira)
    db.session.add(wi_narmaya)
    db.session.add(grimnir)
    db.session.add(valentine_grimnir)
    db.session.add(korwa)
    db.session.add(lecia)
    db.session.add(summer_anila)
    db.session.add(tiamat)
    db.session.add(yurius)
    db.session.add(catura)
    db.session.add(nehan)
    db.session.add(jeanne_d_arc)
    db.session.add(aglovale)
    db.session.add(l_cagliostro)
    db.session.add(hallessena)
    db.session.add(halluel_and_malluel)
    db.session.add(io)
    db.session.add(noa)
    db.session.add(zahlhamelina_yukata)
    db.session.add(lucio)
    db.session.add(l_nicholas)

    db.session.commit()

def undo_characters():
    db.session.execute('TRUNCATE characters RESTART IDENTITY CASCADE;')
    db.session.commit()
