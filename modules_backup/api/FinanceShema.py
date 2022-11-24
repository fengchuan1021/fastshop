#   timestamp: 2022-10-29T02:15:06+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class ApiFinanceTransactionsSearchPostRequest(BaseModel):
    request_time_from: Optional[int] = Field(
        None,
        description='Unix timestamp representing the start of transactions time range one wants to request',
    )
    request_time_to: Optional[int] = Field(
        None,
        description='Unix timestamp representing the end of transactions time range one wants to request',
    )
    transaction_type: List[int]
    page_size: int = Field(
        ...,
        description='The maximum number of transactions to obtain in one single page. The value must',
    )
    offset: int = Field(..., description='The value must be in the range of 0~10000')


class TransactionListItem(BaseModel):
    transaction_type: Optional[int] = Field(
        None, description='Withdraw:1<br>Settle:2<br>Transfer:3<br>Reverse:4'
    )
    transaction_time: Optional[int] = Field(None, description='Transaction create time')
    transaction_amount: Optional[str] = Field(None, description='Transaction amount')
    transaction_currency: Optional[str] = Field(
        None, description='Transaction currency'
    )
    transaction_status: Optional[int] = Field(
        None, description='INIT:1<br>PROCESSING:2<br>SUCCESS:3<br>FAILED:4<br>Reverse:5'
    )


class Data(BaseModel):
    total: Optional[int] = Field(None, description='Total number of transactions')
    more: Optional[bool] = Field(
        None, description='Whether there are more transactions on the next page or not'
    )
    transaction_list: Optional[List[TransactionListItem]] = None


class ApiFinanceTransactionsSearchPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ApiFinanceOrderSettlementsGetRequest(BaseModel):
    order_id: str = Field(..., description='Order ID')


class SettlementInfo(BaseModel):
    settlement_time: Optional[int] = Field(
        None,
        description='The time TTS pays out the money. Not necessarily the time merchants receive the money.',
    )
    currency: Optional[str] = Field(None, description='')
    user_pay: Optional[str] = Field(None, description="Buyer's payment.")
    platform_promotion: Optional[str] = Field(None, description='')
    shipping_fee_subsidy: Optional[str] = Field(
        None,
        description='A positive amount represents the shipping fee discount received for participating in a platform campaign, and a negative amount represents a shipping fee discount you need to return.',
    )
    refund: Optional[str] = Field(None, description='')
    payment_fee: Optional[str] = Field(
        None,
        description="The technical service fee charged on the platform's online payment, refund, settlement and other categories (X% of settlement amount)",
    )
    platform_commission: Optional[str] = Field(
        None,
        description='The platform commission fee charged by the platform (X% of settled orders)',
    )
    flat_fee: Optional[str] = Field(
        None, description='The flat fee is a fixed amount charged per valid order'
    )
    sales_fee: Optional[str] = Field(
        None,
        description='The sales fee is a percentage of the product price after the seller discount, charged to the seller',
    )
    affiliate_commission: Optional[str] = Field(
        None,
        description="The commission fee one needs to pay to a creator when s/he promotes a product on Tiktok platform and generates orders (the amount depends on the seller's promotion plan)",
    )
    vat: Optional[str] = Field(
        None,
        description="VAT paid by platform on one's Behalf. Only applicable for cross-border shop orders. All the other fields' amount in this API is vat excluded.",
    )
    shipping_fee: Optional[str] = Field(
        None,
        description='The shipping fee paid by the merchant when the merchant selects logistics services supported by TikTok Shop',
    )
    small_order_fee: Optional[str] = Field(
        None,
        description='The small order fee is a service fee paid by the customer on small value orders.',
    )
    shipping_fee_adjustment: Optional[str] = Field(
        None,
        description='Adjustment fee charged to compensate for the difference in the amount between the actual shipping fee and the pre-paid shipping fee',
    )
    charge_back: Optional[str] = Field(
        None,
        description='The returned amount to the payment card after a customer successfully disputes an item on his/her account statement or transactions report',
    )
    customer_service_compensation: Optional[str] = Field(
        None, description='The refund amount after an order is paid or over-refunded'
    )
    promotion_adjustment: Optional[str] = Field(None, description='')
    other_adjustment: Optional[str] = Field(None, description='')
    settlement_amount: Optional[str] = Field(
        None,
        description='settlement_amount=user_pay+platform_promotion+shipping_fee_subsidy-refund-payment_fee-platform_commission-flat_fee-sales_fee-affiliate_commission-vat-shipping_fee-small_order_fee+the sum of adjustment',
    )
    transaction_fee: Optional[str] = Field(None, description='')


class SettlementListItem(BaseModel):
    sku_id: Optional[str] = Field(
        None, description="Sku ID. Indonesia orders don't have this value yet."
    )
    sku_name: Optional[str] = Field(
        None, description="Sku Name. Indonesia orders don't have this value yet."
    )
    product_name: Optional[str] = Field(
        None, description="Product Name. Indonesia orders don't have this value yet."
    )
    sett_status: Optional[int] = Field(
        None,
        description="Only when sett_status=SUCCESS, the order is successfully settled. For the other sett status, the other fields' value will be 0.<br>1:WAITING<br>2:PROCESSING<br>3:FAILED<br>4:SUCCESS",
    )
    unique_key: Optional[int] = Field(None, description='Unique Key')
    settlement_info: Optional[SettlementInfo] = None


class Data1(BaseModel):
    settlement_list: Optional[List[SettlementListItem]] = None


class ApiFinanceOrderSettlementsGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None


class ApiFinanceSettlementsSearchPostRequest(BaseModel):
    request_time_from: Optional[int] = Field(None, description='')
    request_time_to: Optional[int] = Field(None, description='')
    page_size: int = Field(..., description='')
    cursor: Optional[str] = Field(None, description='')
    sort_type: Optional[int] = Field(None, description='')


class SettlementInfo1(BaseModel):
    settlement_time: Optional[int] = Field(
        None,
        description='The time TTS pays out the money. Not necessarily the time merchants receive the money.',
    )
    currency: Optional[str] = Field(None, description='')
    user_pay: Optional[str] = Field(None, description="Buyer's payment.")
    platform_promotion: Optional[str] = Field(
        None,
        description='Promotion expenses subsidized by the platform, which may include coupons and other promotional events organized by the platform',
    )
    shipping_fee_subsidy: Optional[str] = Field(
        None,
        description='A positive amount represents the shipping fee discount received for participating in a platform campaign, and a negative amount represents a shipping fee discount you need to return.',
    )
    refund: Optional[str] = Field(None, description='')
    payment_fee: Optional[str] = Field(
        None,
        description="The technical service fee charged on the platform's online payment, refund, settlement and other categories (X% of settlement amount)",
    )
    platform_commission: Optional[str] = Field(
        None,
        description='The platform commission fee charged by the platform (X% of settled orders)',
    )
    flat_fee: Optional[str] = Field(
        None, description='The flat fee is a fixed amount charged per valid order'
    )
    sales_fee: Optional[str] = Field(
        None,
        description='The sales fee is a percentage of the product price after the seller discount, charged to the seller',
    )
    affiliate_commission: Optional[str] = Field(
        None,
        description="The commission fee one needs to pay to a creator when s/he promotes a product on Tiktok platform and generates orders (the amount depends on the seller's promotion plan)",
    )
    vat: Optional[str] = Field(
        None,
        description="VAT paid by platform on one's Behalf. Only applicable for cross-border shop orders. All the other fields' amount in this API is vat excluded.",
    )
    shipping_fee: Optional[str] = Field(
        None,
        description='The shipping fee paid by the merchant when the merchant selects logistics services supported by TikTok Shop',
    )
    small_order_fee: Optional[str] = Field(
        None,
        description='The small order fee is a service fee paid by the customer on small value orders.',
    )
    seller_reason_fund_deduction: Optional[str] = Field(
        None,
        description="Due to seller's liability, which brings unpleasant experience for buyers, then seller will bear the cost of buyer's loss.",
    )
    shipping_fee_adjustment: Optional[str] = Field(
        None,
        description='Adjustment fee charged to compensate for the difference in the amount between the actual shipping fee and the pre-paid shipping fee. <br>Positive value: TTS pays the merchants; <br>Negative value: TTS charges the merchants.',
    )
    charge_back: Optional[str] = Field(
        None,
        description='The returned amount to the payment card after a customer successfully disputes an item on his/her account statement or transactions report.<br>Positive value: TTS pays the merchants; <br>Negative value: TTS charges the merchants.',
    )
    customer_service_compensation: Optional[str] = Field(
        None,
        description='The refund amount after an order is paid or over-refunded.<br>Positive value: TTS pays the merchants; <br>Negative value: TTS charges the merchants.',
    )
    promotion_adjustment: Optional[str] = Field(
        None,
        description='Positive value: TTS pays the merchants; <br>Negative value: TTS charges the merchants.',
    )
    other_adjustment: Optional[str] = Field(
        None,
        description='Positive value: TTS pays the merchants; <br>Negative value: TTS charges the merchants.',
    )
    settlement_amount: Optional[str] = Field(
        None,
        description='settlement_amount=user_pay+platform_promotion+shipping_fee_subsidy-refund-payment_fee-platform_commission-flat_fee-sales_fee-affiliate_commission-vat-shipping_fee-small_order_fee+the sum of adjustment',
    )


class SettlementListItem1(BaseModel):
    unique_key: Optional[int] = Field(None, description='Unique key')
    order_id: Optional[str] = Field(
        None, description='Order ID: one of Order ID and Adjustment ID must not be 0'
    )
    adjustment_id: Optional[str] = Field(
        None,
        description='Adjustment ID: one of Order ID and Adjustment ID must not be 0',
    )
    related_order_id: Optional[str] = Field(
        None,
        description='If the Order ID is not null, related_order_id is the order ID itself<br>If the Adjustment ID is not null and the adjustment is based on a specific order, related_order_id is the order ID corresponding to that adjustment; if the Adjustment ID is not null and the adjustment is based on shop level, related_order_id will be null.',
    )
    sku_id: Optional[str] = Field(
        None, description="Sku ID. Indonesia orders don't have this value yet."
    )
    sku_name: Optional[str] = Field(
        None, description="Sku Name. Indonesia orders don't have this value yet."
    )
    product_name: Optional[str] = Field(
        None, description="Product Name. Indonesia orders don't have this value yet."
    )
    settlement_info: Optional[SettlementInfo1] = None


class Data2(BaseModel):
    next_cursor: Optional[str] = Field(
        None, description='Cursor used for searching for more information'
    )
    more: Optional[bool] = Field(
        None, description='Whether there are more orders on the next page or not'
    )
    settlement_list: Optional[List[SettlementListItem1]] = None


class ApiFinanceSettlementsSearchPostResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data2] = None
