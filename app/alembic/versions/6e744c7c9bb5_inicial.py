"""Inicial

Revision ID: 6e744c7c9bb5
Revises: 
Create Date: 2022-08-10 10:17:38.232950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e744c7c9bb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('PATIENTS', 'FIRST_NAME',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    op.alter_column('PATIENTS', 'LAST_NAME',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    op.alter_column('PATIENTS', 'DATE_OF_BIRTH',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.create_index(op.f('ix_PATIENTS_DATE_OF_BIRTH'), 'PATIENTS', ['DATE_OF_BIRTH'], unique=False)
    op.create_index(op.f('ix_PATIENTS_FIRST_NAME'), 'PATIENTS', ['FIRST_NAME'], unique=False)
    op.create_index(op.f('ix_PATIENTS_LAST_NAME'), 'PATIENTS', ['LAST_NAME'], unique=False)
    op.alter_column('PHARMACIES', 'NAME',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('PHARMACIES', 'CITY',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.create_index(op.f('ix_PHARMACIES_CITY'), 'PHARMACIES', ['CITY'], unique=False)
    op.create_index(op.f('ix_PHARMACIES_NAME'), 'PHARMACIES', ['NAME'], unique=False)
    op.create_index(op.f('ix_PHARMACIES_UUID'), 'PHARMACIES', ['UUID'], unique=False)
    op.alter_column('TRANSACTIONS', 'PATIENT_UUID',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('TRANSACTIONS', 'PHARMACY_UUID',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('TRANSACTIONS', 'AMOUNT',
               existing_type=sa.NUMERIC(),
               nullable=True)
    op.alter_column('TRANSACTIONS', 'TIMESTAMP',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.create_index(op.f('ix_TRANSACTIONS_AMOUNT'), 'TRANSACTIONS', ['AMOUNT'], unique=False)
    op.create_index(op.f('ix_TRANSACTIONS_TIMESTAMP'), 'TRANSACTIONS', ['TIMESTAMP'], unique=False)
    op.create_index(op.f('ix_TRANSACTIONS_UUID'), 'TRANSACTIONS', ['UUID'], unique=False)
    op.alter_column('USERS', 'USERNAME',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('USERS', 'PASSWORD',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.create_index(op.f('ix_USERS_PASSWORD'), 'USERS', ['PASSWORD'], unique=False)
    op.create_index(op.f('ix_USERS_USERNAME'), 'USERS', ['USERNAME'], unique=False)
    op.create_index(op.f('ix_USERS_UUID'), 'USERS', ['UUID'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_USERS_UUID'), table_name='USERS')
    op.drop_index(op.f('ix_USERS_USERNAME'), table_name='USERS')
    op.drop_index(op.f('ix_USERS_PASSWORD'), table_name='USERS')
    op.alter_column('USERS', 'PASSWORD',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('USERS', 'USERNAME',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.drop_index(op.f('ix_TRANSACTIONS_UUID'), table_name='TRANSACTIONS')
    op.drop_index(op.f('ix_TRANSACTIONS_TIMESTAMP'), table_name='TRANSACTIONS')
    op.drop_index(op.f('ix_TRANSACTIONS_AMOUNT'), table_name='TRANSACTIONS')
    op.alter_column('TRANSACTIONS', 'TIMESTAMP',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('TRANSACTIONS', 'AMOUNT',
               existing_type=sa.NUMERIC(),
               nullable=False)
    op.alter_column('TRANSACTIONS', 'PHARMACY_UUID',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('TRANSACTIONS', 'PATIENT_UUID',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_index(op.f('ix_PHARMACIES_UUID'), table_name='PHARMACIES')
    op.drop_index(op.f('ix_PHARMACIES_NAME'), table_name='PHARMACIES')
    op.drop_index(op.f('ix_PHARMACIES_CITY'), table_name='PHARMACIES')
    op.alter_column('PHARMACIES', 'CITY',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('PHARMACIES', 'NAME',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.drop_index(op.f('ix_PATIENTS_LAST_NAME'), table_name='PATIENTS')
    op.drop_index(op.f('ix_PATIENTS_FIRST_NAME'), table_name='PATIENTS')
    op.drop_index(op.f('ix_PATIENTS_DATE_OF_BIRTH'), table_name='PATIENTS')
    op.alter_column('PATIENTS', 'DATE_OF_BIRTH',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('PATIENTS', 'LAST_NAME',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    op.alter_column('PATIENTS', 'FIRST_NAME',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    # ### end Alembic commands ###
