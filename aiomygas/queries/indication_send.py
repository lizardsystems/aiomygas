"""GraphQL query for sending indication to MyGas API."""
from .base import BaseQuery
from ..const import ATTR_ELS_ID, ATTR_LSPU_ID, ATTR_DEVICE_INFO
from ..device_info import DEVICE_INFO


class IndicationSend(BaseQuery):
    """GraphQL query for sending indication to MyGas API."""

    OPERATION_NAME = "indicationSendV4"
    DATA_NAME = "data"
    QUERY = """
mutation indicationSendV4($input: IndicationSendV4Input!, $deviceInfo: DeviceInfoInputV2!) {
  indicationSendV4(input: $input, deviceInfo: $deviceInfo) {
    ok
    error
    data {
      lspuId
      counters {
        uuid
        sent
        message
      }
    }
  }
}
"""

    def __init__(self, els_id, lspu_id: int, uuid: str, value_day: int | float) -> None:
        """Initialize."""
        self.variables = {
            'input': {
                ATTR_ELS_ID: els_id,
                "lspuGroups": [{
                    ATTR_LSPU_ID: lspu_id,
                    "counters": [{
                        "uuid": uuid,
                        "serviceId": 0.0,  # необязательный параметр (по умолчанию 0)
                        "valueDay": value_day,
                        "valueNight": None,
                        "valueMiddle": None,
                        "overlapDay": False,
                        "overlapMiddle": False,
                        "overlapNight": False
                    }
                    ]
                }
                ]
            },
            ATTR_DEVICE_INFO: DEVICE_INFO
        }
