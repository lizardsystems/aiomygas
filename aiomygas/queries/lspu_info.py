from aiomygas.const import ATTR_LSPU_ID
from aiomygas.queries import BaseQuery


class LspuInfo(BaseQuery):
    OPERATION_NAME = "lspuInfo"
    DATA_NAME = "info"
    QUERY = """
query lspuInfo($lspuId: Float!) {
  lspuInfo(lspuId: $lspuId) {
    ok
    error
    info {
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
      providerId
      providerName
      comissionTotal
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
        id
        lspu
        lspuId
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
        children {
          abonentUuid
          counterCoefficient
          endDate
          equipmentUuid
          name
          nodeUuid
          norm
          price
          regimeUuid
          serviceUuid
          startDate
          tariff
        }
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
        measure
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
        }
        tariff
        price {
          day
          middle
          night
        }
      }
      contracts {
        active
        name
        number
        serviceName
        beginDate
        endDate
        status
        contractKind
        description
        uuid
        serviceUuid
        notification
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
}"""

    def __init__(self, lspu_id: int):
        """Initialize the query."""
        self.variables = {
            ATTR_LSPU_ID: lspu_id
        }
