# aiomygas

Asynchronous Python API for [Мой Газ](https://мойгаз.смородина.онлайн/).

## Installation

Use pip to install the library:

```commandline
pip install aiomygas
```

## Usage

```python

import asyncio
from pprint import pprint

import aiohttp

from aiomygas import SimpleMyGasAuth, MyGasApi


async def main(email: str, password: str) -> None:
    """Create the aiohttp session and run the example."""
    async with aiohttp.ClientSession() as session:
        auth = SimpleMyGasAuth(email, password, session)
        api = MyGasApi(auth)

        data = await api.async_get_accounts()

        pprint(data)


if __name__ == "__main__":
    _email = str(input("Email: "))
    _password = str(input("Password: "))
    asyncio.run(main(_email, _password))

```


This will return accounts list that looks a little like this:

```json
{
    "elsGroup": [
        {
            "els": {
                "id": 1111111,
                "jntAccountNum": "111111111111",
                "isFull": true,
                "alias": "Дом",
                "address": null,
                "epd": {
                    "id": 9,
                    "name": "ЕПД Ростов-на-Дону",
                    "typePaymentCode": "10031",
                    "ENABLE_PAPER_RECEIPT_EPD": 1,
                    "UNITED_PAY_INDICATION_EPD": 0
                },
                "params": null,
                "paperReceiptSetting": {
                    "value": 1,
                    "dateTime": "2023-09-08T19:00:42.421Z"
                }
            },
            "lspu": [
                {
                    "id": 22222222,
                    "account": "222222222222",
                    "isFull": 1,
                    "alias": "",
                    "address": null,
                    "provider": {
                        "id": 41,
                        "name": "Межрегионгаз Ростов-на-Дону",
                        "exchangeType": {
                            "id": 1,
                            "code": "EXCHANGE_TYPE_ONLINE",
                            "name": "Онлайн",
                            "description": "Получение, отправка и обновление информации происходит в рамках настроенного поставщиком времени (как правило, это от 30 сек. до 30 минут)"
                        },
                        "setup": {
                            "ACCOUNT_ATTACH_HINT": "Укажите номер лицевого счета поставщика газа (12 знаков), указанные на квитанции, без пробелов и запятых.\nПример: 370012345678",
                            "ALLOW_ACCESS_TYPE_CHARGE": "1",
                            "ALLOW_ACCESS_TYPE_COUNTER": "1",
                            "ALLOW_ACCESS_TYPE_PIN": "1",
                            "ALLOW_INDICATION_SEND": "1",
                            "ALLOW_INDICATION_SEND_LITE": "1",
                            "ALLOW_PAY": "1",
                            "ENABLE_PAYMENT_EXCHANGE": "1",
                            "ALLOW_PAY_APPLE": "0",
                            "ALLOW_PAY_GOOGLE": "0",
                            "ALLOW_PAY_SBP": "1",
                            "COUNTER_CHECK_DATE": "25",
                            "DAYS_BEFORE_CONTRACT_END": "60",
                            "DAYS_BEFORE_EQUIPMENT_CHECK": "60",
                            "ENABLE_AGREEMENT_SECTION": "1",
                            "ENABLE_APPLICATIONS_SECTION": "1",
                            "ENABLE_CALCULATION_SECTION": "1",
                            "ENABLE_INDICATION_SOURCE": "0",
                            "ENABLE_NOTIFICATION_DOCUMENT": "0",
                            "ENABLE_NOTIFICATION_EQUIPMENT": "1",
                            "ENABLE_PAYMENTS_SECTION": "1",
                            "ENABLE_PAYMENT_DETAILS_FULL": "1",
                            "ENABLE_PAYMENT_DETAILS_LITE": "0",
                            "ENABLE_PRINT_INVOICE": "1",
                            "ENABLE_PRIVILEGES_SECTION": "0",
                            "FULL_REQUEST_EMAIL": "Support_AO@rostovregiongaz.ru",
                            "IS_DEFAULT_FULL": "0",
                            "MAX_CONSUMPTION": "10000",
                            "MESSAGE_AFTER_CONTRACT_END": "Срок действия Вашего договора закончился. Требуется перезаключить договор",
                            "MESSAGE_AFTER_EQUIPMENT_CHECK": "Срок поверки прибора учета закончился. Показания будут отправляться, но не будут приняты к учету поставщиком услуг.",
                            "MESSAGE_BEFORE_CONTRACT_END": "Уважаемый абонент, срок действия Вашего договора заканчивается, пожалуйста не забудьте перезаключить его",
                            "MESSAGE_BEFORE_EQUIPMENT_CHECK": "Уважаемый абонент срок действия поверки Вашего прибора учета скоро заканчивается",
                            "SERVICE_UNAVAILABLE": "0",
                            "SUPPORT_EMAIL": "Support_AO@rostovregiongaz.ru",
                            "ENABLE_COUNTER_RATE": "1",
                            "ENABLE_PAPER_RECEIPT": "1",
                            "DUBLICATE_PAPER_RECEIPT": "1",
                            "ENABLE_NOTIFICATION_INDICATION": "0",
                            "MESSAGE_INDICATION_SECTION": "",
                            "SHOW_PAPER_RECEIPT_OFFER": "1",
                            "SHOW_NORMS_AND_RATES": "1",
                            "ALLOW_INDICATION_ZERO": "1",
                            "KKT_PAYMENT_METHOD_TYPE": "4",
                            "KKT_PAYMENT_SUBJECT_TYPE": "4",
                            "PAYMENT_MESSAGE": "",
                            "ENABLE_PAYMENT_MESSAGE": "0",
                            "ALLOW_AUTOPAY": "1",
                            "CHARGES_INTERVAL_MONTHS_NUMBER": "12",
                            "ALLOW_INDICATION_OVERLAP": "1",
                            "PROVIDER_ALLOW_OFFER_ELS": "1",
                            "ALLOW_INDICATION_CHECK_EXPIRED": "1",
                            "ALLOW_MIR_PAY": "1",
                            "GAS_COUNTER_TARIFF": "0",
                            "ENABLE_PRINT_EPD": null,
                            "ALLOW_CREATE_AGREEMENT_TICKET": null,
                            "DEPARTMET_EMAIL": null,
                            "ALLOW_DOWNLOAD_CHARGES": null,
                            "ALLOW_INDICATION_DATE_CHANGE": null,
                            "ENABLE_EQUIPMENTS_DATE": null,
                            "ENABLE_EQUIPMENTS_SERIAL": null,
                            "ENABLE_ABONENT_FULLNAME": null,
                            "ALLOW_TICKET_INSPECTOR_SEND": null,
                            "RTP_TOPIC_ID": "",
                            "TICKET_SRC_PROVIDER_OPD": ""
                        }
                    },
                    "paperReceiptSetting": {
                        "value": 1,
                        "dateTime": "2023-01-01T10:33:44.437Z"
                    },
                    "hasAutopay": false,
                    "elsAvailable": null
                }
            ],
            "lspuDublicate": []
        },
        {
            "els": {
                "id": 3333333,
                "jntAccountNum": "333333333333",
                "isFull": true,
                "alias": "Офис",
                "address": null,
                "epd": {
                    "id": 9,
                    "name": "ЕПД Ростов-на-Дону",
                    "typePaymentCode": "10031",
                    "ENABLE_PAPER_RECEIPT_EPD": 1,
                    "UNITED_PAY_INDICATION_EPD": 0
                },
                "params": null,
                "paperReceiptSetting": {
                    "value": 1,
                    "dateTime": "2023-09-08T19:00:30.744Z"
                }
            },
            "lspu": [
                {
                    "id": 44444444,
                    "account": "444444444444",
                    "isFull": 1,
                    "alias": "",
                    "address": null,
                    "provider": {
                        "id": 41,
                        "name": "Межрегионгаз Ростов-на-Дону",
                        "exchangeType": {
                            "id": 1,
                            "code": "EXCHANGE_TYPE_ONLINE",
                            "name": "Онлайн",
                            "description": "Получение, отправка и обновление информации происходит в рамках настроенного поставщиком времени (как правило, это от 30 сек. до 30 минут)"
                        },
                        "setup": {
                            "ACCOUNT_ATTACH_HINT": "Укажите номер лицевого счета поставщика газа (12 знаков), указанные на квитанции, без пробелов и запятых.\nПример: 370012345678",
                            "ALLOW_ACCESS_TYPE_CHARGE": "1",
                            "ALLOW_ACCESS_TYPE_COUNTER": "1",
                            "ALLOW_ACCESS_TYPE_PIN": "1",
                            "ALLOW_INDICATION_SEND": "1",
                            "ALLOW_INDICATION_SEND_LITE": "1",
                            "ALLOW_PAY": "1",
                            "ENABLE_PAYMENT_EXCHANGE": "1",
                            "ALLOW_PAY_APPLE": "0",
                            "ALLOW_PAY_GOOGLE": "0",
                            "ALLOW_PAY_SBP": "1",
                            "COUNTER_CHECK_DATE": "25",
                            "DAYS_BEFORE_CONTRACT_END": "60",
                            "DAYS_BEFORE_EQUIPMENT_CHECK": "60",
                            "ENABLE_AGREEMENT_SECTION": "1",
                            "ENABLE_APPLICATIONS_SECTION": "1",
                            "ENABLE_CALCULATION_SECTION": "1",
                            "ENABLE_INDICATION_SOURCE": "0",
                            "ENABLE_NOTIFICATION_DOCUMENT": "0",
                            "ENABLE_NOTIFICATION_EQUIPMENT": "1",
                            "ENABLE_PAYMENTS_SECTION": "1",
                            "ENABLE_PAYMENT_DETAILS_FULL": "1",
                            "ENABLE_PAYMENT_DETAILS_LITE": "0",
                            "ENABLE_PRINT_INVOICE": "1",
                            "ENABLE_PRIVILEGES_SECTION": "0",
                            "FULL_REQUEST_EMAIL": "Support_AO@rostovregiongaz.ru",
                            "IS_DEFAULT_FULL": "0",
                            "MAX_CONSUMPTION": "10000",
                            "MESSAGE_AFTER_CONTRACT_END": "Срок действия Вашего договора закончился. Требуется перезаключить договор",
                            "MESSAGE_AFTER_EQUIPMENT_CHECK": "Срок поверки прибора учета закончился. Показания будут отправляться, но не будут приняты к учету поставщиком услуг.",
                            "MESSAGE_BEFORE_CONTRACT_END": "Уважаемый абонент, срок действия Вашего договора заканчивается, пожалуйста не забудьте перезаключить его",
                            "MESSAGE_BEFORE_EQUIPMENT_CHECK": "Уважаемый абонент срок действия поверки Вашего прибора учета скоро заканчивается",
                            "SERVICE_UNAVAILABLE": "0",
                            "SUPPORT_EMAIL": "Support_AO@rostovregiongaz.ru",
                            "ENABLE_COUNTER_RATE": "1",
                            "ENABLE_PAPER_RECEIPT": "1",
                            "DUBLICATE_PAPER_RECEIPT": "1",
                            "ENABLE_NOTIFICATION_INDICATION": "0",
                            "MESSAGE_INDICATION_SECTION": "",
                            "SHOW_PAPER_RECEIPT_OFFER": "1",
                            "SHOW_NORMS_AND_RATES": "1",
                            "ALLOW_INDICATION_ZERO": "1",
                            "KKT_PAYMENT_METHOD_TYPE": "4",
                            "KKT_PAYMENT_SUBJECT_TYPE": "4",
                            "PAYMENT_MESSAGE": "",
                            "ENABLE_PAYMENT_MESSAGE": "0",
                            "ALLOW_AUTOPAY": "1",
                            "CHARGES_INTERVAL_MONTHS_NUMBER": "12",
                            "ALLOW_INDICATION_OVERLAP": "1",
                            "PROVIDER_ALLOW_OFFER_ELS": "1",
                            "ALLOW_INDICATION_CHECK_EXPIRED": "1",
                            "ALLOW_MIR_PAY": "1",
                            "GAS_COUNTER_TARIFF": "0",
                            "ENABLE_PRINT_EPD": null,
                            "ALLOW_CREATE_AGREEMENT_TICKET": null,
                            "DEPARTMET_EMAIL": null,
                            "ALLOW_DOWNLOAD_CHARGES": null,
                            "ALLOW_INDICATION_DATE_CHANGE": null,
                            "ENABLE_EQUIPMENTS_DATE": null,
                            "ENABLE_EQUIPMENTS_SERIAL": null,
                            "ENABLE_ABONENT_FULLNAME": null,
                            "ALLOW_TICKET_INSPECTOR_SEND": null,
                            "RTP_TOPIC_ID": "",
                            "TICKET_SRC_PROVIDER_OPD": ""
                        }
                    },
                    "paperReceiptSetting": {
                        "value": 1,
                        "dateTime": "2023-01-01T10:32:52.489Z"
                    },
                    "hasAutopay": false,
                    "elsAvailable": null
                }
            ],
            "lspuDublicate": []
        }
    ],
    "lspu": []
}

```

## Timeouts

aiomygas does not specify any timeouts for any requests. You will need to specify them in your own code. We recommend the `async_timeout` package:

```python
import async_timeout

with async_timeout.timeout(10):
    data = await api.async_get_accounts()
```
