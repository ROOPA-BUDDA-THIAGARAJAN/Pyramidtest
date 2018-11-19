"""init

Revision ID: c75316d85d29
Revises: 4ce8827a239e
Create Date: 2018-11-13 13:08:26.024052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c75316d85d29'
down_revision = '4ce8827a239e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_roles_email_user_info', 'roles', type_='foreignkey')
    op.create_foreign_key(op.f('fk_roles_email_user_info'), 'roles', 'user_info', ['email'], ['email'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_roles_email_user_info'), 'roles', type_='foreignkey')
    op.create_foreign_key('fk_roles_email_user_info', 'roles', 'user_info', ['email'], ['email'])
    # ### end Alembic commands ###
