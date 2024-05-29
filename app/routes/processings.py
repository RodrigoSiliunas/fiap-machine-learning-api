from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List

from app.configs.database import engine
from app.models import User, Processing

from app.packages.Auth import (
    get_current_user
)

router = APIRouter(prefix="/v1")


@router.get('/processings', response_model=List[Processing])
async def get_processings(user: User = Depends(get_current_user),
                          limit: int = Query(10, ge=1, le=100),
                          offset: int = Query(0, ge=0)
                          ) -> JSONResponse:
    with Session(engine) as session:
        processings = session.exec(
            select(Processing).offset(offset).limit(limit)
        ).all()

        total_processings = session.exec(select(Processing)).count()

        return JSONResponse({
            "success": {
                "message": "Processings fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processings": processings,
            "pagination": {
                "total": total_processings,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/processings/{id}', response_model=Processing)
async def get_processing(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        processing = session.query(Processing).filter(
            Processing.id == id).first()

        if not processing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Processing not found."}}
            )

        return JSONResponse({
            "success": {
                "message": "Processing fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processing": processing
        }, status_code=status.HTTP_200_OK)


@router.get('/processings/product/{product_name}', response_model=List[Processing])
async def get_processings_by_product(product_name: str, user: User = Depends(get_current_user),
                                     limit: int = Query(10, ge=1, le=100),
                                     offset: int = Query(0, ge=0)
                                     ) -> JSONResponse:
    with Session(engine) as session:
        processings = session.exec(
            select(Processing).where(Processing.product_name ==
                                     product_name).offset(offset).limit(limit)
        ).all()

        if not processings:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Processings not found."}}
            )

        total_processings = session.exec(
            select(Processing).where(Processing.product_name == product_name)
        ).count()

        return JSONResponse({
            "success": {
                "message": "Processings fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processings": processings,
            "pagination": {
                "total": total_processings,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/processings/category/{category}', response_model=List[Processing])
async def get_processings_by_category(category: str, user: User = Depends(get_current_user),
                                      limit: int = Query(10, ge=1, le=100),
                                      offset: int = Query(0, ge=0)
                                      ) -> JSONResponse:
    with Session(engine) as session:
        processings = session.exec(
            select(Processing).where(Processing.category ==
                                     category).offset(offset).limit(limit)
        ).all()

        if not processings:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Processings not found."}}
            )

        total_processings = session.exec(
            select(Processing).where(Processing.category == category)
        ).count()

        return JSONResponse({
            "success": {
                "message": "Processings fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processings": processings,
            "pagination": {
                "total": total_processings,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/processings/subcategory/{subcategory}', response_model=List[Processing])
async def get_processings_by_subcategory(subcategory: str, user: User = Depends(get_current_user),
                                         limit: int = Query(10, ge=1, le=100),
                                         offset: int = Query(0, ge=0)
                                         ) -> JSONResponse:
    with Session(engine) as session:
        processings = session.exec(
            select(Processing).where(Processing.subcategory ==
                                     subcategory).offset(offset).limit(limit)
        ).all()

        if not processings:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Processings not found."}}
            )

        total_processings = session.exec(
            select(Processing).where(Processing.subcategory == subcategory)
        ).count()

        return JSONResponse({
            "success": {
                "message": "Processings fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processings": processings,
            "pagination": {
                "total": total_processings,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/processings/year/{year}', response_model=List[Processing])
async def get_processings_by_year(year: int, user: User = Depends(get_current_user),
                                  limit: int = Query(10, ge=1, le=100),
                                  offset: int = Query(0, ge=0)) -> JSONResponse:
    with Session(engine) as session:
        processings = session.exec(select(Processing).where(
            Processing.year == year).offset(offset).limit(limit)).all()

        if not processings:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Processings not found."}}
            )

        total_processings = session.exec(
            select(Processing).where(Processing.year == year)
        ).count()

        return JSONResponse({
            "success": {
                "message": "Processings fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processings": processings,
            "pagination": {
                "total": total_processings,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/processings/year', response_model=List[Processing])
async def get_processings_by_year_range(start_year: int,
                                        end_year: int,
                                        limit: int = Query(10, ge=1, le=100),
                                        offset: int = Query(0, ge=0),
                                        user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        processings = session.exec(select(Processing).where(
            Processing.year >= start_year, Processing.year <= end_year).offset(offset).limit(limit)).all()

        if not processings:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Processings not found."}}
            )

        total_processings = session.exec(select(Processing).where(
            Processing.year >= start_year, Processing.year <= end_year)).count()

        return JSONResponse({
            "success": {
                "message": "Processings fetched successfully.",
                "type": "ProcessingInfo",
                "code": 200
            },
            "processings": processings,
            "pagination": {
                "total": total_processings,
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)
