"""empty message

Revision ID: d7695f89976f
Revises: 8ad62be11dd7
Create Date: 2025-04-23 10:19:37.039860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7695f89976f'
down_revision = '8ad62be11dd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint('comment_like_id_fkey', type_='foreignkey')
        batch_op.drop_column('like_id')

    with op.batch_alter_table('follower', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('comment_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])
        batch_op.create_foreign_key(None, 'comment', ['comment_id'], ['id'])

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('post_like_id_fkey', type_='foreignkey')
        batch_op.drop_column('like_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('like_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('post_like_id_fkey', 'likes', ['like_id'], ['id'])

    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('comment_id')
        batch_op.drop_column('post_id')

    with op.batch_alter_table('follower', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('like_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('comment_like_id_fkey', 'likes', ['like_id'], ['id'])

    # ### end Alembic commands ###
