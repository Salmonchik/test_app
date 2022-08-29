from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.figures import GetFigure, FigureCreate, GetFigureResponse, GetFigureByType

router = APIRouter()


@router.get('/figure')
def get_figure(
        get_figure: GetFigure = Depends(),
        db: Session = Depends(deps.get_db),
):
    response = crud.figure.get_figures(
        db,
        get_figure,
    )
    return GetFigureResponse(
        total=response.count,
        size=get_figure.limit,
        data=response.data
    )


@router.get('/figures')
def get_figures(
        get_figures_by_type: GetFigureByType = Depends(),
        db: Session = Depends(deps.get_db),
):
    response = crud.figure.get_by_type(
        db,
        get_figures_by_type,
    )
    return GetFigureResponse(
        total=response.count,
        size=get_figures_by_type.limit,
        data=response.data
    )


@router.post('/figure')
def add_figure(
        figure_in_create: FigureCreate,
        db: Session = Depends(deps.get_db),
):
    response = crud.figure.create(
        db=db,
        obj_in=figure_in_create,
    )

    return {'data': response.__dict__}


@router.delete('/figure', status_code=204)
def delete_figure(
        id: UUID4,
        db: Session = Depends(deps.get_db),
):
    item = crud.figure.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')

    crud.figure.remove(db=db, id=id)
