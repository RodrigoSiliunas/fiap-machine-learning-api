from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.param_functions import Body
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlmodel import select
from typing import List

from app.configs.database import engine
from app.models import Product, User

from app.packages.Auth import (
    get_current_user
)

router = APIRouter(prefix="/v1")


@router.get('/products', response_model=List[Product])
async def get_all_products(user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        products = session.exec(select(Product)).all()

        return JSONResponse({"success": {
            "message": "Products fetched successfully.",
            "type": "ProductInfo",
            "code": 200
        }, "products": products}, status.HTTP_200_OK)


@router.get('/products/{id}', response_model=Product)
async def get_product(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        product = session.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Product not found."}}
            )

        return JSONResponse({"success": {
            "message": "Product fetched successfully.",
            "type": "ProductInfo",
            "code": 200
        }, "product": product}, status.HTTP_200_OK)


@router.get('/products/{name}', response_model=Product)
async def get_product_by_name(name: str, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        product = session.query(Product).filter(Product.name == name).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Product not found."}}
            )

        return JSONResponse({"success": {
            "message": "Product fetched successfully.",
            "type": "ProductInfo",
            "code": 200
        }, "product": product}, status.HTTP_200_OK)


@router.get('/products/category/{category}', response_model=List[Product])
async def get_products_by_category(category: str, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        products = session.query(Product).filter(
            Product.category == category).all()

        if not products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Products category not found."}}
            )

        return JSONResponse({"success": {
            "message": "Products fetched successfully.",
            "type": "ProductInfo",
            "code": 200
        }, "products": products}, status.HTTP_200_OK)
