from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix = "/item",
    tags = ["item"]
)

@router.get("/all/")
def getallitems(nm:str, quantity:int):
    return {"message": f"we have {quantity} items of {nm}"}

@router.get("/category/{category}")
def items_category(category:Optional[str], nm:str, quantity:int):
    if category:
        return {"message": f"we have {nm} {category} of quantity {quantity}"}
    return {"message": f"we have {nm} of quantity {quantity}"}

@router.get("/{id}")
def getItem(id:int):
    return {"message": f"Item with id {id}"}



