from typing import Optional

from pydantic import BaseModel, root_validator, validator, conlist, confloat, conint

from app.core.enums import FigureTypes
from app.models.figures import Figure


class FigureCreate(BaseModel):
    type: FigureTypes
    color: str = '#AA0000'
    norm: conlist(float, min_items=3, max_items=3)
    lat: confloat(ge=-90, le=90)
    lon: confloat(ge=-180, le=180)
    radius: Optional[float] = None
    side: Optional[float] = None

    @root_validator(pre=True, allow_reuse=True)
    def dimension_validator(cls, values: dict):
        figure_type = values.get('type')
        radius = values.get('radius')
        side = values.get('side')

        if figure_type == FigureTypes.TYPE_SPHERE:
            if radius is None:
                raise ValueError('radius missing')
            if radius <= 0:
                raise ValueError('radius must be greater than 0')

        elif figure_type == FigureTypes.TYPE_CUBE:
            if side is None:
                raise ValueError('side missing')
            if side <= 0:
                raise ValueError('side must be greater than 0')

        return values

    @validator('norm')
    def normal_validator(cls, value):
        if all([-1 <= x <= 1 for x in value]):
            return value

        raise ValueError('the normal value can be in the range from -1 to 1')


class GetFigure(BaseModel):
    lat: float
    lon: float
    type: Optional[FigureTypes]
    skip: conint(ge=0) = 0
    limit: conint(ge=0) = 5

    @validator('lat')
    def check_latitude(cls, lat):
        if lat < -90 or lat > 90:
            raise ValueError('latitude must be in range -90 to 90')
        return lat

    @validator('lon')
    def check_longitude(cls, lon):
        if lon < -180 or lon > 180:
            raise ValueError('longitude must be in range -180 to 180')
        return lon


class GetFigureResponse(BaseModel):
    total: int
    size: int
    data: list[Figure]

    class Config:
        arbitrary_types_allowed = True


class GetFigureByType(BaseModel):
    type: FigureTypes
    skip: conint(ge=0) = 0
    limit: conint(ge=0) = 5
