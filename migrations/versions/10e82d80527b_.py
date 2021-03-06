"""empty message

Revision ID: 10e82d80527b
Revises: 
Create Date: 2021-10-03 21:50:24.953021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10e82d80527b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('archetypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('charge_attacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charge_attack_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('elements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('element_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('races',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('race_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('specialties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specialty_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_url', sa.String(), nullable=True),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('max_hp', sa.Integer(), nullable=True),
    sa.Column('max_atk', sa.Integer(), nullable=True),
    sa.Column('element_id', sa.Integer(), nullable=True),
    sa.Column('race_id', sa.Integer(), nullable=True),
    sa.Column('specialty_id', sa.Integer(), nullable=True),
    sa.Column('archetype_id', sa.Integer(), nullable=True),
    sa.Column('charge_attack_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['archetype_id'], ['archetypes.id'], ),
    sa.ForeignKeyConstraint(['charge_attack_id'], ['charge_attacks.id'], ),
    sa.ForeignKeyConstraint(['element_id'], ['elements.id'], ),
    sa.ForeignKeyConstraint(['race_id'], ['races.id'], ),
    sa.ForeignKeyConstraint(['specialty_id'], ['specialties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('archetype_values',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('enmity_value', sa.Integer(), nullable=True),
    sa.Column('stamina_value', sa.Integer(), nullable=True),
    sa.Column('sustain_value', sa.Integer(), nullable=True),
    sa.Column('ougi_value', sa.Integer(), nullable=True),
    sa.Column('skill_damage_value', sa.Integer(), nullable=True),
    sa.Column('otk_value', sa.Integer(), nullable=True),
    sa.Column('multi_value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character_party_joins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('party_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['party_id'], ['parties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('party_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['party_id'], ['parties.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('skill_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('support_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('support_skill_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('support_skills')
    op.drop_table('skills')
    op.drop_table('ratings')
    op.drop_table('character_party_joins')
    op.drop_table('archetype_values')
    op.drop_table('parties')
    op.drop_table('characters')
    op.drop_table('users')
    op.drop_table('specialties')
    op.drop_table('races')
    op.drop_table('elements')
    op.drop_table('charge_attacks')
    op.drop_table('archetypes')
    # ### end Alembic commands ###
