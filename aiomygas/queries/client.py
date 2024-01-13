"""GraphQL queries for client."""
from .base import BaseQuery


class ClientV2(BaseQuery):
    OPERATION_NAME = "clientV2"
    DATA_NAME = "client"
    QUERY = """
query clientV2 {
  clientV2 {
    ok
    error
    client {
      id
      identifier
      email
      phone
      name
      photo
      token
      hash
      widgets {
        code
        size
      }
      ssoProviders {
        name
        type
        attached
      }
      eulaAccepted
      passwordInfo {
        updateDate
        needUpdate
        message
      }
    }
  }
}
"""
