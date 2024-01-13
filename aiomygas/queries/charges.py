"""GraphQL queries for charges."""
from .base import BaseQuery
from ..const import ATTR_LSPU_ID


class Charges(BaseQuery):
    OPERATION_NAME = "clientCharges"
    DATA_NAME = "data"
    QUERY = """
query clientCharges($lspuId: Float!) {
  clientCharges(lspuId: $lspuId) {
    ok
    error
    data {
      abonentUuid
      recalculation
      recalculationVolume
      totalAccountingPeriod
      serviceType
      serviceName
      area
      livingPeople
      volume
      rate
      privileges
      account
      date
      detailed
      ownerServiceType
      serviceUuid
      norm
      organizationUuid
      id
      organizationCode
      bankBik
      operatingAccountNumber
      children {
        abonentUuid
        recalculation
        recalculationVolume
        totalAccountingPeriod
        serviceType
        serviceName
        area
        livingPeople
        volume
        rate
        privileges
        account
        date
        detailed
        ownerServiceType
        serviceUuid
        norm
        organizationUuid
        id
        organizationCode
        bankBik
        operatingAccountNumber
      }
    }
  }
}
"""

    def __init__(self, lspu_id: int) -> None:
        """Initialize."""
        self.variables = {
            ATTR_LSPU_ID: lspu_id
        }
