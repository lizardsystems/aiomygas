"""GraphQL queries for payments."""
from .base import BaseQuery
from ..const import ATTR_LSPU_ID


class Payments(BaseQuery):
    """GraphQL query for payments."""
    OPERATION_NAME = "paymentsByLspu"
    DATA_NAME = "data"
    QUERY = """
query paymentsByLspu($lspuId: Float!) {
  paymentsByLspu(lspuId: $lspuId) {
    ok
    error
    data {
      paymentId
      amountKop
      amountRub
      lspu
      source
      date
      fiscalized
      sentToProvider
      savedToProvider
      serviceName
      kktId
      detail {
        sbp
        email
        status
        documentUuid
        serviceUuid
        providerName
        providerInn
        id
        session
        order
        type
        cardNumber
        cardBrand
        approvalCode
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
