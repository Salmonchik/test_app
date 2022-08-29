from typing import NamedTuple
from sqlalchemy.orm import Session

from app.core.enums import FigureTypes
from app.crud.base import CRUDBase
from app.models.figures import Figure
from app.schemas.figures import FigureCreate, GetFigure, GetFigureByType


class GetFigures(NamedTuple):
    count: int
    data: list


class CRUDFigure(CRUDBase[Figure, FigureCreate]):
    @staticmethod
    def __get_count(db: Session, filter_expression: list) -> int:
        return db.query(Figure).filter(*filter_expression).count()

    def create(self, db: Session, *, obj_in: FigureCreate) -> Figure:
        if obj_in.type == FigureTypes.TYPE_CUBE:
            dimension = obj_in.side
        else:
            dimension = obj_in.radius

        obj_in.radius = None
        obj_in.side = None
        db_obj = Figure(**obj_in.dict(exclude_none=True), dimension=dimension)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def get_by_type(cls, db: Session, get_figures: GetFigureByType) -> GetFigures:
        filter_expression = [Figure.type == get_figures.type]

        return GetFigures(
            count=cls.__get_count(db, filter_expression),
            data=db.query(Figure).filter(*filter_expression).order_by(Figure.created_at.desc()).offset(
                get_figures.skip).limit(get_figures.limit).all()
        )

    @classmethod
    def get_figures(cls, db: Session, get_figure: GetFigure) -> GetFigures:
        filter_expression = [Figure.lat == get_figure.lat, Figure.lon == get_figure.lon]
        if get_figure.type is not None:
            filter_expression.append(Figure.type == get_figure.type)

        return GetFigures(
            count=cls.__get_count(db, filter_expression),
            data=db.query(
                Figure
            ).filter(
                *filter_expression
            ).order_by(
                Figure.created_at.desc()
            ).offset(
                get_figure.skip
            ).limit(
                get_figure.limit
            ).all()
        )


figure = CRUDFigure(Figure)
