from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated


class UserInputs(BaseModel):

    gender: Annotated[Literal["Male","Female","Other" ], Field(..., description="User Gender")]
    age: Annotated[int, Field(..., gt=0, lt=101,description="User Age")]
    country: Annotated[Literal["AU","US","DE","IN","PK","FR","UK","CA"], Field(..., description="Country")]
    subscription_type: Annotated[Literal["Premium","Free","Student","Family" ], Field(..., description="Subscription Type")]
    listening_time: Annotated[int, Field(..., gt=0, description="Listening time in minutes")]
    songs_played_per_day: Annotated[int, Field(...,gt=0, description="Songs played per day")]
    skip_rate: Annotated[float, Field(..., gt=0, lt=1.01,description="Skip Rate")]
    device_type: Annotated[Literal["Desktop","Web","Mobile"], Field(..., description="Device Type")]
    ads_listened_per_week: Annotated[float, Field(...,gt=0, description="Ads lintened per week")]
    offline_listening: Annotated[bool, Field(..., description="Offline Listening")]

    @field_validator("country")
    @classmethod
    def normalize_country(cls, v:str) -> str:
        v = v.strip().upper()
        return v