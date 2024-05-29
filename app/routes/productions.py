from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List

from app.configs.database import engine
from app.models import Product, Production, User

from app.packages.Auth import (
    get_current_user
)

router = APIRouter(prefix="/v1")


@router.get('/productions', response_model=List[Production])
async def get_productions(user: User = Depends(get_current_user),
                          limit: int = Query(10, ge=1, le=100),
                          offset: int = Query(0, ge=0)
                          ) -> JSONResponse:
    with Session(engine) as session:
        productions = session.exec(
            select(Production).offset(offset).limit(limit)
        ).all()

        total_productions = session.exec(select(Production)).count()

        return JSONResponse({
            "success": {
                "message": "Productions fetched successfully.",
                "type": "ProductionInfo",
                "code": 200
            },
            "productions": productions,
            "pagination": {
                "total": total_productions,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/productions/{id}', response_model=Production)
async def get_production(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        production = session.query(Production).filter(
            Production.id == id).first()

        if not production:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Production not found.",
                                  "type": "ProductionInfo", "code": 404}}
            )

        return JSONResponse({"success": {
            "message": "Production fetched successfully.",
            "type": "ProductionInfo",
            "code": 200
        }, "product": production}, status.HTTP_200_OK)


@router.get('/productions/product/{product_id}', response_model=List[Production])
async def get_productions_by_product_id(product_id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        productions = session.query(Production).filter(
            Production.product_id == product_id).all()

        if not productions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Production not found.",
                                  "type": "ProductionInfo", "code": 404}}
            )

        return JSONResponse({"success": {
            "message": "Productions fetched successfully.",
            "type": "ProductionInfo",
            "code": 200
        }, "products": productions}, status.HTTP_200_OK)


@router.get('/productions/product/{product_name}', response_model=List[Production])
async def get_productions_by_product_name(product_name: str, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        product = session.query(Product).filter(
            Product.name == product_name).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Product not found.",
                                  "type": "ProductInfo", "code": 404}}
            )

        productions = session.query(Production).filter(
            Production.product_id == product.id).all()

        if not productions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Production not found.",
                                  "type": "ProductionInfo", "code": 404}}
            )

        return JSONResponse({"success": {
            "message": "Productions fetched successfully.",
            "type": "ProductionInfo",
            "code": 200
        }, "products": productions}, status.HTTP_200_OK)


@router.get('/productions/year/{year}', response_model=List[Production])
async def get_productions_by_year(year: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        productions = session.query(Production).filter(
            Production.year == year).all()

        if not productions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Production not found.",
                                  "type": "ProductionInfo", "code": 404}}
            )

        return JSONResponse({"success": {
            "message": "Productions fetched successfully.",
            "type": "ProductionInfo",
            "code": 200
        }, "products": productions}, status.HTTP_200_OK)


@router.get('/productions/year', response_model=List[Production])
async def get_productions_by_year_range(min_year: int, max_year: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        productions = session.exec(
            select(Production).where(
                Production.year >= min_year,
                Production.year <= max_year
            )
        ).all()

        if not productions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Productions not found.",
                                  "type": "ProductionInfo", "code": 404}}
            )

        return JSONResponse({
            "success": {
                "message": "Productions fetched successfully.",
                "type": "ProductionInfo",
                "code": 200
            },
            "productions": productions
        }, status_code=status.HTTP_200_OK)


@router.get('/productions/category/{category}', response_model=List[Production])
async def get_productions_by_category(category: str, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        productions = session.query(Production).filter(
            Production.category == category).all()

        if not productions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Production not found.",
                                  "type": "ProductionInfo", "code": 404}}
            )

        return JSONResponse({"success": {
            "message": "Productions fetched successfully.",
            "type": "ProductionInfo",
            "code": 200
        }, "products": productions}, status.HTTP_200_OK)
