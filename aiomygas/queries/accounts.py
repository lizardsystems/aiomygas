"""GraphQL queries for accounts."""
from .base import BaseQuery


class Accounts(BaseQuery):
    OPERATION_NAME = "accountsN"
    DATA_NAME = "accounts"
    QUERY = """
query accountsN {
  accountsN {
    ok
    error
    accounts {
      elsGroup {
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
        lspu {
          id
          account
          isFull
          alias
          address
          provider {
            id
            name
            exchangeType {
              id
              code
              name
              description
            }
            setup {
              ACCOUNT_ATTACH_HINT
              ALLOW_ACCESS_TYPE_CHARGE
              ALLOW_ACCESS_TYPE_COUNTER
              ALLOW_ACCESS_TYPE_PIN
              ALLOW_INDICATION_SEND
              ALLOW_INDICATION_SEND_LITE
              ALLOW_PAY
              ENABLE_PAYMENT_EXCHANGE
              ALLOW_PAY_APPLE
              ALLOW_PAY_GOOGLE
              ALLOW_PAY_SBP
              COUNTER_CHECK_DATE
              DAYS_BEFORE_CONTRACT_END
              DAYS_BEFORE_EQUIPMENT_CHECK
              ENABLE_AGREEMENT_SECTION
              ENABLE_APPLICATIONS_SECTION
              ENABLE_CALCULATION_SECTION
              ENABLE_INDICATION_SOURCE
              ENABLE_NOTIFICATION_DOCUMENT
              ENABLE_NOTIFICATION_EQUIPMENT
              ENABLE_PAYMENTS_SECTION
              ENABLE_PAYMENT_DETAILS_FULL
              ENABLE_PAYMENT_DETAILS_LITE
              ENABLE_PRINT_INVOICE
              ENABLE_PRIVILEGES_SECTION
              FULL_REQUEST_EMAIL
              IS_DEFAULT_FULL
              MAX_CONSUMPTION
              MESSAGE_AFTER_CONTRACT_END
              MESSAGE_AFTER_EQUIPMENT_CHECK
              MESSAGE_BEFORE_CONTRACT_END
              MESSAGE_BEFORE_EQUIPMENT_CHECK
              SERVICE_UNAVAILABLE
              SUPPORT_EMAIL
              ENABLE_COUNTER_RATE
              ENABLE_PAPER_RECEIPT
              DUBLICATE_PAPER_RECEIPT
              ENABLE_NOTIFICATION_INDICATION
              MESSAGE_INDICATION_SECTION
              SHOW_PAPER_RECEIPT_OFFER
              SHOW_NORMS_AND_RATES
              ALLOW_INDICATION_ZERO
              KKT_PAYMENT_METHOD_TYPE
              KKT_PAYMENT_SUBJECT_TYPE
              PAYMENT_MESSAGE
              ENABLE_PAYMENT_MESSAGE
              ALLOW_AUTOPAY
              CHARGES_INTERVAL_MONTHS_NUMBER
              ALLOW_INDICATION_OVERLAP
              PROVIDER_ALLOW_OFFER_ELS
              ALLOW_INDICATION_CHECK_EXPIRED
              ALLOW_MIR_PAY
              GAS_COUNTER_TARIFF
              ENABLE_PRINT_EPD
              ALLOW_CREATE_AGREEMENT_TICKET
              DEPARTMET_EMAIL
              ALLOW_DOWNLOAD_CHARGES
              ALLOW_INDICATION_DATE_CHANGE
              ENABLE_EQUIPMENTS_DATE
              ENABLE_EQUIPMENTS_SERIAL
              ENABLE_ABONENT_FULLNAME
              ALLOW_TICKET_INSPECTOR_SEND
              RTP_TOPIC_ID
              TICKET_SRC_PROVIDER_OPD
            }
          }
          paperReceiptSetting {
            value
            dateTime
          }
          hasAutopay
          elsAvailable
        }
        lspuDublicate {
          lspu
          lspuId
          providerId
          providerName
        }
      }
      lspu {
        id
        account
        isFull
        alias
        address
        provider {
          id
          name
          exchangeType {
            id
            code
            name
            description
          }
          setup {
            ACCOUNT_ATTACH_HINT
            ALLOW_ACCESS_TYPE_CHARGE
            ALLOW_ACCESS_TYPE_COUNTER
            ALLOW_ACCESS_TYPE_PIN
            ALLOW_INDICATION_SEND
            ALLOW_INDICATION_SEND_LITE
            ALLOW_PAY
            ENABLE_PAYMENT_EXCHANGE
            ALLOW_PAY_APPLE
            ALLOW_PAY_GOOGLE
            ALLOW_PAY_SBP
            COUNTER_CHECK_DATE
            DAYS_BEFORE_CONTRACT_END
            DAYS_BEFORE_EQUIPMENT_CHECK
            ENABLE_AGREEMENT_SECTION
            ENABLE_APPLICATIONS_SECTION
            ENABLE_CALCULATION_SECTION
            ENABLE_INDICATION_SOURCE
            ENABLE_NOTIFICATION_DOCUMENT
            ENABLE_NOTIFICATION_EQUIPMENT
            ENABLE_PAYMENTS_SECTION
            ENABLE_PAYMENT_DETAILS_FULL
            ENABLE_PAYMENT_DETAILS_LITE
            ENABLE_PRINT_INVOICE
            ENABLE_PRIVILEGES_SECTION
            FULL_REQUEST_EMAIL
            IS_DEFAULT_FULL
            MAX_CONSUMPTION
            MESSAGE_AFTER_CONTRACT_END
            MESSAGE_AFTER_EQUIPMENT_CHECK
            MESSAGE_BEFORE_CONTRACT_END
            MESSAGE_BEFORE_EQUIPMENT_CHECK
            SERVICE_UNAVAILABLE
            SUPPORT_EMAIL
            ENABLE_COUNTER_RATE
            ENABLE_PAPER_RECEIPT
            DUBLICATE_PAPER_RECEIPT
            ENABLE_NOTIFICATION_INDICATION
            MESSAGE_INDICATION_SECTION
            SHOW_PAPER_RECEIPT_OFFER
            SHOW_NORMS_AND_RATES
            ALLOW_INDICATION_ZERO
            KKT_PAYMENT_METHOD_TYPE
            KKT_PAYMENT_SUBJECT_TYPE
            PAYMENT_MESSAGE
            ENABLE_PAYMENT_MESSAGE
            ALLOW_AUTOPAY
            CHARGES_INTERVAL_MONTHS_NUMBER
            ALLOW_INDICATION_OVERLAP
            PROVIDER_ALLOW_OFFER_ELS
            ALLOW_INDICATION_CHECK_EXPIRED
            ALLOW_MIR_PAY
            GAS_COUNTER_TARIFF
            ENABLE_PRINT_EPD
            ALLOW_CREATE_AGREEMENT_TICKET
            DEPARTMET_EMAIL
            ALLOW_DOWNLOAD_CHARGES
            ALLOW_INDICATION_DATE_CHANGE
            ENABLE_EQUIPMENTS_DATE
            ENABLE_EQUIPMENTS_SERIAL
            ENABLE_ABONENT_FULLNAME
            ALLOW_TICKET_INSPECTOR_SEND
            RTP_TOPIC_ID
            TICKET_SRC_PROVIDER_OPD
          }
        }
        paperReceiptSetting {
          value
          dateTime
        }
        hasAutopay
        elsAvailable
      }
    }
  }
}
"""
