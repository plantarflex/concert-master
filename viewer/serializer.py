from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from models import *


class PerformSchema(ModelSchema):
    class Meta:
        model = Perform
