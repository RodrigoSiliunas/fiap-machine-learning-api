from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List

from app.configs.database import engine
from app.models import User, Commercialization, Product

from app.packages.Auth import (
    get_current_user
)

router = APIRouter(prefix="/v1")


@router.get('/commercializations')
async def get_commercializations(limit: int = Query(10, ge=1, le=100),
                                 offset: int = Query(0, ge=0),
                                 user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        commercializations = session.query(Commercialization).offset(offset).limit(limit).all()

        total_commercializations = session.query(Commercialization).count()

        return JSONResponse({
            "success": {
                "message": "Commercializations fetched successfully.",
                "type": "CommercializationInfo",
                "code": 200
            },
            "commercializations": jsonable_encoder(commercializations),
            "pagination": {
                "total": jsonable_encoder(total_commercializations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/commercializations/{id}')
async def get_commercialization(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        commercialization = session.query(Commercialization).filter(
            Commercialization.id == id).first()

        if not commercialization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Commercialization not found."}}
            )

        return JSONResponse({
            "success": {
                "message": "Commercialization fetched successfully.",
                "type": "CommercializationInfo",
                "code": 200
            },
            "commercialization": commercialization
        }, status_code=status.HTTP_200_OK)


@router.get('/commercializations/product/{product_id}', response_model=List[Commercialization])
async def get_commercializations_by_product(product_id: int,
                                            limit: int = Query(
                                                10, ge=1, le=100),
                                            offset: int = Query(0, ge=0),
                                            user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        commercializations = session.query(Commercialization).where(
            Commercialization.product_id == product_id).offset(offset).limit(limit).all()

        if not commercializations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Commercialization not found."}}
            )

        total_commercializations = session.query(Commercialization).where(Commercialization.product_id == product_id).count()

        return JSONResponse({
            "success": {
                "message": "Commercializations fetched successfully.",
                "type": "CommercializationInfo",
                "code": 200
            },
            "commercializations": jsonable_encoder(commercializations),
            "pagination": {
                "total": jsonable_encoder(total_commercializations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/commercializations/product/name/{product_name}', response_model=List[Commercialization])
async def get_commercializations_by_product(product_name: str,
                                            limit: int = Query(
                                                10, ge=1, le=100),
                                            offset: int = Query(0, ge=0),
                                            user: User = Depends(get_current_user),) -> JSONResponse:
    with Session(engine) as session:
        product = session.query(Product).where(Product.name == product_name).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Product not found."}}
            )

        commercializations = session.query(Commercialization).where(
                Commercialization.product_id == product.id).offset(offset).limit(limit).all()

        total_commercializations = session.query(Commercialization).where(Commercialization.product_id == product.id).count()

        return JSONResponse({
            "success": {
                "message": "Commercializations fetched successfully.",
                "type": "CommercializationInfo",
                "code": 200
            },
            "commercializations": jsonable_encoder(commercializations),
            "pagination": {
                "total": jsonable_encoder(total_commercializations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/commercializations/year/{year}', response_model=List[Commercialization])
async def get_commercializations_by_year(year: int,
                                         limit: int = Query(
                                             10, ge=1, le=100),
                                         offset: int = Query(0, ge=0),
                                         user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        commercializations = session.query(Commercialization).where(
                Commercialization.year == year).offset(offset).limit(limit).all()

        if not commercializations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Commercialization not found."}}
            )

        total_commercializations = session.query(Commercialization).where(Commercialization.year == year).count()

        return JSONResponse({
            "success": {
                "message": "Commercializations fetched successfully.",
                "type": "CommercializationInfo",
                "code": 200
            },
            "commercializations": jsonable_encoder(commercializations),
            "pagination": {
                "total": jsonable_encoder(total_commercializations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/commercializations/years/range', response_model=List[Commercialization])
async def get_commercializations_by_year_range(start_year: int,
                                               end_year: int,
                                               limit: int = Query(
                                                   10, ge=1, le=100),
                                               offset: int = Query(0, ge=0),
                                               user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        commercializations = session.query(Commercialization).where(
                Commercialization.year >= start_year,
                Commercialization.year <= end_year).offset(offset).limit(limit).all()

        if not commercializations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Commercialization not found."}}
            )

        total_commercializations = session.query(Commercialization).where(Commercialization.year >= start_year,
                                            Commercialization.year <= end_year).count()

        return JSONResponse({
            "success": {
                "message": "Commercializations fetched successfully.",
                "type": "CommercializationInfo",
                "code": 200
            },
            "commercializations": jsonable_encoder(commercializations),
            "pagination": {
                "total": jsonable_encoder(total_commercializations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)
