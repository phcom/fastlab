""" Item model.
"""
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Item(models.Model):
    """
    The Item model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)
    description = fields.TextField(null=True)
    price = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ["price"]
    

Item_Pydantic = pydantic_model_creator(Item, name="Item")
ItemIn_Pydantic = pydantic_model_creator(Item, name="ItemIn", exclude_readonly=True)
