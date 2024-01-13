"""GraphQL queries for ELS Info."""
from .base import BaseQuery
from ..const import ATTR_ELS_ID


class ElsInfo(BaseQuery):
    OPERATION_NAME = "elsInfo"
    DATA_NAME = "info"
    QUERY = """
query elsInfo($elsId: Float!) {
  elsInfo(elsId: $elsId) {
    ok
    error
    info {
      els {
        id
        jntAccountNum
        isFull
        alias
        address
        epd {
          id
          name
          typePaymentCode
          ENABLE_PAPER_RECEIPT_EPD
          UNITED_PAY_INDICATION_EPD
        }
        params {
          someField
        }
        paperReceiptSetting {
          value
          dateTime
        }
      }
      lspuInfoGroup {
        hasInfo
        hasCounters
        hasAutopay
        paymentSourceAvailable
        insuranceAvailable
        isFull
        alias
        accountId
        account
        balance
        comissionTotal
        providerId
        providerName
        comissionThreshold
        actions {
          type
          iconUrl
          title
          description
          value
          color
        }
        alerts {
          title
          description
        }
        services {
          lspuId
          lspu
          id
          name
          balance
          providerId
          providerName
          providerExchangeName
          providerExchangeCode
          providerExchangeDescription
          comissionType
          comissionRate
          comissionAmount
          isInsurance
          insuranceId
          color
          children {
            abonentUuid
            equipmentUuid
            serviceUuid
            regimeUuid
            nodeUuid
            counterCoefficient
            norm
            price
            tariff
            name
            startDate
            endDate
          }
        }
        equipments {
          type
          name
          uuid
          serialNumber
          state
          needVerification
          numberOfRates
          municipalResource
          meterType
          stateInt
          position
          model
          factorySeal
          equipmentKind
          date
          checkDate
          techSupportDate
          sealDate
          factorySealDate
          commissionedOn
          notification
          color
        }
        counters {
          lspuId
          name
          uuid
          serialNumber
          numberOfRates
          capacity
          stateInt
          state
          notification
          averageRate
          monthsCount
          serviceName
          serviceLinkId
          needVerification
          position
          model
          factorySeal
          equipmentKind
          meterType
          checkDate
          techSupportDate
          sealDate
          factorySealDate
          commissionedOn
          values {
            valueDay
            valueMiddle
            valueNight
            overlap
            rate
            state
            source
            date
            dateDt
            saved
            value
            previousValue
            color
          }
          tariff
          measure
          price {
            day
            middle
            night
          }
          date
          checkNotification
          municipalResource
          color
        }
        contracts {
          active
          name
          number
          serviceName
          status
          contractKind
          description
          uuid
          serviceUuid
          notification
          beginDate
          endDate
          color
        }
        tickets {
          uuid
          document
          text
          status
          date
          number
          ticketTypeUuid
          ticketSubtypeUuid
          providerName
        }
        balances {
          uuid
          date
          name
          balanceStartSum
          balanceEndSum
          chargedSum
          chargedVolume
          circulationSum
          forgivenDebt
          organizationCode
          paymentAdjustments
          plannedSum
          privilegeSum
          privilegeVolume
          restoredDebt
          endBalanceApgp
          prepaymentChargedAccumSum
          debtSum
          paidSum
          children {
            date
            name
            chargedSum
            serviceUuid
          }
        }
        payments {
          uuid
          date
          paidSum
          serviceName
          serviceUuid
          source
          status
          internalCode
          transactionNumber
          color
          cardNumber
          externalCode
          approval
        }
        acts {
          uuid
          name
          data
          works {
            sum
            serviceUuid
            serviceName
            equipmentUuid
            equipmentName
          }
        }
        parameters {
          date
          name
          value
        }
        privileges {
          abonentUuid
          active
          beginDate
          endDate
          name
        }
      }
    }
  }
}
"""

    def __init__(self, els_id: int):
        """Initialize the query."""
        self.variables = {
            ATTR_ELS_ID: els_id
        }
