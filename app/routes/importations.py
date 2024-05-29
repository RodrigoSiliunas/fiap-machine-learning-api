from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List

from app.configs.database import engine
from app.models import User, Importation

from app.packages.Auth import (
    get_current_user
)

router = APIRouter(prefix="/v1")


@router.get('/imports')
async def get_imports(limit: int = Query(10, ge=1, le=100),
                      offset: int = Query(0, ge=0),
                      user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        imports = session.query(Importation).offset(offset).limit(limit).all()

        if not imports:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_imports = session.query(Importation).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(imports),
            "pagination": {
                "total": jsonable_encoder(total_imports),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/{id}')
async def get_import(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importation = session.query(Importation).filter(
            Importation.id == id).first()

        if not importation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importation)
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/country/{country}', response_model=List[Importation])
async def get_imports_by_country(country: str,
                                 limit: int = Query(10, ge=1, le=100),
                                 offset: int = Query(0, ge=0),
                                 user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.country == country).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.country == country).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/category/{category}', response_model=List[Importation])
async def get_imports_by_category(category: str,
                                  limit: int = Query(10, ge=1, le=100),
                                  offset: int = Query(0, ge=0),
                                  user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.category == category).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.category == category).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/weight/{weight}', response_model=List[Importation])
async def get_imports_by_weight(weight: int,
                                limit: int = Query(10, ge=1, le=100),
                                offset: int = Query(0, ge=0),
                                user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.weight == weight).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.weight == weight).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/weight/range', response_model=List[Importation])
async def get_imports_by_weight_range(start_weight: int,
                                      end_weight: int,
                                      limit: int = Query(10, ge=1, le=100),
                                      offset: int = Query(0, ge=0),
                                      user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.weight >= start_weight,
                Importation.weight <= end_weight).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.weight >= start_weight,
                Importation.weight <= end_weight).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/value/{value}', response_model=List[Importation])
async def get_imports_by_value(value: int,
                               limit: int = Query(10, ge=1, le=100),
                               offset: int = Query(0, ge=0),
                               user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.value == value).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.value == value).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/value/range', response_model=List[Importation])
async def get_imports_by_value_range(start_value: int,
                                     end_value: int,
                                     limit: int = Query(10, ge=1, le=100),
                                     offset: int = Query(0, ge=0),
                                     user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.value >= start_value,
                Importation.value <= end_value).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.value >= start_value,
                Importation.value <= end_value).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/year/{year}', response_model=List[Importation])
async def get_imports_by_year(year: int,
                              limit: int = Query(10, ge=1, le=100),
                              offset: int = Query(0, ge=0),
                              user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.year == year).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.year == year).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/imports/years/range', response_model=List[Importation])
async def get_imports_by_year_range(start_year: int,
                                    end_year: int,
                                    limit: int = Query(10, ge=1, le=100),
                                    offset: int = Query(0, ge=0),
                                    user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        importations = session.query(Importation).where(
                Importation.year >= start_year,
                Importation.year <= end_year).offset(offset).limit(limit).all()

        if not importations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Importation not found."}}
            )

        total_importations = session.query(Importation).where(
                Importation.year >= start_year,
                Importation.year <= end_year).count()

        return JSONResponse({
            "success": {
                "message": "Imports fetched successfully.",
                "type": "ImportInfo",
                "code": 200
            },
            "importations": jsonable_encoder(importations),
            "pagination": {
                "total": jsonable_encoder(total_importations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)
