from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List

from app.configs.database import engine
from app.models import User, Exportation

from app.packages.Auth import (
    get_current_user
)

router = APIRouter(prefix="/v1")


@router.get('/exports')
async def get_exports(limit: int = Query(10, ge=1, le=100),
                      offset: int = Query(0, ge=0),
                      user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exports = session.query(Exportation).offset(offset).limit(limit).all()

        if not exports:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exports = session.query(Exportation).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exports),
            "pagination": {
                "total": jsonable_encoder(total_exports),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/{id}')
async def get_import(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportation = session.query(Exportation).filter(
            Exportation.id == id).first()

        if not Exportation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportation)
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/country/{country}', response_model=List[Exportation])
async def get_exports_by_country(country: str,
                                 limit: int = Query(10, ge=1, le=100),
                                 offset: int = Query(0, ge=0),
                                 user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.country == country).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.country == country).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/category/{category}', response_model=List[Exportation])
async def get_exports_by_category(category: str,
                                  limit: int = Query(10, ge=1, le=100),
                                  offset: int = Query(0, ge=0),
                                  user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.category == category).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.category == category).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/weight/{weight}', response_model=List[Exportation])
async def get_exports_by_weight(weight: int,
                                limit: int = Query(10, ge=1, le=100),
                                offset: int = Query(0, ge=0),
                                user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.weight == weight).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.weight == weight).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/weight/range', response_model=List[Exportation])
async def get_exports_by_weight_range(start_weight: int,
                                      end_weight: int,
                                      limit: int = Query(10, ge=1, le=100),
                                      offset: int = Query(0, ge=0),
                                      user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.weight >= start_weight,
                Exportation.weight <= end_weight).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.weight >= start_weight,
                Exportation.weight <= end_weight).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/value/{value}', response_model=List[Exportation])
async def get_exports_by_value(value: int,
                               limit: int = Query(10, ge=1, le=100),
                               offset: int = Query(0, ge=0),
                               user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.value == value).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.value == value).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/value/range', response_model=List[Exportation])
async def get_exports_by_value_range(start_value: int,
                                     end_value: int,
                                     limit: int = Query(10, ge=1, le=100),
                                     offset: int = Query(0, ge=0),
                                     user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.value >= start_value,
                Exportation.value <= end_value).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.value >= start_value,
                Exportation.value <= end_value).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/year/{year}', response_model=List[Exportation])
async def get_exports_by_year(year: int,
                              limit: int = Query(10, ge=1, le=100),
                              offset: int = Query(0, ge=0),
                              user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.year == year).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.year == year).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)


@router.get('/exports/years/range', response_model=List[Exportation])
async def get_exports_by_year_range(start_year: int,
                                    end_year: int,
                                    limit: int = Query(10, ge=1, le=100),
                                    offset: int = Query(0, ge=0),
                                    user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        exportations = session.query(Exportation).where(
                Exportation.year >= start_year,
                Exportation.year <= end_year).offset(offset).limit(limit).all()

        if not exportations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"message": "Exportation not found."}}
            )

        total_exportations = session.query(Exportation).where(
                Exportation.year >= start_year,
                Exportation.year <= end_year).count()

        return JSONResponse({
            "success": {
                "message": "Exports fetched successfully.",
                "type": "ExportInfo",
                "code": 200
            },
            "exportations": jsonable_encoder(exportations),
            "pagination": {
                "total": jsonable_encoder(total_exportations),
                "limit": limit,
                "offset": offset
            }
        }, status_code=status.HTTP_200_OK)
