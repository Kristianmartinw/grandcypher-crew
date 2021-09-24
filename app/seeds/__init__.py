from app.seeds.charge_attacks import seed_charge_attacks
from flask.cli import AppGroup
from .users import seed_users, undo_users
from .charge_attacks import seed_charge_attacks, undo_charge_attacks
from .archetypes import seed_archetypes, undo_archetypes
from .elements import seed_elements, undo_elements
from .races import seed_races, undo_races
from .specialties import seed_specialties, undo_specialties
from .parties import seed_parties, undo_parties
from .characters import seed_characters, undo_characters
from .skills import seed_skills, undo_skills
from .archetype_values import seed_archetype_values, undo_archetype_values
from .character_party_joins import seed_character_party_joins, undo_character_party_joins
from .support_skills import seed_support_skills, undo_support_skills

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    seed_users()
    seed_charge_attacks()
    seed_archetypes()
    seed_elements()
    seed_races()
    seed_specialties()
    seed_parties()
    seed_characters()
    seed_skills()
    seed_archetype_values()
    seed_character_party_joins()
    seed_support_skills()


@seed_commands.command('undo')
def undo():
    undo_users()
    undo_charge_attacks()
    undo_archetypes()
    undo_elements()
    undo_races()
    undo_specialties()
    undo_parties()
    undo_characters()
    undo_skills()
    undo_archetype_values()
    undo_character_party_joins()
    undo_support_skills()
